def distance_from_car( u, t ):
    """ Function that calculates the distance traveled by car moving at speed u over time t.
    Follows s = u * t, assuming constant speed
    Input: speed [ m/s], time [s]
    Output: distance [ m ] """
    
    s = u * t
    
    print( "your car moved", s, " m. " )
    
    return s