import tkinter

from paint import draw_all_basic_elements, draw_points
from save import save_rewards
from tools.gui_tools import create_circle
from tools.points_cell import PointsCell
from tools.settings import Settings
import numpy as np
import typing

class Gui():

    def __init__(self,setting:Settings):
        self.master = tkinter.Tk()
        self.master.resizable(False, False)
        self.master.title("Menu")
        buttons_pannel=tkinter.PanedWindow(self.master)
        button1=tkinter.Button(buttons_pannel,text="Save",command=self.save)
        self.settings=setting
        button2 =tkinter.Button(buttons_pannel,text="dwa")
        button3 =tkinter.Button(buttons_pannel,text="trzy")
        button1.grid(column=0,row=0)
        button2.grid(column=1,row=0)
        button3.grid(column=2,row=0)
        self.points_list:typing.List[PointsCell]=[]
        self.bursh_size=5


        self.canvas = tkinter.Canvas(self.master, width=setting.map_size, height=setting.map_size)
        self.canvas.pack()
        draw_all_basic_elements(setting.map_size,setting.r_of_LR,setting.intuder_size,setting.minimal_hand_range,self.canvas)
        buttons_pannel.pack()



        # self.canvas.bind('<B1-Motion>', self.hover)
        self.canvas.bind('<Motion>', self.hover)
        self.canvas.bind('<Button-1>', self.click)
        self.master.mainloop()




    def save(self):
        save_rewards(self.points_list)
        self.master.destroy()

    def hover(self, event):
        self.canvas.delete("all")

        create_circle(event.x,event.y,self.bursh_size,self.canvas,"red")
        self.draw_all_elements()

    def draw_all_elements(self):
        draw_all_basic_elements(self.settings.map_size,self.settings.r_of_LR,self.settings.intuder_size,self.settings.minimal_hand_range,self.canvas)
        draw_points(self.points_list,self.canvas)

    def click(self,event):
        if event.y>self.settings.intuder_size+self.bursh_size:
            self.points_list.append(PointsCell(event.x,event.y,self.bursh_size,5))
