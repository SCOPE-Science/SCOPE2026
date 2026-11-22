#!/usr/bin/env python3
"""Standalone exact checks for self-inverse partial isometries of finite stars."""
from itertools import combinations, permutations
from math import comb, factorial, lgamma, log, exp, sqrt

def telephone(k):
    return sum(factorial(k)//(2**j*factorial(j)*factorial(k-2*j))
               for j in range(k//2+1))

def rank_polynomial(m):
    a = [comb(m, k)*telephone(k) for k in range(m+1)]
    ans = [0]*(m+2)
    for k, value in enumerate(a):
        ans[k] += value
        ans[k+1] += value
    ans[2] += m
    return ans

def independent_enumeration(m):
    vertices = tuple(range(m+1))
    out = [0]*(m+2)
    for k in range(m+2):
        for dom in combinations(vertices, k):
            for image in permutations(dom):
                f = dict(zip(dom, image))
                if any(f[f[v]] != v for v in dom):
                    continue
                def distance(x,y):
                    return 0 if x==y else (1 if x==0 or y==0 else 2)
                if all(distance(x,y)==distance(f[x],f[y]) for x in dom for y in dom):
                    out[k]+=1
    return out

for m in range(2,7):
    predicted = rank_polynomial(m)
    observed = independent_enumeration(m)
    assert predicted == observed, (m,predicted,observed)
    assert sum(predicted) == 2*sum(comb(m,k)*telephone(k) for k in range(m+1))+m
    print('EXACT',m,','.join(map(str,predicted)))

# The auxiliary two-colour singleton assembly has exponential generating
# function exp(2*x+x*x/2), hence a(0)=1, a(1)=2, and
# a(m)=2*a(m-1)+(m-1)*a(m-2).
a0,a1=1,2
for m in range(2,101):
    anew=2*a1+(m-1)*a0
    assert anew == sum(comb(m,k)*telephone(k) for k in range(m+1))
    a0,a1=a1,anew

# Numerical illustrations ONLY, not used as proof of convergence.
for m in (25,50,100,200,400):
    r = sqrt(m+1)-1
    masses = [comb(m,u)*telephone(m-u) for u in range(m+1)]
    total = sum(masses)
    tv = sum(abs(value/total-exp(-r+u*log(r)-lgamma(u+1)))
             for u,value in enumerate(masses))/2
    print('POISSON_DIAGNOSTIC',m,format(tv,'.8f'))
print('STAR_PARTIAL_INVOLUTIONS_VERIFIED m=2..6; recurrence m<=100')
