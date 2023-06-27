n =  int(input("enter how many rows: "))
"""for i in range (1,n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()"""

for i in range (1,n+1):
    print(" "*(n-i), end="")
    print("* "*i)