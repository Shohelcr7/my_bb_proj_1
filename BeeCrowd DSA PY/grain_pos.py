a,b,c,d=map(int,input().split())
ind=[]
pos=1
for i in a,b,c,d:
    ind.append(i)
    if i==1:
        pos+=int(ind.index(i))
        
print(pos)