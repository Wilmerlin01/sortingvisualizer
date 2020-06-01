'''
Created on May 31, 2020

@author: wilmerlin
'''

import model
import time

def selectionsort():
#     for i in range(0,len(model.value_arry)):
#         model.canvas.itemconfig(model.rect_arry[i], fill = "red")
#         time.sleep(0.05)

    for i in range(0,len(model.value_arry)):
        min_ind = i
        model.canvas.itemconfig(model.rect_arry[i], fill = "green")
        
        for j in range(i+1, len(model.value_arry)):
                
            model.canvas.itemconfig(model.rect_arry[j], fill = "red")
            
            if(model.value_arry[j]<model.value_arry[min_ind]):
                
                #model.canvas.itemconfig(model.rect_arry[min_ind], fill = "red")
                min_ind = j
                model.canvas.itemconfig(model.rect_arry[min_ind], fill = "green")
                #time.sleep(0.05)
        
                

        #swaps in value array        
        temp = model.value_arry[i]
        model.value_arry[i] = model.value_arry[min_ind]
        model.value_arry[min_ind] = temp
        
        #swap in rectangle array
        
        #saves coords to be swapped
        current_coords = model.canvas.coords(model.rect_arry[i])
        min_coords = model.canvas.coords(model.rect_arry[min_ind])
        
        
        model.canvas.move(model.rect_arry[i],min_coords[0]-current_coords[0],0)
        
        model.canvas.move(model.rect_arry[min_ind],-(min_coords[0]-current_coords[0]),0)
        model.canvas.itemconfig(model.rect_arry[min_ind], fill = "#a68fbf")
        
        #swaps them in array
        temp = model.rect_arry[i]
        model.rect_arry[i] = model.rect_arry[min_ind]

        model.rect_arry[min_ind] = temp

        
        model.root.update()
        time.sleep(0.05)
        
    