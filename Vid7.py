print(complex(7.5))
print(complex(False))
print(complex("ten"))
print(complex('10.5'))
print(complex('0B1111'))
print(complex(False, True))
print(complex('10', '21'))
print(complex('10', 20))
print(complex(10,'20'))
print(complex(10, j))
print(bool(0))
print(bool(10))
print(bool('one'))
print(bool('zero'))
print(bool(0.5))
print(bool(-10))
print(bool(0.0))
print(bool(10+20j))
print(bool(10+0j))
print(bool(0+0j))
print(bool(0+20j))
print(bool(10.5+20.5j))
print(bool(1j))
print(bool('one'))
print(bool('zero'))
print(bool())
print(bool(''))
print(str(''))
print(str(10+20j))
print(str(True))
print(str(1j))
print(str(' '))
print(str(0.5))
print(str())
print(str('10'+20j))
print(str('10'+'20j'))
x = y = z = 10
print(x) 
print(y)
print(z)

id(x)
id(y)
id(z)

y = 'py'
x is y
x is not y

str1 = 'py'
str2 = 'py'
str1 is str2

a = 256
b = 256
a is b

a = 257
b = 257
a is b

a = 10.3
b = 10.3
a is b

a = 10+20j
b = 10+20j
a is b

a = 'py'
b = 'py'
a is b