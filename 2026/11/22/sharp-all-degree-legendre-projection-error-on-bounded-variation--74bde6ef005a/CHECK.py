"""Reproducible checks for the sharp BV-to-L2 Legendre tail theorem.

Requires Python 3.10+, sympy and scipy. Numerical tests are corroboration;
the proof for all degrees is algebraic/analytic in RESULT.md.
"""
from sympy import symbols, legendre, integrate, factor, diff, Rational, simplify, binomial
from scipy.special import roots_legendre, eval_legendre
import math
x=symbols('x',real=True)
assertions=0
for n in range(16):
    En = factor(integrate(legendre(n,x)*legendre(n+1,x), (x,x,1)))
    closed=Rational(1,2)*(legendre(n,x)**2+legendre(n+1,x)**2-2*x*legendre(n,x)*legendre(n+1,x))
    assert simplify(En-closed)==0
    assertions+=1
    assert simplify(diff(En,x)+legendre(n,x)*legendre(n+1,x))==0
    assertions+=1
    assert En.subs(x,1)==0 and En.subs(x,-1)==0
    assertions+=1
    if n%2==0:
        m=n//2
        exact=Rational(1,2)*(binomial(2*m,m)/4**m)**2
        assert simplify(En.subs(x,0)-exact)==0
        assertions+=1
# Sonin/Sturm energy decreases strictly between positive Legendre zeros.
for n in range(10):
    g=legendre(n+1,x)
    lam=(n+1)*(n+2)
    phi=(1-x**2)**2*diff(g,x)**2+lam*(1-x**2)*g**2
    assert simplify(diff(phi,x)+2*lam*x*g**2)==0
    assertions+=1
# Parseval residual for exact rational discontinuity locations.
for n in range(8):
    for t in [Rational(-2,3), Rational(-1,7), Rational(0), Rational(2,3)]:
        integral=1-t
        projection=sum(Rational(2*k+1,2)*integrate(legendre(k,x),(x,t,1))**2 for k in range(n+1))
        expected=(legendre(n,t)**2+legendre(n+1,t)**2-2*t*legendre(n,t)*legendre(n+1,t))/2
        assert simplify(integral-projection-expected)==0
        assertions+=1
for n in range(1,80):
    z=roots_legendre(n+1)[0]
    ind=min(range(n+1),key=lambda j:abs(z[j]))
    xi=abs(z[ind]); C=0.5*eval_legendre(n,xi)**2
    candidates=[(0.5*eval_legendre(n,abs(v))**2,abs(v)) for v in z]
    assert abs(C-max(t[0] for t in candidates))<1e-11
    assertions+=1
    positive=sorted((u for u in candidates if u[1]>1e-10),key=lambda pair:pair[1])
    assert all(positive[j][0]>positive[j+1][0] - 1e-12 for j in range(len(positive)-1))
    assertions+=1
    if n%2==0:
        assert xi<1e-10
    else:
        assert xi>0 and abs(eval_legendre(n,xi))>0
    assertions+=1
    for zz in [-.997,-.8,-.3,0,.19,.79,.995]:
        K=sum((2*j+1)/2*eval_legendre(j,zz)**2 for j in range(n+1))
        E=(1-zz**2)*K/(n+1)**2
        closed=0.5*(eval_legendre(n,zz)**2+eval_legendre(n+1,zz)**2-2*zz*eval_legendre(n,zz)*eval_legendre(n+1,zz))
        assert abs(E-closed)<1e-9
        assertions+=1
for m in [10,100,300,1000]:
    c2=0.5*math.exp(2*(math.lgamma(2*m+1)-2*math.lgamma(m+1)-2*m*math.log(2)))
    assert abs((2*m)*c2-1/math.pi)<0.1/m
    assertions+=1
print('PASS: ', assertions,' independently evaluated assertions')
