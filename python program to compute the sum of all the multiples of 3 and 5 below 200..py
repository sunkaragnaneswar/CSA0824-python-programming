c=0 
l=[]
for i in range(1,200):
    if i%3==0 and i%5==0:
        l.append(i) 
print(sum(l))
