sm=0
for i in range(int(input())):
    x,y=map(int,input().split())
    if x>y and y%2==0:
        for p in range(y+1,x,1):
            if p%2!=0:
                sm+=p
    elif x>y and y%2!=0:
        for p in range(y+1,x,1):
            if p%2!=0:
                sm+=p
    elif x<y and x%2==0:
        for p in range(x+1,y,1):
            if p%2!=0:
                sm+=p

    elif x<y and x%2!=0:
        for p in range(x+1,y,1):
            if p%2!=0:
                sm+=p

    print(sm)
    sm=0

