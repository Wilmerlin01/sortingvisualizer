'''
Created on May 31, 2020

@author: wilmerlin
'''

import sorting

from tkinter import *
import random
import time
  
root = Tk()
width = 1000
height = 800
    
#creates base
canvas = Canvas(root,width = width,height = height)
canvas.grid(row=1,column=0,columnspan = 4)
 
#sorting buttons 
selection_sort = Button(root, text = "Selection sort", command =lambda: sorting.selectionsort())
selection_sort.grid(row=0,column=0)  
  
quick_sort = Button(root, text = "Quick sort", command =lambda: sorting.quickSort_high_pivot(0, len(value_arry)-1))
quick_sort.grid(row=0,column=1)

merge_sort = Button(root, text = "Merge sort", command =lambda: sorting.mergesort(value_arry, rect_arry,0))
merge_sort.grid(row=0,column=2)  

#creates scale setting
array_size = Scale(root, from_=10, to=200,orient = HORIZONTAL,length = 400)
array_size.grid(row=0,column=3)

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
    x0 = 50+((width-100)/array_size.get())*x
    y0 = 10
    x1 = 50+((width-100)/array_size.get())*(x+1)
    y1 = 10+((height-200)/array_size.get())*value_arry[x]
    rect_arry.append(canvas.create_rectangle(x0,y0,x1,y1,fill = "white"))
    

