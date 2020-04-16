import sys
from math import pow

sumSqr = 0
sqrSum = 0

n = int(sys.argv[1])    #how many first digits do you want? (from 1 to n, give n)

sqr = []
numbers = list([])

for i in range(1, n + 1):
    numbers.append(i)
    sumDigits = sum(numbers)
    sqrSum = int(pow(sumDigits, 2))

    sqr.append(int(pow(numbers[i-1], 2)))
    sumSqr = sum(sqr)

diff = sqrSum - sumSqr
print(sumSqr)   #gives the sum of 1^2 + 2^2 +...+n^2
print(sqrSum)   #gives the square of sum (1+2+3+...+n)^2
print("the difference is: ", diff)










