#!/usr/bin/env python3
"""Independent exact cyclic Rule-126 formula versus forward enumeration.
Public-domain style standalone verification: Python 3 stdlib only.
"""
from collections import Counter

def fib(k):
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a

def path_poly_at(k,t):
    # Independence polynomial of a path on k vertices (k=0,1,...),
    # with the empty edge gap k=-1 defined to contribute 1.
    if k<=0:return 1
    a,b=1,1+t  # P_0,P_1
    for _ in range(2,k+1):a,b=b,b+t*a
    return b

def inverse_count_formula(bits):
    n=len(bits)
    assert n>=1 and set(bits)<={0,1}
    if not any(bits):return 2
    if all(bits):
        lucas=fib(n-1)+fib(n+1)
        return lucas+(2 if n%3==0 else -1)
    starts=[i for i in range(n) if bits[i]==0 and bits[(i-1)%n]==1]
    assert starts
    rotated=[bits[(starts[0]+i)%n] for i in range(n)]
    zeros=0;runs=[];p=0
    while p<n:
        z=0
        while p<n and rotated[p]==0:z+=1;p+=1
        assert z>=1
        zeros+=z
        ell=0
        while p<n and rotated[p]==1:ell+=1;p+=1
        assert ell>=1
        runs.append(ell)
    if any(ell==1 for ell in runs):return 0
    forced= zeros+len(runs)
    plus=minus=1
    for ell in runs:
        plus*=path_poly_at(ell-3,1)
        minus*=path_poly_at(ell-3,-1)
    return plus+ (minus if (n-forced)%2==0 else -minus)

def forward_rule126(x,n):
    out=0
    for i in range(n):
        a=(x>>((i-1)%n))&1
        b=(x>>i)&1
        c=(x>>((i+1)%n))&1
        out|= ((126>>((a<<2)|(b<<1)|c))&1)<<i
    return out

def test():
    for n in range(1,16):
        actual=Counter(forward_rule126(x,n) for x in range(1<<n))
        for y in range(1<<n):
            bits=[(y>>i)&1 for i in range(n)]
            got=inverse_count_formula(bits)
            assert got==actual[y], (n,y,got,actual[y])
        mx=max(actual.values())
        max_targets={y for y in range(1<<n) if actual[y]==mx}
        if n==1:assert mx==2 and max_targets=={0}
        elif n==2:assert mx==2 and max_targets=={0,3}
        else:
            assert max_targets=={(1<<n)-1},(n,max_targets)
        assert sum(inverse_count_formula([(y>>i)&1 for i in range(n)]) for y in range(1<<n))==1<<n
        print('n=',n,'image=',len(actual),'largest_fiber=',mx,'maximizers=',len(max_targets))
    print('FORMULA_VERIFY_OK')

if __name__=='__main__':test()
