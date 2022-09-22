def quad (a, b, c):
    
    """Function will be working the quadratic formula and outputting the roots of the formula into two variables.
    
    Input: numbers given, (a,b,c)
    
    Output: Root1
            
            Root2
  """
    
    root1 = -b + np.sqrt(b-(4*a*c))
    
    root1 = root1/(2*a)
    
    root2 = -b - np.sqrt(b-(4*a*c))
    
    root2 = root2/(2*a)
    
    print (root1, root2)
    
    return [root1, root2]