import tkinter

from actions import find_point_on_list
from paint import draw_all_basic_elements, draw_points
from save import save_rewards
from tools.gui_tools import create_circle
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

        #modifi text
        self.info_lab_text = tkinter.StringVar()
        self.spin_value_points = tkinter.StringVar()

        self.spin_value_points.set("5")
        self.info_lab_text.set("value: ")


        #create pannels
        button_pannel=tkinter.PanedWindow(self.master)
        check_value_pannel=tkinter.PanedWindow(button_pannel)
        add_point_pannel=tkinter.PanedWindow(button_pannel)


        #spin
        spin_box = tkinter.Spinbox(add_point_pannel,
            from_=0,
            to=5000,
            textvariable=self.spin_value_points)

        #create labs
        labInfo=tkinter.Label(check_value_pannel, textvariable=self.info_lab_text)


        self.canvas = tkinter.Canvas(self.master, width=setting.map_size, height=setting.map_size)

        #create buttons
        btn_add_points =tkinter.Button(add_point_pannel,text="Add points",command=self.btn_add_points)
        buttonSave=tkinter.Button(button_pannel,text="Save",command=self.save)
        buttonCheckValue =tkinter.Button(check_value_pannel, text="Check value", command=self.btn_check_value)

        #check value panel
        labInfo.grid(column=0,row=1)
        buttonCheckValue.grid(column=0,row=0)

        #add point pannel
        btn_add_points.grid(column=0,row=0)
        spin_box.grid(column=0,row=1)

        #main panel
        buttonSave.grid(column=0,row=0,padx=10)
        add_point_pannel.grid(column=2,row=0,padx=10)
        check_value_pannel.grid(column=1,row=0,padx=10)




        self.points_list:typing.List[PointsCell]=[]




        self.canvas.pack()
        draw_all_basic_elements(setting.map_size,setting.r_of_LR,setting.intuder_size,setting.minimal_hand_range,self.canvas)

        button_pannel.pack()



        # self.canvas.bind('<B1-Motion>', self.hover)
        self.canvas.bind('<Motion>', self.hover)
        self.canvas.bind('<Button-1>', self.click)
        self.master.mainloop()




    def save(self):
        save_rewards(self.points_list)
        self.master.destroy()

    def btn_check_value(self):
        self.pointer_status=Pointer_status.CHECKING_VALUE

    def btn_add_points(self):
        self.pointer_status=Pointer_status.ADDING_POINTS

    def hover(self, event):
        self.canvas.delete("all")
        if self.pointer_status==Pointer_status.ADDING_POINTS:
         create_circle(event.x,event.y,self.bursh_size,self.canvas,"red")
        self.draw_all_elements()

    def draw_all_elements(self):
        draw_all_basic_elements(self.settings.map_size,self.settings.r_of_LR,self.settings.intuder_size,self.settings.minimal_hand_range,self.canvas)
        draw_points(self.points_list,self.canvas)

    def click(self,event):
        if self.pointer_status==Pointer_status.ADDING_POINTS:
            if event.y>self.settings.intuder_size+self.bursh_size:
                self.points_list.append(PointsCell(event.x,event.y,self.bursh_size,int(self.spin_value_points.get())))
        elif self.pointer_status==Pointer_status.CHECKING_VALUE:
            point=find_point_on_list(self.points_list,event.x,event.y)
            self.info_lab_text.set("value: "+ str(point.points))



