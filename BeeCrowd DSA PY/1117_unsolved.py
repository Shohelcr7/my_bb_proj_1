sm=0
count=0
while True:
    x=float(input())
    if x>=0 and x<=10:
        sm+=x
        count+=1
        y=float(input())
        if y>=0 and y<=10:
            sm+=y
            count+=1
            avg=sm/2
            print(f"media = {avg:.2f}")
            break
        else:
            print("nota invalida")
            count-=1
            continue
    else:
        print("nota invalida")
        continue
