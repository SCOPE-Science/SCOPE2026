#!/usr/bin/env python3
"""Independent direct trace and coefficient checks for forbidden single internal runs.
No external dependencies; invoke: python verify.py
"""
from itertools import product
from math import comb

def avoids(x,n,r,cyclic):
    m=r+2
    for i in range(n if cyclic else max(0,n-m+1)):
        bits=[(x>>((i+j)%n if cyclic else (i+j)))&1 for j in range(m)]
        if bits==[0]+[1]*r+[0]:
            return False
    return True

def predicted(mask,n,m,cyclic):
    return not any(all((mask>>((i+j)%n if cyclic else i+j))&1 for j in range(m)) for i in range(n if cyclic else max(0,n-m+1)))

def direct_check(n,r,cyclic):
    m=r+2
    concepts=[x for x in range(1<<n) if avoids(x,n,r,cyclic)]
    counts=[0]*(n+1)
    for mask in range(1<<n):
        coords=[i for i in range(n) if (mask>>i)&1]
        traces={tuple((x>>i)&1 for i in coords) for x in concepts}
        is_shattered=(len(traces)==1<<len(coords))
        expected=predicted(mask,n,m,cyclic)
        assert is_shattered==expected,(n,r,cyclic,mask,is_shattered,expected)
        if is_shattered:counts[len(coords)]+=1
    return counts

def polynomial_from_formula(n,m,cyclic):
    # dynamic coefficient extraction of B(x)^j, B=1+x+..+x^(m-1)
    def power_coeff(q,k):
        a=[1]+[0]*k
        for _ in range(q):
            b=[0]*(k+1)
            for i,c in enumerate(a):
                for v in range(min(m,k-i+1)):
                    b[i+v]+=c
            a=b
        return a[k]
    ans=[0]*(n+1)
    if cyclic:
        for q in range(1,n+1):
            k=n-q
            x=n*power_coeff(q,k)
            assert x%q==0
            ans[k]+=x//q
    else:
        for q in range(n+1):
            k=n-q
            ans[k]+=power_coeff(q+1,k)
    return ans

def run():
    cases=0;supports=0
    for r in range(1,5):
        m=r+2
        for n in range(0,11):
            a=direct_check(n,r,False)
            b=polynomial_from_formula(n,m,False)
            assert a==b,(n,r,'line formula',a,b)
            assert max(i for i,x in enumerate(a) if x)==n-n//m
            cases+=1;supports+=1<<n
            if n>=m:
                a=direct_check(n,r,True)
                b=polynomial_from_formula(n,m,True)
                assert a==b,(n,r,'cyclic formula',a,b)
                assert max(i for i,x in enumerate(a) if x)==n-(n+m-1)//m
                cases+=1;supports+=1<<n
    print('PASS direct trace tests:',cases,'cases,',supports,'supports; all polynomial coefficients and VC ranks verified')
    for n,r in [(8,2),(10,2),(10,3)]:
        print('example n,r',n,r,'line',polynomial_from_formula(n,r+2,False),'circle',polynomial_from_formula(n,r+2,True))
if __name__=='__main__':run()
