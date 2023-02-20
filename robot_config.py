import robot_model as model
import math
import numpy as np

theta = math.pi/2



# planar manipulator

# planar manipulator link 1
L1 = model.dh_transformation(1,0,0,theta)
# planar manipulator link 2
L2 = model.dh_transformation(1,0,0,theta)

# get homogenous transformation for the kinematic chain
transformation = model.kinematic_chain(L1, L2)

# get xyz coordinates from the transformation
coords = model.get_pos(transformation)

# get roth, pitch and yaw angles
angles = model.get_rot(transformation)

# print results
print("Two Link Planar Manipulator Results:"+"\n"+
      "x: "+str(coords[0])+"\n"+
      "y: "+str(coords[1])+"\n"+
      "z: "+str(coords[2])+"\n"+
      "roll:  "+str(angles[0])+"\n"+
      "pitch: "+str(angles[1])+"\n"+
      "yaw:   "+str(angles[2]))

print()
print()
print()



# case 1 UR5e robot

# get all 6 joint transformations
J1 = model.dh_transformation(0,         theta,  0.1625,  0)
J2 = model.dh_transformation(-0.425,    0,      0,      0)
J3 = model.dh_transformation(-0.3922,   0,      0,      0)
J4 = model.dh_transformation(0,         theta,  1.1333, 0)
J5 = model.dh_transformation(0,         -theta, 0.0997, 0)
J6 = model.dh_transformation(0,         0,      0.0996, 0)

# get homogenous transformations for the kinematic chain
T1 = model.kinematic_chain(J1, J2)
T2 = model.kinematic_chain(T1, J3)
T3 = model.kinematic_chain(T2, J4)
T4 = model.kinematic_chain(T3, J5)
transformation = model.kinematic_chain(T4, J6)

# get xyz coordinates from the transformation
coords = model.get_pos(transformation)

# get roth, pitch and yaw angles
angles = model.get_rot(transformation)

# print results
print("Case 1 UR5e Robot Results:"+"\n"+
      "x: "+str(coords[0])+"\n"+
      "y: "+str(coords[1])+"\n"+
      "z: "+str(coords[2])+"\n"+
      "roll:  "+str(angles[0])+"\n"+
      "pitch: "+str(angles[1])+"\n"+
      "yaw:   "+str(angles[2]))

print()
print()
print()



# case 2 UR5e robot

# get all 6 joint transformations
J1 = model.dh_transformation(0,         theta,  0.1625,  0)
J2 = model.dh_transformation(-0.425,    0,      0,      -theta)
J3 = model.dh_transformation(-0.3922,   0,      0,      0)
J4 = model.dh_transformation(0,         theta,  0.1333, 0)
J5 = model.dh_transformation(0,         -theta, 0.0997, 0)
J6 = model.dh_transformation(0,         0,      0.0996, 0)

# get homogenous transformations for the kinematic chain
T1 = model.kinematic_chain(J1, J2)
T2 = model.kinematic_chain(T1, J3)
T3 = model.kinematic_chain(T2, J4)
T4 = model.kinematic_chain(T3, J5)
transformation = model.kinematic_chain(T4, J6)

# get xyz coordinates from the transformation
coords = model.get_pos(transformation)

# get roth, pitch and yaw angles
angles = model.get_rot(transformation)

# print results
print("Case 2 UR5e Robot Results:"+"\n"+
      "x: "+str(coords[0])+"\n"+
      "y: "+str(coords[1])+"\n"+
      "z: "+str(coords[2])+"\n"+
      "roll:  "+str(angles[0])+"\n"+
      "pitch: "+str(angles[1])+"\n"+
      "yaw:   "+str(angles[2]))