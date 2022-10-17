
tab,action=map(int,input().split())
a_type=''
for i in range(action):
    a_type=input()
    if a_type=='fechou':
        tab+=1
    elif a_type=='clicou':
        tab-=1
        
print(tab)