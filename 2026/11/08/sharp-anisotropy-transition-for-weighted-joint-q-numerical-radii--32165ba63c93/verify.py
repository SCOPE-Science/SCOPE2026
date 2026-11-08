#!/usr/bin/env python3
"""Finite diagnostics for a weighted two-observable q-overlap norm theorem.

All universal assertions are proved analytically in RESULT.md; this script
only checks selected parameter sets and independent vector samples.
"""
import cmath
import math
import random


def formula(p, q, alpha, beta):
    assert 1 <= p <= math.inf and 0 < abs(q) < 1 and alpha >= beta > 0
    s = math.sqrt(1 - abs(q)**2)
    if p >= 2:
        if math.isinf(p):
            return alpha
        return (alpha**p + (beta*s)**p)**(1/p)
    k = 2*p/(2-p)
    if s <= (beta/alpha)**(p/(2-p)):
        return math.sqrt(1+s*s)*(alpha**k+beta**k)**(1/k)
    return (alpha**p + (beta*s)**p)**(1/p)


def curve(p, q, alpha, beta, theta):
    s = math.sqrt(1-q*q)
    u = math.cos(theta) + 1j*s*math.sin(theta)
    v = math.sin(theta) - 1j*s*math.cos(theta)
    return ((alpha*abs(u))**p + (beta*abs(v))**p)**(1/p)


def main():
    rng = random.Random(20261106)
    checks = 0
    for p in (1,1.1,1.5,1.9,2,2.5,3,5,11):
        for q in (0.07,0.25,0.5,0.75,0.93,0.998):
            for alpha,beta in ((1,1),(1.1,1),(1.5,1),(2,1),(4,1),(10,1)):
                target = formula(p,q,alpha,beta)
                samples = max(curve(p,q,alpha,beta, j*math.pi/720) for j in range(721))
                assert samples <= target + 1.e-10, (p,q,alpha,beta,samples,target)
                assert target-samples <= 2.e-4*max(1,target), (p,q,alpha,beta,samples,target)
                checks += 2
                # q-overlap vectors independently generate the same inequality.
                for _ in range(35):
                    x0=complex(rng.gauss(0,1),rng.gauss(0,1))
                    x1=complex(rng.gauss(0,1),rng.gauss(0,1))
                    nn=math.sqrt(abs(x0)**2+abs(x1)**2)
                    x0/=nn;x1/=nn
                    z0=-x1.conjugate();z1=x0.conjugate()
                    phi=2*math.pi*rng.random()
                    yy=cmath.exp(1j*phi)*math.sqrt(1-q*q)
                    y0=q*x0+yy*z0;y1=q*x1+yy*z1
                    # Sigma_x x=(x1,x0); Sigma_y x=(-i x1,i x0).
                    w1=y0.conjugate()*x1 + y1.conjugate()*x0
                    w2=y0.conjugate()*(-1j*x1) + y1.conjugate()*(1j*x0)
                    val=((alpha*abs(w1))**p+(beta*abs(w2))**p)**(1/p)
                    assert val <= target + 1.e-9, (p,q,alpha,beta,val,target)
                    checks += 1
    for q in (0.1,0.63,0.97):
        for alpha,beta in ((1,1),(2,1),(5,2)):
            assert abs(formula(math.inf,q,alpha,beta)-alpha)<1.e-12
            checks+=1
    print('PASS', checks, 'finite diagnostic assertions')

if __name__=='__main__':
    main()
