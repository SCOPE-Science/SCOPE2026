from fractions import Fraction as F
from math import comb
from random import Random

def tail(ps, low):
    # independent DP method, unrelated to pivot-event proof
    a=[F(1)]
    for p in ps:
        b=[F(0)]*(len(a)+1)
        for k,v in enumerate(a):
            b[k]+=v*(1-p)
            b[k+1]+=v*p
        a=b
    return sum(a[low:], F(0))

def exact_gain(m, source, target, rest):
    # Two ways of calculating success, with one copied vote (weight two)
    n=2*m+1
    direct=tail([source,target]+[rest]*(n-2),m+1)
    # target contributes two; the remaining 2m-1 voters one each
    p_rest=[rest]*(n-2)
    delegated=target*tail(p_rest,m-1)+(1-target)*tail(p_rest,m+1)
    return delegated-direct

def closed_gain(m,source,target,rest):
    t=m-1
    a=(1-rest)*target*(1-source)-rest*source*(1-target)
    return comb(2*t+1,t)*a*(rest*(1-rest))**t

def mix(m,states,prior):
    return prior*exact_gain(m,*states[0])+(1-prior)*exact_gain(m,*states[1])

def closed_mix(m,states,prior):
    return prior*closed_gain(m,*states[0])+(1-prior)*closed_gain(m,*states[1])

# source, target, rest, with target more competent in each signal state
witness_harm_to_help=[(F(3,5),F(3,4),F(3,5)),(F(3,5),F(7,10),F(9,10))]
witness_help_to_harm=[(F(3,5),F(13,20),F(3,5)),(F(3,5),F(49,50),F(9,10))]
for name,w in [('harm-to-help',witness_harm_to_help),('help-to-harm',witness_help_to_harm)]:
    print(name)
    for m in range(1,9):
        d=mix(m,w,F(1,2))
        c=closed_mix(m,w,F(1,2))
        assert d==c
        print(2*m+1, f'{d.numerator}/{d.denominator}', float(d))

rng=Random(260816738)
vals=[F(a,b) for b in (5,7,9,11,13) for a in range(1,b)]
checks=0
for m in range(1,9):
    for it in range(600):
        st=[tuple(rng.choice(vals) for _ in range(3)) for _ in range(2)]
        pi=rng.choice(vals)
        d=mix(m,st,pi)
        c=closed_mix(m,st,pi)
        assert d==c, (m,st,pi,d,c)
        checks+=1
print('independent rational comparisons',checks)

# finite grid all two-state parameters for modest n
from itertools import product
v=[F(1,4),F(1,2),F(3,4)]
s=list(product(v,repeat=3))
count=0
for m in (1,2,3,4):
    for st in product(s,repeat=2):
        d=mix(m,st,F(2,5))
        c=closed_mix(m,st,F(2,5))
        assert d==c
        count+=1
print('grid comparisons',count)
