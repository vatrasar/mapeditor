from tkinter import Canvas

from tools.gui_tools import create_squer, create_line, create_circle, from_rgb
from tools.point import Point
import numpy as np

def draw_all_basic_elements(map_size_x,map_size_y, hand_range, intruder_size, minimal_hand_range,canvas,left_box,right_box):

    squer_bootm_start=0
    squer_top_end=map_size_x/2.0



    create_squer(squer_bootm_start,0,squer_top_end, intruder_size,canvas,"red")
    squer_bootm_start=map_size_x/2.0
    squer_top_end=map_size_x

    create_squer(squer_bootm_start,0,squer_top_end, intruder_size,canvas,"blue")#target
    # create_circle(476,354,hand_size,self.canvas,"black") #marker




        #create_circle(hand.position.x, hand.position.y, hand_size, self.canvas, hand.color)

        # ranges boxes
    boxes = []



    up_start = Point(0, hand_range)
    up_end = Point(map_size_x/2.0,hand_range)
    boxes.append((up_start, up_end, "red"))
    right_start = Point(map_size_x/2.0,hand_range)
    right_end = left_box
    down_start=left_box
    down_end=Point(left_box.x,intruder_size)
    boxes.append((right_start, right_end, "red"))
    boxes.append((down_start, down_end, "red"))




    up_start = Point(map_size_x/2.0,hand_range)
    up_end = Point(map_size_x,hand_range)
    boxes.append((up_start, up_end, "blue"))
    left_start = Point(map_size_x/2.0,hand_range)
    left_end = right_box
    boxes.append((left_start, left_end, "blue"))

    down_start=right_box
    down_end=Point(right_box.x+1,intruder_size)
    boxes.append((down_start, down_end, "blue"))


    for box in boxes:
        create_line(box[0], box[1], canvas, box[2])




def  draw_points(points_list,canvas:Canvas):

    max=0
    for point in points_list:
        if point.points>max:
            max=point.points


    for point in points_list:
        color_b=255-int(255*(point.points/float(max)))
        color_r=int(255*(point.points/float(max)))
        create_circle(point.x,point.y,point.r,canvas,from_rgb(color_r,color_b,color_b))


def draw_invisible_boxes(invisible_boxes_list,canvas):
    max=0



    for point in invisible_boxes_list:

        create_circle(point.x,point.y,point.r,canvas,"grey")

