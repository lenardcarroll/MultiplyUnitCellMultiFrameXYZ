import numpy as np
from ase.io import read
from ase.io import write
import os

class increaseCell:
    def __init__(self,coordinates,cell_x,cell_y,cell_z,u_x,u_y,u_z,selection=None,filename=None):

        coordinates = coordinates.coordinates

        if selection==None:
            selection = range(len(coordinates[0]))

        CellVectors = [cell_x,cell_y,cell_z]

        altCornerVecs = []
        CornerVecs = [[1,0,0],[0,1,0],[0,0,1]]

        for i in CornerVecs:
            altCornerVecs.append(np.matmul(i,CellVectors))

        X_Multi = []
        Y_Multi = []
        Z_Multi = []

        for i in range(1,u_x+1):
            if i%2==1:
                X_Multi.append([altCornerVecs[0][0]*(int((i - 1)/2)),altCornerVecs[0][1],altCornerVecs[0][2]])
            elif i%2==0:
                X_Multi.append([-altCornerVecs[0][0]*(int(i/2)),altCornerVecs[0][1],altCornerVecs[0][2]])
        for i in range(1,u_y+1):
            if i%2==1:
                Y_Multi.append([altCornerVecs[1][0],altCornerVecs[1][1]*(int((i - 1)/2)),altCornerVecs[1][2]])
            elif i%2==0:
                Y_Multi.append([altCornerVecs[1][0],-altCornerVecs[1][1]*(int((i)/2)),altCornerVecs[1][2]])
        for i in range(1,u_z+1):
            if i%2==1:
                Z_Multi.append([altCornerVecs[2][0],altCornerVecs[2][1],altCornerVecs[2][2]*(int((i - 1)/2))])
            elif i%2==0:
                Z_Multi.append([-altCornerVecs[2][0],altCornerVecs[2][1],-altCornerVecs[2][2]*(int(i/2))])

        self.allcombos = []

        for i in X_Multi:
            for j in Y_Multi:
                for k in Z_Multi:
                    self.allcombos.append(np.array(i)+np.array(j)+np.array(k))

        file_open = open("Multiply.xyz","w")
        file_open.close()

        for i in range(len(coordinates)):
            #frame_coordinates = []
            file_open = open("Multiply.xyz","a")
            print(len(selection)*u_x*u_y*u_z,file=file_open)
            print("Multiplied Cell",file=file_open)
            for k in self.allcombos:
                for j in selection:
                        coords = np.array([coordinates[i][j][1],coordinates[i][j][2],coordinates[i][j][3]]) + k
                        print(coordinates[i][j][0],coords[0],coords[1],coords[2],file=file_open)
            file_open.close()    

        if filename!=None:

            temp = read("Multiply.xyz",index=':')
            write(filename,temp)
            #os.remove("Multiply.xyz")      
