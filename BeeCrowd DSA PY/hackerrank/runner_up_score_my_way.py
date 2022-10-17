arr=[]
n=int(input())
for m in range(n):
     arr.append(int(input()))
mx_no=max(arr)
mx_2=0
for i in arr:
    if i==mx_no:
        continue
    else:
        if i>=mx_2:
            mx_2=i


print(mx_2)
