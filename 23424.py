a=list(input())
c=int(input())
b=[]
for i in range(1,len(a)//c+1):
    n=c
    k=1

    while k<=c:

     b.append(a[i*n-k])
     k+= 1
print(b)

