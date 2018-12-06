import numpy as np  
import matplotlib.pyplot as plt

def visu(matPoint,style):

    matPoint = np.transpose(matPoint)
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)
"""  
B2 = np.array([[1,0,0],[-2,2,0],[1,-2,1]])
B3 = np.array([[1,0,0,0], [-3,3,0,0], [3,-6,3,0], [-1,3,-3,1]])
symetrie = np.array([[-1,0],[0,1]])
"""
def pointcontrole3(point1, point2, point3):
    matrice = np.array([ [point1[0], point1[1] ], [point2[0], point2[1] ], [point3[0], point3[1] ]])
    return matrice


def pointcontrole4(point1, point2, point3, point4):
    matrice = np.array([ [point1[0], point1[1] ], [point2[0], point2[1] ], [point3[0], point3[1] ], [point4[0], point4[1]]])
    return matrice

def matricefonction4(nbpoints):
    ligne1 = np.ones(nbpoints)
    ligne2 = np.linspace(0,1,nbpoints)
    ligne3 = ligne2**2
    ligne4 = ligne2**3
    
    t = np.array([ligne1, ligne2, ligne3, ligne4])
    t = t.transpose() 
    
    return t
    
def matricefonction3(nbpoints):
    ligne1 = np.ones(nbpoints)
    ligne2 = np.linspace(0,1,nbpoints)
    ligne3 = ligne2**2
    
    t = np.array([ligne1, ligne2, ligne3])
    t = t.transpose() 
    
    return t
    
"""

point1 = [0, 4]
point2 = [1.5,5.5]
point3 = [2.3,4]

point4 = [2*point3[0]-point2[0], 2*point3[1]-point2[1]]
point5 = [0.5,1.5]
point6 = [0,0]


plt.figure()
plt.axis('scaled') # la position est importante
maxXY=15
delta=2
plt.xlim(-3,3)  
plt.ylim(0, 5)
"""
def appliquesymetrie(point):
    return np.dot(point, symetrie)
    
    
def matPrecision(nbPoint):
    ligne1 = np.ones(nbPoint)
    ligne2 = np.linspace(0.0 , 1.0 , num = nbPoint , endpoint = False)
    ligne3 = ligne2 **2
    t = np.array([ligne1,ligne2,ligne3])
    return np.transpose(t)

def bezier3(point1,point2,point3):
    t = matricefonction3(100)
    p = pointcontrole3(point1,point2,point3)
    result = np.dot(t, B2)
    result = np.dot(result, p)   
    visu(result, 'b') 

    
def bezier4(point1,point2,point3,point4):
    t = matricefonction4(100)
    p = pointcontrole4(point1,point2,point3,point4)
    result = np.dot(t, B3)
    result = np.dot(result, p)   
    visu(result, 'y') 
""""    
bezier3(point1, point2, point3)
bezier4(point3, point4, point5, point6)

bezier3(appliquesymetrie(point1), appliquesymetrie(point2), appliquesymetrie(point3))
bezier4(appliquesymetrie(point3), appliquesymetrie(point4), appliquesymetrie(point5), appliquesymetrie(point6))
"""