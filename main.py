'''
Created on May 30, 2020

@author: wilmerlin
'''
from tkinter import *

import random
import model
import time

#resizes array based on scale value
def resize(rect_arr, size, canvas):
    for bar in rect_arr:
        canvas.delete(bar)
    rect_arr = []
    value_arr = []
            
    for x in range(1,size+1):
        value_arr.append(x)
    random.shuffle(value_arr)
    
    for x in range(0,size):
        x0 = 50+((model.width-100)/size)*x
        y0 = 10
        x1 = 50+((model.width-100)/size)*(x+1)
        y1 = 10+((model.height-200)/size)*value_arr[x]
        rect_arr.append(canvas.create_rectangle(x0,y0,x1,y1, fill = "white"))
    return (rect_arr, value_arr)
    
if __name__ == '__main__':

    
     
    current_size = model.array_size.get()
  
    while(True):
        if(current_size != model.array_size.get()):
            new_values = resize(model.rect_arry, model.array_size.get(), model.canvas)
            model.rect_arry = new_values[0]
            model.value_arry = new_values[1]
                  
            current_size = model.array_size.get()
            
        model.root.update()
        
     
 
    
    model.root.mainloop()


