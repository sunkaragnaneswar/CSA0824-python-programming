l = [1, 3, 4, 2, 2]
l1 = []
for i in l:
    if l.count(i) > 1:
        l1.append(i)
s=set(l1) 
print(list(s))
