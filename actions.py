import typing

from tools.distance import get_2d_distance
from tools.point import Point
from tools.points_cell import PointsCell


def find_point_on_list(list:typing.List[PointsCell],x,y):

    for point in list:
        if get_2d_distance(Point(point.x,point.y),Point(x,y))<=point.r:
            return point

    return PointsCell(0,0,0,0)