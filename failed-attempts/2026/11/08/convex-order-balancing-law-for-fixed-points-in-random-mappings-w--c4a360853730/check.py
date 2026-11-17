#!/usr/bin/env python3
"""Exact finite cross-checks of prescribed-indegree random-map fixed-point laws.

This script uses only the Python standard library. Exhaustive finite checks corroborate,
but do not replace, the all-order analytic argument.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import factorial


def rising_poly_product(values):
    e = [1]
    for x in values:
        e.append(0)
        for j in range(len(e) - 1, 0, -1):
            e[j] += x * e[j - 1]
    return e


def falling(n, r):
    return factorial(n) // factorial(n-r)


def law_formula(d):
    n=len(d)
    e=rising_poly_product(d)
    binom_moments=[Fraction(e[r],falling(n,r)) for r in range(n+1)]
    from math import comb
    return [sum(((-1)**(r-k))*comb(r,k)*binom_moments[r]
                for r in range(k,n+1)) for k in range(n+1)]


def law_enum(d):
    n=len(d)
    counts=Counter(); arr=[None]*n; remaining=list(d)
    def visit(i):
        if i==n:
            counts[sum(arr[j]==j for j in range(n))]+=1
            return
        for j in range(n):
            if remaining[j]:
                remaining[j]-=1;arr[i]=j
                visit(i+1)
                remaining[j]+=1
    visit(0)
    den=sum(counts.values())
    assert den == factorial(n)//__import__('math').prod(factorial(x) for x in d)
    return [Fraction(counts.get(k,0),den) for k in range(n+1)]


def compositions(n, slots):
    if slots==1:
        yield (n,)
    else:
        for d in range(n+1):
            for tail in compositions(n-d,slots-1):
                yield (d,)+tail


def check():
    exact=0; comparisons=0
    for n in range(2,7):
        for d in compositions(n,n):
            p=law_enum(d)
            assert p==law_formula(d), (n,d,p,law_formula(d))
            assert sum(p)==1
            assert sum(k*p[k] for k in range(n+1))==1
            v=sum(Fraction((k-1)**2)*p[k] for k in range(n+1))
            assert v==Fraction(n*n-sum(x*x for x in d), n*(n-1))
            exact+=1
            for i in range(n):
                for j in range(n):
                    if d[i]<d[j]+2:continue
                    d2=list(d);d2[i]-=1;d2[j]+=1
                    new=law_formula(d2)
                    c=Fraction(d[i]-d[j]-1,n*(n-1))
                    rem=[d[k] for k in range(n) if k not in (i,j)]
                    dummy=d[i]+d[j]-2
                    if n==2:
                        ylaw=[Fraction(1)]
                    else:
                        e=rising_poly_product(rem)
                        ylaw=[sum(((-1)**(s-k))*__import__('math').comb(s,k)*Fraction(e[s],falling(n-2,s))
                            for s in range(k,n-1)) for k in range(n-1)]
                    assert sum(ylaw)==1 and all(x>=0 for x in ylaw)
                    assert all(new[k]-p[k]== c*sum(ylaw[y]*((1 if k==y else 0)
                             -(2 if k==y+1 else 0)+(1 if k==y+2 else 0))
                             for y in range(n-1)) for k in range(n+1)), (d,d2)
                    for t in range(n):
                        stop=lambda law:sum(Fraction(max(k-t,0))*law[k] for k in range(n+1))
                        assert stop(new)>=stop(p), (d,d2,t)
                    comparisons+=1
    print('PASS:',exact,'exhaustive degree vectors of orders 2..6;',comparisons,'exact transfer comparisons')

if __name__=='__main__': check()
