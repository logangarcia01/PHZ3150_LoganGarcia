def kepler_3rd(period):
    """ Converts regular years to astronomical units
    Input: Normal Year
    Output: Astronomical Unit
    """
    import numpy as np
    
    year = np.divide(period, 365.25)
    
    #p1 = 1 year
    #α1 = 1 Astronomical
    #p2 = 'years'
    #α2 = distance Astronomical year
    
    Au = np.power(year,2/3)
    
    return Au