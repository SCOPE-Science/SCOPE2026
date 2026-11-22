#!/usr/bin/env python3
"""Check exact identities and finite-precision examples for a passive-sampler pulse model.

This script does not replace the general symbolic proof in RESULT.md.
Requires only Python's standard library.
"""
from fractions import Fraction as F
from math import exp, expm1, log, isclose
from random import Random


def recovered(q1, q2, q3):
    s = q2 / q1
    v = q3 / q1
    d2 = 4 * v - 3 * s * s
    if d2 <= 0:
        raise ValueError("not a non-degenerate pulse")
    delta = d2 ** .5
    return (s + delta) / 2, (s - delta) / 2, q1 / delta


def readings(C, x, z):
    return tuple(C * (x**j - z**j) for j in (1, 2, 3))


def check():
    n = 0
    C, X, Z = F(4), F(1, 2), F(1, 4)
    q1, q2, q3 = readings(C, X, Z)
    assert (q1, q2, q3) == (F(1), F(3, 4), F(7, 16)); n += 1
    s, v = q2/q1, q3/q1
    delta_sq = 4*v - 3*s*s
    assert delta_sq == F(1, 16) and X-Z == F(1, 4); n += 1
    assert C*(X-Z) == q1; n += 1
    q4 = C*(X**4-Z**4)
    assert q4 == F(15, 64); n += 1
    assert q1*q1*q4 == q2 * (2*q1*q3-q2*q2); n += 1
    # Two-channel ambiguity: same q1, q2, but distinct 3rd channel.
    X2, Z2 = F(9,16), F(3,16)
    C2 = q1/(X2-Z2)
    p1,p2,p3 = readings(C2,X2,Z2)
    assert p1==q1 and p2==q2 and p3!=q3; n += 1
    # Exact Jacobian determinant with variables (C, X, Z).
    def det3(M):
        a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
        return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    JJ=[[X**j-Z**j, C*j*X**(j-1), -C*j*Z**(j-1)] for j in (1,2,3)]
    assert det3(JJ)==-C*C*(X-Z)**4==F(-1,16);n+=1
    # Local sensitivity: perturb the third normalized channel only.
    eps=1e-8
    cp=recovered(float(q1),float(q2),float(q3)+eps)[2]
    cm=recovered(float(q1),float(q2),float(q3)-eps)[2]
    assert isclose((cp-cm)/(2*eps),-128.,rel_tol=2e-7);n+=1
    # Exact derivatives from the implicit inverse and Jacobian.
    assert -2/(X-Z)**3 == -128; n += 1
    sensitivity = 2*(X**2+X*Z+Z**2)/(X-Z)**2
    assert sensitivity == F(14); n += 1
    # 15,000 interior models: reconstruct one rectangular pulse from 3 channels.
    rng = Random(20261120)
    for i in range(15000):
        Zf = rng.uniform(0.08, 0.65)
        Xf = rng.uniform(Zf+0.03, .99)
        Cf = rng.uniform(0.1, 20)
        a,b,c = readings(Cf,Xf,Zf)
        xr,zr,cr = recovered(a,b,c)
        assert isclose(xr, Xf, rel_tol=3e-10, abs_tol=3e-12)
        assert isclose(zr, Zf, rel_tol=3e-10, abs_tol=3e-12)
        assert isclose(cr, Cf, rel_tol=4e-10, abs_tol=3e-11)
        n+=3
    # Relative q3 sensitivity is exactly dependent on pulse width only.
    for i in range(1000):
        h = rng.uniform(0.2, 3.)
        r = exp(-h)
        S = 2*(1+r+r*r)/(1-r)**2
        Xf = rng.uniform(0.5, 0.95)
        Zf = Xf*r
        Cx = rng.uniform(.5,5.)
        aa,bb,cc = readings(Cx,Xf,Zf)
        Sr = 2*cc/(Cx*(Xf-Zf)**3)
        assert isclose(S,Sr,rel_tol=1e-10);n+=1
    # Sharp short-pulse coefficient 6 and strict monotonicity in duration.
    last = 1e100
    for i in range(1000):
        h = .01 + (i/999)*5.
        r = exp(-h)
        S = 2*(1+r+r*r)/(1-r)**2
        assert S<last; n+=1
        last=S
    for h in (1e-2,1e-3,1e-4):
        r=exp(-h)
        S=2*(1+r+r*r)/(1-r)**2
        assert abs(S*h*h/6-1)<h*.03; n+=1
    print(f"PASS: {n} assertions; exact witness, ambiguity, inversion, stability and asymptotic checks")

if __name__=='__main__': check()
