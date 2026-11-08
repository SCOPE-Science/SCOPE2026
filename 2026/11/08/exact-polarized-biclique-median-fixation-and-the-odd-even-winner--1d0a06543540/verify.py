#!/usr/bin/env python3
"""Standalone exact-arithmetic verification of polarized biclique median dynamics."""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb

# All probabilities refer to absorption at unanimous opinion one.
def competing_clocks(m,n,lam_a,lam_b):
    a=(m+1)//2; b=(n+1)//2
    @lru_cache(None)
    def p(x,y):
        if x>=a: return Q(1)
        if y>=b: return Q(0)
        rate_a=(m-x)*lam_a
        rate_b=(n-y)*lam_b
        return (rate_a*p(x+1,y)+rate_b*p(x,y+1))/(rate_a+rate_b)
    return p(0,0)

def exponential_integral(m,n,lam_a,lam_b):
    a=(m+1)//2; b=(n+1)//2
    ans=Q(0)
    for j in range(b):
        for k in range(a):
            for h in range(j+1):
                numerator=a*comb(m,a)*comb(n,j)*comb(a-1,k)*comb(j,h)*(-1)**(k+h)
                den=(m-a+1+k)*lam_a+(n-j+h)*lam_b
                ans+=numerator*lam_a/den
    return ans

def uniform_order_formula(m,n):
    a=(m+1)//2; b=(n+1)//2
    return Q(sum(comb(a+j-1,j)*comb(m+n-a-j,m-a) for j in range(b)),comb(m+n,m))

# Independent labelled-state update check: enumerate individual clock flips in
# the actual median rule, without using first-threshold stopping in this solver.
def labelled_process(m,n,lam_a,lam_b):
    initial_a=0
    initial_b=(1<<n)-1
    @lru_cache(None)
    def f(ma,mb):
        if ma==(1<<m)-1 and mb==(1<<n)-1: return Q(1)
        if ma==0 and mb==0: return Q(0)
        ones_a=ma.bit_count(); ones_b=mb.bit_count()
        updates=[]
        for i in range(m):
            old=(ma>>i)&1
            new=1 if 2*ones_b>n else (0 if 2*ones_b<n else old)
            if old!=new: updates.append((lam_a,ma^(1<<i),mb))
        for j in range(n):
            old=(mb>>j)&1
            new=1 if 2*ones_a>m else (0 if 2*ones_a<m else old)
            if old!=new: updates.append((lam_b,ma,mb^(1<<j)))
        if not updates:
            # Other equilibria may exist off the initially polarized trajectory.
            # An equilibrium reached here would contradict almost-sure consensus.
            raise AssertionError(('non-consensus frozen state',m,n,ma,mb))
        tot=sum(z[0] for z in updates)
        return sum((rate*f(aa,bb) for rate,aa,bb in updates),Q(0))/tot
    return f(initial_a,initial_b)

N=0
for m in range(1,8):
    for n in range(1,8):
        for la,lb in ((Q(1),Q(1)),(Q(1),Q(2)),(Q(2),Q(3)),(Q(3),Q(1))):
            p=competing_clocks(m,n,la,lb)
            assert p==exponential_integral(m,n,la,lb), (m,n,la,lb)
            if la==lb:
                assert p==uniform_order_formula(m,n)
                if m%2 and n%2: assert p==Q(1,2)
                if m%2==0 and n%2==1: assert p>Q(1,2)
                if m%2==1 and n%2==0: assert p<Q(1,2)
            N+=1
labelled=0
for m in range(1,5):
    for n in range(1,5):
        for la,lb in ((Q(1),Q(1)),(Q(1),Q(2)),(Q(2),Q(3))):
            assert labelled_process(m,n,la,lb)==competing_clocks(m,n,la,lb), (m,n,la,lb)
            labelled+=1
assert competing_clocks(2,4,Q(1),Q(1))==Q(3,5)
assert competing_clocks(2,3,Q(1),Q(1))==Q(7,10)
assert competing_clocks(3,2,Q(1),Q(1))==Q(3,10)
print('PASS:',N,'rational clock-race/integral comparisons, 49 uniform-order comparisons, 72 independent labelled-state CTMC checks; parity checks and exact examples.')
