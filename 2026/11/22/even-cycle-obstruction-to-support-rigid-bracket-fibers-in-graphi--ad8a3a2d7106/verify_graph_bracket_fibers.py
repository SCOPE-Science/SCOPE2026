"""Standalone exhaustive test of graphical Lie bracket fibers over small fields.

The test enumerates horizontal input pairs and compares with a matching-number
Fourier formula for graphs without even cycles. It also checks the even-cycle
boundary, where equal target zero patterns need not imply equal fibers.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod


def field(q):
    if q == 4:
        def mul(a, b):
            out = 0
            for _ in range(2):
                if b & 1:
                    out ^= a
                b >>= 1
                a <<= 1
                if a & 4:
                    a ^= 7  # x^2+x+1
            return out
        return (lambda a,b: a^b), (lambda a,b: a^b), mul
    assert q in (2,3,5)
    return (lambda a,b: (a+b)%q), (lambda a,b: (a-b)%q), (lambda a,b: (a*b)%q)


def direct_fibers(n, edges, q):
    _, sub, mul = field(q)
    out=Counter()
    vectors=list(product(range(q),repeat=n))
    for x in vectors:
        for y in vectors:
            z=tuple(sub(mul(x[i],y[j]),mul(x[j],y[i])) for i,j in edges)
            out[z]+=1
    return out


def max_matching(n, edges):
    best=0
    for mask in range(1<<len(edges)):
        used=0;count=0
        for k,(i,j) in enumerate(edges):
            if mask>>k&1:
                if (used>>i&1) or (used>>j&1):
                    break
                used|=(1<<i)|(1<<j)
                count+=1
        else:
            best=max(best,count)
    return best


def matching_formula(n, edges, q):
    m=len(edges)
    terms=[]
    for mask in range(1<<m):
        selected=[edges[i] for i in range(m) if (mask>>i)&1]
        nu=max_matching(n,selected)
        terms.append((mask, Fraction(q**(2*n-m), q**(2*nu))))
    out={}
    for z in product(range(q),repeat=m):
        t=tuple(q-1 if v==0 else -1 for v in z)
        value=sum((coeff*prod(t[i] for i in range(m) if mask>>i&1)
                   for mask,coeff in terms), Fraction(0))
        assert value.denominator==1, (n,edges,q,z,value)
        out[z]=int(value)
    return out


def test(n,edges,q):
    exact=direct_fibers(n,edges,q)
    prediction=matching_formula(n,edges,q)
    assert all(exact.get(z,0)==v for z,v in prediction.items()), (n,edges,q,[(z,exact.get(z,0),v) for z,v in prediction.items() if exact.get(z,0)!=v][:3])
    assert sum(exact.values())==q**(2*n)
    print('PASS', 'q=',q,'vertices=',n,'edges=',len(edges),
          'targets=',q**len(edges),'pairs=',q**(2*n),
          'distinct-fibers=',len(set(exact.values())),
          'min=',min(prediction.values()),'max=',max(prediction.values()))


def run():
    cases=[
      (2,[(0,1)],2),
      (3,[(0,1),(1,2),(2,0)],2),
      (3,[(0,1),(1,2),(2,0)],3),
      (3,[(0,1),(1,2),(2,0)],4),
      (4,[(0,1),(1,2),(2,3)],3),
      (5,[(i,(i+1)%5) for i in range(5)],2),
      (5,[(i,(i+1)%5) for i in range(5)],3),
      (5,[(i,(i+1)%5) for i in range(5)],4),
      (5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],2),
      (5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],3),
      (7,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(0,5),(5,6),(6,0)],2),
    ]
    for case in cases:
        test(*case)
    n=4;edges=[(0,1),(1,2),(2,3),(3,0)]
    for q in (3,4):
        exact=direct_fibers(n,edges,q)
        a=(1,1,1,1)
        b=(1,1,1,2)
        assert exact[a]!=exact[b]
        print('EVEN-CYCLE WITNESS',q,a,exact[a],b,exact[b])
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    run()
