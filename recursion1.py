
def add(m,n):
    if n!=0:
        return add(m+1,n-1)
    else:
        return m
m=int(input("num1: "))
n=int(input("num2: "))
print(add(m,n))