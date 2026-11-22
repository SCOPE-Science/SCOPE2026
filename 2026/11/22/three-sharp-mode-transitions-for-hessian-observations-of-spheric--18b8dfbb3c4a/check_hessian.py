"""Reproducible checks for the quadratic spherical covariant-Hessian cap spectrum.

Run: python check_hessian.py (requires sympy, numpy).
Analytic proof is in RESULT.md; finite quadrature is corroborative only.
"""
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

n, u = sp.symbols('n u', positive=True)
FT = 1-2*(1-u)/n+(n+3)*2*(1-u)**2/(n*(n+2))
FM = 1-(u+(1-u)/n)+(n+3)*2*u*(1-u)/n
FZ = 1-2*(1+(n*n-1)*u)/(n*(n+1))+(n+3)*(1-(n+1)*u)**2/(n*(n+1))
polynomials = {'T':sp.factor(FT),'M':sp.factor(FM),'Z':sp.factor(FZ)}
assert all(sp.simplify(expr.subs({n:3,u:sp.Rational(2,5)})) > 0 for expr in polynomials.values())

# The change-of-variables density is beta(1/2,n/2). Integration of the
# polynomial gap equals minus the boundary primitive.
checks=0
for first,second,a,b in [
 ('Z','M',4/n,-2*(n+3)/n),
 ('M','T',-2*(n+4)/(n*(n+2)),4*(n+3)/(n*(n+2))),
 ('Z','T',2/(n+2),-2*(n+3)/(n+2))]:
 gap=sp.factor(polynomials[first]-polynomials[second])
 # derivative of u^(1/2) (1-u)^(n/2) (a+bu) divided by density factor
 differentiated=sp.expand((sp.Rational(1,2)-(n+1)*u/2)*(a+b*u)+b*u*(1-u))
 assert sp.simplify(gap-differentiated)==0
 checks+=1
# Globally averaged local tensor norm equals one in each sector.
mean_u=1/(n+1)
mean_u2=3/((n+1)*(n+3))
for expr in polynomials.values():
 p=sp.Poly(expr,u)
 assert sp.simplify(p.nth(0)+p.nth(1)*mean_u+p.nth(2)*mean_u2-1)==0
 checks+=1
# Pointwise addition theorem: trace of observation density is constant.
rank_T=(n-1)*(n+2)/2
weighted=sp.factor(polynomials['Z']+n*polynomials['M']+rank_T*polynomials['T'])
assert sp.simplify(weighted-(1+n+rank_T))==0
checks+=1

# Independent full 5x5 Gram integration for d=3, not just the sector formulas.
B=np.zeros((5,3,3),float)
B[0]=np.diag([1,1,-2])/np.sqrt(6.)
B[1,0,2]=B[1,2,0]=1/np.sqrt(2.)
B[2,1,2]=B[2,2,1]=1/np.sqrt(2.)
B[3]=np.diag([1,-1,0])/np.sqrt(2.)
B[4,0,1]=B[4,1,0]=1/np.sqrt(2.)
assert np.allclose(np.einsum('iab,jab->ij',B,B),np.eye(5))
T=np.eye(5)
phi=2*np.pi*np.arange(72)/72
zz,ww=leggauss(85)
for t in [0.02,0.18,0.2,0.25,0.4,0.5,0.6,0.8,0.94]:
    h=np.sqrt(t); z=(1+h)/2+(1-h)*zz/2; w=(1-h)*ww/2
    G=np.zeros((5,5))
    for zi,wi in zip(z,w):
        x=np.array([np.sqrt(1-zi*zi)*np.cos(phi),np.sqrt(1-zi*zi)*np.sin(phi),np.full_like(phi,zi)]).T
        Ax=np.einsum('iab,pa->pib',B,x)
        f=np.einsum('pa,pia->pi',x,Ax)
        q=np.einsum('pia,pja->pij',Ax,Ax)
        local=T-2*q+5*np.einsum('pi,pj->pij',f,f)
        G += wi*local.mean(axis=0)
    assert np.max(abs(G-np.diag(np.diag(G))))<2e-13
    # d=3 beta half-density becomes uniform in |z|.
    calc=[]
    for name in ['Z','M','T']:
        pp=sp.Poly(polynomials[name].subs(n,2),u)
        calc.append(sum(float(pp.nth(k))*(1-h**(2*k+1))/(2*k+1) for k in range(3)))
    assert np.max(abs(np.diag(G)-[calc[0],calc[1],calc[1],calc[2],calc[2]]))<2e-12
    C=np.sqrt(t)*(1-t)/(2) # beta(1/2,1)=2 for d=3
    assert abs((calc[0]-calc[1])-C*2/2*(5*t-2))<2e-12
    checks+=12

print('HESSIAN_CAP_CHECKS_PASS',checks)
print('Symbolic sector formulae:')
for name,poly in polynomials.items():print(name,poly)
