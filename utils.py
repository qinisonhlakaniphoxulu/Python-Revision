def find_max(list):
    is_not_empty = len(list) > 0
    if is_not_empty == True:
        max = list[0]
        for value in list:
            if type(value) != int:
                return "Please enter numerical values"
            if value > max:
                max = value
        return max
    
    else:
        return "Your list is empty"