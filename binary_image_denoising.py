import numpy as np
from numpy import asarray
from PIL import Image
import statistics
import copy

image = Image.open("bakteries.bmp")
image = image.convert('1')
matrix = asarray(image, dtype = np.uint8)



def frame(matrix01,WB):
    line = 0
    newmatrix = matrix01
    for i in matrix01: 
        i[0] = WB
        i[-1] = WB
        newmatrix[line] = i
        line = line + 1
    line = 0
    for i in newmatrix[0]:
        newmatrix[0][line] = WB
        line = line + 1
    line = 0
    for i in newmatrix[-1]:
        newmatrix[-1][line] = WB
        line = line + 1
    return newmatrix
    
def denoising(matrix01):
    newmatrix = copy.deepcopy(matrix01)
    width = len(matrix01)
    z = 0
    for x in range(1,width - 1):
        for y in range(1,width - 1):
                mean = statistics.median([matrix01[x + 1][y - 1],matrix01[x + 1][y],matrix01[x + 1][y+1],
                                            matrix01[x][y - 1],matrix01[x][y],matrix01[x][y+1],
                                            matrix01[x-1][y-1],matrix01[x-1][y],matrix01[x-1][y+1]])
                if mean == 1:
                    newmatrix[x][y] = 1
                elif mean == 0:
                    newmatrix[x][y] = 0


    return newmatrix


def dilation(matrix01):
    newmatrix = copy.deepcopy(matrix01)
    width = len(matrix01)
    for x in range(1,width - 1):
        for y in range(1,width - 1):
                if matrix01[x][y] == 0 :
                     neighbors = [matrix01[x + 1][y - 1],matrix01[x + 1][y],matrix01[x + 1][y+1],
                                 matrix01[x][y - 1],matrix01[x][y+1],
                                 matrix01[x-1][y-1],matrix01[x-1][y],matrix01[x-1][y+1]]
                     for i in neighbors:
                          if i == 1:
                               newmatrix[x][y] = 1
                               break
    return newmatrix
    

def erosion(matrix01):
    newmatrix = copy.deepcopy(matrix01)
    width = len(matrix01)
    for x in range(1,width - 1):
        for y in range(1,width - 1):
                neighbors = [matrix01[x + 1][y - 1],matrix01[x + 1][y],matrix01[x + 1][y+1],
                                 matrix01[x][y - 1],matrix01[x][y+1],
                                 matrix01[x-1][y-1],matrix01[x-1][y],matrix01[x-1][y+1]]
                if matrix01[x][y] == 1 :
                     for i in neighbors:
                          if i == 0:
                               newmatrix[x][y] = 0
                               break
    return newmatrix
     






nm = erosion(denoising(denoising(dilation(denoising(frame(matrix,0))))))

img = Image.fromarray(nm * 255)
img.show()
