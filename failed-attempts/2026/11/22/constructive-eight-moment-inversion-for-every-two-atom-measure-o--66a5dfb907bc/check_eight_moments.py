"""Numerical supplementary checks for an eight-moment, two-atom reconstruction.

Only Python standard library is required. Numerics do NOT replace the proof.
Run: python3 check_eight_moments.py
"""
import cmath
import itertools
import math
import random

OMEGA = ((0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3), (1, 1))

def samples(terms):
    return {(a, b): sum(c*z**a*w**b for z, w, c in terms) for a, b in OMEGA}

def marginal(s):
    s0, s1, s2, s3 = s
    scale = max(1.0, *(abs(x) for x in s))
    delta = s0*s2 - s1*s1
    if abs(delta) > 1e-9 * scale*scale:
        product = (s1*s3 - s2*s2)/delta
        total = (s0*s3 - s1*s2)/delta
        disc = cmath.sqrt(total*total-4*product)
        a, b = (total+disc)/2, (total-disc)/2
        u = (s1-b*s0)/(a-b)
        return [(a,u),(b,s0-u)]
    if abs(s0) > 1e-9*scale:
        return [(s1/s0,s0)]
    if max(abs(x) for x in s) < 1e-9 * scale:
        return []
    raise ValueError('inconsistent 1D marginal')

def recover(measured):
    X = marginal([measured[a,0] for a in range(4)])
    Y = marginal([measured[0,b] for b in range(4)])
    h = measured[1,1]
    if len(X) == len(Y) == 2:
        for perm in itertools.permutations(Y):
            if max(abs(X[i][1]-perm[i][1]) for i in range(2)) < 1e-7:
                candidate = [(X[i][0],perm[i][0],X[i][1]) for i in range(2)]
                if abs(samples(candidate)[1,1]-h) < 1e-7:
                    return candidate
        raise ValueError('incompatible pairing')
    if len(X) == 2:
        w = Y[0][0] if len(Y) == 1 else h/measured[1,0]
        return [(z,w,c) for z,c in X]
    if len(Y) == 2:
        z = X[0][0] if len(X) == 1 else h/measured[0,1]
        return [(z,w,c) for w,c in Y]
    if len(X) == len(Y) == 1:
        return [(X[0][0],Y[0][0],X[0][1])]
    if len(X) == len(Y) == 0 and abs(h) < 1e-9:
        return []
    raise ValueError('inconsistent marginals')

def check(terms):
    orig = samples(terms)
    rec = recover(orig)
    assert len(rec) == len(terms), (terms,rec)
    assert max(abs(orig[t]-samples(rec)[t]) for t in OMEGA) < 3e-7
    for z,w,c in terms:
        assert any(max(abs(z-Z),abs(w-W),abs(c-C)) < 3e-7 for Z,W,C in rec), (terms,rec)

random.seed(260821)
unit = lambda: cmath.exp(2j*math.pi*random.random())
random_count = 0
for regime in ('generic','equal_weights','same_x','same_y','same_x_cancel','same_y_cancel','one'):
    for _ in range(100):
        z1,z2,w1,w2=unit(),unit(),unit(),unit()
        while abs(z1-z2)<0.2:z2=unit()
        while abs(w1-w2)<0.2:w2=unit()
        c1,c2=unit()*(0.5+random.random()),unit()*(0.5+random.random())
        if regime == 'equal_weights':c2=c1
        if regime.startswith('same_x'):z2=z1
        if regime.startswith('same_y'):w2=w1
        if regime.endswith('cancel'):c2=-c1
        terms=[(z1,w1,c1),(z2,w2,c2)]
        if regime == 'one':terms=terms[:1]
        check(terms)
        random_count+=1

roots_z=[cmath.exp(2j*math.pi*j/7) for j in range(7)]
roots_w=[cmath.exp(2j*math.pi*k/5) for k in range(5)]
points=list(itertools.product(roots_z,roots_w))
coeff=(1,-1,1+2j)
grid_count=0
for ((z1,w1),(z2,w2)) in itertools.combinations(points,2):
    for c1,c2 in itertools.product(coeff,repeat=2):
        check([(z1,w1,c1),(z2,w2,c2)])
        grid_count+=1
check([])
print('PASS: %d random configurations; %d root-grid and coefficient configurations; empty case.'%(random_count,grid_count))
