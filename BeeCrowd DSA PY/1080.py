
x=[]
mx=ind=0
for i in range(1,6,1):
    a=int(input())
    x.append(a)
    if a>mx:
        mx=a
        ind=i
print(mx)
print(ind)
