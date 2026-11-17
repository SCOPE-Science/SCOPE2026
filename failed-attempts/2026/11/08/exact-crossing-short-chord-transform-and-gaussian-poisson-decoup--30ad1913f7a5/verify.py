#!/usr/bin/env python3
"""Exact finite checks for simple-chord/crossing identities (stdlib only)."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def pairings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for i in range(1, len(points)):
        b = points[i]
        rest = points[1:i] + points[i+1:]
        for p in pairings(rest):
            yield ((a, b),) + p


def statistics(pairs, n):
    small = sum((b == a+1 or (a == 0 and b == 2*n-1)) for a, b in pairs)
    cross = 0
    for (a,b),(c,d) in combinations(pairs, 2):
        cross += (a < c < b < d) or (c < a < d < b)
    return small, cross


def num_cycle_matchings(n, k):
    return 2*n*comb(2*n-k, k)//(2*n-k)


def double_fact_odd(n):
    v = 1
    for i in range(1,n+1):
        v *= 2*i-1
    return v


def exact_census(n):
    return Counter(statistics(p,n) for p in pairings(tuple(range(2*n))))


def main():
    checks=0
    T={0:Counter({0:1})}
    for n in range(1,7):
        tab=exact_census(n)
        if sum(tab.values()) != double_fact_odd(n):
            raise AssertionError((n,'matching count'))
        checks+=1
        T[n]=Counter()
        for (s,x),v in tab.items():
            T[n][x]+=v

        if n==1:
            assert tab==Counter({(1,0):1})
            checks+=1
            continue

        # Independently enumerate matchings in the boundary cycle for n<=5.
        if n<=5:
            E=[(i,(i+1)%(2*n)) for i in range(2*n)]
            for k in range(n+1):
                direct=sum(len(set(z for i in ids for z in E[i]))==2*k
                           for ids in combinations(range(2*n),k))
                assert direct==num_cycle_matchings(n,k),(n,k,direct)
                checks+=1

        for k in range(n+1):
            lhs=Counter()
            for (s,x),a in tab.items():
                if s>=k: lhs[x]+=comb(s,k)*a
            rhs=Counter({x:num_cycle_matchings(n,k)*a for x,a in T[n-k].items()})
            assert lhs==rhs,(n,k,lhs,rhs)
            checks+=len(set(lhs)|set(rhs))

        # Invert the entire binomial transform to reproduce the joint law.
        for x in range(n*(n-1)//2+1):
            for s in range(n+1):
                predicted=sum((-1)**(k-s)*comb(k,s)*num_cycle_matchings(n,k)*T[n-k][x]
                              for k in range(s,n+1))
                assert predicted==tab[(s,x)],(n,s,x,predicted,tab[(s,x)])
                checks+=1

        total=double_fact_odd(n)
        es=sum(s*a for (s,x),a in tab.items())
        ex=sum(x*a for (s,x),a in tab.items())
        es2=sum(s*s*a for (s,x),a in tab.items())
        ex2=sum(x*x*a for (s,x),a in tab.items())
        esx=sum(s*x*a for (s,x),a in tab.items())
        E_s=Fraction(es,total)
        E_x=Fraction(ex,total)
        V_s=Fraction(es2,total)-E_s**2
        V_x=Fraction(ex2,total)-E_x**2
        Cov=Fraction(esx,total)-E_s*E_x
        assert E_s==Fraction(2*n,2*n-1)
        assert E_x==Fraction(n*(n-1),6)
        assert V_s==Fraction(4*n*(n-1),(2*n-1)**2)
        assert V_x==Fraction(n*(n-1)*(n+3),45)
        assert Cov==Fraction(-2*n*(n-1),3*(2*n-1))
        assert Cov**2/V_s/V_x==Fraction(5,n+3) and Cov<0
        checks+=6
        print(f'n={n}: perfect matchings={total}, distinct joint cells={len(tab)}, covariance={Cov}, rho^2={Cov**2/V_s/V_x}')
    print(f'PASS: {checks} exact assertions (all pairings through n=6 and independent cycle-submatchings through n=5)')

if __name__=='__main__': main()
