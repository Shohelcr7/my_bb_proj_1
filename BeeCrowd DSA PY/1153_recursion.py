x=int(input())

def fact(x):
    if x==1:
        return 1
    else:
        res=x*fact(x-1)
        return res

print(fact(x))