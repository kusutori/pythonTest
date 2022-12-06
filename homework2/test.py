# from itertools import count
#
#
# print("欢迎来玩我的游戏")
#
# answer = 8
# count = 3
# while count > 0:
#     count -= 1
#     guess = int(input("请输入一个数字："))
#     if guess == answer:
#         print("恭喜你猜对了")
#         break
#     elif guess > answer:
#         print("猜大了")
#     else:
#         print("猜小了")
#     if count == 0:
#         print("游戏结束")
#         break
#     else:
#         print("还有%d次机会" % count)

from itertools import count

print("你好")

answer=8
count=3
while count>0:
    count-=1
    guess=int(input("please enter a number:"))
    if guess==answer:
        print("right!")
        break
    elif guess >answer:
        print("so big!")
    else:
        print("so little!")
    if count ==0:
        print("the end!")
        break
    else:
        print("还有%d次机会" % count)