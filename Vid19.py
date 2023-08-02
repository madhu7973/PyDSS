# n = int(input('enter numbser '))
# sum = 0
# i = 1
# while i <= n :
#    sum = sum + i
#    i +=1
# print('sum of first',n, 'numbers is:', sum)

# name = ''
# while name != 'madhu':
#    name = input('Enter correct name: ')
# print('hello', name, 'thanks for confirmation')

# name=''
# pwd = ''
# while name != 'madhu' or pwd != 'pyt':
#    name = input('enter name ')
#    pwd = input('enter pwd ')
# print('hello welcome ' + name)

# for i in range (3):
#    for j in range (3):
#       print('i = {} and j={}'.format(i,j))

n = int(input('enter the number of rows: '))
for i in range(1, n+1):
   for j in range(1, i+1):
      print('m', end=' ')
   print()