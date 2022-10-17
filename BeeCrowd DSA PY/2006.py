x=[1,2,3,4]
c_guess=0
tea=int(input())
a,b,c,d,e=map(int,input().split())
for i in a,b,c,d,e:
    if i==tea:
        c_guess+=1
print(c_guess)
    