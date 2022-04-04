from tools.point import Point


def check_if_box_in_bondaries(up_bond,down_bond,right_bond,left_bond,point:Point):
    if point.x<right_bond and left_bond<point.x and point.y>down_bond and point.y<up_bond:
        return True
    else:
        return False
