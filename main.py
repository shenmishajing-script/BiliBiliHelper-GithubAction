import sys
import asyncio

sys.path.append(sys.path[0] + "/Src")

from Auth import Auth
from Coin2Silver import Coin2Silver
from GiftSend import GiftSend
from Group import Group
from Silver2Coin import Silver2Coin
from Task import Task
from Config import *
from CaseJudger import CaseJudger
from MainDailyTask import MainDailyTask
from MatchTask import MatchTask

# 初始化所有class
Auth = Auth()
CaseJudger = CaseJudger()
Coin2Silver = Coin2Silver()
GiftSend = GiftSend()
Group = Group()
Silver2Coin = Silver2Coin()
Task = Task()
MainDailyTask = MainDailyTask()
MatchTask = MatchTask()


async def main():

    daily_tasks = [
        CaseJudger.work(),
        Coin2Silver.work(),
        GiftSend.work(),
        Group.work(),
        Silver2Coin.work(),
        Task.work(),
        MainDailyTask.work(),
        MatchTask.work()
    ]

    # 先登陆一次
    Auth.work()

    for task in daily_tasks:
        await task


if __name__ == '__main__':
    asyncio.run(main())
