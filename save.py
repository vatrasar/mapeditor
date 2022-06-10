import typing

from tools.point import Point
from tools.points_cell import PointsCell

def sort_fun(element):
    return element.x
def save_rewards(points_list:typing.List[PointsCell],box_range_right_down,box_range_left_down,invisible_boxes:typing.List[PointsCell]):
    points_list.sort(key=sort_fun)
    try:

        file_rewards = open("settingsFiles/rewards.txt", mode="w")
        file_rewards.write("# x y point_range reward\n")
        for point in points_list:
            file_rewards.write("%d %d %d %.2f\n"%(point.x,point.y,point.r,point.points))

        file_rewards.close()
        file_boxes = open("settingsFiles/boxes.txt", mode="w")
        file_boxes.write("%f %f\n"%(box_range_right_down.x,box_range_right_down.y))
        file_boxes.write("%f %f\n"%(box_range_left_down.x,box_range_left_down.y))
        file_boxes.close()
        file_invisible = open("settingsFiles/invisible_boxes.txt", mode="w")
        for point in invisible_boxes:
            file_invisible.write("%d %d %d\n"%(point.x,point.y,point.r))


    except Exception as exp:
        print(str(exp))
        return


def load_rewards(points_list:typing,box_range_right_down,box_range_left_down,invisible_boxes:typing.List[PointsCell]):
    try:

        file_rewards = open("settingsFiles/rewards.txt", mode="r")
        for record in file_rewards.readlines():
            if record[0]=="#":
                continue
            fields_list=record.split(" ")
            fields_list=list(filter("".__ne__,fields_list))
            for i,field in enumerate(fields_list):
                fields_list[i]=field.strip("\n")
            points_list.append(PointsCell(int(fields_list[0]),int(fields_list[1]),int(fields_list[2]),float(fields_list[3])))
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


    try:

        file_invisible = open("settingsFiles/invisible_boxes.txt", mode="r")
        for record in file_invisible.readlines():

            fields_list=record.split(" ")
            invisible_boxes.append(PointsCell(int(fields_list[0]),int(fields_list[1]),int(fields_list[2]),0))
    except Exception as exp:
        print(str(exp))
        return





