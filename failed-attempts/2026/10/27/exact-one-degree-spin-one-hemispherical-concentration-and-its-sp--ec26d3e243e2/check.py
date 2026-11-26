"""Independent rational and numerical checks for spin-one hemisphere localization.

Run: python check.py. Requires SymPy, NumPy, and SciPy.
Finite checks supplement, but do not replace, the all-degree proof.
"""
from fractions import Fraction
from math import comb, factorial, pi
import numpy as np
from scipy.special import lpmv, gammaln, roots_legendre
import sympy as sp


def predicted(ell, m):
    k = abs(m)
    if k == 0 or (ell + k) % 2:
        return Fraction(1, 2)
    a, b = (ell + k) // 2, (ell - k) // 2
    delta = Fraction((2*ell + 1)*k*comb(2*a, a)*comb(2*b, b),
                     2*ell*(ell + 1)*4**ell)
    return Fraction(1, 2) + (-delta if m > 0 else delta)


def exact_integral(ell, m):
    x = sp.symbols('x')
    k = abs(m)
    P = sp.legendre(ell, x)
    Q = sp.diff(P, x, k)
    if k:
        bracket = (1-x*x)*sp.diff(Q,x) + (m-k*x)*Q
        integrand = sp.expand((1-x*x)**(k-1)*bracket**2)
    else:
        integrand = sp.expand((1-x*x)*sp.diff(P,x)**2)
    factor = sp.Rational((2*ell+1)*factorial(ell-k),
                         2*ell*(ell+1)*factorial(ell+k))
    return factor*sp.integrate(integrand, (x,0,1))


def numeric_integral(ell,m,x,w):
    k=abs(m)
    nrm = np.exp(.5*(np.log((2*ell+1)/(4*pi))+
                   gammaln(ell-k+1)-gammaln(ell+k+1)))
    P=lpmv(k,ell,x)
    prev=lpmv(k,ell-1,x) if k<ell else np.zeros_like(x)
    derivative=((ell+k)*prev-ell*x*P)/(1-x*x)
    R=nrm*(np.sqrt(1-x*x)*derivative+m*P/np.sqrt(1-x*x))
    return 2*pi/(ell*(ell+1))*np.dot(w,R*R)


def main():
    exact=0; numeric=0; ordering=0
    for ell in range(1,11):
        for m in range(-ell,ell+1):
            value=exact_integral(ell,m)
            want=predicted(ell,m)
            assert value==sp.Rational(want.numerator,want.denominator), (ell,m,value,want)
            exact+=1
    x,w=roots_legendre(180);x=(x+1)/2;w=w/2
    worst=0.0
    for ell in range(1,29):
        vals=[]
        for m in range(-ell,ell+1):
            v=numeric_integral(ell,m,x,w)
            err=abs(v-float(predicted(ell,m)))
            worst=max(worst,err)
            assert err<1e-10,(ell,m,v,predicted(ell,m))
            vals.append(v)
            numeric+=1
        assert abs(sum(vals)-(2*ell+1)/2)<1e-9
        numeric+=1
    for ell in range(1,201):
        vals=[predicted(ell,m) for m in range(-ell,ell+1)]
        d=predicted(ell,-ell)-Fraction(1,2)
        assert max(vals)==predicted(ell,-ell)
        assert min(vals)==predicted(ell,ell)
        assert vals.count(Fraction(1,2))==(ell+1 if ell%2==0 else ell)
        assert sum(vals)==Fraction(2*ell+1,2)
        ordering+=4
        if ell>=2:
            second=max(v for m,v in zip(range(-ell,ell+1),vals) if m!=-ell)
            gap=d*Fraction(ell+1,2*ell-1)
            assert second==predicted(ell,-ell)-gap
            ordering+=1
        if ell>=2:
            dprev=predicted(ell-1,-(ell-1))-Fraction(1,2)
            assert d==dprev*Fraction(2*ell+1,2*(ell+1))
            ordering+=1
    print(f'PASS: {exact} exact rational integrals, {numeric} quadrature/trace checks, {ordering} exact spectral and gap checks.')
    print(f'Maximum absolute Gauss-Legendre discrepancy: {worst:.3g}.')
    print('Sample spectrum ell=3:', [str(predicted(3,m)) for m in range(-3,4)])

if __name__=='__main__':
    main()
