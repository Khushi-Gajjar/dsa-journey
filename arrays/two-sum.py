nums = [2,7,11,15]
target = 9
seen=set()
for i in nums:
    res=target-i
    if res in seen:
        print(res,i)
    else:
        seen.add(i)