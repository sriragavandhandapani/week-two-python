n=int(input("Enter rows:"))
for i in range(1,n+1):
    x=" *"
    x=x*i
    print(f'{x:^10}')