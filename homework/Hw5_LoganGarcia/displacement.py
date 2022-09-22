def displacement(u_init, t, a):
    """ 
        Parameters:
        u_init:  initial speed of body
        t: time duration of displacement of body
        a: constant acceleration of body

        Returns: 
        s: displacement
  
    """
    s = u_init * t + (0.5 * a *( t * t))
    return s