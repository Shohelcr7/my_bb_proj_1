sm=0
ls=[]
while True:
    x,y=map(int,input().split())
    if x<=0 or y<=0:
        break
    else:
        if x<=y:
            for i in range(x,y+1,1):
                ls.append(i)
                sm+=i
            print(*ls, sep = ' ',end=f' Sum={sm}\n')
            sm=0
            ls=[]
        else:
            for i in range(y,x+1,1):
                ls.append(i)
                sm+=i
            print(*ls, sep = ' ' ,end=f' Sum={sm}\n')
            sm=0
            ls=[]
