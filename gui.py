import tkinter

from actions import find_point_on_list, find_all_points_on_list
from paint import draw_all_basic_elements, draw_points
from save import save_rewards, load_rewards
from tools.check import check_if_box_in_bondaries
from tools.distance import get_2d_distance
from tools.gui_tools import create_circle
from tools.point import Point
from tools.pointer_status import Pointer_status
from tools.points_cell import PointsCell
from tools.settings import Settings
import numpy as np
import typing





class Gui():

    def __init__(self,setting:Settings):
        self.master = tkinter.Tk()
        self.master.resizable(False, False)
        self.master.title("Menu")
        self.settings=setting

        #my virables
        self.pointer_status=Pointer_status.ADDING_POINTS
        self.bursh_size=5
        self.box_range_right_down=[Point(setting.map_size_x, setting.minimal_hand_range), 0]
        self.box_range_left_down=[Point(0, setting.minimal_hand_range), 0]


        #modifi text
        self.info_lab_text = tkinter.StringVar()
        self.spin_value_points = tkinter.StringVar()

        self.spin_value_points.set("5")
        self.info_lab_text.set("value: ")


        #create pannels
        button_pannel=tkinter.PanedWindow(self.master)
        check_value_pannel=tkinter.PanedWindow(button_pannel)
        add_point_pannel=tkinter.PanedWindow(button_pannel)
        save_pannel=tkinter.PanedWindow(button_pannel)
        hand_range_boxes_panel=tkinter.PanedWindow(button_pannel)


        #spin
        spin_box = tkinter.Spinbox(add_point_pannel,
            from_=0,
            to=5000,
            textvariable=self.spin_value_points)

        #create labs
        labInfo=tkinter.Label(check_value_pannel, textvariable=self.info_lab_text)


        self.canvas = tkinter.Canvas(self.master, width=setting.map_size_x, height=setting.map_size_y)

        #create buttons
        btn_add_points=tkinter.Button(add_point_pannel,text="Add points",command=self.btn_add_points)
        buttonSave=tkinter.Button(save_pannel,text="Save",command=self.save)
        buttonCheckValue=tkinter.Button(check_value_pannel, text="Check value", command=self.btn_check_value)
        buttonDeletePoints=tkinter.Button(save_pannel, text="Delte Points", command=self.btn_delete_points)
        btn_range_boxes=tkinter.Button(hand_range_boxes_panel, text="Hand ranges", command=self.btn_boxes)


        #save panel
        buttonSave.grid(column=0,row=1)
        buttonDeletePoints.grid(column=0,row=0)

        #check value panel
        labInfo.grid(column=0,row=1)
        buttonCheckValue.grid(column=0,row=0)

        #add point pannel
        btn_add_points.grid(column=0,row=0)
        spin_box.grid(column=0,row=1)

        #panle with ranges
        btn_range_boxes.grid(column=0,row=0)

        #main panel
        save_pannel.grid(column=0,row=0,padx=10)
        add_point_pannel.grid(column=2,row=0,padx=10)
        check_value_pannel.grid(column=1,row=0,padx=10)
        hand_range_boxes_panel.grid(column=3,row=0,padx=10)




        self.points_list:typing.List[PointsCell]=[]
        load_rewards(self.points_list,self.box_range_right_down,self.box_range_left_down)




        self.canvas.pack()
        self.draw_all_elements()

        button_pannel.pack()



        # self.canvas.bind('<B1-Motion>', self.hover)
        self.canvas.bind('<Motion>', self.hover)
        self.canvas.bind('<Button-1>', self.click)
        self.master.mainloop()



    def btn_boxes(self):
        self.pointer_status=Pointer_status.RANGES_BOXES
        self.draw_all_elements()

    def save(self):
        save_rewards(self.points_list,self.box_range_right_down[0],self.box_range_left_down[0])

        self.master.destroy()

    def btn_check_value(self):
        self.pointer_status=Pointer_status.CHECKING_VALUE

    def btn_delete_points(self):
        self.pointer_status=Pointer_status.DELETING_POINTS

    def btn_add_points(self):
        self.pointer_status=Pointer_status.ADDING_POINTS

    def hover(self, event):

        self.draw_all_elements()
        if self.pointer_status==Pointer_status.ADDING_POINTS:
         create_circle(event.x,event.y,self.bursh_size,self.canvas,"red")
        elif self.pointer_status==Pointer_status.DELETING_POINTS:
            create_circle(event.x,event.y,self.bursh_size,self.canvas,"yellow")


    def draw_all_elements(self):
        self.canvas.delete("all")
        draw_all_basic_elements(self.settings.map_size_x, self.settings.map_size_y, self.settings.r_of_LR, self.settings.intuder_size, self.settings.minimal_hand_range, self.canvas, self.box_range_right_down[0],self.box_range_left_down[0])
        if self.pointer_status!=Pointer_status.RANGES_BOXES:
            draw_points(self.points_list,self.canvas)
        if self.pointer_status==Pointer_status.RANGES_BOXES:
            color="black"
            if self.box_range_right_down[1]==1:
                color="gold"
            create_circle(self.box_range_right_down[0].x, self.box_range_right_down[0].y, self.settings.uav_size, self.canvas, color)

            color="black"
            if self.box_range_left_down[1]==1:
                color="gold"
            create_circle(self.box_range_left_down[0].x, self.box_range_left_down[0].y, self.settings.uav_size, self.canvas, color)
    def click(self,event):
        if self.pointer_status==Pointer_status.ADDING_POINTS:
            if event.y>self.settings.intuder_size+self.bursh_size:
                self.points_list.append(PointsCell(event.x,event.y,self.bursh_size,int(self.spin_value_points.get())))
        elif self.pointer_status==Pointer_status.CHECKING_VALUE:
            point=find_point_on_list(self.points_list,event.x,event.y)
            self.info_lab_text.set("value: "+ str(point.points))
        elif self.pointer_status==Pointer_status.DELETING_POINTS:
            points_to_delete_list=find_all_points_on_list(self.points_list,event.x,event.y)
            for point in points_to_delete_list:
                self.points_list.remove(point)
        elif self.pointer_status==Pointer_status.RANGES_BOXES:
            self.set_range_box(event)

        self.draw_all_elements()

    def set_range_box(self, event):
        if self.box_range_right_down[1] == 1 and check_if_box_in_bondaries(self.settings.r_of_LR, self.settings.intuder_size, self.settings.map_size_x,self.settings.map_size_x/2.0,Point(event.x, event.y)):
            self.box_range_right_down[0] = Point(event.x, event.y)
        if self.box_range_left_down[1] == 1 and check_if_box_in_bondaries(self.settings.r_of_LR, self.settings.intuder_size, self.settings.map_size_x/2.0,0,Point(event.x, event.y)):
            self.box_range_left_down[0] = Point(event.x, event.y)

        if get_2d_distance(self.box_range_right_down[0], Point(event.x, event.y))<self.settings.uav_size:
            self.box_range_right_down[1] = 1
            self.box_range_left_down[1] = 0

        if get_2d_distance(self.box_range_left_down[0], Point(event.x, event.y))<self.settings.uav_size:
            self.box_range_left_down[1] = 1
            self.box_range_right_down[1] = 0





