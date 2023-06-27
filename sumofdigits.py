'''def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 12345
print(getSum(n))'''


def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10

    return sum


n = 12345
print(getSum(n))