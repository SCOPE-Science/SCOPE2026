"""Reproducible exact checks for the first three power-flow prolongations.
This file performs finite consistency tests only, not a proof for all exponents.
"""
import sympy as s
from math import gcd
from functools import reduce

a,b,z=s.symbols('a b z')

def deriv(f,n):
    return s.expand(b**n*s.diff(f,a)+a**n*s.diff(f,b))

def jet(n):
    A=[a];B=[b]
    for i in range(4):
        A.append(deriv(A[-1],n)); B.append(deriv(B[-1],n))
    return A,B

def homogenized_poly_at_a1(f,d):
    p=s.Poly(f,a,b)
    return s.Poly(sum(int(c)*b**j*z**(d-i-j) for (i,j),c in p.terms()),b,z)

for n in range(3,9):
    A,B=jet(n)
    assert s.expand(A[4]-n*a**(n-2)*b**(n-3)*((n-1)*(n-2)*a**(2*n+2)+n*(4*n-3)*a**(n+1)*b**(n+1)+n*(n-1)*b**(2*n+2)))==0
    for m in range(4):
        l=m+1;d=1+l*(n-1)
        H=s.gcd(A[l],B[l]);expected=(a*b)**max(n-m,0) if m>=1 else 1
        assert s.simplify(H/expected).is_number, (n,m,H,expected)
        if m>=n:
            assert m==n==3
            continue
        if m==0:continue
        r=n-m;M=m*(n-1)
        # A choice of coefficients with nonvanishing pure B_1 term, sufficient for Newton initial ideals.
        F=homogenized_poly_at_a1(A[l]+B[1],d)
        G=homogenized_poly_at_a1(B[l]+2*B[1],d)
        termsF=[(int(c),i,j) for (i,j),c in F.terms()]
        termsG=[(int(c),i,j) for (i,j),c in G.terms()]
        wF=min(i*M+j*r for c,i,j in termsF)
        wG=min(i*M+j*r for c,i,j in termsG)
        Lf={(i,j) for c,i,j in termsF if i*M+j*r==wF}
        Lg={(i,j) for c,i,j in termsG if i*M+j*r==wG}
        assert wF==r*M==wG, (n,m,wF,wG,r*M)
        assert Lf=={(r,0),(0,M)},(n,m,Lf)
        assert Lg=={(0,M)},(n,m,Lg)
        degree=d*d-2*r*M
        assert degree==(m*m+1)*n*n-m*m, (n,m,degree)
    print(n,[(m,((m*m+1)*n*n-m*m)) for m in range(4)])
print('PASS: jets, gcds, weighted initial forms, numerical degree identities for n=3..8, m=0..3')
