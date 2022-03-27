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


def load_rewards(points_list:typing):
    try:

        file_rewards = open("settingsFiles/rewards.txt", mode="r")
        for record in file_rewards.readlines():

            fields_list=record.split(" ")
            points_list.append(PointsCell(int(fields_list[0]),int(fields_list[1]),int(fields_list[2]),int(fields_list[3])))




    except Exception as exp:
        print(str(exp))
        return
