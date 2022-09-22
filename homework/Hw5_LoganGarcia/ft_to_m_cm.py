def ft_to_m_cm(student_h):
    
    #Final list to store the data in form of [[m,cm], [m,cm], ... ]
    
    numlist = []
    
    for singlist in student_h:
        
        meter = singlist[0] * 0.3048
        
        centimeter = singlist[1] * 0.0254
        
        updateList = [meter, centimeter]
        
        numlist.append(updateList)
    
    return numlist