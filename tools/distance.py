import math
from random import Random

import numpy as np

from tools.point import Point


def get_2d_distance(source, position):
	x_target=position.x
	y_target=position.y
	x_source=source.x
	y_source=source.y


	p1 = np.array([x_target, y_target])
	p2 = np.array([x_source, y_source])

	squared_dist = np.sum((p1 - p2) ** 2, axis=0)
	dist = np.sqrt(squared_dist)

	return dist


def get_distance_on_tier1(current_postion:Point,target_postion:Point):
	if current_postion.x-target_postion.x<0:
		return target_postion.x-current_postion.x
	else:
		return current_postion.x-target_postion.x


