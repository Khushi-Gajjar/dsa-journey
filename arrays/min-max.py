def minmax(arr):
    n=len(arr)
    if n == 0:
        return None, None
    if n==1:
        return arr[0],arr[0]
    if arr[0]<arr[1]:
        mn,mx=arr[0],arr[1]
    else:
        mn,mx=arr[1],arr[0]
    for i in range(2,n,2):
        if i+1<n:
            if arr[i]<arr[i+1]:
                mn=min(mn,arr[i])
                mx=max(mx,arr[i+1])
            else:
                mn=min(mn,arr[i+1])
                mx=max(mx,arr[i])
        else:
            mn=min(mn,arr[i])
            mx=max(mx,arr[i])
    return mn,mx
arr=[2,4,8,10,7,3,6]
res=minmax(arr)
print(res)
                
    