# Recursion using sum and tail sum

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

def tailSum(n, accumulator = 0):
    if n == 0:
        return accumulator
    else:
        return tailSum(n-1, accumulator + n)
    
print(sum(10))
print(tailSum(10))