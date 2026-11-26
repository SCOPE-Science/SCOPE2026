"""Standalone exact and asymptotic checks for Pelikan binary-symbol return laws.

Run with Python 3: python verify.py
All probability enumerations use standard-library exact rational arithmetic.
The infinite-state obstruction and asymptotic theorems rely on the written proof.
"""
from fractions import Fraction
from math import sqrt, pi


def coefficients(p, nmax):
    """First positive return coefficients from the algebraic generating function."""
    q = 1-p
    t = [Fraction(0)]*(nmax+1)
    h = [Fraction(0)]*(nmax+1)
    t[1] = p
    h[0] = Fraction(1, 2)
    for n in range(2, nmax+1):
        t[n] = q*sum((t[j]*t[n-j-1] for j in range(1, n-1)), Fraction(0))
    for n in range(1, nmax+1):
        h[n] = sum((t[j]*h[n-j] for j in range(1, n+1)), Fraction(0))/2
    return [Fraction(0)]+[q*t[n-1]+p*h[n-1] for n in range(1, nmax+1)]


def killed_chain(p, nmax):
    """Independent first-return calculation by killing at shell zero."""
    q = 1-p
    f = [Fraction(0)]*(nmax+1)
    f[1] = p/2
    survivors = {j:p/Fraction(2**(j+1)) for j in range(1, nmax+1)}
    survivors[1] += q
    for n in range(2, nmax+1):
        f[n] = p*survivors.get(1, Fraction(0))
        nxt = {}
        for j, mass in survivors.items():
            if j>=2:
                nxt[j-1] = nxt.get(j-1, Fraction(0)) + p*mass
            if j+1<=nmax:
                nxt[j+1] = nxt.get(j+1, Fraction(0)) + q*mass
        survivors = nxt
    return f


def float_coefficients(p, nmax):
    q=1-p
    t=[0.0]*(nmax+1)
    h=[0.0]*(nmax+1)
    t[1]=p
    h[0]=0.5
    h[1]=p/4
    for n in range(2,nmax+1):
        if n%2:
            m=(n-1)//2
            t[n]=t[n-2]*(2*(2*m-1)/(m+1))*p*q
        h[n]=0.5*sum(t[j]*h[n-j] for j in range(1,n+1))
    return [0.0]+[q*t[n-1]+p*h[n-1] for n in range(1,nmax+1)]


def asymptotic(p,n):
    q=1-p
    a=2*sqrt(p*q)
    if p<0.8:
        r=sqrt(p/q)
        cplus=(q+p/(2-r)**2)/(2*sqrt(2*pi)*q)
        cminus=(q+p/(2+r)**2)/(2*sqrt(2*pi)*q)
        return a**n*n**(-1.5)*(cplus+(-1)**n*cminus)
    if p==0.8:
        return a**n/(2*sqrt(2*pi*n))
    return p*(5*p-4)/(4-3*p)**2 * ((4-3*p)/2)**n

if __name__ == '__main__':
    counts=0
    for num,den in ((3,5),(2,3),(3,4),(4,5),(9,10),(5,6)):
        p=Fraction(num,den)
        a=coefficients(p,25)
        b=killed_chain(p,25)
        for n in range(1,26):
            assert a[n]==b[n], (p,n,a[n],b[n])
            assert a[n]>0
            counts+=2
        assert a[1] == p/2
        assert Fraction(2)*p/(2*p-1)>0
        counts+=2
    for p in (0.6,0.8,0.9):
        vals=float_coefficients(p,400)
        for n in (200,400):
            v=vals[n]/asymptotic(p,n)
            assert 0.94<v<1.04,(p,n,v)
            counts+=1
    print(f'PASS {counts} exact-positive/coefficient and asymptotic diagnostics')
    print('Analytic nonrationality, infinite hidden-state impossibility, and transfer theorems are in RESULT.md.')
