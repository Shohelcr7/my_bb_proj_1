for i in range(int(input())):
    x,y,z=map(float,input().split())
    avg=((x*2)+(y*3)+(z*5))/10
    print(f"{avg:.1f}")
