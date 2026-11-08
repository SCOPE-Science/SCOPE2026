"""Finite exact verification of parallel-walk range and cover identities.

All arithmetic in the checks is rational or integer, with no asymptotic theorem inferred from finite tests.
"""
from fractions import Fraction
from collections import defaultdict
from itertools import product
from math import comb

checks=0

def verify(condition, description):
    global checks
    if not condition: raise AssertionError(description)
    checks += 1


def confined_count(t,a,b):
    """Number of signed t-step paths confined to [-b,a], including time zero."""
    if a<0 or b<0: return 0
    d={0:1}
    for _ in range(t):
        next_d=defaultdict(int)
        for x,v in d.items():
            if x+1<=a:next_d[x+1]+=v
            if x-1>=-b:next_d[x-1]+=v
        d=next_d
    return sum(d.values())

def brute_confined(t,a,b):
    count=0
    for increments in product((-1,1),repeat=t):
        x=0
        xs=[0]
        for v in increments:
            x+=v;xs.append(x)
        count+= (min(xs)>=-b and max(xs)<=a)
    return count

def cdf_formula(n,k,t):
    """Exact P(k walks cover C_n by t), using survival in intervals."""
    r=n-2
    subtotal=Fraction(0)
    for a in range(r+1):
        p1=Fraction(confined_count(t,a,r-a),2**t)
        p0=Fraction(confined_count(t,a-1,r-a),2**t)
        subtotal += p1**k-p0**k
    return 1-subtotal

def cdf_independent_maxima(n,k,t):
    """Independent computation from complete one-path (max,-min) distribution."""
    paths=defaultdict(int)
    for increments in product((-1,1),repeat=t):
        x=0; hi=0;lo=0
        for dx in increments:
            x+=dx;hi=max(hi,x);lo=min(lo,x)
        paths[(hi,-lo)]+=1
    states={(0,0):Fraction(1)}
    for _ in range(k):
        next_states=defaultdict(Fraction)
        for (a,b),p in states.items():
            for (u,v),count in paths.items():
                next_states[(max(a,u),max(b,v))]+=p*Fraction(count,2**t)
        states=next_states
    return sum(p for (a,b),p in states.items() if a+b>=n-1)

for t in range(0,10):
    for a in range(0,7):
        for b in range(0,7):
            verify(confined_count(t,a,b)==brute_confined(t,a,b),f'confined {t=} {a=} {b=}')
for t in range(0,9):
    for n in range(3,10):
        for k in range(1,5):
            verify(cdf_formula(n,k,t)==cdf_independent_maxima(n,k,t),f'cover {t=} {n=} {k=}')
for t in range(1,51):
    for a in range(1,51):
        tails=sum(comb(t,j) for j in range(t+1) if 2*j-t>=a)
        tails_strict=sum(comb(t,j) for j in range(t+1) if 2*j-t>=a+1)
        maxhit=2**t-confined_count(t,a-1,t)
        verify(maxhit==tails+tails_strict,f'reflection {t=} {a=}')

print(f'PASS {checks} exact checks')
