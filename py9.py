l=[1,2,3,1,3,4]
u=[]
for i in l:
    if i not in u and l.count (i)==1:
        u.append(i)
        print(list(u))
