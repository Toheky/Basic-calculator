from math import gcd

def lcm(arr):
    '''Algorithm for calculate the least common multiple.'''
    res = []
    if len(arr) % 2 == 0:
        for i in range(0,(len(arr)-1),2):
            res.append((arr[i] * arr[i+1])//gcd(arr[i], arr[i+1]))
    else:
        for i in range(0,(len(arr)-1),2):
            res.append((arr[i] * arr[i+1])//gcd(arr[i], arr[i+1]))
            res.append(arr[-1])
    if len(res) >= 2:
        return lcm(res)
    else:
        return res[-1]

def prod(a,b):
    '''Summation with product.'''
    cnt = 1
    for i in range(a,b+1):
        cnt *= i
    return cnt
    
def summ(a):
    '''Summation.'''
    cnt = 0
    for i in range(int(a[0]),int(a[1])+1):
        cnt += eval(a[2])
    return cnt
