#!/usr/bin/env python3
"""Exact independent checks for two-species antagonistic cycle adsorption.

States 0 (empty), 1 (A), 2 (B). All allowed proposals have
rate 1/2. Each empty site's A and B proposals are repeated forever;
blocked unsuccessful proposals do not change the state.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial


def direct_cycle_blockers(n):
    @lru_cache(None)
    def f(state):
        transitions=[]
        for i, x in enumerate(state):
            if x: continue
            left=state[(i-1)%n]
            right=state[(i+1)%n]
            for kind in (1,2):
                if (left and left!=kind) or (right and right!=kind):
                    continue
                child=state[:i]+(kind,)+state[i+1:]
                transitions.append(child)
        if not transitions:
            return Fraction(state.count(0))
        return sum((f(child) for child in transitions),Fraction()) / len(transitions)
    ans=f((0,)*n)
    return ans,f.cache_info().currsize


def direct_interval_blockers(m, same):
    left=1
    right=1 if same else 2
    @lru_cache(None)
    def f(state):
        edges=[]
        for i,x in enumerate(state):
            if x: continue
            a=left if i==0 else state[i-1]
            b=right if i==m-1 else state[i+1]
            for kind in (1,2):
                if (a and a!=kind) or (b and b!=kind):
                    continue
                edges.append(state[:i]+(kind,)+state[i+1:])
        if not edges: return Fraction(state.count(0))
        return sum((f(s) for s in edges),Fraction())/len(edges)
    return f((0,)*m)


def interval_recurrence(N):
    plus=[Fraction(0)]*(N+1)
    minus=[Fraction(0)]*(N+1)
    plus[1]=Fraction(0); minus[1]=Fraction(1)
    for m in range(2,N+1):
        common=sum((plus[j]+minus[j] for j in range(1,m-1)),Fraction())
        plus[m]=(plus[m-1]+common)/(m-1)
        minus[m]=(minus[m-1]+common)/(m-1)
    return plus,minus


def formula(n):
    S=sum((Fraction((-1)**k, factorial(k)) for k in range(n+1)),Fraction())
    return Fraction(n,2)*S-Fraction(n-1,2*factorial(n-1))


def main():
    maxm=80
    plus,minus=interval_recurrence(maxm)
    checks=0
    for m in range(1,maxm+1):
        assert minus[m]-plus[m] == Fraction(1,factorial(m-1))
        checks+=1
        # closed form from rational GF 0.5*(e^-z/(1-z)^2 - e^z)
        gfcoef=(sum((Fraction((-1)**k*(m-k),factorial(k)) for k in range(m)),Fraction())-Fraction(1,factorial(m-1)))/2
        assert plus[m]==gfcoef
        checks+=1
        assert plus[m]==formula(m+1)
        checks+=1
    for m in range(1,10):
        assert direct_interval_blockers(m,True)==plus[m]
        assert direct_interval_blockers(m,False)==minus[m]
        checks+=2
    for n in range(3,12):
        direct,states=direct_cycle_blockers(n)
        assert direct==plus[n-1]==formula(n),(n,direct,plus[n-1],formula(n))
        checks+=1
        print('n=',n,'E blocked=',direct,'P blocked site=',direct/n,'states=',states)
    for n in range(3,60):
        p=Fraction(formula(n),n)
        p_next=Fraction(formula(n+1),n+1)
        delta=Fraction(n*n-n-1+(-1)**(n+1),2*factorial(n+1))
        assert p_next-p==delta and delta>0
        checks+=1
    print('All',checks,'exact rational comparisons passed')

if __name__=='__main__': main()
