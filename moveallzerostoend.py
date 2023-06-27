def moveallzerostoend(arr, n):
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]= arr[i]
            count+=1
    while count <n:
        arr[count]=0
        count+=1

arr = [1,3,5,0,8,9,0,7,6,0,8,4,0,3]
n=len(arr)
moveallzerostoend(arr, n)
print("Array after moveallzeros to end is :")
print(arr)
