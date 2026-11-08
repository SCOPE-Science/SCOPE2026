#!/usr/bin/env python3
"""Symbolic and numerical checks for the universal annular Hermite peak law.
Requires sympy and mpmath. Numerical tests are checks, not proofs of asymptotics.
"""
import math
import sympy as sp
import mpmath as mp

x = sp.symbols('x', real=True)
for k in range(0, 13):
    H = sp.hermite_prob(k, -x)
    D = -x * sp.diff(H, x, 2)/2 + sp.diff(H, x, 3)/3
    F0 = H**2/sp.factorial(k)
    F1 = (x**3/sp.Integer(6)-x/2)*F0 + 2*H*D/sp.factorial(k)
    critical_term = (x*x+2*k-2)*H*(2*sp.diff(H,x)-x*H)/(6*sp.factorial(k))
    assert sp.simplify(F1 + x*F0/6 + critical_term) == 0, k

# Charlier generating polynomial / Laguerre identity, checked for small indices.
u = sp.symbols('u', positive=True)
for k in range(0, 9):
    for n in range(0, 9):
        C = sp.expand(sum((-1)**j * sp.binomial(k,j) * (sp.factorial(n)/sp.factorial(n-j) if j<=n else 0) * u**(k-j) for j in range(k+1)))
        if n >= k:
            L = sp.assoc_laguerre(k, n-k, u)
            assert sp.simplify(C - (-1)**k * sp.factorial(k) * L) == 0
        else:
            L = sp.assoc_laguerre(n, k-n, u)
            assert sp.simplify(C - (-1)**n * sp.factorial(n) * u**(k-n) * L) == 0

def w2(n, u):
    b = (u-n)**2-n
    return math.exp(-u+n*math.log(u)-math.lgamma(n+1)) * b*b/(2*u*u)

def integrate_simpson(n, R, L=3., steps=64):
    a=R-L/2
    h=L/steps
    result=w2(n,a)+w2(n,a+L)
    for j in range(1,steps):
        result+=(4 if j%2 else 2)*w2(n,a+h*j)
    return result*h/3

L=3.0
coef=8*math.sqrt(5)*math.exp(-2.5)/(3*math.sqrt(2*math.pi))
for R in (100,500,1000,5000):
    cutoff=int(5*math.sqrt(R))+5
    lo=max(0,int(R-cutoff)); hi=int(R+cutoff)+1
    vals={n:integrate_simpson(n,R,L) for n in range(lo,hi)}
    n_left=max((n for n in vals if n<R),key=vals.get)
    n_right=max((n for n in vals if n>R),key=vals.get)
    left=vals[n_left];right=vals[n_right]
    assert left>right>0
    assert abs(n_left-(R-math.sqrt(5*R)))<5
    assert abs(n_right-(R+math.sqrt(5*R)))<5
    ratio=(left-right)*R/(L*coef)
    assert abs(ratio-1)<0.04, (R,ratio)
    print('R',R,'left',n_left,'right',n_right,'gap_R',format((left-right)*R,'.12f'),'pred_R',format(L*coef,'.12f'),'ratio',format(ratio,'.6f'))

# Independent high-precision integral using associated Laguerre polynomials
# at the selected peaks, compared against the Charlier/Poisson formula.
mp.mp.dps=45
for R,n in ((100,79),(100,124),(500,451),(500,551)):
    a=mp.mpf(R)-mp.mpf(L)/2; b=a+mp.mpf(L)
    def direct(t):
        poly=(t*t-2*n*t+n*(n-1))/2
        return 2*mp.exp(-t)*t**(n-2)*poly**2/mp.factorial(n)
    actual=mp.quad(direct,[a,b]); approx=integrate_simpson(n,R,L,steps=128)
    assert abs(float(actual)-approx)<1e-10, (R,n,float(actual),approx)
print('UNIVERSAL_HERMITE_ANNULUS_PASS symbolic_orders=13 laguerre_pairs=81 numerical_radii=4 high_precision=4')
