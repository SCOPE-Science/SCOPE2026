#!/usr/bin/env python3
"""Finite reproducibility checks for the Möbius-ladder moment-price theorem.

Run: python3 verify.py
This script checks finite cases; it is not a proof of asymptotic statements.
Uses the Python standard library only.
"""
from fractions import Fraction as Q
from math import sin, pi, log, gamma, sqrt, isclose, cos, tau

CHECKS = 0

def check(b, message):
    global CHECKS
    assert b, message
    CHECKS += 1


def exact_inverse(M):
    n = len(M)
    a = [list(row) + [Q(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for j in range(n):
        r = next(i for i in range(j, n) if a[i][j] != 0)
        a[r], a[j] = a[j], a[r]
        v = a[j][j]
        a[j] = [x / v for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                v = a[i][j]
                a[i] = [a[i][k] - v * a[j][k] for k in range(2*n)]
    return [row[n:] for row in a]


def cycle_pseudoinverse(n):
    N = 2*n
    A = [[Q(1, N) + Q(2 if i == j else (-1 if (i-j)%N in (1,N-1) else 0))
          for j in range(N)] for i in range(N)]
    inverse = exact_inverse(A)
    return [[inverse[i][j] - Q(1,N) for j in range(N)] for i in range(N)]


def threshold(n,p):
    mu = [4*sin(pi*k/(2*n))**2 for k in range(1,2*n)]
    t = sum(x**(-p-1) for k,x in enumerate(mu, 1) if k%2)
    s = sum(x**(-p) for x in mu) if p else 2*n-1
    return 4*t/s


def spectrum_objective(n,p,price,r):
    # r is rung/rim conductance ratio; unit expenditure.
    a = 1/(n*(2+price*r))
    ev = [a*(4*sin(pi*k/(2*n))**2 + (2*r if k%2 else 0)) for k in range(1,2*n)]
    if p == 0:
        return -sum(log(x) for x in ev)
    return sum(x**(-p) for x in ev)


def positive_optimum_ratio(n,p,c):
    # A strict-convexity check in the actual rung conductance coordinate.
    def cost(b):
        a = (1-n*c*b)/(2*n)
        if a <= 0: return float('inf')
        return spectrum_objective(n,p,c,b/a)
    left,right = 0., 1/(n*c)
    for _ in range(125):
        u=left+(right-left)*.3819660112501051
        v=right-(right-left)*.3819660112501051
        if cost(u)<cost(v): right=v
        else:left=u
    return (left+right)/2


# Exact rational calculations, independent of Fourier-sum formulas.
for n in range(2,10):
    N=2*n
    G=cycle_pseudoinverse(n)
    S=sum(G[i][i] for i in range(N))
    check(S == Q(4*n*n-1,12), ('trace',n,S))
    R=[]
    T=Q(0)
    for i in range(n):
        j=i+n
        Ri=G[i][i]+G[j][j]-2*G[i][j]
        R.append(Ri)
        T += sum((G[v][i]-G[v][j])**2 for v in range(N))/2
    check(all(v==Q(n,2) for v in R), ('resistance',n,R))
    check(T == Q(n*n*(n*n+2),48), ('odd inverse second moment',n,T))
    c0 = Q(n*n,2*n-1)
    c1 = Q(n*n*(n*n+2),4*n*n-1)
    check(abs(threshold(n,0)-float(c0))<1e-10,('det threshold',n))
    check(abs(threshold(n,1)-float(c1))<1e-10,('A threshold',n))

# Independently apply every weighted Laplacian to explicit complex Fourier modes.
for n in range(2,16):
    N=2*n
    for a,b in ((0.17,0.13),(0.46,0.0),(0.07,0.57)):
        for k in range(N):
            vec=[complex(cos(tau*k*j/N),sin(tau*k*j/N)) for j in range(N)]
            eig = a*(2-2*cos(tau*k/N)) + b*(1-(-1)**k)
            for j in range(N):
                Lj = a*(2*vec[j]-vec[(j-1)%N]-vec[(j+1)%N]) + b*(vec[j]-vec[(j+n)%N])
                check(abs(Lj-eig*vec[j])<2e-11,('Fourier mode',n,a,b,k,j))

# Strict finite-price support criterion on both sides of the explicit boundary.
for n in range(2,21):
    for p in (0.0,0.25,0.5,1.0,2.0):
        c=threshold(n,p)
        for fac in (0.65,0.85):
            cc=c*fac
            b=positive_optimum_ratio(n,p,cc)
            check(b>1e-7, ('positive rung',n,p,cc,b))
            a=(1-n*cc*b)/(2*n)
            check(spectrum_objective(n,p,cc,b/a)<spectrum_objective(n,p,cc,0), ('improvement',n,p))
        for fac in (1.2,2):
            cc=c*fac
            b=positive_optimum_ratio(n,p,cc)
            check(b<1e-7, ('deleted rung',n,p,cc,b))

# Cross-regime constants for n to infinity.  Numerical checks are deliberately
# tolerance-based; the infinite theorems use endpoint-sum estimates in RESULT.md.
def asymptotic(n,p):
    from math import exp
    if p==0:
        return n/2
    if p<.5:
        # I_p = 4^-p Gamma(1/2-p)/(sqrt(pi) Gamma(1-p)).
        I = 4**(-p)*gamma(.5-p)/(sqrt(pi)*gamma(1-p))
        # Zeta values required by this test are approximated by a convergent
        # series with an integral tail and a midpoint correction.
        z=zeta(2*p+2)
        return 4*(1-2**(-2*p-2))*z/(pi**(2*p+2)*I)*n**(2*p+1)
    if p==.5:
        return 7*zeta(3)/(2*pi*pi)*n*n/log(n)
    return 4*(1-2**(-2*p-2))*zeta(2*p+2)/(pi*pi*zeta(2*p))*n*n


def zeta(s, K=120000):
    # Euler-Maclaurin two leading tail terms; suitable for s>=1.5 here.
    V=sum(k**(-s) for k in range(1,K))
    return V + K**(1-s)/(s-1) + .5*K**(-s) + s/12*K**(-s-1)

for n in (3000,12000):
    for p,tol in ((0.,.002),(.25,.035),(.5,.15),(.75,.035),(1.,.003),(2.,.003)):
        rel=threshold(n,p)/asymptotic(n,p)
        check(abs(rel-1)<tol,('asymptotic',n,p,rel))

for n in range(2,18):
    mu1=4*sin(pi/(2*n))**2
    last=threshold(n,40)
    check(abs(last*mu1/4-1)<2e-3,('high order',n,last))

print('PASS', CHECKS, 'finite reproducibility checks')
