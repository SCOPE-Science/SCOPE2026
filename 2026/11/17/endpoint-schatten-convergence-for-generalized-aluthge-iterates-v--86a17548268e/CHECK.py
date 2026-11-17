#!/usr/bin/env python3
"""Finite, supplementary arithmetic diagnostics for Aluthge singular-value bounds."""
import math
from fractions import Fraction

checks=0
def check(test):
    global checks
    assert test
    checks+=1

def geom_envelope(a):
    prod=1.0
    result=[]
    for k,x in enumerate(a,1):
        prod*=x
        result.append(prod**(1/k) if prod>0 else 0.0)
    return result

# Carleman's inequality has an infinite-sequence statement; finite prefixes
# of explicitly summable sequences provide a supplementary normalization check.
for n in (1,2,3,8,25,60):
    a=[1.0/(j+1)**2 for j in range(1,n+1)]
    g=geom_envelope(a)
    check(sum(g)<=math.e*sum(a)+1e-10)
    check(all(x>=0 for x in g))
    for j in range(n):
        check(g[j] <= math.e*sum((i+1)*a[i] for i in range(j+1))/((j+1)*(j+2))+1e-10)

# On a cyclic shift the Aluthge transformation takes positive weights to
# adjacent weighted geometric means. Its nonzero eigenvalues have common
# modulus equal to the geometric mean of all original weights.
for t in (.2,.35,.5,.8):
    for p in (.5,1.,1.7,2.,4.):
        original=(1.7,.9,1.2,2.1,0.8)
        initial=sorted((x**p for x in original),reverse=True)
        envelope=geom_envelope(initial)
        target=len(original)*math.exp(p*sum(math.log(x) for x in original)/len(original))
        w=list(original)
        for step in range(121):
            b=sorted((x**p for x in w),reverse=True)
            for k in range(len(b)):
                check(b[k] <= envelope[k]*(1+1e-10))
            check(sum(b)<=math.e*sum(initial)*(1+1e-10))
            w=[w[i]**(1-t)*w[(i+1)%len(w)]**t for i in range(len(w))]
        check(abs(sum(x**p for x in w)-target)<1e-5)

# A finite nilpotent unilateral shift illustrates the zero-eigenvalue edge.
for p in (.5,1.,2.,3.):
    for t in (.2,.5,.8):
        w=[1.8/(j+2) for j in range(21)]+[0.0]
        initial=sorted((x**p for x in w),reverse=True)
        envelope=geom_envelope(initial)
        for step in range(30):
            b=sorted((x**p for x in w),reverse=True)
            for k in range(len(b)):
                check(b[k] <= envelope[k]*(1+1e-9))
            w=[w[i]**(1-t)*w[i+1]**t for i in range(len(w)-1)]+[0.0]
        check(sum(x**p for x in w)<1e-13)
print(f"Finite diagnostic assertions passed: {checks}")
