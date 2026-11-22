"""Finite diagnostics for a small-radius finite-Blaschke boundary-speed theorem.

Python >=3.9; standard library only. The analytic proof, not these tests,
handles every degree and a continuous range of small radii.
"""
from fractions import Fraction
from math import cos, pi
import cmath


def mul(a,b):
    return (a[0]*b[0],a[0]*b[1]+a[1]*b[0])


def p_sums_linear(n,c,mmax):
    """Constant and linear Taylor coefficients in t of Newton power sums."""
    a={0:(Fraction(-1),c),1:(Fraction(0),-c)}
    p={0:(Fraction(n),Fraction(0))}
    for m in range(1,mmax+1):
        v=(Fraction(0),Fraction(0))
        if m<=n:
            for j in range(1,m):
                v=(v[0]+mul(a.get(n-j,(0,0)),p[m-j])[0],
                   v[1]+mul(a.get(n-j,(0,0)),p[m-j])[1])
            a_term=a.get(n-m,(Fraction(0),Fraction(0)))
            v=(v[0]+m*a_term[0],v[1]+m*a_term[1])
        else:
            for j in range(1,n+1):
                term=mul(a.get(n-j,(0,0)),p[m-j])
                v=(v[0]+term[0],v[1]+term[1])
        p[m]=(-v[0],-v[1])
    return p


def perturbed_zeros(n,r):
    c=n*n/(n-1)**2
    t=r*r
    def poly(z):return z**n-1-c*t*(z-1)
    def deriv(z):return n*z**(n-1)-c*t
    roots=[]
    for k in range(n):
        z=cmath.exp(2j*pi*k/n)
        for _ in range(35):
            delta=poly(z)/deriv(z)
            z-=delta
            if abs(delta)<1e-14:break
        assert abs(poly(z))<1e-10
        roots.append(z)
    assert abs(roots[0]-1)<1e-12
    assert all(abs(z)<1 for z in roots[1:])
    return [r*z for z in roots]


def energy(a):
    # Positive-term Parseval sum avoids cancellation at tiny radii.
    return sum(abs(sum(x**m for x in a))**2 for m in range(1,101))


def main():
    checks=0
    for n in range(3,14):
        c=Fraction(n*n,(n-1)**2)
        p=p_sums_linear(n,c,n)
        assert p[n-1]==(0,(n-1)*c)
        assert p[n]==(n,-n*c)
        for m in range(1,n-1):assert p[m]==(0,0)
        # Only p_n(0), its linear response, and p_(n-1)'(0)
        # contribute to the first two energy powers t^n,t^(n+1).
        leading=n*n
        correction=2*n*p[n][1]+p[n-1][1]**2
        assert leading==n*n
        assert correction==Fraction(-n**4,(n-1)**2)
        checks+=5+n-2
    for n in range(3,10):
        for r in (0.07,0.12,0.20):
            a=perturbed_zeros(n,r)
            regular=[r*cmath.exp(2j*pi*k/n) for k in range(n)]
            e=energy(a); e0=energy(regular)
            target=n*n*r**(2*n)-(n**4/(n-1)**2)*r**(2*n+2)
            assert 0<e<e0
            # This is a finite diagnostic: an O_n(r^(2n+4)) residual.
            relative_residual=abs(e-target)/r**(2*n+4)
            assert relative_residual < 2000*n**4
            checks+=3
    print('PASS: exact Newton tests for degrees 3..13; numerical polygon tests for degrees 3..9')

if __name__=='__main__':main()
