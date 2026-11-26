#!/usr/bin/env python3
"""Independent algebraic and quadrature checks for planar Gaussian sketch projections.

The universal theorem rests on the accompanying analytic proof, not on these finite checks.
Requires Python 3 and SymPy.
"""
import math
import sympy as sp


def require(cond, why):
    if not bool(cond):
        raise AssertionError(why)


def symbolic():
    q = sp.symbols('q', real=True)
    a4 = (3 + 4*q + q*q)/8
    b4 = (3 - 4*q + q*q)/8
    c4 = (1-q*q)/8
    M = sp.Matrix([[a4, c4], [c4, b4]])
    lam = sp.symbols('lam')
    characteristic = sp.factor((M-lam*sp.eye(2)).det())
    require(sp.simplify(characteristic -
       (lam*lam-(3+q*q)*lam/4+(1-q*q)/8)) == 0,
       'characteristic polynomial mismatch')
    require(sp.simplify((1+4*q-q*q)**2-(1+14*q*q+q**4)-8*q*(1-q*q)) == 0,
       'strict one-step versus asymptotic gap identity mismatch')
    require(sp.simplify((3+q*q)**2-(1+14*q*q+q**4)-8*(1-q*q)) == 0,
       'positive eigenvalue discriminant mismatch')
    Mhalf=M.subs(q, sp.Rational(1,2))
    require(Mhalf==sp.Matrix([[sp.Rational(21,32),sp.Rational(3,32)],
                              [sp.Rational(3,32),sp.Rational(5,32)]]),
            'rational example matrix mismatch')
    require(Mhalf.eigenvals()=={(13+sp.sqrt(73))/32:1,(13-sp.sqrt(73))/32:1},
            'rational example eigenvalue mismatch')
    # Check true quadratic decrease and exact line subproblem update.
    h1,h2,x1,x2,z1,z2=sp.symbols('h1 h2 x1 x2 z1 z2',nonzero=True)
    H=sp.diag(h1,h2);x=sp.Matrix([x1,x2]);z=sp.Matrix([z1,z2])
    d=(z.T*H*z)[0];gd=(z.T*H*x)[0]
    xp=x-z*gd/d
    energy_drop=sp.factor(((x.T*H*x)[0]-(xp.T*H*xp)[0])/2-gd**2/(2*d))
    require(energy_drop==0,'exact line-search energy identity mismatch')
    return 6


def quadrature():
    # Deterministic midpoint trapezoidal integration of smooth 2pi-periodic functions,
    # not evidence of universal identities or infinite-dimensional claims.
    n=32768; tol=2e-10
    tested=0
    for aa,bb in [(1,1),(1,sp.Rational(3,2)),(1,2),(1,3),(1,5),(2,7),(3,4),(1,11)]:
        a=float(aa);b=float(bb)
        q=(b-a)/(b+a)
        t2=t4=u4=v4=uv=0.0
        for j in range(n):
            t=(j+0.5)*2*math.pi/n
            c=math.cos(t); s=math.sin(t)
            norm2=a*a*c*c+b*b*s*s
            v1sq=b*b*s*s/norm2
            v2sq=a*a*c*c/norm2
            t2+=v1sq
            t4+=v1sq*v1sq
            u4+=v2sq*v2sq
            uv+=v1sq*v2sq
        obs=[t2/n,t4/n,u4/n,uv/n]
        target=[(1+q)/2,(3+4*q+q*q)/8,(3-4*q+q*q)/8,(1-q*q)/8]
        for o,t in zip(obs,target):
            require(abs(o-t)<tol, f'angular moment quadrature mismatch a={a}, b={b}: {o} != {t}')
            tested+=1
    return tested


if __name__=='__main__':
    checks=symbolic()+quadrature()
    print('VERIFY_OK', checks, 'symbolic/periodic-quadrature checks')
