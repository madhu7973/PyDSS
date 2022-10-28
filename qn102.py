list =[1,2,3,4,5,6,7,8,9,10]
even_list = []
odd_list = []
def sort_list(my_list):
  for i in my_list:
      if i % 2 == 0:
          even_list.append(i)
      else:
          odd_list.append(i)
#   even_list.sort(),odd_list.sort()
#   even_list.extend(odd_list)
  return even_list

sort_list(list)
print({1:odd_list, 0: even_list})