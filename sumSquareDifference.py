import sys
from math import pow

sumSqr = 0
sqrSum = 0

n = int(sys.argv[1])    #how many digits do you want? (from one to n, give n)

sqr = []
numbers = list([])

for i in range(1, n + 1):
    numbers.append(i)
    sumDigits = sum(numbers)
    sqrSum = int(pow(sumDigits, 2))

    sqr.append(int(pow(numbers[i-1], 2)))
    sumSqr = sum(sqr)

diff = sqrSum - sumSqr
print(sumSqr)
print(sqrSum)
print("the difference is: ", diff)










