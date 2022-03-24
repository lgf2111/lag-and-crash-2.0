# Python program to convert
# numpy array to image
  
# import required libraries
import numpy as np
from PIL import Image as im
  
# define a main function
#With file path, get file data and convert to array
dataArray = []
with open("flag.txt", "r") as f:
    for line in f:
        for character in line:
            print(character)
            dataArray.append(ord(character))

print(dataArray)
lengthOfData = len(dataArray)
print(lengthOfData)
counter = 0
while len(dataArray) < 102240:
    if (counter==lengthOfData):counter=0
    dataArray.append(dataArray[counter])
    counter+=1
# create a numpy array using array function.
# 426 x 240 = 102240 is the amount of pixels.
# np.uint8 is a data type containing
# numbers ranging from 0 to 255 
# and no non-negative integers

#To insert array below
array = np.array(dataArray, dtype=np.uint8)
print(array)
# check type of array
print(type(array))
    
# our array will be of width 
# 102240 pixels That means it 
# will be a long dark line
print(array.shape)
    
# Reshape the array into a 
# familiar resolution

# variable array to be replaced
array = np.reshape(array, (426, 240))
    
# show the shape of the array
print(array.shape)

# show the array
print(array)
    
# creating image object of
# above array
dataInImage = im.fromarray(array)
    
# saving the final output 
# as a PNG file
dataInImage.save("flag.png")
