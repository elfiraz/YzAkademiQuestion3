# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:18:31 2022

@author: asus
"""

arr=[2,3,4,3,2]
ballEneryg=4
def hesapla(dizi,ballEnergy):
    for i in dizi:
        height=i
        newEnergy=ballEnergy-(height-ballEnergy)
        delta=newEnergy-ballEnergy       
        
        print(ballEnergy,height,"+"+str(delta))
        ballEnergy=newEnergy
    print(ballEnergy)    
hesapla(arr,ballEneryg)