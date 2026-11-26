#!/usr/bin/env python3
"""Exact-rational diagnostics for a minimal nested-occupancy observation law.

Run: python3 verify_nested.py
Only Python standard library is required. Checks supplement the written proof.
"""
from fractions import Fraction as Q
from itertools import product

N = 0

def check(condition, message):
    global N
    N += 1
    if not condition:
        raise AssertionError(message)

def law(psi, theta, p, f):
    result = {}
    for x, y, z in product((0, 1), repeat=3):
        probability = Q(0)
        for occupied in (0, 1):
            w = psi if occupied else (1 - psi)
            if not occupied:
                u_choices = [(0, 0, Q(1))]
            else:
                u_choices = [(u, v, (theta if u else 1-theta)
                              * (theta if v else 1-theta))
                             for u, v in product((0, 1), repeat=2)]
            for u, v, wu in u_choices:
                q = p if u else f
                r = p if v else f
                probability += w * wu * (q if x else 1-q) * (q if y else 1-q) * (r if z else 1-r)
        result[x,y,z] = probability
    return result

def observed_moments(P):
    A = sum(w*x for (x,y,z),w in P.items())
    B = sum(w*x*y for (x,y,z),w in P.items())
    C = sum(w*x*z for (x,y,z),w in P.items())
    D = P[1,1,1]
    return A,B,C,D

def reconstruct_law(A, B, C, D):
    # The full exchangeable triple law is determined by four moments.
    return {(1,1,1):D, (1,1,0):B-D,
            (1,0,1):C-D, (0,1,1):C-D,
            (1,0,0):A-B-C+D, (0,1,0):A-B-C+D,
            (0,0,1):A-2*C+D,
            (0,0,0):1-3*A+B+2*C-D}

def invert_with_known_square_root(A,B,C,D,p_minus_f):
    v=C-A*A
    L=(D-A*B)/v
    delta=L*L-4*(L*A-B)
    check(delta == p_minus_f*p_minus_f, 'discriminant')
    f=(L-p_minus_f)/2
    p=(L+p_minus_f)/2
    t=A-f
    psi=t*t/(v+t*t)
    theta=t/(psi*(p-f))
    return psi,theta,p,f

for i in range(1,1501):
    psi=Q((31*i)%89+5,100)
    theta=Q((19*i)%83+6,100)
    p=Q((17*i)%49+50,100)
    f=Q((7*i)%22+1,100)
    P=law(psi,theta,p,f)
    A,B,C,D=observed_moments(P)
    recovered=invert_with_known_square_root(A,B,C,D,p-f)
    check(recovered==(psi,theta,p,f), 'exact parameter recovery')
    check(reconstruct_law(A,B,C,D)==P, 'complete law from moments')
    check(sum(P.values())==1,'normalization')
    check(all(Q(0)<w<Q(1) for w in P.values()),'strictly positive cell probabilities')
    check(C>A*A,'cross-primary dependence')
    check(D-A*B==(C-A*A)*(p+f),'latent covariance identity')
    check(B == A*(p+f)-p*f,'within-primary identity')

P=law(Q(2,5),Q(3,5),Q(4,5),Q(1,10))
check(observed_moments(P)==(Q(67,250),Q(403,2500),Q(1427,12500),Q(10163,125000)), 'displayed exact example')
# Consequences of the full distribution at boundary cases. In these cases
# the interior inverse is not applicable; no impossible conclusions are drawn.
check(observed_moments(law(Q(1),Q(1,2),Q(3,4),Q(1,9)))[2] == observed_moments(law(Q(1),Q(1,2),Q(3,4),Q(1,9)))[0]**2,'occupied-site boundary')
check(law(Q(1,3),Q(1,2),Q(1,5),Q(1,5)) == law(Q(2,3),Q(3,4),Q(1,5),Q(1,5)), 'uninformative assay')
# On a single primary unit, the entire detection law depends only on
# the product psi*theta. Two unequal parameter pairs produce the same law.
def single_primary(psi, theta, p, f):
    return {bits: (psi*theta)*Q(1) * __import__('math').prod((p if b else 1-p) for b in bits)
            + (1-psi*theta)*__import__('math').prod((f if b else 1-f) for b in bits)
            for bits in product((0,1), repeat=3)}
check(single_primary(Q(1,3),Q(3,4),Q(4,5),Q(1,10)) ==
      single_primary(Q(1,2),Q(1,2),Q(4,5),Q(1,10)), 'one-primary nonidentification')

print(f'PASS: {N} exact rational assertions (analytic proof required for infinite claims).')
