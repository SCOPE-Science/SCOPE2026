"""Standalone numerical checks for the scalar-Schur modal saddle-point theorem.
Run with Python 3 and NumPy: python check.py
The symbolic argument is in RESULT.md; numerical checks do not prove it.
"""
import cmath
import math
import random
import numpy as np


def predicted_factor(bvals, c, q):
    a = 1.0 - c*c/q
    return max(max(abs((a+cmath.sqrt(a*a-4*b*b/q))/2),
                   abs((a-cmath.sqrt(a*a-4*b*b/q))/2)) for b in bvals)


def optimum(bvals, c):
    beta, B = min(bvals), max(bvals)
    h = B*B + beta*beta
    r = 2*B*B/(h+math.sqrt(h*h+4*c*c*B*B))
    return r, B*B/(r*r)


def actual_factor(bvals, c, q):
    m = len(bvals)
    I = np.eye(m)
    B = np.diag(bvals)
    Z = np.zeros((m,m))
    K = np.block([[I,Z,B],[Z,I,c*I],[B,c*I,Z]])
    P = np.block([[I,Z,Z],[Z,I,c*I],[Z,Z,-q*I]])
    T = np.eye(3*m)-np.linalg.solve(P,K)
    return max(abs(np.linalg.eigvals(T)))


def verify():
    checks = 0
    # Exact analytic baseline: beta=1, B=3, c=4, optimal q=36, radius 1/2.
    r, q = optimum([1, 3], 4)
    assert abs(r-0.5)<1e-14; checks+=1
    assert abs(q-36)<1e-12; checks+=1
    assert abs(predicted_factor([1, 3], 4, 36)-0.5)<1e-14; checks+=1
    assert abs(predicted_factor([1, 3], 4, 25)-0.6)<1e-14; checks+=1
    assert abs(actual_factor([1, 3], 4, 36)-0.5)<1e-12; checks+=1
    assert abs(actual_factor([1, 3], 4, 25)-0.6)<1e-12; checks+=1
    rng = random.Random(340626)
    for case in range(250):
        d = rng.randrange(2,8)
        bvals = [math.exp(rng.uniform(-1.4,1.4)) for _ in range(d)]
        if case%5==0:
            bvals = [bvals[0]]*d  # repeated modal strength; critical roots
        c = math.exp(rng.uniform(-1.1,1.8))
        r, q = optimum(bvals,c)
        beta, B = min(bvals),max(bvals)
        assert abs(c*c*r*r+(B*B+beta*beta)*r-B*B)<1e-9*B*B; checks+=1
        assert 0<r<1 and q>0; checks+=1
        assert abs(predicted_factor(bvals,c,q)-r)<(1e-7 if case%5==0 else 1e-9); checks+=1
        if case%5!=0: # avoid fragile numerical Jordan eigenvalues at repeated mode
            assert abs(actual_factor(bvals,c,q)-r)<5e-7; checks+=1
        for j in range(30):
            scale = math.exp(rng.uniform(-3.0,3.0))
            candidate = predicted_factor(bvals,c,q*scale)
            assert candidate >= r-1e-10, (case,j,candidate,r); checks+=1
        for s in [0.999,1.001,0.97,1.03]:
            assert predicted_factor(bvals,c,q*s)>r-1e-10; checks+=1
    print('PASS',checks,'checks; example optimal radius',0.5,'versus Schur-max radius',0.6)


if __name__=='__main__':
    verify()
