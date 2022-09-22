def ft_to_m_cm(student_h):
    
    """ Function takes the height of the student and converts from standard system to metric system
   
            input: ft and inches
            output: Meters and Centimeters.
    """
    #Final list
    
    numlist = []
    
    for singlist in student_h:
        
        meter = singlist[0] * 0.3048
        
        centimeter = singlist[1] * 0.0254
        
        updateList = [meter, centimeter]
        
        numlist.append(updateList)
    
    return numlist