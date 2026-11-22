"""Exact polynomial checks for the FIR-filtered quadratic feedback map.

Optional dependencies: sympy (symbolic regression), numpy (root diagnostics).
These finite tests complement the algebraic proof and do not certify the full theorem.
"""
from fractions import Fraction
from math import comb, sqrt
import sympy as sp
import numpy as np

alpha=Fraction(7,5)
beta=Fraction(3,10)
z=sp.symbols('z')
for n in range(2,8):
    for r in (sp.Rational(1,20),sp.Rational(1,3),sp.Rational(9,10),sp.Integer(1),sp.Rational(6,5)):
        a=sp.expand((1+r)**n-1+sp.Rational(3,10))
        w=[(sp.binomial(n,j+1)*r**(j+1)+(sp.Rational(3,10) if j==1 else 0))/a for j in range(n)]
        assert all(v>0 for v in w)
        assert sp.simplify(sum(w)-1)==0
        P=sp.expand(z**n+a*sum(w[j]*z**(n-1-j) for j in range(n))-sp.Rational(3,10)*z**(n-2))
        assert sp.simplify(P-(z+r)**n)==0
        D=(a+sp.Rational(7,10))**2
        G2=(D-sp.Rational(49,100))/(4*sp.Rational(7,5))
        p=2*sp.Rational(7,5)/((sp.Rational(7,10))+sp.sqrt(D))
        assert sp.simplify(2*G2*p-a)==0
        if r<1:
            assert abs(complex(-float(r)))<1
        elif r>1:
            assert abs(complex(-float(r)))>1

# For small feedback a<beta+1 the baseline delayed selector w_1=1
# is stable, and small strictly-positive tap perturbations retain stability.
for n in range(2,8):
    for a in (0.01,0.2,0.75,1.15,1.299):
        w=np.full(n,1e-6)
        w[1]+=1-n*1e-6
        assert min(w)>0 and abs(sum(w)-1)<1e-12
        polynomial=[1]+list(a*w)
        polynomial[2]-=0.3
        eig=np.roots(polynomial)
        assert max(abs(eig))<1,(n,a,max(abs(eig)))

for n in range(2,8):
    Astar=2**n-0.7
    Gstar2=(4**n-0.49)/5.6
    assert abs(Astar*(Astar+1.4)/5.6-Gstar2)<1e-8
    for a in (0.3,0.9,1.7,2.4, min(Astar-0.01,5.7)):
        if a<=0.3 or a>=Astar:continue
        r=(1+a-0.3)**(1/n)-1
        w=np.array([(comb(n,j+1)*r**(j+1)+(0.3 if j==1 else 0))/a for j in range(n)])
        assert np.all(w>0) and abs(sum(w)-1)<1e-10
        coeff=[1]+list(a*w)
        coeff[2]-=0.3
        e=np.roots(coeff)
        assert abs(max(abs(e))-r)<0.02,(n,a,e,r)
# Direct companion-Jacobian characteristic identity (independent of root placement).
for n in range(2,6):
    a=sp.Rational(7,5)
    weights=[sp.Rational(j+1,n*(n+1)//2) for j in range(n)]
    J=sp.zeros(n,n)
    for j in range(n): J[0,j]=-a*weights[j]+(sp.Rational(3,10) if j==1 else 0)
    for j in range(1,n):J[j,j-1]=1
    P=sp.expand(z**n+a*sum(weights[j]*z**(n-1-j) for j in range(n))-sp.Rational(3,10)*z**(n-2))
    assert sp.factor(J.charpoly(z).as_expr()-P)==0
print('FIR_HENON_POLYNOMIAL_VERIFY_OK')
