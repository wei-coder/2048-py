#import pythoncom
# -*- coding:utf-8 -*-
import pdb
import copy
import random

def set_randomnum(arry):
    list_tmp=[]
    for x in range(4):
        for y in range(4):
            if arry[x][y]==0:
                list_tmp.append(x*4+y)
    num_value=random.sample([2,4],1)
    num_seq=random.randint(0,list_tmp.__len__()-1)
    arry[list_tmp[num_seq]//4][list_tmp[num_seq]%4]=num_value[0]
    return

def print_arry(arry):
    print ("┌"+("─"*5+"┬")*3+"─"*5+"┐")
    print ("│%4d │%4d │%4d │%4d │"%(arry[0][0],arry[0][1],arry[0][2],arry[0][3]))
    print ("├"+("─"*5+"┼")*3+"─"*5+"┤")
    print ("│%4d │%4d │%4d │%4d │"%(arry[1][0],arry[1][1],arry[1][2],arry[1][3]))
    print ("├"+("─"*5+"┼")*3+"─"*5+"┤")
    print ("│%4d │%4d │%4d │%4d │"%(arry[2][0],arry[2][1],arry[2][2],arry[2][3]))
    print ("├"+("─"*5+"┼")*3+"─"*5+"┤")
    print ("│%4d │%4d │%4d │%4d │"%(arry[3][0],arry[3][1],arry[3][2],arry[3][3]))
    print ("└"+("─"*5+"┴")*3+"─"*5+"┘")
    return

def arry_turn(arry):
    for x in range(4):
        tmp = arry[x][0]
        arry[x][0]=arry[x][3]
        arry[x][3]=tmp
        tmp=arry[x][1]
        arry[x][1]=arry[x][2]
        arry[x][2]=tmp
    return arry

def arry_row2colum(arry):
    arry_tmp=copy.deepcopy(arry)
    for x in range(4):
        for y in range(4):
            arry[x][y]=arry_tmp[y][x]
    return arry

def left(arry):
    for x in range(4):
        tmp=[0,0,0,0]
        k=0
        for y in range(4):
            if arry[x][y]!=0:
                tmp[k]=arry[x][y]
                k+=1
        arry[x]=tmp
    return arry

def left_add(arry):
    for x in range(4):
        if arry[x][0]== arry[x][1]:
            arry[x][0]+=arry[x][1]
            arry[x][1]=0
        elif arry[x][1] == arry[x][2]:
            arry[x][1]+=arry[x][2]
            arry[x][2]=0
        if arry[x][2] == arry[x][3]:
            arry[x][2]+=arry[x][3]
            arry[x][3]=0
    return arry

#pdb.set_trace()
arry=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]        

set_randomnum(arry)
print_arry(arry)
while True:
    key=input()
    if key == 'a':
        left_add(left(arry))
        set_randomnum(arry)
        print_arry(arry)
    elif key=='d':
        arry_turn(left_add(left(arry_turn(arry))))
        set_randomnum(arry)
        print_arry(arry)
    elif key=='w':
        arry_row2colum(left_add(left(arry_row2colum(arry))))
        set_randomnum(arry)
        print_arry(arry)
    elif key=='s':
        arry_row2colum(arry_turn(left_add(left(arry_turn(arry_row2colum(arry))))))
        set_randomnum(arry)
        print_arry(arry)
    elif key=='r':
        arry=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        set_randomnum(arry)
        print_arry(arry)
    elif key=='q':
        break

  
