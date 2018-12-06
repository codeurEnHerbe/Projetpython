import Bezier as bz
import numpy as np
import matplotlib.pyplot as plt
import random as r

def affiche(porte):
    plt.axis([0,50,0,50])
    bz.visu(porte,'r')
    #bz.visu(np.array([[23,27],[25,27]]),'b')
    
    
def bezier(controle):
    matP = bz.matPrecision(100)
    B2 = np.array([[1,0,0],[-2,2,0],[1,-2,1]])
    
    result = np.dot(B2, controle)
    result = np.dot(matP, result)   
    return result    
    
def trouvePoint(depart, arrivee, porte):
    trouve = False 
    
    while(trouve == False):
        point = np.array([r.randint(0,50),r.randint(0,50)])
        controle = np.array([depart ,point, arrivee]) 
        points = bezier(controle)
        trouve = verifPoint(points,porte)
        
    bz.visu(points, 'b')
           
def verifPoint(points, porte):
    for i in range(0, len(points)):
        if points[i,0] > porte[0,0] and points[i,0] < porte[1,0] and points[i,1] > porte[0,1] and points[i,1] < porte[1,1] :
            print(points[i])
            return True
    
    return False               
        
porte = np.array([[11,22],[13,24]])
affiche(porte)
trouvePoint(np.array([0,0]), np.array([50,0]), porte)