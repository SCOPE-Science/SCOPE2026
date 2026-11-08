#!/usr/bin/env python3
"""Standalone arithmetic diagnostics for a positive-extrapolation resolvent gain theorem.

Only the proof in RESULT.md establishes its universal quantifiers. This script
checks the displayed rational example and representative bounded linear cases.
"""
from fractions import Fraction as F
import cmath
import math
import random


def c(theta, q):
    return math.sqrt(theta*theta+(1-theta*theta)*q*q)


def psi(theta, q):
    return (1-q)*(1+theta)+c(theta,q)


def criterion(mu_a, mu_b, L, alpha, theta):
    q=1/(1+alpha*mu_a)
    return mu_a*mu_b > L*psi(theta,q)


def det2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]


def det_I_minus(m):
    return (1-m[0][0])*(1-m[1][1])-m[0][1]*m[1][0]


def run():
    groups=0
    # Verify all arithmetic using exact rational numbers for the separation.
    q=F(1,4); b=F(4,5); g=F(29,100)
    new=[[q,q*g],[b,b*(1+2*q*g)]]
    old=[[q,q*g],[b*(2*q+1),b*(1+2*q*g)]]
    assert det_I_minus(new)==F(1,200)
    assert det_I_minus(old)==-F(3,125)
    assert (1-q)*(1-b)>q*b*g*(3-2*q)
    assert (1-q)*(1-b)<q*b*g*3
    assert F(3,4)>F(29,100)*(3-2*q)
    assert F(3,4)<3*F(29,100)
    groups+=1

    # A skew operator has a resolvent on the boundary of the FNE disk;
    # it realizes the claimed sharp transfer factor at every theta in [0,1].
    for k in range(1,100):
        q=k/100
        nu=math.sqrt(1-q*q)/q
        z=1/(1+1j*nu)
        assert abs(abs(z)-q)<2e-14
        for j in range(21):
            theta=j/20
            lhs=abs((1+theta)*z-theta)
            assert abs(lhs-c(theta,q))<2e-13, (q,theta,lhs,c(theta,q))
            assert c(theta,q)<=(1+theta)*q+theta+1e-13
            groups+=1

    # Exact scalar iteration p(1) = det(I-T) = alpha beta q b (muA muB - LH)
    for na in [F(1,4),F(1),F(2),F(7,2)]:
        for nb in [F(1,5),F(1),F(5)]:
            for lh in [F(0),na*nb,F(3)*na*nb/F(2)]:
                for alpha in [F(1,10),F(1),F(3)]:
                    for beta in [F(1,7),F(2)]:
                        for theta in [F(0),F(1,3),F(1)]:
                            q=1/(1+alpha*na)
                            b=1/(1+beta*nb)
                            t=[[q,alpha*q*lh],
                               [beta*b*((1+theta)*q-theta),
                                b*(1+alpha*beta*(1+theta)*q*lh)]]
                            assert det_I_minus(t)==alpha*beta*q*b*(na*nb-lh)
                            groups+=1

    # For all extrapolations the refined threshold is at most its theta=1 value.
    for q in [j/50 for j in range(1,50)]:
        for theta in [j/40 for j in range(41)]:
            assert psi(theta,q)<=3-2*q+1e-12
            assert psi(theta,q)>=1-1e-12
            groups+=1

    rng=random.Random(20261107)
    # On positive-curvature-plus-skew planar operators, the resolvent is FNE
    # and the improved componentwise gain bounds the exact two-block map.
    for _ in range(4000):
        mu_a=10**rng.uniform(-1,1)
        mu_b=10**rng.uniform(-1,1)
        alpha=10**rng.uniform(-2,1)
        beta=10**rng.uniform(-2,1)
        L=10**rng.uniform(-2,1)
        theta=rng.random()
        skew_a=rng.uniform(-3,3)
        skew_b=rng.uniform(-3,3)
        phase=rng.uniform(-math.pi,math.pi)
        ja=1/(1+alpha*(mu_a+1j*skew_a))
        jb=1/(1+beta*(mu_b+1j*skew_b))
        H=L*cmath.exp(1j*phase)
        q=1/(1+alpha*mu_a)
        b=1/(1+beta*mu_b)
        # first-row output for arbitrary differences
        dy=complex(rng.uniform(-2,2),rng.uniform(-2,2))
        dx=complex(rng.uniform(-2,2),rng.uniform(-2,2))
        dyp=ja*(dy-alpha*H*dx)
        dep=(1+theta)*dyp-theta*dy
        dxp=jb*(dx+beta*dep)
        uy=q*abs(dy)+alpha*q*L*abs(dx)
        ux=beta*b*c(theta,q)*abs(dy)+b*(1+alpha*beta*(1+theta)*q*L)*abs(dx)
        assert abs(dyp)<=uy+1e-11
        assert abs(dxp)<=ux+1e-11
        groups+=1
    print('PASS:',groups,'exact and numerical diagnostic groups')
    print('PASS: separation determinants',det_I_minus(new),det_I_minus(old))


if __name__=='__main__':
    run()
