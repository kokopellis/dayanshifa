#!/usr/bin/python
from random import randint


def yan():
    shi = 50
    shi -= 1
    for i in range(3):
        left = randint(1,shi - 2)
        right = shi - left 
        right -= 1
        if left % 4 == 0:
            left = left - 4
        else: 
            left = left - left % 4
        if right % 4 == 0:
            right -= 4
        else: 
            right -= right % 4
        #right = right - (right % 4 == 0) ? 4 : right % 4
        shi = left + right
    #print("shi = " + str(shi) + " , shi / 4 = " + str(shi / 4) + " , shi % 4 = " + str(shi % 4))
    return shi / 4



def display():
    stack = []
    for i in range(6):
        stack.append(yan())
    
    for i in range(6):
        yao = stack.pop()
        if yao == 6:
            print("6 -- 一")
        elif yao == 7:
            print("7 一 一")
        elif yao == 8:
            print("8 -- --")
        else:
            print("9 一 --")




def distribution_test():
    dis = [0, 0, 0, 0]
    for i in range(100000):
        temp = int(yan())
        dis[temp - 6] += 1
    for i in dis:
        print(i)


display()
#distribution_test()

    
