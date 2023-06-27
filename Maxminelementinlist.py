list = [2,-1,4,5,6,7,9,7,5,3,3,5,6,7,89,6,5]

def maxmin(list):
    max=list[0]
    min=list[0]
    for n in list:
        if n>max:
            max=n
        elif n<min:
            min=n
    return max,min
print(maxmin(list))