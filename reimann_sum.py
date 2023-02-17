def reimannSum(function, lower_bound, upper_bound, num_rectangles):
 
    #width of each rectangle
    width = (upper_bound - lower_bound) / num_rectangles
 
    #total area
    total_area = 0
 
    #loop over the rectangles
    for i in range(num_rectangles):
 
        #calculate the height of each rectangle
        height = function(lower_bound + i * width)
 
        #calculate the area of the rectangle
        area = width * height
 
        #add the area to the total
        total_area += area
 
    return total_area