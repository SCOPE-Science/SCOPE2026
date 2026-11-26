#!/usr/bin/env python3
"""Exact-arithmetic tests for optimal two-class trace probing on odd screened cycles."""
from fractions import Fraction
from itertools import product

checks=0

def insist(condition, msg):
    global checks
    if not condition:
        raise AssertionError(msg)
    checks+=1

def green(n,r):
    r=Fraction(r)
    c=r/((1-r*r)*(1-r**n))
    return [c*(r**d+r**(n-d)) for d in range(n)]

def trace_variance(g,s):
    n=len(s)
    return 4*sum((g[(j-i)%n]**2 for i in range(n) for j in range(i+1,n) if s[i]==s[j]),Fraction(0))

def exact_min(n,g):
    m=(n-1)//2
    return 4*sum((d if d%2 else n-d)*g[d]**2 for d in range(1,m+1))

for n in (5,7,9,11,13,15):
    m=(n-1)//2
    for r in (Fraction(1,5), Fraction(1,2),Fraction(4,5)):
        g=green(n,r)
        mu=(1-r)**2/r
        # The difference equation checks the inverse of the screened-cycle operator.
        for d in range(n):
            insist((mu+2)*g[d]-g[(d-1)%n]-g[(d+1)%n]==int(d==0),f'inverse {n=} {r=} {d=}')
        vals=[]
        minimum=exact_min(n,g)
        optimizer_count=0
        for bits in product((-1,1),repeat=n-1):
            s=(1,)+bits
            v=trace_variance(g,s)
            # exact global optimum, with a nonempty class.
            if all(x==1 for x in s):
                continue
            insist(v>=minimum,f'lower bound {n=} {r=} {s=}')
            S=sum(s)
            insist(abs(S)>=1 and abs(S)%2==1, f'odd magnetization {n=} {r=} {s=}')
            for k in range(2,m+1):
                wk=sum(sum(s[(i+a)%n] for a in range(k))**2 for i in range(n))
                insist(wk >= (n if k%2 else 2*k), f'window lower bound {n=} {r=} {k=} {s=}')
            if v==minimum:
                optimizer_count+=1
                insist(sum(s[i]==s[(i+1)%n] for i in range(n))==1,f'optimizer shape {n=} {r=} {s=}')
        insist(optimizer_count==n,f'optimizer count {n=} {r=} {optimizer_count=}')
        near=tuple(1 if i%2==0 else -1 for i in range(n))
        insist(trace_variance(g,near)==minimum,f'formula {n=} {r=}')
        for k in range(2,m+1):
            W=sum(sum(near[(i+a)%n] for a in range(k))**2 for i in range(n))
            insist(W==(n if k%2 else 2*k),f'window equality {n=} {r=} {k=}')
        # The discrete convex decomposition must reproduce the distance weights.
        w=[None]+[g[d]**2 for d in range(1,m+1)]+[g[m]**2]
        coeff={k:w[k-1]-2*w[k]+w[k+1] for k in range(2,m+1)}
        for k,v in coeff.items():
            insist(v>0,f'convex coefficient {n=} {r=} {k=}')
        for d in range(1,m+1):
            insist(w[d]==w[m]+sum((k-d)*coeff[k] for k in range(d+1,m+1)),f'weight decomposition {n=} {r=} {d=}')
        print(f'PASS odd n={n}, r={r}, exactly {optimizer_count} unlabeled minimizers')
print(f'PASS {checks} exact-rational checks')
