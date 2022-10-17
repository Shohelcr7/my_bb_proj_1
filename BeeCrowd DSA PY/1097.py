a=7
for i in range(1,10,1):
    if i%2!=0:
        print(f"I={i} J={a}")
        print(f"I={i} J={a-1}")
        print(f"I={i} J={a-2}")
        a+=2
