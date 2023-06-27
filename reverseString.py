s = input("enter the string: ")
print(s[::-1]) # using slicing

# use while loop
s=input("enter the string: ")
i=len(s)-1
rev=""
while i>=0:
    rev=rev+s[i]
    i=i-1
print(rev)