'''
Created on May 31, 2020

@author: wilmerlin
'''

import sorting

from tkinter import *
import random
import time
  
root = Tk()
width = 500
height = 500
    
#creates base
canvas = Canvas(root,width = width,height = height)
canvas.grid(row=1,column=0)
 
#sorting buttons 
selection_sort = Button(root, text = "Selection sort", command =lambda: sorting.selectionsort())
selection_sort.grid(row=0,column=0)  
  
#creates scale setting
array_size = Scale(root, from_=10, to=100,orient = HORIZONTAL,length = 200)
array_size.grid(row=0,column=1)

#contains rectangle objects
rect_arry = []
#contains length to be sorted
value_arry = []   

#creates initial array of values
for x in range(1,array_size.get()+1):
    value_arry.append(x)
    
#shuffles array
random.shuffle(value_arry)

#creates rectangle objects based on array elements
for x in range(0,array_size.get()):
    x0 = 50+(400/array_size.get())*x
    y0 = 10
    x1 = 50+(400/array_size.get())*(x+1)
    y1 = 10+(300/array_size.get())*value_arry[x]
    rect_arry.append(canvas.create_rectangle(x0,y0,x1,y1))
    

