#!/usr/bin/env python3
"""Reproduce the block-spectrum and phase-alphabet count tests.

Requires Python 3.10+ standard library only. This checks finite instances;
the unbounded assertion is proved in RESULT.md, not by enumeration.
"""
import cmath
import itertools
import math
import random

TOL = 2e-10
checks = 0


def assert_close(a, b, tol=TOL):
    global checks
    checks += 1
    assert abs(a-b) <= tol, (a,b)


def mat_and_prediction(n, step, phases):
    p = n // 2
    g = [cmath.exp(1j*t)/math.sqrt(n) for t in phases]
    omega = cmath.exp(2j*math.pi/n)
    frame = []
    for k in (0, step, 2*step):
        for a in range(p):
            frame.append([omega**(2*a*j)*g[(j-k)%n] for j in range(n)])
    S = [[sum(v[j]*v[k].conjugate() for v in frame)
          for k in range(n)] for j in range(n)]
    z = [n*g[j]*g[(j+p)%n].conjugate() for j in range(n)]
    sig = [sum(z[(j-k*step)%n] for k in range(3)) for j in range(n)]
    for j in range(n):
        for k in range(n):
            expect = (1.5 if j == k else
                      .5*sig[j] if (k-j)%n == p else 0j)
            assert_close(S[j][k], expect)
    for j in range(p):
        assert_close(sig[j+p], sig[j].conjugate())
        for eig in (1.5-abs(sig[j])/2, 1.5+abs(sig[j])/2):
            assert eig >= -TOL
    return sig


def exact_q_count(n, s, q):
    p = n//2
    count = 0
    third = q//3
    # Exact exponent arithmetic for q-th roots of unity.
    for exps in itertools.product(range(q), repeat=n):
        z = [(exps[j]-exps[j+p])%q for j in range(p)]
        z += [(-v)%q for v in z]
        success = q%3==0
        if success:
            for j in range(n):
                triple = {z[(j-k*s)%n] for k in range(3)}
                if triple != {z[j],(z[j]+third)%q,(z[j]+2*third)%q}:
                    success = False
                    break
        if success:
            count += 1
    return count


def construct(n, s, q):
    p=n//2
    d=math.gcd(n,s)
    order=n//d
    assert order%6==3 and q%3==0
    z=[None]*n
    w=q//3
    for j in range(n):
        if z[j] is not None:continue
        for t in range(order):
            a=(j+t*s)%n
            b=(a+p)%n
            assert z[a] is None and z[b] is None
            z[a]=(w*t)%q
            z[b]=(-w*t)%q
    exps=[0]*n
    for j in range(p):exps[j+p]=(-z[j])%q
    omega=2*math.pi/q
    sig=mat_and_prediction(n,s,[omega*v for v in exps])
    for a in sig:assert_close(a,0j)


def main():
    rand=random.Random(20261106)
    for n in (4,6,8,10,12,18):
        for s in range(1,n):
            if n//math.gcd(n,s)<3:continue
            for rep in range(3):
                phases=[rand.uniform(-math.pi,math.pi) for _ in range(n)]
                mat_and_prediction(n,s,phases)
    for n in (6,12,18,24,30):
        for s in range(1,n):
            if (n//math.gcd(n,s))%6 == 3:
                construct(n,s,3)
                construct(n,s,6)
    for n,s,q in ((6,2,3),(6,1,3),(6,2,6),(8,1,3),(8,2,3)):
        d=math.gcd(n,s)
        order=n//d
        expected = q**(n//2)*(2*q)**(d//2) if order%6==3 and q%3==0 else 0
        got = exact_q_count(n,s,q)
        assert_close(got,expected,0)
    print('PASS:',checks,'direct matrix/eigenvalue/tightness/count checks')

if __name__ == '__main__':
    main()
