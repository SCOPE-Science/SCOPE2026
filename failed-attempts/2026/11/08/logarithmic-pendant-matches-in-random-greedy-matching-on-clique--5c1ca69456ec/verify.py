"""Exact independent checks for random-edge greedy matching on complete-graph coronas."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
import math


def add_scaled(target, source, fac, shift):
    for k, v in source.items():
        target[k + shift] += fac * v


def full_state_law(n):
    # A labeled-vertex state-space recursion, without any lumping by the
    # number of unmatched core vertices.
    edges = [(i, j, False) for i in range(n) for j in range(i+1, n)]
    edges += [(i, n+i, True) for i in range(n)]
    @lru_cache(None)
    def rec(mask):
        candidates = [(i,j,leaf) for i,j,leaf in edges
                      if mask & (1<<i) and mask & (1<<j)]
        if not candidates:
            return ((0, Fraction(1)),)
        dist = defaultdict(Fraction)
        for i,j,leaf in candidates:
            child = dict(rec(mask & ~(1<<i) & ~(1<<j)))
            add_scaled(dist, child, Fraction(1,len(candidates)), int(leaf))
        return tuple(sorted(dist.items()))
    return dict(rec((1<<(2*n))-1))


def reduced_laws(N):
    arr = [{0: Fraction(1)}, {1: Fraction(1)}]
    for n in range(2,N+1):
        d=defaultdict(Fraction)
        add_scaled(d, arr[n-1], Fraction(2,n+1), 1)
        add_scaled(d, arr[n-2], Fraction(n-1,n+1), 0)
        arr.append(dict(d))
    return arr[:N+1]


def brute_order_law(n):
    edges = [(i,j,False) for i in range(n) for j in range(i+1,n)]
    edges += [(i,n+i,True) for i in range(n)]
    d=defaultdict(int)
    for order in permutations(edges):
        matched=set(); x=0
        for i,j,leaf in order:
            if i not in matched and j not in matched:
                matched.add(i); matched.add(j)
                x+=int(leaf)
        d[x]+=1
    return {k:Fraction(v,math.factorial(len(edges))) for k,v in d.items()}


def run():
    laws=reduced_laws(22)
    for n in range(1,8):
        assert full_state_law(n)==laws[n], ('full labeled disagreement',n)
    for n in range(1,4):
        assert brute_order_law(n)==laws[n], ('permutation disagreement',n)
    from sympy import symbols, Rational
    z=symbols('z')
    # Check the coefficient identity by a second extraction based on the
    # exponential formula for odd-cycle permutations.
    for n in range(0,19):
        # [t^k] exp(2z sum_{odd j} t^j/j)
        arr=[Rational(1)] + [Rational(0)]*(n+1)
        for odd in range(1,n+2,2):
            next_arr=[Rational(0)]*(n+2)
            for j in range(0,(n+1)//odd+1):
                fac=(2*z/Rational(odd))**j/math.factorial(j)
                for k in range(n+2-j*odd):
                    next_arr[k+j*odd]+=arr[k]*fac
            arr=next_arr
        pgf=(arr[n+1]/(2*z)).expand()
        from_law=sum(Rational(v.numerator,v.denominator)*z**k for k,v in laws[n].items())
        assert (pgf-from_law).expand()==0, ('GF mismatch',n)
    for n in range(0,23):
        assert sum(laws[n].values())==1
        assert all((k-n)%2==0 for k in laws[n])
        if n>=1:
            assert all(0<=k<=n for k in laws[n])
    # Asymptotic moment predictions from the exact probability recurrence.
    mu=[0.0,1.0]; second=[0.0,1.0]
    for n in range(2,100001):
        p=2/(n+1)
        m=p*(1+mu[-1])+(1-p)*mu[-2]
        s=p*(1+2*mu[-1]+second[-1])+(1-p)*second[-2]
        mu.append(m); second.append(s)
    n=100000
    mean_const=math.log(2)+0.5772156649015329-1
    var_const=math.log(2)+0.5772156649015329-math.pi**2/6
    assert abs(mu[n]-(math.log(n)+mean_const))<0.005
    assert abs((second[n]-mu[n]**2)-(math.log(n)+var_const))<0.005
    print('PASS: 7 exact labeled state laws, 3 exhaustive edge-permutation laws, 19 exact generating-function identities, 23 normalization/parity identities, two large-n cumulants')

if __name__=='__main__': run()
