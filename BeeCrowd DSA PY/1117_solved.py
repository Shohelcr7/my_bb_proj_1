count=0
num_sum=0
while(True):
    try:
        if(count==2):
            break
        a = float(input())
        if(a>=0 and a<=10):
            count+=1
            num_sum+=a
        else:
            print("nota invalida")
    except EOFError:
        break
avg=num_sum/2.00
print(f"media = {avg:.2f}")
