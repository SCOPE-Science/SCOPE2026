#!/usr/bin/env python3
"""Exact direct verification of pure inoculation equilibria on small cycles."""
from fractions import Fraction
from itertools import product
from math import comb, ceil, floor
from collections import defaultdict

def components_on_cycle(bits):
    n=len(bits)
    remaining={i for i,b in enumerate(bits) if b==0}
    pieces=[]
    while remaining:
        i=remaining.pop(); piece={i}; queue=[i]
        while queue:
            u=queue.pop()
            for v in ((u-1)%n,(u+1)%n):
                if v in remaining:
                    remaining.remove(v); piece.add(v); queue.append(v)
        pieces.append(piece)
    return pieces

def after_unvaccinated_component(bits,i):
    modified=list(bits);modified[i]=0
    return next(len(s) for s in components_on_cycle(modified) if i in s)

def direct_equilibrium(bits,t):
    return all((after_unvaccinated_component(bits,i)<=t if b==0 else after_unvaccinated_component(bits,i)>=t) for i,b in enumerate(bits))

def cost_in_units_of_L_over_n(bits,t):
    return sum(bits)*t+sum(len(s)**2 for s in components_on_cycle(bits))

def trace_poly_coefficient(n,k,t):
    h=min(t.numerator//t.denominator,n-k)
    total=0
    for starting in range(h+1):
        dp={(starting,0):1}
        for _ in range(k):
            nxt=defaultdict(int)
            for (previous,degree),count in dp.items():
                for current in range(min(h,n-k-degree)+1):
                    if previous+current+1>=t:
                        nxt[current,degree+current]+=count
            dp=nxt
        total+=dp.get((starting,n-k),0)
    numerator=n*total
    assert numerator%k==0,(n,k,t,numerator)
    return numerator//k

def formula_counts(n,t):
    out={}
    for k in range(n+1):
        if k==0:c=int(n<=t)
        elif k==1:c=n*int(n-1<=t<=n)
        else:c=trace_poly_coefficient(n,k,t)
        if c:out[k]=c
    return out

def direct_counts(n,t):
    out=defaultdict(int)
    for bs in product((0,1),repeat=n):
        if direct_equilibrium(bs,t):out[sum(bs)]+=1
    return dict(out)

def perrin(n):
    p=[3,0,2]
    for i in range(3,n+1):p.append(p[i-2]+p[i-3])
    return p[n]

def run():
    checked=0
    for n in range(3,12):
        ts=[Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(3),Fraction(7,2),Fraction(n-1,1),Fraction(n),Fraction(2*n+1,2)]
        for t in sorted(set(ts)):
            expected=direct_counts(n,t)
            actual=formula_counts(n,t)
            assert actual==expected,(n,t,actual,expected)
            if t==Fraction(3,2):
                assert sum(actual.values())==perrin(n)
                for k,v in actual.items():
                    if n-k>=1 and n/2<=k<=2*n/3:
                        want=Fraction(n*comb(n-k,2*k-n),n-k)
                        assert v==want
            checked+=1
    for n in range(3,12):
        for t in (Fraction(6,5),Fraction(3,2),Fraction(9,5)):
            all_cost=[cost_in_units_of_L_over_n(x,t) for x in product((0,1),repeat=n)]
            opt=min(all_cost)
            best=Fraction(n+(t-1)*ceil(n/2))
            assert opt==best,(n,t,opt,best)
            ne=[cost_in_units_of_L_over_n(x,t) for x in product((0,1),repeat=n) if direct_equilibrium(x,t)]
            assert min(ne)==best
            assert max(ne)==Fraction(n+(t-1)*floor(2*n/3))
            checked+=1
    for n in range(3,12):
        for t in (Fraction(11,5),Fraction(5,2),Fraction(14,5)):
            optimum=min(cost_in_units_of_L_over_n(x,t) for x in product((0,1),repeat=n))
            assert optimum==n+(t-1)*ceil(n/2)
            equilibria=[cost_in_units_of_L_over_n(x,t) for x in product((0,1),repeat=n) if direct_equilibrium(x,t)]
            minimum=n+(t-1)*(n//2)+(2 if n%2 else 0)
            assert min(equilibria)==minimum,(n,t,min(equilibria),minimum)
    print('VERIFY_OK: transfer/direct counts', checked-27,'cost/PoA',27,'parity/PoS',27,'cycles n=3..11')
if __name__=='__main__':run()
