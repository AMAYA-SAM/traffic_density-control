# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:53:59 2020

@author: amaya
"""
import cv2
import matplotlib.pyplot as plt
import random 
import time

car_cascade = cv2.CascadeClassifier("cars.xml")
lane1=cv2.VideoCapture("empty.mp4")
lane2=cv2.VideoCapture("low.mp4")
lane3=cv2.VideoCapture("mid.mp4")
lane4=cv2.VideoCapture("high.mp4")

def getcount(a):
    if a==1:
        ret,frames=lane1.read()
    elif a==2:
        ret,frames=lane2.read()
    elif a==3:
        ret,frames=lane3.read()
    else :
        ret,frames=lane4.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5)
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video2', frames)
    cv2.waitKey(2000)
    return len(cars)

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


while True:
    i=0
    
    for i in (1,2,3,4):
       fig, ax = plt.subplots()
       label = ax.annotate("lane 1", xy=(0.8, 0.8), fontsize=30, ha="center")
       label = ax.annotate("lane 2", xy=(0.2, 0.8), fontsize=30, ha="center")
       label = ax.annotate("lane 4", xy=(0.8, 0.2), fontsize=30, ha="center")
       label = ax.annotate("lane 3", xy=(0.2, 0.2), fontsize=30, ha="center")
       count=getcount(i)
       print ("Total vehicle at lane "+str(i)+ " = "+str(count))
       t= density(count,i)
       print("Green light at lane "+str(i)+"  and  "+ str(t)+" seconds remaining") 
       logic(i,t)
       #time.sleep(t)
       if i==4:
         print("ORange light at lane 4 and lane 1")
       else:
           print("orange light at lane "+str(i) +" and  lane  "+ str(i+1))
       time.sleep(1)
       print("---------------------------------------")
    
    print('-------------------------------')
    print("one cycle over")
    print("-------------------------------")
