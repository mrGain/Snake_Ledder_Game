# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:17:38 2020

@author: RAKESH
"""

from PIL import Image
import random

end=100

def show_board():
    img = Image.open("D:\\PROGRAMMING\\PYTHON\\snake_ledder_board.jpg")
    img.show()
    
def check_ladder(points):
    if points==8:
        print("Ladder")
        return 26
    elif points==21:
        print("Ladder")
        return 82
    elif points==43:
        print("Ladder")
        return 77
    elif points==50:
        print("Ladder")
        return 91
    elif points==54:
        print("Ladder")
        return 93
    elif points==62:
        print("Ladder")
        return 96
    elif points==66:
        print("Ladder")
        return 87
    elif points==80:
        print("Ladder")
        return 100
    else:
        # Not a Ladder
        return points
    
def check_snake(points):
    if points==44:
        print("Snake")
        return 22
    elif points==46:
        print("Snake")
        return 5
    elif points==48:
        print("Snake")
        return 9
    elif points==52:
        print("Snake")
        return 11
    elif points==55:
        print("Snake")
        return 7
    elif points==59:
        print("Snake")
        return 17
    elif points==64:
        print("Snake")
        return 36
    elif points==69:
        print("Snake")
        return 33
    elif points==73:
        print("Snake")
        return 1
    elif points==83:
        print("Snake")
        return 19
    elif points==92:
        print("Snake")
        return 51
    elif points==95:
        print("Snake")
        return 24
    elif points==98:
        print("Snake")
        return 28
    else:
        # No Snake
        return points
    
def reached_end(points):
    if points==end:
        return True
    else:
        return False
    
def play():
    # Input the name of the Player1 and Player 2.
    p1_name=input("Player-1 ,Enter Your Name: ")
    p2_name=input("Player-2 ,Enter Your name: ")
    pp1=0      #Initial points of Players
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name,"Your Turn..")
            c=input("Press 1 to continue and 0 to quit :")
            if c=='0':
                print(p1_name,"Scored",pp1)
                print(p2_name,"Scored",pp2)
                print("Quiting the game thanks for Playing.")
                break
            dice=random.randint(1,6)  #Generate a random number from 1 to 6
            print("Dice showed ",dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            
            #check if the player is going beyond the board.
            if pp1>end:
                pp1=end
            print(p1_name," Your score ",pp1)
            
            if reached_end(pp1):
                print(p1_name,"Own")
                break
        else:
            print(p2_name,"Your Turn..")
            c=input("Press 1 to continue and 0 to quit :")
            if c=='0':
                print(p1_name,"Scored",pp1)
                print(p2_name,"Scored",pp2)
                print("Quiting the game thanks for Playing.")
                break
            dice=random.randint(1,6)  #Generate a random number from 1 to 6
            print("Dice showed ",dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            
            #check if the player is going beyond the board.
            if pp2>end:
                pp2=end
            print(p2_name," Your score ",pp2)
            
            if reached_end(pp2):
                print(p2_name,"Own")
                break
        turn=turn+1
        
show_board()
play()