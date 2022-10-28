def find_nth(mstring, sstring, n):
    start = mstring.find(sstring)
    while start >= 0 and n > 1:
        start = mstring.find(sstring, start+len(sstring))
        n -= 1
    return start
 
char = find_nth("foofoofoofoofoo", "foo",5)
print(char)

# import re
# s = "yoofpofbof"
# n = 3
# result = [m.start() for m in re.finditer(r"of" , s)]
# if(len(result)<=n):
#     print(result[n-1])
