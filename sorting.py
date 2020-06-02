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


    

def insertionsort():
    
    for i in range(0,len(model.value_arry)):
        for j in range(0,i):
            if(model.value_arry[i] < model.value_arry[j]):
                model.value_arry[i], model.value_arry[j] = model.value_arry[j], model.value_arry[i]
                
                current_coords = model.canvas.coords(model.rect_arry[i])
                other_coords = model.canvas.coords(model.rect_arry[j])
                model.canvas.move(model.rect_arry[i], other_coords[0]-current_coords[0], 0)
                model.canvas.move(model.rect_arry[j], -(other_coords[0]-current_coords[0]), 0)
                model.canvas.itemconfig(model.rect_arry[i], fill = "#a68fbf")
                model.canvas.itemconfig(model.rect_arry[j], fill = "red")
                model.rect_arry[i], model.rect_arry[j] = model.rect_arry[j],model.rect_arry[i]

                model.root.update()
                
        if(i == len(model.value_arry)-1):
            model.canvas.itemconfig(model.rect_arry[i],fill = "#a68fbf" )
            

    
        
def mergesort(val_arry, rect_arry,canvas_ind):
    #print(canvas_ind, "outside")
    
    if(len(val_arry) > 1):
        mid = len(val_arry)//2
        val_left = val_arry[:mid]
        val_right = val_arry[mid:]
        rect_left = rect_arry[:mid]
        rect_right = rect_arry[mid:]
        
        mergesort(val_left,rect_left,canvas_ind)
        mergesort(val_right,rect_right,mid)
        
        i = 0
        j = 0
        k = 0
        l = canvas_ind
        
        while(i < len(val_left) and j < len(val_right)):
            if(val_left[i] < val_right[j]):
                val_arry[k] = val_left[i]
                  
                current_coords = model.canvas.coords(rect_left[i])
                other_coords = model.canvas.coords(rect_arry[k])
                model.canvas.itemconfig(rect_arry[k],state = "hidden")
                model.canvas.itemconfig(rect_left[i],state = "hidden") 
                model.rect_arry[l] = model.canvas.create_rectangle(other_coords[0],current_coords[1],other_coords[2],current_coords[3],fill="white")
                rect_arry[k] = model.rect_arry[l]  
                i+=1
                model.root.update()
            else:
                val_arry[k] = val_right[j]
                
                current_coords = model.canvas.coords(rect_right[j])
                other_coords = model.canvas.coords(rect_arry[k])
                model.canvas.itemconfig(rect_arry[k],state = "hidden")
                model.canvas.itemconfig(rect_right[j],state = "hidden")
                model.rect_arry[l] = model.canvas.create_rectangle(other_coords[0],current_coords[1],other_coords[2],current_coords[3],fill="white")
                rect_arry[k] = model.rect_arry[l] 
                j+=1
                model.root.update()
            k+=1
            l+=1
        
        while(i < len(val_left)):
            val_arry[k] = val_left[i]

            current_coords = model.canvas.coords(rect_left[i])
            other_coords = model.canvas.coords(rect_arry[k])
            model.canvas.itemconfig(rect_arry[k],state = "hidden")
            model.canvas.itemconfig(rect_left[i],state = "hidden")
            model.rect_arry[l]=model.canvas.create_rectangle(other_coords[0],current_coords[1],other_coords[2],current_coords[3],fill="white")
            rect_arry[k] = model.rect_arry[l]  
            i+=1   
            k+=1
            l+=1
            model.root.update()
            
        while(j < len(val_right)):
            val_arry[k] = val_right[j]
            
            current_coords = model.canvas.coords(rect_right[j])
            other_coords = model.canvas.coords(rect_arry[k])
            model.canvas.itemconfig(rect_arry[k],state = "hidden")
            model.canvas.itemconfig(rect_right[j],state = "hidden")
            model.rect_arry[l]=model.canvas.create_rectangle(other_coords[0],current_coords[1],other_coords[2],current_coords[3],fill="white")
            rect_arry[k] = model.rect_arry[l]
            j+=1 
            k+=1   
            l+=1 
            model.root.update()
           
            
            
        model.root.update()
        
        if(mid == len(model.value_arry)//2):
            for x in range(0,model.array_size.get()):
                model.canvas.itemconfig(model.rect_arry[x], fill = "#a68fbf")
                current_coords = model.canvas.coords(model.rect_arry[x])
                model.canvas.move(model.rect_arry[x], (50+((model.width-100)/model.array_size.get())*x)-current_coords[0],0)
                model.root.update()
                
#             for x in model.rect_arry:
#                 print(tuple(model.canvas.coords(x)))
#                 model.canvas.itemconfig(x,state="normal",fill = "#a68fbf")
#                 model.canvas.move()
#                 model.root.update()
            

        
        
        
        
        
        
        
        
        