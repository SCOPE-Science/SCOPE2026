"""Exact checks for signed maximal independent sets of a path.
Standard library only.  Run: python check_path_mis.py
"""
from itertools import product

BLOCK = (1, -1, 1, -1, 1, -1, 1)

def maximal_masks(n):
    full = (1 << n) - 1
    return [s for s in range(1 << n)
            if not (s & (s << 1))
            and (s | (s >> 1) | (s << 1)) & full == full]

def signed_sum_direct(n, signs):
    total = 0
    for mask in maximal_masks(n):
        t = 1
        for j in range(n):
            if mask & (1 << j):
                t *= signs[j]
        total += t
    return total

def step(v, z):
    a,b,c = v
    return (c, z*(a+c), b)

def signed_sum_transfer(signs):
    assert len(signs) >= 2
    v = (0, signs[1], signs[0])
    for z in signs[2:]:
        v = step(v,z)
    return v[1] + v[2]

def hadamard_inplace(a):
    n = len(a)
    length = 1
    while length < n:
        for i in range(0,n,2*length):
            for j in range(i, i+length):
                x,y=a[j],a[j+length]
                a[j],a[j+length]=x+y,x-y
        length *= 2

for n in range(2,15):
    masks=maximal_masks(n)
    arr=[0]*(1<<n)
    for m in masks: arr[m]=1
    hadamard_inplace(arr)
    zero=sum(y == 0 for y in arr)
    predicted=(n%7 in (2,3,5))
    assert (zero>0)==predicted,(n,zero,predicted)
    assert arr[0]==len(masks)
    print('n',n,'sets',len(masks),'zero Fourier coefficients',zero)
    if n<=10:
        for bits in range(1<<n):
            signs=tuple(-1 if bits & (1<<j) else 1 for j in range(n))
            assert signed_sum_transfer(signs)==arr[bits]

# Explicit universal seven-vertex transfer identity in long dimensions.
for n in range(2,111):
    signs=tuple((-1 if (j*17+n*11)%5<2 else 1) for j in range(n))
    assert signed_sum_transfer(signs+BLOCK)==-signed_sum_transfer(signs)

# Construct zero witnesses for every length in all three classes.
seeds={2:(1,-1), 3:(1,1,-1), 5:(-1,1,1,1,1)}
for n in range(2,211):
    if n%7 in (2,3,5):
        k=(n-{2:2,3:3,5:5}[n%7])//7
        signs=seeds[n%7]+BLOCK*k
        assert len(signs)==n
        assert signed_sum_transfer(signs)==0

print('PATH_MIS_FOURIER_PERIOD_SEVEN_ALL_CHECKS_PASS')
