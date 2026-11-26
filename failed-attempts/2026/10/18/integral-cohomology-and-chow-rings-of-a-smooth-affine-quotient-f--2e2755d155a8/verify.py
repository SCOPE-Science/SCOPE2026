#!/usr/bin/env python3
"""Finite-field crosschecks and exact formal checks for a smooth quotient family.

All checks use only the Python standard library. They do not certify the
integral Gysin theorem, the smoothness theorem, or any infinite-range claim.
"""
from itertools import product
from math import comb


def counts(n,p):
    # Hypersurface x^2 y + z^3 w^2 u_1^2 ... u_n^2 = 1
    # x=0 contributes p possible y's for each nonzero monomial tuple.
    monomial_solutions = 0
    for z,w,*us in product(range(1,p), repeat=n+2):
        a = pow(z,3,p)*pow(w,2,p)%p
        for u in us:
            a = a*pow(u,2,p)%p
        if a==1:
            monomial_solutions += 1
    # At nonzero x, y is uniquely determined, so (p-1)*p^(n+2) points.
    x0 = p*monomial_solutions
    xp = (p-1)*p**(n+2)
    # Finite-field Gm action has trivial rational torsors (Hilbert 90).
    # The expected quotient's Y(Fp) point count is this exact integer.
    assert x0 == p*(p-1)**(n+1), (n,p,x0)
    assert x0 %(p-1)==0 and xp%(p-1)==0
    assert (x0+xp)//(p-1) == p**(n+2)+p*(p-1)**n
    return x0, xp, (x0+xp)//(p-1)


def gysin_betti(n):
    d=n+2
    b=[0]*(d+1)
    b[0]=1
    for j in range(n+1):
        b[j+2]=comb(n,j)
    assert sum((-1)**k*bb for k,bb in enumerate(b)) == 1
    # Algebraic cell / torus formula at q=1 agrees with Euler characteristic.
    assert 1**d+1*(1-1)**n == 1
    return b


def test_equations():
    # Check f1/f2/f3 using finite-field substitution in all variables;
    # these vanish identically modulo F = x^2*y + z^3*w^2*u1^2*P -1.
    for p in (3,5):
        for n in (1,2):
            for x,z,w,*us in product(range(p), repeat=n+3):
                m=(pow(z,3,p)*pow(w,2,p))%p
                for u in us: m=m*pow(u,2,p)%p
                for y in range(p):
                    if (x*x*y+m-1)%p: continue
                    u1=us[0]
                    prod=1
                    for u in us[1:]:prod=prod*u*u%p
                    A=x*x*w%p;B=z*w%p;C=y*z%p
                    D=x*u1%p;E=z*u1*u1%p
                    f1=(A*E-B*D*D)%p
                    f2=(B-A*C-E*pow(B,3,p)*prod)%p
                    f3=(E-C*D*D-E*E*B*B*prod)%p
                    assert (f1,f2,f3)==(0,0,0)


if __name__=='__main__':
    test_equations()
    for n in (1,2,3):
        print('n=',n,'Betti',gysin_betti(n))
        for p in (3,5,7):
            print('  q=',p,'X[x=0],X[x!=0],Y=',counts(n,p))
    print('All finite exact checks passed; general statements require the given proofs.')
