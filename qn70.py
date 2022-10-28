from collections import Counter
l=['apple', 'google','apple','yahoo','yahoo','facebook','apple','gmail','gmail','gmail']
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
      l2.append(i)
      #print(i,end=' ')
#print(l2)

c = Counter(l2)
dc = c.most_common()
print(dc)