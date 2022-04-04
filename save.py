import typing

from tools.point import Point
from tools.points_cell import PointsCell


def save_rewards(points_list:typing.List[PointsCell],box_range_right_down,box_range_left_down):

    try:

        file_rewards = open("settingsFiles/rewards.txt", mode="w")
        for point in points_list:
            file_rewards.write("%d %d %d %d\n"%(point.x,point.y,point.r,point.points))

        file_rewards.close()
        file_boxes = open("settingsFiles/boxes.txt", mode="w")
        file_boxes.write("%f %f\n"%(box_range_right_down.x,box_range_right_down.y))
        file_boxes.write("%f %f\n"%(box_range_left_down.x,box_range_left_down.y))
        file_boxes.close()

    except Exception as exp:
        print(str(exp))
        return


def load_rewards(points_list:typing,box_range_right_down,box_range_left_down):
    try:

        file_rewards = open("settingsFiles/rewards.txt", mode="r")
        for record in file_rewards.readlines():

            fields_list=record.split(" ")
            points_list.append(PointsCell(int(fields_list[0]),int(fields_list[1]),int(fields_list[2]),int(fields_list[3])))
    except Exception as exp:
        print(str(exp))
        return

    try:

        file_box = open("settingsFiles/boxes.txt", mode="r")
        record=file_box.readlines()
        field_list=record[1].split(" ")
        box_range_left_down[0]=Point(float(field_list[0]),float(field_list[1]))
        field_list=record[0].split(" ")
        box_range_right_down[0]=Point(float(field_list[0]),float(field_list[1]))
    except Exception as exp:
        print(str(exp))
        return






