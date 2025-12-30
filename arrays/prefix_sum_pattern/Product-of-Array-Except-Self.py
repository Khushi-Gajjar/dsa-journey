arr=[1,2,3,4]
n=len(arr)
res=[]
for i in range(n):
    product=1
    for j in range(n):
        if i!=j:
            product*=arr[j]
    res.append(product)
print(res)