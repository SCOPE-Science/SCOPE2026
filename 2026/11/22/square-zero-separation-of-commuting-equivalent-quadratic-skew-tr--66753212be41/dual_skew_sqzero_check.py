"""Exhaustive independent square-zero enumerations in quadratic skew truncations.

Run: python dual_skew_sqzero_check.py
Coefficients are pairs (a,b) for a+b*z, with z*z=d, sigma(z)=-z.
All arithmetic uses a direct Ore-product implementation, not the proof's valuation recursion.
"""
from itertools import product
from collections import Counter

def e_mul(x,y,q,d):
    return ((x[0]*y[0]+d*x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q)

def e_tau(x,q):return (x[0],(-x[1])%q)

def square_zero(x,q,d):
    n=len(x)
    out=[(0,0)]*n
    for i,ci in enumerate(x):
        if ci==(0,0):continue
        for j in range(n-i):
            cj=x[j]
            if cj==(0,0):continue
            t=e_mul(ci,cj if i%2==0 else e_tau(cj,q),q,d)
            out[i+j]=((out[i+j][0]+t[0])%q,(out[i+j][1]+t[1])%q)
    return all(z==(0,0) for z in out)

def count(q,n,d,split):
    els=list(product(range(q),repeat=2))
    counts=Counter()
    for tup in product(els,repeat=n):
        if square_zero(tup,q,d):
            v=next((i for i,t in enumerate(tup) if t!=(0,0)),n)
            counts[v]+=1
    upper=n//2
    exp={n:1}
    for k in range(upper+1,n):
        exp[k]=(q*q-1)*q**(2*(n-k-1))
    if split:
        for k in range(1,upper+1,2):
            exp[k]=2*(q-1)*q**(n-1)
    assert dict(counts)==exp,(q,n,d,split,counts,exp)
    expected=q**(n-1)*(1+2*((n+1)//4)*(q-1)) if split else q**(n-1)
    assert sum(counts.values())==expected
    print(f'q={q} n={n} d={d} type={"split" if split else "field"}: squarezero={expected}; valuation counts={sorted(counts.items())}')

if __name__=='__main__':
    count(3,3,1,True)
    count(3,3,2,False)
    count(3,5,1,True)
    count(3,5,2,False)
    count(5,3,1,True)
    count(5,3,2,False)
    print('ALL_CHECKS_PASS')
