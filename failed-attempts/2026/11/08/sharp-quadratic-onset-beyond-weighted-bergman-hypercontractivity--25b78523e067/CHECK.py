#!/usr/bin/env python3
"""Standalone, finite checks for the weighted Bergman dilation expansion.
Run: python3 BERGMAN_CHECK.py. Only Python standard library is used.
Finite tests corroborate, but do not prove, the infinite-dimensional theorem.
"""
import math
from fractions import Fraction

checks=0

def test(ok, label):
    global checks
    if not ok: raise AssertionError(label)
    checks += 1

def rising(a,n):
    y=1
    for j in range(n): y*=a+j
    return y

def moment(a,n): return Fraction(math.factorial(n),rising(a,n))

def moment4_poly(a, coeff, r2):
    """Exact fourth-power integral for unnormalized polynomial coefficients."""
    terms=[sum(coeff[i]*coeff[k-i] for i in range(len(coeff))
             if 0<=k-i<len(coeff)) for k in range(2*len(coeff)-1)]
    return sum(moment(a,k)*r2**k*term**2 for k,term in enumerate(terms))

def moment2_poly(a, coeff):
    return sum(moment(a,k)*v*v for k,v in enumerate(coeff))

for alpha in (2,3,4,7,11):
    for k in range(1,29):
        weights=sum(Fraction(rising(alpha,i)*rising(alpha,k-i),math.factorial(i)*math.factorial(k-i)) for i in range(k+1))
        test(weights == Fraction(rising(2*alpha,k),math.factorial(k)), f'Chu-Vandermonde alpha={alpha},k={k}')
        ck=Fraction(rising(2*alpha,k), (2**k)*rising(alpha,k))
        if k==1: test(ck==1, 'first-mode equality')
        else: test(ck<Fraction(rising(2*alpha,k-1), (2**(k-1))*rising(alpha,k-1)), 'monotonicity')
    c2=Fraction(rising(2*alpha,2),4*rising(alpha,2))
    test(1-c2==Fraction(1,2*(alpha+1)), 'critical gap')
    # Exact norm identity for rational polynomials across radii.
    for coeff in [(Fraction(1),Fraction(2,3),Fraction(-1,4)),
                  (Fraction(3,2),Fraction(0),Fraction(1,8),Fraction(-2,5)),
                  (Fraction(1),Fraction(1),Fraction(1),Fraction(1))]:
        norm2=moment2_poly(alpha,coeff)
        test(norm2>0, 'norm positivity')
        for r2 in (Fraction(1,2),Fraction(7,13),Fraction(11,20)):
            F=moment4_poly(alpha,coeff,r2)
            # Independently multiply the polynomial and integrate each angular diagonal.
            product=[sum(coeff[i]*coeff[k-i] for i in range(len(coeff)) if 0<=k-i<len(coeff)) for k in range(2*len(coeff)-1)]
            alternate=sum(Fraction(math.factorial(k),rising(alpha,k))*r2**k*product[k]*product[k] for k in range(len(product)))
            test(F==alternate,'independent moment expansion')
    # Trial f=a0+a1 e1 + a2 e2, normalized in A²_alpha.
    m=math.sqrt(2*alpha/(alpha+1))
    for delta in (0.001,0.0005,0.0002):
        a1=math.sqrt((alpha+1)*delta)
        a2=m*a1*a1/2
        a0=math.sqrt(1-a1*a1-a2*a2)
        # unnormalized Taylor coefficients from normalized monomial basis.
        vec=(a0,a1*math.sqrt(alpha),a2*math.sqrt(alpha*(alpha+1)/2))
        fourth=float(moment4_poly(alpha,vec, (1+delta)/2))
        test(abs(float(moment2_poly(alpha,vec))-1)<2e-13,'normalized trial')
        test(abs((fourth-1)/delta**2-(alpha+1)) < 0.15*(alpha+1), 'supercritical limiting coefficient')
    for n in range(2,25):
        test(0<2-2**(2-n)<2,'positive high-mode spectral deficit')
print('BERGMAN_SUPERCRITICAL_CHECKS_PASS',checks)
