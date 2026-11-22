"""Reproduce the exact cubic Greville spectral-edge calculations.
Run: python checker.py (requires sympy, numpy, scipy)."""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as sp
from scipy.optimize import brentq


def matrix(n, exact=False):
    assert n >= 4
    m = n + 1
    z = sp.zeros(m) if exact else np.zeros((m, m))
    F = sp.Rational if exact else lambda p, q: p / q
    def put(i,j,p,q): z[i,j] = F(p,q)
    for i in range(m):
        if i == 0 or i == m-1:
            row = [(0,61,108),(1,43,324),(2,1,162)]
            if i == m-1:
                row = [(m-1-j,a,b) for j,a,b in row]
            for j,a,b in row:put(i,j,a,b)
        elif i == 1 or i == m-2:
            row=[(0,1,4),(1,7,12),(2,1,6)]
            if i == m-2:row=[(m-1-j,a,b) for j,a,b in row]
            for j,a,b in row:put(i,j,a,b)
        else:
            for j,a,b in [(i-1,1,6),(i,2,3),(i+1,1,6)]:put(i,j,a,b)
    return z



def b_spline_entry(knots, i, degree, x):
    """Exact Cox-de Boor recursion at a rational interior Greville site."""
    if degree == 0:
        return Fraction(1) if knots[i] <= x < knots[i+1] else Fraction(0)
    a = b = Fraction(0)
    den1 = knots[i+degree] - knots[i]
    den2 = knots[i+degree+1] - knots[i+1]
    if den1:
        a = (x-knots[i])*b_spline_entry(knots,i,degree-1,x)/den1
    if den2:
        b = (knots[i+degree+1]-x)*b_spline_entry(knots,i+1,degree-1,x)/den2
    return a+b


for test_n in range(4, 13):
    knots=[Fraction(0)]*4+[Fraction(i) for i in range(1,test_n)]+[Fraction(test_n)]*4
    nodes=[sum(knots[i+1:i+4],Fraction(0))/3 for i in range(test_n+3)]
    exact_matrix=matrix(test_n,exact=True)
    for i in range(1,test_n+2):
        for j in range(1,test_n+2):
            direct=b_spline_entry(knots,j,3,nodes[i])
            assert sp.Rational(direct.numerator,direct.denominator)==exact_matrix[i-1,j-1], (test_n,i,j)
print('Exact Cox-de Boor collocation comparisons n=4..12: PASSED.')

s=sp.symbols('s',positive=True)
p=9-10*s+s**2-4*s**3
q=4-s+10*s**2-9*s**3
A=31*s**4+172*s**3-294*s**2+172*s+31
assert sp.simplify(A-(31*(1-s)**4+296*s*(1-s)**2+112*s**2))==0
assert sp.factor(sp.diff(p/q,s)+A/q**2)==0
R=-p/q
K=sp.factor(s*sp.diff(R,s)/R)
E=93*s**8+1032*s**7-3524*s**6+6520*s**5-5682*s**4+6520*s**3-3524*s**2+1032*s+93
u=s+1/s-2
assert sp.simplify(E-s**4*(93*u**4+1776*u**3+4528*u**2+3200*u+2560))==0
assert sp.simplify(sp.diff(K,s)-12*(s-1)*(s+1)*E/(p*p*q*q))==0
assert sp.limit(K,s,1)==7
assert sp.simplify(sp.diff(p,s)-(-12*s*s+2*s-10))==0

f_p=sp.lambdify(s,p,'numpy');f_q=sp.lambdify(s,q,'numpy')
edge=brentq(f_p,0.7,0.85,xtol=1e-15)
edge_lam=(4-edge-1/edge)/6
pprime=float(sp.diff(p,s).subs(s,edge)); q_edge=f_q(edge)
coef=(1/edge**2-1)/3*q_edge/(-pprime)
print('edge_s',format(edge,'.15f'),'edge_lambda',format(edge_lam,'.15f'))
print('splitting_coefficient',format(coef,'.15f'))

for n in range(4,42):
    T=matrix(n)
    eig=np.linalg.eigvals(T)
    assert np.max(np.abs(eig.imag)) < 2e-9, (n,eig)
    eig=np.sort(eig.real)
    assert np.min(eig)>0 and np.max(eig)<1 and np.min(np.diff(eig))>1e-12,(n,eig)
    count=int(np.sum(eig<1/3-1e-10))
    assert count==(1 if n<=8 else 2),(n,count,eig[:3])
    if n==8:assert abs(eig[1]-1/3)<1e-12
    smin=2-sqrt(3)
    root1=brentq(lambda t:f_p(t)-t**(n-1)*f_q(t),smin,edge,xtol=1e-14)
    lam1=(4-root1-1/root1)/6
    assert abs(eig[0]-lam1)<1e-10, (n,eig[0],lam1)
    if n>=9:
        root2=brentq(lambda t:f_p(t)+t**(n-1)*f_q(t),edge,0.999999,xtol=1e-14)
        lam2=(4-root2-1/root2)/6
        assert abs(eig[1]-lam2)<1e-10,(n,eig[1],lam2)
    if n in (4,7,8,9,12,20,30,40):
        print('n',n,'smallest',*([format(x,'.12f') for x in eig[:3]]))

for n in range(4,13):
    T=matrix(n,exact=True)
    determinant=sp.factor((T-sp.eye(n+1)/3).det())
    assert (determinant==0)==(n==8), (n,determinant)
print('Exact band-edge determinants n=4..12: only n=8 vanishes.')
for n in (20,30,40):
    eig=np.sort(np.linalg.eigvals(matrix(n)).real)
    print('n',n,'splitting ratio',float((eig[1]-eig[0])/(coef*edge**(n-1))))
print('All symbolic and numerical checks PASSED.')
