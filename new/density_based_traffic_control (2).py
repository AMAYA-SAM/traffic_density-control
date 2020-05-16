# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:29:44 2020

@author: abhij
"""

import random
import time
def density(count,w):
    if count==0:
        print("EMPTY at lane " + str(w))
        return 3
    elif count <4 and count>0:
        print("LIGHT at lane " +str(w) )
        return 4
    elif count >3 and count <8:
        print("MEDIUM at lane "+ str(w))
        return 6
    elif count >7 :
        print("HEAVY at lane "+str(w))
        return 8
    
#print( random.randint(1,10) )

while True:
    i=0
    
    for i in (1,2,3,4):
       count=random.randint(1,10)
       print ("Total vehicle at lane "+str(i)+ " = "+str(count))
       t= density(count,i)
       print("Green light at lane "+str(i)+"  and  "+ str(t)+" seconds remaining") 
       time.sleep(t)
       if i==4:
         print("ORange light at lane 4 and lane 1")
       else:
           print("orange light at lane "+str(i) +" and  lane  "+ str(i+1))
       time.sleep(1)
       print("---------------------------------------")
    
    print('-------------------------------')
    print("one cycle over")
    print("-------------------------------")
    
    
    
    