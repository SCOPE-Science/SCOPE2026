#!/usr/bin/env python3
"""Exact counts via root colour and nonzero independent edge differences."""
from itertools import product
from math import factorial

def multinomial(*ks):
    from math import prod
    return factorial(sum(ks))//prod(factorial(k) for k in ks)

def predicted(beta):
    m=len(beta);a=beta.count(0);b=beta.count(1);c=beta.count(2)
    return (-1)**m * (2*(-2)**a-(-2)**b-(-2)**c)

def check(n):
    m=n-1; hist={}; zeros=0
    for beta in product(range(3),repeat=m):
        counts=[0,0,0]
        for y in product((1,2),repeat=m):
            if sum(y)%3==0: continue
            counts[sum(i*j for i,j in zip(beta,y))%3]+=1
        assert counts[1]==counts[2], (n,beta,counts)
        actual=3*(counts[0]-counts[1])
        want=predicted(beta)
        assert actual==want,(n,beta,actual,want)
        hist[actual]=hist.get(actual,0)+1
        zeros+=(actual==0)
    if n%3==1:
        k=(n-1)//3
        z=multinomial(k,k,k)+(2*multinomial(k-1,k,k+1) if k>=1 else 0)
    else: z=0
    assert zeros==z,(n,zeros,z)
    return n,zeros,3**m-zeros,len(hist)

if __name__=='__main__':
    for n in range(3,10):print(*check(n))
    print('PASS increment enumeration')
