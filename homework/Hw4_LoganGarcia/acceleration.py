def acceleration(u1,u2,t1,t2):
    """function that takes the chang of a body's speed over a time interval
    
    Input: initial speed [m/s], ending speed [m/s], inital time [s], ending time [s]
    
    Output: acceleration [m/s^2]  """
    
     a = (u2-u1)/(t2-t1)
        
        print( 'The acceleration of the object is' , a , 'm/s^2')
        
        return a
            