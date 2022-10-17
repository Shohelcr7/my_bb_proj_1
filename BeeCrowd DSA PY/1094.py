c=r=s=0
for i in range(int(input())):
    a,b=input().split()
    a=int(a)
    if b=='c':
        c+=a
    elif b=='r':
        r+=a
    elif b=='s':
        s+=a

t=c+r+s
c1=(c/t)*100
r1=(r/t)*100
s1=(s/t)*100
print(f"Total: {t} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {c1:.2f} %")
print(f"Percentual de ratos: {r1:.2f} %")
print(f"Percentual de sapos: {s1:.2f} %")
