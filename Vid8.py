# a1 = 1
# a2 = 2
# print(a1, a2)

# x = [10, 25, 'thirty', 4+5j, True]
# y = bytes(x, 'utf-8')
# for z in y: print(z)

# a = ['ten', 'twenty', 'thirty','forty', 'fifty']
# b = bytes(a)
# for c in b: print(c)

# a = [True, False]
# b = bytes(a)
# for c in b: print(c) #1 and 0
# print(type(b))

# a = [1.1, 1.2, 1.3, 1.4, 1.5]
# b = bytes(a)
# for c in b: print(c)

# a = [10, 20, 30, 40, 50]
# b = bytes(a)
# for c in b: print(c)

a = [10, 20, 30]
b = bytearray(a)
a[0] = 23
for c in b: print(c)
