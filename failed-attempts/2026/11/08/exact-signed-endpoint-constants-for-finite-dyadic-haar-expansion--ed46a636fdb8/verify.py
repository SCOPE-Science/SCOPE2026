#!/usr/bin/env python3
"""Exact independent checks for finite-depth Haar transform endpoint norm."""
from fractions import Fraction as F
from itertools import product
from random import Random

def target(d):
    return F(2*d,3)+F(5,9)+F(4,9)*F(-1,2)**d

def path_row(d, sig):
    # Piecewise-constant kernel at a fixed target leaf; dyadic masses exact.
    prefix=1
    total=F(0)
    for j,s in enumerate(sig):
        total += F(abs(prefix-s*2**j),2**(j+1))
        prefix += s*2**j
    total+=F(abs(prefix),2**d)
    return total

for d in range(0,13):
    val=max(path_row(d,sig) for sig in product([-1,1],repeat=d))
    assert val==target(d),(d,val,target(d))
print('EXHAUSTIVE_SIGN_PATHS_MATCH_CLOSED_FORM',sum(2**d for d in range(13)))

# Independent direct kernel rows of a finite Haar transform with randomly
# chosen signs at *all* nodes, checking the exact row-norm reduction.
rng=Random(2207)
for d in range(1,7):
    N=2**d
    nodes=[(j,k) for j in range(d) for k in range(2**j)]
    for run in range(16):
        sig={node:rng.choice((-1,1)) for node in nodes}
        for x in range(N):
            vals=[]
            for y in range(N):
                v=1
                for j in range(d):
                    a=x>>(d-j)
                    if (y>>(d-j)) != a:
                        continue
                    s=1 if (x>>(d-j-1)) == (y>>(d-j-1)) else -1
                    v+=sig[(j,a)]*(2**j)*s
                vals.append(v)
            direct=F(sum(abs(v) for v in vals),N)
            path=path_row(d,tuple(sig[(j,x>>(d-j))] for j in range(d)))
            assert direct == path,(d,run,x,direct,path)
            assert direct<=target(d)
print('INDEPENDENT_FULL_KERNEL_ROW_CALCULATIONS_PASSED',sum(16*2**d for d in range(1,7)))

# Exact Bellman envelope: test rational b at all dyadic samples for each h.
# This uses full exhaustive controls for h<=9, independently of the recursion.
for h in range(0,10):
    for bnum in range(-8,9):
        b=F(bnum,8)
        v=F(0)
        for sig in product((-1,1),repeat=h):
            z=b; cost=F(0)
            for s in sig:
                cost+=F(1-s*z,2)
                z=(z+s)/2
            cost+=abs(z)
            v=max(v,cost)
        c=F(1,3)+F(2,3)*F(-1,2)**h
        a=F(2*h,3)+F(2,9)*(1-F(-1,2)**h)
        assert v==a+c*abs(b),(h,b,v,a,c)
print('EXHAUSTIVE_BELLMAN_ENVELOPE_CHECKS_PASSED',10*17)
print('ALL_FINITE_HAAR_ENDPOINT_CHECKS_PASSED')
