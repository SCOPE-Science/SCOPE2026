"""Symbolic and numerical arithmetic checks for a two-dimensional Banach-plane asymptotic identity.

Requires sympy, scipy and mpmath. These finite computations complement, but
cannot replace, the compactness and implicit-function proof in RESULT.md.
"""
import math
import sympy as sp
import mpmath as mp
from scipy.optimize import minimize_scalar

r = sp.symbols('r', positive=True)
L, Q = sp.log(r), 1+r*r
M, P = sp.log(1-r), sp.log(1+r)
a1=sp.log(Q)/4-r*r*L/(2*Q)
b1=sp.log(Q)/4-3*r*r*L/(2*Q)
a2=-sp.log(Q)/4+r*r*L/(2*Q)-r*r*L*L/(2*Q*Q)
b2=-sp.log(Q)/4+r*r*L/(2*Q)-9*r*r*L*L/(2*Q*Q)
n1=L+b1
AA,BB,NN=a2+a1*a1,b2+b1*b1,b2+n1*n1
lp,lm=M-sp.log(Q)/2,P-sp.log(Q)/2
plus=[(1-r,a1-r*n1,AA-r*NN,lp),(1+r,r*a1+b1,r*AA+BB,lm)]
minus=[(1+r,a1+r*n1,AA+r*NN,lm),(1-r,b1-r*a1,BB-r*AA,lp)]

def derivative_sums(vec):
    one=sp.S.Zero
    two=sp.S.Zero
    for h,h1,h2,l in vec:
        d=h1/h
        e=h2/h-d*d
        U=l+2*d
        V=2*d+2*e
        one += (h*h/Q)*U
        two += (h*h/Q)*(U*U+V)
    return one,two

s1p,s2p=derivative_sums(plus)
s1m,s2m=derivative_sums(minus)
g_calc=sp.sqrt(2)*(s1p-s1m)/4
g_formula=-sp.sqrt(2)*r*L/Q
assert sp.simplify(g_calc-g_formula)==0
k_calc=sp.sqrt(2)/2*((s2p-s2m)/4-(s1p*s1p-s1m*s1m)/16-(2+sp.log(2))*(s1p-s1m)/8)
k_formula=sp.sqrt(2)*r*L/(4*Q**2)*(Q*sp.log(2)-(1-r)**2*M-(1+r)**2*P-2*(1-2*r*r)*L)
assert sp.simplify(sp.expand_log(k_calc-k_formula,force=True)) == 0

mp.mp.dps=55
u=mp.findroot(lambda v:v-mp.coth(v),1.2)
r0=mp.exp(-u)
C=1/(mp.sqrt(2)*mp.sinh(u))
K=mp.mpf(str(sp.N(k_formula.subs(r,sp.Float(str(r0),60)),50)))

def F(p,z):
    a=(1+z**p)**(-1/p)
    b=(1+z**(p*(p-1)))**(-1/p)
    return ((a-z**(p-1)*b)**p+(z*a+b)**p)**(1/p)-((a+z**(p-1)*b)**p+(b-z*a)**p)**(1/p)

assert abs(mp.diff(lambda p:F(p,r0),mp.mpf(2),1)-C)<mp.mpf('1e-45')
assert abs(mp.diff(lambda p:F(p,r0),mp.mpf(2),2)/2-K)<mp.mpf('1e-45')
for z in [mp.mpf(i)/100 for i in [2,8,14,20,32,45,65,80,93]]:
    g=-mp.sqrt(2)*z*mp.log(z)/(1+z*z)
    kr=mp.mpf(str(sp.N(k_formula.subs(r,sp.Float(str(z),60)),50)))
    assert abs(mp.diff(lambda p:F(p,z),mp.mpf(2))-g)<mp.mpf('1e-42')
    assert abs(mp.diff(lambda p:F(p,z),mp.mpf(2),2)/2-kr)<mp.mpf('1e-42')

def realF(p,z):
    a=(1+z**p)**(-1/p)
    b=(1+z**(p*(p-1)))**(-1/p)
    return ((a-z**(p-1)*b)**p+(z*a+b)**p)**(1/p)-((a+z**(p-1)*b)**p+(b-z*a)**p)**(1/p)

for p in [1.999,2.001,1.99,2.01,1.95,2.05]:
    res=minimize_scalar(lambda z:-abs(realF(p,z)),bounds=(0.001,0.999),method='bounded',options={'xatol':1e-13})
    assert res.success
    approx=float(C)*abs(p-2)+float(K)*(p-2)*abs(p-2)
    tolerance=2*abs(p-2)**3
    assert abs(-res.fun-approx)<tolerance,(p,-res.fun,approx)
    assert abs(res.x-float(r0))<.30*abs(p-2)

# Boundary checks are zero for all p, hence cannot attain the interior maximum.
for p in [1.5,1.9,2.1,3,4]:
    assert abs(realF(p,0))<1e-14
    assert abs(realF(p,1))<1e-14
print('PASS: symbolic first and second p-derivatives; 9 high-precision comparison points; 6 optimized near-Hilbert tests; endpoint checks')
print('u=',mp.nstr(u,24),'r0=',mp.nstr(r0,24),'C=',mp.nstr(C,24),'K=',mp.nstr(K,24))
