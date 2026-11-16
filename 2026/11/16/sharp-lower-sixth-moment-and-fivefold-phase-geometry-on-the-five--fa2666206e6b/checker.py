#!/usr/bin/env python3
"""Finite-field parabola p=5: exhaustive collision identity and independent tests."""
from collections import defaultdict
from itertools import combinations_with_replacement, product
from math import factorial, pi
import cmath
import random

P = 5

def frequencies(triple):
    return (sum(triple) % P, sum(t*t for t in triple) % P)

def weight(triple):
    w = factorial(3)
    for t in set(triple):
        w //= factorial(triple.count(t))
    return w

def phase_ratios(a):
    return [a[(s-1)%P]*a[(s+1)%P]/(a[(s-2)%P]*a[(s+2)%P]) for s in range(P)]

def cyclic_rows():
    return [[int(t==(s-1)%P)+int(t==(s+1)%P)
            -int(t==(s-2)%P)-int(t==(s+2)%P)
             for t in range(P)] for s in range(P)]

def det(a):
    if len(a)==1: return a[0][0]
    return sum((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(len(a)))

def proof_collisions():
    fibers=defaultdict(list)
    for t in combinations_with_replacement(range(P), 3):
        fibers[frequencies(t)].append((t,weight(t)))
    assert len(fibers)==25
    assert sorted(len(v) for v in fibers.values()) == [1]*15 + [2]*10
    assert all(w==3 for arr in fibers.values() if len(arr)==2 for _,w in arr)
    assert sum(w*w for arr in fibers.values() for _,w in arr)==545
    left=[]
    for arr in fibers.values():
        if len(arr)==2:
            t,u=[a[0] for a in arr]
            left.append(tuple(t.count(j)-u.count(j) for j in range(P)))
    W=cyclic_rows()
    right=[tuple(W[s][j]-W[t][j] for j in range(P)) for s in range(P) for t in range(s+1,P)]
    assert sorted(min(v,tuple(-x for x in v)) for v in left)==sorted(min(v,tuple(-x for x in v)) for v in right)
    assert all(sum(row)==0 for row in W)
    assert all(sum(W[s][t] for s in range(P))==0 for t in range(P))
    assert abs(det([row[1:] for row in W[1:]]))==5
    return fibers

# An exact cyclotomic equality is a coefficient difference that is constant,
# since Phi_5(X)=1+X+X^2+X^3+X^4.
def compare_cyclotomic(a, fibers):
    phase=lambda t: sum(a[x] for x in t)%5
    lhs=[0]*5
    for arr in fibers.values():
        for t,wt in arr:
            for u,wu in arr:
                lhs[(phase(t)-phase(u))%5]+=wt*wu
    W=cyclic_rows()
    b=[sum(W[s][t]*a[t] for t in range(P))%5 for s in range(P)]
    rhs=[0]*5
    rhs[0]=500
    for bs in b:
        for bt in b:
            rhs[(bs-bt)%5]+=9
    diff=[x-y for x,y in zip(lhs,rhs)]
    assert len(set(diff))==1,(a,diff)

def direct_moment(a):
    omega=cmath.exp(2j*pi/P)
    return sum(abs(sum(a[t]*omega**((x*t+y*t*t)%P) for t in range(P)))**6
               for x in range(P) for y in range(P))/25

def main():
    fibers=proof_collisions()
    print('EXACT: 25 fibers; 15 singletons, 10 doubletons; 545 diagonal; bijection to ten Legendre-ratio pairs; determinant abs=5')
    checked=0
    for v in product(range(5),repeat=4):
        compare_cyclotomic((0,)+v,fibers);checked+=1
    print('EXACT: cyclotomic coefficient identity passed for',checked,'normalized fifth-root assignments')
    W=cyclic_rows()
    minimum=set()
    for v in product(range(P),repeat=P-1):
        exps=(0,)+v
        bexps=[sum(W[s][t]*exps[t] for t in range(P))%P for s in range(P)]
        if len(set(bexps))==P: minimum.add(exps)
    predicted={(0,)+tuple((A*t+B*t*t+C*t*t*t)%P for t in range(1,P))
               for A in range(P) for B in range(P) for C in range(1,P)}
    assert minimum == predicted and len(minimum)==100
    print('EXACT: all 100 normalized fifth-root minimizers are cubic chirps')
    rng=random.Random(240516647)
    for k in range(200):
        a=[cmath.exp(2j*pi*rng.random()) for t in range(P)]
        lhs=direct_moment(a)
        rhs=500+9*abs(sum(phase_ratios(a)))**2
        assert abs(lhs-rhs)<1e-7,(k,lhs,rhs)
    print('NUMERICAL: 200 independent continuous-phase direct-DFT checks')
    omega=cmath.exp(2j*pi/P)
    a=[omega**(t*t*t%P) for t in range(P)]
    assert abs(sum(phase_ratios(a)))<1e-10
    assert abs(direct_moment(a)-500)<1e-8
    a=[1+0j]*P
    assert abs(direct_moment(a)-725)<1e-8
    print('EXPLICIT: cubic chirp minimum 500; constant phase maximum 725')
    # The cofactor is the degree of the phase-ratio map, not a simulation count.
    print('PASS')

if __name__=='__main__':main()
