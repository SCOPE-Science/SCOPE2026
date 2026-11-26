#!/usr/bin/env python3
"""Independent finite consistency checks for two concentric kernel-sampling rings.
Requires Python 3, numpy, sympy. The theorem is proved analytically elsewhere;
finite tests are not a certificate for unbounded integer kernel order or node count.
"""
import math, cmath
from math import comb
import numpy as np
import sympy as sp


def poly_numerator(n, m, order):
    x = sp.Symbol('x')
    p = sp.Integer(1)
    for j in range(1,order):
        p=sp.cancel(sp.expand(((m+j)+(n*j-m-j)*x)*p+n*x*(1-x)*sp.diff(p,x))/j)
        p=sp.expand(p)
    return sp.Poly(p,x)


def alias(n,m,a,t):
    p=poly_numerator(n,m,a)
    z=complex(t)
    # Horner order constant-to-leading reversal
    numer=0j
    for c in p.all_coeffs():numer=numer*z+complex(c)
    return numer/(1-z)**a


def spectrum_blocks(n,a,r,s,delta):
    out=[]
    for m in range(n):
        A=n*(r**(2*m))*alias(n,m,a,r**(2*n)).real
        C=n*(s**(2*m))*alias(n,m,a,s**(2*n)).real
        B=n*((r*s)**m)*abs(alias(n,m,a,(r*s)**n*cmath.exp(-1j*n*delta)))
        disc=math.hypot(A-C,2*B)
        out.extend(((A+C-disc)/2,(A+C+disc)/2))
    return np.array(sorted(out,reverse=True))


def direct_spectrum(n,a,r,s,delta):
    zeta=cmath.exp(2j*math.pi/n)
    points=[r*zeta**j for j in range(n)]+[s*cmath.exp(1j*delta)*zeta**j for j in range(n)]
    K=np.array([[(1-z*complex(w).conjugate())**(-a) for w in points] for z in points],dtype=complex)
    return np.linalg.eigvalsh(K)[::-1]


def run():
    root_cases=0
    for n in range(2,8):
        for a in range(1,10):
            for m in range(n):
                p=poly_numerator(n,m,a)
                assert all(c>0 for c in p.all_coeffs())
                if p.degree()>0 and a<=7 and n<=5:
                    # Number of distinct negative real roots: exact Sturm calculation.
                    assert p.count_roots(-sp.oo, 0) == p.degree(),(n,m,a,p)
                    root_cases+=1
    cases=0
    for n,a,r,s in [(2,1,.23,.71),(3,2,.34,.85),(4,3,.29,.77),
                    (5,4,.41,.88),(7,5,.22,.84),(6,8,.38,.78),(8,10,.26,.72)]:
        low=spectrum_blocks(n,a,r,s,math.pi/n)
        high=spectrum_blocks(n,a,r,s,0.0)
        assert np.min(low)>0
        for v in [.06,.18,.31,.58,.79,.96]:
            delta=v*math.pi/n
            mid=spectrum_blocks(n,a,r,s,delta)
            assert np.max(abs(direct_spectrum(n,a,r,s,delta)-mid))<1.e-7
            assert np.all(np.cumsum(low) <= np.cumsum(mid)+1.e-7)
            assert np.all(np.cumsum(mid) <= np.cumsum(high)+1.e-7)
            assert abs(sum(mid)-sum(low))<1.e-7
            assert low[0]<mid[0] and low[-1]>mid[-1]
            assert sum(1/low) < sum(1/mid) and sum(1/mid)<sum(1/high)
            assert sum(np.log(low))>sum(np.log(mid)) and sum(np.log(mid))>sum(np.log(high))
            cases+=1
    print('PASS root_cases=',root_cases,'all_polynomial_cases=',sum(n*9 for n in range(2,8)))
    print('PASS independent_kernel_spectrum_cases=',cases)

if __name__=='__main__':run()
