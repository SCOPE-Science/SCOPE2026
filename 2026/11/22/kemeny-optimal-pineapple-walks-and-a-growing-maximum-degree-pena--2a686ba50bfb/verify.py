"""Exact and numerical checks for optimal stochastic walks on clique-pineapple networks.
Run: python verify.py (requires SymPy; NumPy optional for random competitors).
"""
from fractions import Fraction
import math
import random
import sympy as sp

assertions = 0

def check(p):
    global assertions
    assert p
    assertions += 1

def L_from_weights(n, r, a, b, c):
    N = n + r
    L = sp.zeros(N)
    def add(i,j,w):
        L[i,i] += w; L[j,j] += w
        L[i,j] -= w; L[j,i] -= w
    for i in range(1,n): add(0,i,a)
    for j in range(n,N): add(0,j,b)
    for i in range(1,n):
        for j in range(i+1,n): add(i,j,c)
    return L

def K_formula(n,r,a,b,c):
    N=n+r
    return (sp.Rational(r+1,N)/a + sp.Rational(r*(N-1),N)/b
            + sp.Rational(n-2,1)/(a+(n-1)*c))

def K_sat(n,r,z):
    N=n+r
    a=z/(n-1)
    b=(1-z)/r
    c=(1-a)/(n-2)
    return K_formula(n,r,a,b,c)

def deriv(n,r,z):
    N=n+r
    A=(r+1)*(n-1)/N
    B=r*r*(N-1)/N
    return -A/z**2 + B/(1-z)**2 + (n-2)**2*(n-1)/((n-1)**2-z)**2

def solve(n,r):
    l=1e-13; u=1-1e-13
    for _ in range(90):
        m=(l+u)/2
        if deriv(n,r,m)>0: u=m
        else:l=m
    return (l+u)/2

for n in range(3,10):
    for r in range(1,6):
        N=n+r
        for k in (2,3,5):
            a=sp.Rational(1,k*(n-1)); b=sp.Rational(1,k*r); c=sp.Rational(1,k*(n-2))
            L=L_from_weights(n,r,a,b,c)
            J=sp.ones(N)/N
            K_exact=sp.trace((L+J).inv())-1
            K_pred=K_formula(n,r,a,b,c)
            check(sp.factor(K_exact-K_pred)==0)
        z=solve(n,r)
        check(0<z<1)
        check(abs(deriv(n,r,z))<1e-7*max(1,r*r))
        f=K_sat(n,r,z)
        for zz in (.005,.035,.2,.4,.6,.8,.965,.995):
            check(f<=K_sat(n,r,zz)+1e-8)
        # exact maximum-degree benchmark
        Delta=N-1
        kmd=K_formula(n,r,sp.Rational(1,Delta),sp.Rational(1,Delta),sp.Rational(1,Delta))
        check(sp.factor(kmd - sp.Rational(Delta)*(r+sp.Rational(1,N)+sp.Rational(n-2,n)))==0)
        check(float(kmd) >= f-1e-8)

for r in (1,2,3,5,10):
    zstar=math.sqrt(r+1)/(r+math.sqrt(r+1))
    for n in (100,1000,10000):
        z=solve(n,r)
        check(abs(z-zstar)<5/(n))
        a=z/(n-1); b=(1-z)/r
        check(abs(b - 1/(r+math.sqrt(r+1)))<5/n)
        kopt=K_sat(n,r,z)
        klimit=n-3+(r+math.sqrt(r+1))**2
        check(abs(kopt-klimit)<200*(r+1)**3/n)
        N=n+r; Delta=N-1
        kmd=Delta*(r+1/N+(n-2)/n)
        check(abs(kmd/kopt-(r+1))<30*(r+1)**3/n)

print('VERIFY_OK',assertions,'exact and numerical assertions')
