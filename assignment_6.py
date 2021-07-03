male_names_list = ["bob","Jimmy","max b","bernie","jordan","future hendrix"]
def letter_count (names_list):
    even_names_list = []
    odd_names_list = []
    for name in names_list:
        if len(name) % 2 == 0:
            even_names_list.append(name)
        else:
            odd_names_list.append(name)
    print(even_names_list)
    print(odd_names_list)
letter_count(male_names_list)

    