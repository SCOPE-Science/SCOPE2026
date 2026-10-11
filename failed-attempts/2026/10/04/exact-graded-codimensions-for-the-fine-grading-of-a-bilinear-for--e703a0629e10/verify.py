#!/usr/bin/env python3
from itertools import product
from math import comb


def brute(n,m):
    # alphabet 0,1,...,n; nonzero symbols record fine degrees e_i
    total=0
    for w in product(range(n+1), repeat=m):
        parity=[0]*n
        for a in w:
            if a:
                parity[a-1]^=1
        if sum(parity)<=1:
            total+=1
    return total

def formula(n,m):
    num=sum(comb(n,j)*(n+1-2*j)**(m+1) for j in range(n+1))
    den=2**n
    assert num % den == 0
    return num//den

for n in range(1,7):
    for m in range(1,9):
        b=brute(n,m)
        f=formula(n,m)
        assert b==f,(n,m,b,f)

for m in range(1,13):
    k=(3**(m+1)+2+(-1)**(m+1))//4
    assert k==formula(2,m)

print('n=2 first values:', [formula(2,m) for m in range(1,9)])
print('checked n=1..6, m=1..8 by exhaustive degree-word enumeration')
print('checked Klein specialization m=1..12')
print('CHECK_OK')
