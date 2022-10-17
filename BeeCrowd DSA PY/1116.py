for i in range(int(input())):
    x,y=map(int,input().split())
    if y==0:
        print("divisao impossivel")
    elif y!=0:
        div=x/y
        print(f"{div:.1f}")



