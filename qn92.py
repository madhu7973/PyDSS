letters = 'acbd defg'
found_dict = {}
for i in letters:
    if i in found_dict:
        print(i)
        break
    else:
        found_dict[i]= 1