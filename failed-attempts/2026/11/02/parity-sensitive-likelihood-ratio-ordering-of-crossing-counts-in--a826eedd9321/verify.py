#!/usr/bin/env python3
"""Exact checks for matching-cut crossing distribution and parity-sensitive ordering."""
from fractions import Fraction
from math import factorial
from functools import lru_cache

checks = 0

def check(test, context):
    global checks
    checks += 1
    if not test:
        raise AssertionError(context)

def double_factorial_odd(n):
    out = 1
    for j in range(1,n+1,2): out *= j
    return out

def law(m, a):
    b = m-a
    den = double_factorial_odd(m-1)
    return {
        k: Fraction(factorial(a)*factorial(b),
              factorial(k)*2**((m-2*k)//2)*factorial((a-k)//2)*factorial((b-k)//2)*den)
        for k in range(min(a,b)+1) if ((a-k)&1)==0 and ((b-k)&1)==0
    }

@lru_cache(None)
def enumerated(m, a):
    freq = {}
    def rec(remaining, edges):
        if not remaining:
            cross = sum((u<a) != (v<a) for u,v in edges)
            freq[cross] = freq.get(cross,0)+1
            return
        u=remaining[0]
        for j in range(1,len(remaining)):
            v=remaining[j]
            rec(remaining[1:j]+remaining[j+1:], edges+((u,v),))
    rec(tuple(range(m)),())
    den = sum(freq.values())
    return {k:Fraction(x,den) for k,x in freq.items()}

for m in range(4,14,2):
    for a in range(m+1):
        p=law(m,a)
        check(sum(p.values()) == 1, ('normalization',m,a))
        check(p==enumerated(m,a),('exhaustive',m,a,p,enumerated(m,a)))
        check(sum(k*v for k,v in p.items())==Fraction(a*(m-a),m-1),('mean',m,a))
for m in range(4,42,2):
    N=m//2
    for a in range(N+1):
        p=law(m,a)
        check(sum(p.values())==1,('sum',m,a))
        if a<N:
            q=law(m,a+1)
            check(sum(k*v for k,v in q.items())>sum(k*v for k,v in p.items()),('mean rise',m,a))
            if a>=1:
                d={t:sum(q.get(j,0) for j in range(t,m+1))-sum(p.get(j,0) for j in range(t,m+1)) for t in range(1,m+1)}
                check(min(d.values())<0 and max(d.values())>0,('incomparable',m,a,d))
                t=1 if a%2 else 2
                check(d[t]==-Fraction(t,m-a)*p[t],('threshold down',m,a,t))
                check(d[t+1]==Fraction(m-a-t,m-a)*p[t],('threshold up',m,a,t))
        if a+2<=N:
            q=law(m,a+2)
            common=sorted(p)
            ratios=[q[k]/p[k] for k in common]
            check(all(x<y for x,y in zip(ratios,ratios[1:])),('LR',m,a,ratios))
            check(q[a+2]>0,('extra support',m,a))
            for k in common:
                b=m-a
                expected=Fraction((a+2)*(a+1)*(b-k),b*(b-1)*(a+2-k))
                check(q[k]/p[k]==expected,('ratio formula',m,a,k))
            for threshold in range(1,m+1):
                check(sum(q.get(j,0) for j in range(threshold,m+1))>=sum(p.get(j,0) for j in range(threshold,m+1)),('tail',m,a,threshold))
print(f'{checks} exact assertions passed; independent enumeration through 12 vertices')
