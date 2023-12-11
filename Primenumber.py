n=int(input('Enter a number '))
j=0
for i in range(2,n):
 if n%i ==0:
  print("not a Prime number")
  j=1
  break
if j==0:
 print("prime number")