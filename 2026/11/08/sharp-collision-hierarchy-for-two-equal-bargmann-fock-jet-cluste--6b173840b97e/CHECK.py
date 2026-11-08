"""Numerical cross-checks for Bargmann--Fock double-jet collision laws.

Requires mpmath. Run `python CHECK.py` from this directory.
Tests supplement, rather than replace, the all-order exterior-minor proof.
"""
import math
import mpmath as mp

mp.mp.dps = 90
checks = 0

def check(value, message):
    global checks
    checks += 1
    assert bool(value), message


def laguerre_poly(n, alpha, t):
    return mp.fsum(mp.binomial(n+alpha,n-h)*(-t)**h/mp.factorial(h) for h in range(n+1))

def normalized_overlap(m, r):
    """Laguerre-polynomial transition amplitudes, independent of Taylor minors."""
    t = r*r
    E = mp.exp(-t/2)
    C = mp.matrix(m)
    for k in range(m):
        for j in range(m):
            if k >= j:
                C[k, j] = E*mp.sqrt(mp.factorial(j)/mp.factorial(k))*r**(k-j)*laguerre_poly(j, k-j, t)
            else:
                C[k, j] = E*mp.sqrt(mp.factorial(k)/mp.factorial(j))*(-r)**(j-k)*laguerre_poly(k, j-k, t)
    return C


def direct_coefficient(k, j, r):
    """Coefficient of z**k in the normalized displaced Fock monomial."""
    a = mp.fsum(mp.binomial(j, ell)*(-r)**(j-ell)*r**(k-ell)/mp.factorial(k-ell)
                for ell in range(min(j,k)+1))
    return mp.exp(-r*r/2)*mp.sqrt(mp.factorial(k)/mp.factorial(j))*a


def gam(m, p):
    return (mp.factorial(p-1)**2 / (mp.factorial(2*p-1)*mp.factorial(2*p-2))
            * mp.sqrt(mp.factorial(m+p-1)/mp.factorial(m-p)))


def minor_c(m, p):
    return (mp.sqrt(mp.fprod(mp.factorial(m+i)/mp.factorial(m-p+i) for i in range(p)))
            * mp.fprod(mp.factorial(i)/mp.factorial(p+i) for i in range(p)))


# The exact leading-minor identity can be independently evaluated as a determinant.
for m in range(1, 7):
    for p in range(1, m+1):
        A = mp.matrix([[1/mp.factorial(p+i-j) for j in range(p)] for i in range(p)])
        exact = mp.fprod(mp.factorial(i)/mp.factorial(p+i) for i in range(p))
        check(mp.almosteq(mp.det(A),exact,rel_eps=mp.mpf('1e-75')),
              ('factorial determinant',m,p))
        check(mp.almosteq(minor_c(m,p)/minor_c(m,p-1) if p>1 else minor_c(m,p),
                          gam(m,p), rel_eps=mp.mpf('1e-75')),
              ('exterior-product quotient',m,p))

# Independently reconstruct the Gram block by evaluating Fock monomial coefficients.
for m in range(1, 6):
    for s in ['0.16', '0.3', '0.72', '1.1', '2.0']:
        r = mp.mpf(s)
        C = normalized_overlap(m,r)
        I = mp.eye(m)
        K = I-C.T*C
        eig = list(mp.eigsy(K,eigvals_only=True))
        check(all(v>0 for v in eig), ('positive leakage',m,s))
        check(all(v<1 for v in eig), ('strictly subunit leakage',m,s))
        for j in range(m):
            for k in range(m):
                check(mp.almosteq(C[k,j],direct_coefficient(k,j,r),abs_eps=mp.mpf('1e-80')),
                      ('direct Fock overlap',m,s,j,k))
        for j in range(m):
            for l in range(m):
                tail=mp.fsum(direct_coefficient(k,j,r)*direct_coefficient(k,l,r)
                             for k in range(m,m+155))
                check(mp.almosteq(K[j,l],tail,abs_eps=mp.mpf('1e-75')),
                      ('independent leakage identity',m,s,j,l))
        # The block Gram spectrum equals 1 +/- singular values of the overlap block.
        G=mp.matrix(2*m)
        for j in range(m):
            for k in range(m):
                G[j,k]=int(j==k)
                G[j+m,k+m]=int(j==k)
                G[j,k+m]=C[j,k]
                G[k+m,j]=C[j,k]
        vals=list(mp.eigsy(G,eigvals_only=True))
        lambdas=sorted([1-mp.sqrt(1-v) for v in eig]+[1+mp.sqrt(1-v) for v in eig])
        check(all(mp.almosteq(x,y,abs_eps=mp.mpf('1e-72')) for x,y in zip(vals,lambdas)),
              ('Gram eigenvalue pairing',m,s))
        if r <= mp.mpf('0.3'):
            # Sharp powers/constants: all p simultaneous (stronger than least mode).
            for p,v in enumerate(eig[::-1],1):
                ratio=mp.sqrt(v)/(gam(m,p)*r**(2*p-1))
                check(abs(ratio-1)<mp.mpf('0.35'), ('collision power test',m,p,s,ratio))
                if r<=mp.mpf('0.16'):
                    check(abs(ratio-1)<mp.mpf('0.08'), ('small r constant test',m,p,s,ratio))
        if m==2:
            t=r*r
            sigma=mp.exp(-t/2)*(mp.sqrt(4+t*t)+t)/2
            check(mp.almosteq(vals[0],1-sigma,abs_eps=mp.mpf('1e-75')),
                  ('closed formula at two jets',s))

print('PASS:', checks, 'high-precision finite-dimensional assertions')
