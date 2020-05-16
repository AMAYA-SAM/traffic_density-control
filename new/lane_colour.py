# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:43:59 2020

@author: amaya
"""

"""
Created on Thu May 14 18:09:37 2020


"""
import matplotlib.pyplot as plt
import random 
import time

def density(count,w):
    if count<=1:
        print("Very low traffic at lane " + str(w))
        return 3
    elif count <3 and count>1:
        print("LIGHT traffic at lane " +str(w) )
        return 4
    elif count >2 and count <4:
        print("MEDIUM traffic at lane "+ str(w))
        return 6
    elif count >=4 :
        print("HEAVY traffic at lane "+str(w))
        return 8


#fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()



#fig.savefig('plotcircles.png')

def greenlane(i):
    
    if(i==1):
        circle2 = plt.Circle((0.8, 0.8), 0.2, color='green',clip_on=False)
        circle3 = plt.Circle((0.2, 0.2), 0.2, color='r', clip_on=False)
        circle4 = plt.Circle((0.2, 0.8), 0.2, color='r', clip_on=False)
        circle1 = plt.Circle((0.8, 0.2), 0.2, color='r',clip_on=False)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(circle3)
        ax.add_artist(circle4)
        plt.show()

    elif(i==2):
        circle2 = plt.Circle((0.8, 0.8), 0.2, color='r',clip_on=False)
        circle3 = plt.Circle((0.2, 0.2), 0.2, color='r', clip_on=False)
        circle4 = plt.Circle((0.2, 0.8), 0.2, color='green', clip_on=False)
        circle1 = plt.Circle((0.8, 0.2), 0.2, color='r',clip_on=False)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(circle3)
        ax.add_artist(circle4)
        plt.show()

    elif(i==3):
        circle2 = plt.Circle((0.8, 0.8), 0.2, color='r',clip_on=False)
        circle3 = plt.Circle((0.2, 0.2), 0.2, color='green', clip_on=False)
        circle4 = plt.Circle((0.2, 0.8), 0.2, color='r', clip_on=False)
        circle1 = plt.Circle((0.8, 0.2), 0.2, color='r',clip_on=False)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(circle3)
        ax.add_artist(circle4)
        plt.show()

    elif(i==4):
        circle2 = plt.Circle((0.8, 0.8), 0.2, color='r',clip_on=False)
        circle3 = plt.Circle((0.2, 0.2), 0.2, color='r', clip_on=False)
        circle4 = plt.Circle((0.2, 0.8), 0.2, color='r', clip_on=False)
        circle1 = plt.Circle((0.8, 0.2), 0.2, color='green',clip_on=False)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(circle3)
        ax.add_artist(circle4)
        plt.show()

def orange(i):
        if(i==1):
            fig, ax = plt.subplots()
            label = ax.annotate("lane 1", xy=(0.8, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 2", xy=(0.2, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 4", xy=(0.8, 0.2), fontsize=30, ha="center")
            label = ax.annotate("lane 3", xy=(0.2, 0.2), fontsize=30, ha="center")
            circle2 = plt.Circle((0.8, 0.8), 0.2, color='yellow',clip_on=False)
            circle3 = plt.Circle((0.2, 0.2), 0.2, color='r', clip_on=False)
            circle4 = plt.Circle((0.2, 0.8), 0.2, color='yellow', clip_on=False)
            circle1 = plt.Circle((0.8, 0.2), 0.2, color='r',clip_on=False)
            ax.add_artist(circle1)
            ax.add_artist(circle2)
            ax.add_artist(circle3)
            ax.add_artist(circle4)
            plt.show()
            
        elif(i==2):
            fig, ax = plt.subplots()
            label = ax.annotate("lane 1", xy=(0.8, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 2", xy=(0.2, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 4", xy=(0.8, 0.2), fontsize=30, ha="center")
            label = ax.annotate("lane 3", xy=(0.2, 0.2), fontsize=30, ha="center")
            circle2 = plt.Circle((0.8, 0.8), 0.2, color='r',clip_on=False)
            circle3 = plt.Circle((0.2, 0.2), 0.2, color='yellow', clip_on=False)
            circle4 = plt.Circle((0.2, 0.8), 0.2, color='yellow', clip_on=False)
            circle1 = plt.Circle((0.8, 0.2), 0.2, color='r',clip_on=False)
            ax.add_artist(circle1)
            ax.add_artist(circle2)
            ax.add_artist(circle3)
            ax.add_artist(circle4)
            plt.show()

        elif(i==3):
            fig, ax = plt.subplots()
            label = ax.annotate("lane 1", xy=(0.8, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 2", xy=(0.2, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 4", xy=(0.8, 0.2), fontsize=30, ha="center")
            label = ax.annotate("lane 3", xy=(0.2, 0.2), fontsize=30, ha="center")
            circle2 = plt.Circle((0.8, 0.8), 0.2, color='r',clip_on=False)
            circle3 = plt.Circle((0.2, 0.2), 0.2, color='yellow', clip_on=False)
            circle4 = plt.Circle((0.2, 0.8), 0.2, color='r', clip_on=False)
            circle1 = plt.Circle((0.8, 0.2), 0.2, color='yellow',clip_on=False)
            ax.add_artist(circle1)
            ax.add_artist(circle2)
            ax.add_artist(circle3)
            ax.add_artist(circle4)
            plt.show()
        elif(i==4):
            fig, ax = plt.subplots()
            label = ax.annotate("lane 1", xy=(0.8, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 2", xy=(0.2, 0.8), fontsize=30, ha="center")
            label = ax.annotate("lane 4", xy=(0.8, 0.2), fontsize=30, ha="center")
            label = ax.annotate("lane 3", xy=(0.2, 0.2), fontsize=30, ha="center")
            circle2 = plt.Circle((0.8, 0.8), 0.2, color='yellow',clip_on=False)
            circle3 = plt.Circle((0.2, 0.2), 0.2, color='r', clip_on=False)
            circle4 = plt.Circle((0.2, 0.8), 0.2, color='r', clip_on=False)
            circle1 = plt.Circle((0.8, 0.2), 0.2, color='yellow',clip_on=False)
            ax.add_artist(circle1)
            ax.add_artist(circle2)
            ax.add_artist(circle3)
            ax.add_artist(circle4)
            plt.show()
    
        
    


def logic(i,t):
    if(i==1):
        greenlane(1)
        time.sleep(t)
        #close('all')
        orange(1)
        time.sleep(5)
    elif(i==2):
        greenlane(2)
        time.sleep(t)
        orange(2)
        time.sleep(5)
    elif(i==3):
        greenlane(3)
        time.sleep(t)
        orange(3)
        time.sleep(5)
    elif(i==4):
        greenlane(4)
        time.sleep(t)
        orange(4)
        time.sleep(5)

        
        
    
for i in (1,2,3,4):
    fig, ax = plt.subplots()
    label = ax.annotate("lane 1", xy=(0.8, 0.8), fontsize=30, ha="center")
    label = ax.annotate("lane 2", xy=(0.2, 0.8), fontsize=30, ha="center")
    label = ax.annotate("lane 4", xy=(0.8, 0.2), fontsize=30, ha="center")
    label = ax.annotate("lane 3", xy=(0.2, 0.2), fontsize=30, ha="center")

    count=random.randint(1,10)
    t= density(count,i)
    print("Green light at lane "+str(i)+"  and  "+ str(t)+" seconds remaining")
    logic(i,t)