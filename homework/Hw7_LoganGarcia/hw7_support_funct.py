import numpy as np

def circle(x, x0, y0, r):
    
    """
    Input: x0,x,y0,r. These are the x coordinates and y coordinate along with the radius.
    
    Output: y and plot of circle
    """
    a = np.sqrt(r**2 -(x-x0)**2)
    
    y1 = a +y0
    
    y2 = y0 - a
    
    return (y1,y2)
    
def order_array(input_array):
    """ Input: takes an array inputed
        output: Orders the array """
    i = 0
    for index in range(len(input_array)):
            val = input_array[i]
            i = i - 1
    
            while i>=0:
                if val < input_array[i]:
                    input_array[i+1] = input_array[i]
                    input_array[i] = val
                    i-=1
                else:
                    break
        
        
    print(input_array)