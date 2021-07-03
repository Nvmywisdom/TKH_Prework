def find_largest_name(names_list):
    
# names_list = 
    longest_name = ""
    for name in names_list :
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name
big_name = find_largest_name (["bob","Jimmy","max b","bernie","jordan","future hendrix"])
        