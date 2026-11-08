#!/usr/bin/env python3
"""Exact finite checks for a two-recipient binary online allocation model."""
from fractions import Fraction as Q
from itertools import product
from math import comb


def marginal_tail(m, p, q):
    a = p*q/2                 # recipient loses a mutually valued good
    b = p*(1-q/2)            # recipient gets a valued good
    c = 1-p                  # recipient values the good at zero
    d = {0: Q(1)}
    for _ in range(m):
        nxt = {}
        for k, w in d.items():
            for step, prob in ((1,a),(-1,b),(0,c)):
                nxt[k+step] = nxt.get(k+step,Q(0)) + w*prob
        d = nxt
    return sum((w for k,w in d.items() if k >= 3), Q(0))


def law(m, p1, p2):
    return 1 - marginal_tail(m,p1,p2) - marginal_tail(m,p2,p1)


def direct(m,p1,p2):
    # Coordinates: (v1,v2,recipient,probability). The disliked-by-both
    # good is assigned to recipient 1; this cannot affect fairness.
    labels = ((0,0,1,(1-p1)*(1-p2)),
              (1,0,1,p1*(1-p2)),
              (0,1,2,(1-p1)*p2),
              (1,1,1,p1*p2/2),
              (1,1,2,p1*p2/2))
    out = Q(0)
    for xs in product(labels,repeat=m):
        weight = Q(1)
        own = [0,0]
        total = [0,0]
        for u,v,recipient,prob in xs:
            weight *= prob
            total[0] += u
            total[1] += v
            if recipient == 1: own[0] += u
            else: own[1] += v
        if not weight: continue
        fair = all(2*own[i] + (2 if total[i] > own[i] else 0) >= total[i]
                   for i in range(2))
        if fair: out += weight
    return out


def run():
    cases = [(Q(1,2),Q(1,2)),(Q(1,3),Q(2,3)),
             (Q(1),Q(1,2)),(Q(1),Q(1)),
             (Q(0),Q(1,2)),(Q(1,5),Q(4,5))]
    total = 0
    for p1,p2 in cases:
        for m in range(1,7):
            lhs=law(m,p1,p2)
            rhs=direct(m,p1,p2)
            assert lhs==rhs,(m,p1,p2,lhs,rhs)
            assert Q(0)<=lhs<=Q(1)
            total+=1
    for m in range(1,35):
        if m%2==0:
            t=m//2
            numerator=comb(m,t-1)+comb(m,t)+comb(m,t+1)
        else:
            numerator=2*comb(m,m//2)
        assert law(m,Q(1),Q(1))==Q(numerator,2**m)
        total+=1
    for p1,p2 in cases:
        for m in (1,2,3,4):
            assert law(m,p1,p2)==law(m,p2,p1)
            total+=1
    for p1,p2 in cases:
        assert law(3,p1,p2)==1-(p1*p2)**3/4
        a=p1*p2/2
        assert law(4,p1,p2)==1-(2*a**4+4*a**3*(2-p1-p2))
        total+=2
    print('PASS: exact outcome enumerations, marginal-law identities, all-liked formula, symmetry, small-horizon identities')
    print('Checks:', total)
    print('Examples:')
    for p1,p2,m in ((Q(1,2),Q(1,2),5),(Q(1,3),Q(2,3),6),(Q(1),Q(1),5)):
        print(f'p1={p1}, p2={p2}, m={m}, success={law(m,p1,p2)}')

if __name__=='__main__': run()
