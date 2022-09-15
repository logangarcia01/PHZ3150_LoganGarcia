def force_acceleration ( F, m ): 
    """function that finds the acceleration of am object using the force divided by the mass
        Follows : a = F / m
        Input : Force [N], mass [kg]
        output : acceleration [m/s^2]"""
    
    a = F / m
    
    print( 'The acceleration of the object is' , a , 'm/s^2')
    
    return a