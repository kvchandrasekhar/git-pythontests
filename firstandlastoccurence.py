def firstandlast(arr, n, x):
    first = -1
    last = -1
    for i in range(0,n):
        if(x !=  arr[i]):
            continue
        if (first==-1):
            first=i
        last=i
    if(first !=  -1):
        print("first occurrence is :", first)
        print("last occurence is : ", last)
    else:
        print("not found")

arr=[2,3,4,5,6,7,8,7,6,5,4,5,5,5,5]
n= len(arr)
x=7
firstandlast(arr, n, x)


