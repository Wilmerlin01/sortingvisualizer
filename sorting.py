'''
Created on May 31, 2020

@author: wilmerlin
'''

import model
import time

def selectionsort():
    for i in range(0,len(model.value_arry)):
        min_ind = i
        model.canvas.itemconfig(model.rect_arry[i], fill = "green")
        
        for j in range(i+1, len(model.value_arry)):
                
            model.canvas.itemconfig(model.rect_arry[j], fill = "red")
            
            if(model.value_arry[j]<model.value_arry[min_ind]):
                
                #model.canvas.itemconfig(model.rect_arry[min_ind], fill = "red")
                min_ind = j
                model.canvas.itemconfig(model.rect_arry[min_ind], fill = "green")

        
        model.value_arry[i],model.value_arry[min_ind] = model.value_arry[min_ind],model.value_arry[i]
        
        #swap in rectangle array
        current_coords = model.canvas.coords(model.rect_arry[i])
        min_coords = model.canvas.coords(model.rect_arry[min_ind])
        
        model.canvas.move(model.rect_arry[i],min_coords[0]-current_coords[0],0)
        model.canvas.move(model.rect_arry[min_ind],-(min_coords[0]-current_coords[0]),0)
        model.canvas.itemconfig(model.rect_arry[min_ind], fill = "#a68fbf")
        
        model.rect_arry[i], model.rect_arry[min_ind] = model.rect_arry[min_ind],model.rect_arry[i]

        
        model.root.update()
        time.sleep(0.05)
        
    
def partition_high_pivot(low,high):
    lower = low-1
    pivot = model.value_arry[high]
    
    for i in range(low,high):
        if model.value_arry[i] < pivot:
            lower +=1
            
            model.value_arry[lower],model.value_arry[i] = model.value_arry[i],model.value_arry[lower]
            
            current_coords = model.canvas.coords(model.rect_arry[lower])
            other_coords = model.canvas.coords(model.rect_arry[i])
            model.canvas.move(model.rect_arry[lower],other_coords[0]-current_coords[0],0)
            model.canvas.move(model.rect_arry[i],-(other_coords[0]-current_coords[0]),0)
            model.rect_arry[i], model.rect_arry[lower] = model.rect_arry[lower],model.rect_arry[i]
            model.root.update()
            #time.sleep(0.001)
            
            
    model.value_arry[lower+1],model.value_arry[high] = model.value_arry[high],model.value_arry[lower+1]
    
    current_coords = model.canvas.coords(model.rect_arry[lower+1])
    other_coords = model.canvas.coords(model.rect_arry[high])
    model.canvas.move(model.rect_arry[lower+1],other_coords[0]-current_coords[0],0)
    model.canvas.move(model.rect_arry[high],-(other_coords[0]-current_coords[0]),0)
    model.rect_arry[lower+1], model.rect_arry[high] = model.rect_arry[high],model.rect_arry[lower+1]
    
    model.canvas.itemconfig(model.rect_arry[lower+1], fill = "#a68fbf")
    model.root.update()
    return lower+1

def quickSort_high_pivot(low,high):
    if(low < high):
        new_pivot = partition_high_pivot(low, high)
        
        quickSort_high_pivot(low, new_pivot-1)
        quickSort_high_pivot(new_pivot+1, high)
        
    if(low==0 and high == len(model.value_arry)-1):
        for i in range(0,high+1):
            if(model.canvas.itemcget(model.rect_arry[i],"fill") == "white"):
                model.canvas.itemconfig(model.rect_arry[i], fill = "#a68fbf")
                model.root.update()
                time.sleep(0.05)
    