import math
import numpy as np



def dh_transformation(Ai,   # link length   
                      ai,   # link twist
                      Di,   # link offset
                      Ti    # joint angle
                      ):
    
    # pass the DH params into desired transformation
    transformation = np.array([[math.cos(Ti),   -math.sin(Ti) * math.cos(ai),   math.sin(Ti) * math.sin(ai),    Ai * math.cos(Ti)],
                               [math.sin(Ti),   math.cos(Ti) * math.cos(ai),    -math.cos(Ti) * math.sin(ai),   Ai * math.sin(Ti)],
                               [0,              math.sin(ai),                   math.cos(ai),                   Di               ],
                               [0,              0,                              0,                              1                ]])
    
    # return the transformation
    return transformation


def kinematic_chain(DH1, DH2):
    # initialize total transformation
    TT = np.identity(4)       
    
    # loop through the transformation matrices to multiply them
    for i in range(4):
        for j in range(4):
            TT[i][j] = (DH1[i][0]*DH2[0][j]) + (DH1[i][1]*DH2[1][j]) + (DH1[i][2]*DH2[2][j]) + (DH1[i][3]*DH2[3][j])
    
    # return the resulting transformation
    return TT
    


def get_pos(trans):
    # get x coord
    x = trans[0][3]   
    # get y coord  
    y = trans[1][3]  
    # get z coord  
    z = trans[2][3]     
    
    # return the xyz coordinates
    return [x,y,z]      


def get_rot(trans):
    # get roll
    roll = math.atan(trans[2][1]/trans[2][2])
    # get pitch                                       
    pitch = math.atan(-trans[2][0]/(math.sqrt(trans[2][1]**2+trans[2][2]**2)))  
    # get yaw    
    yaw = math.atan(trans[1][0]/trans[0][0])                                        
    
    # return the roll, pitch and yaw
    return [roll, pitch, yaw]       