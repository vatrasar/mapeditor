import typing

from tools.points_cell import PointsCell


def save_rewards(points_list:typing.List[PointsCell]):

    try:

        file_rewards = open("settingsFiles/rewards.txt", mode="w")
        for point in points_list:
            file_rewards.write("%d %d %d %d\n"%(point.x,point.y,point.r,point.points))
        file_rewards.close()


    except Exception as exp:
        print(str(exp))
        return
