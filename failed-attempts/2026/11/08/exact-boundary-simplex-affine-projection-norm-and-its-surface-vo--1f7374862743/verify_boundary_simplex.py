"""Exact rational checks for affine least-squares projection on a regular simplex boundary.

No external source files are required. Run with Python 3 and sympy.
"""
from fractions import Fraction as Q
from math import comb, factorial
import sympy as sp

def moments(m):
    # For uniform mass on each of m facets, Dirichlet(1,...,1) on m-1 coordinates.
    E1=Q(1,m)
    E2=Q(2,m*m)
    E12=Q(m-2,m*m*(m-1))
    return E1,E2,E12

def direct_abs_integral(m):
    # Kernel for a vertex: K = m(m-1)lambda_1 - (m-2).
    # On the facet opposite vertex 1, lambda_1=0 with mass 1/m.
    # On any other facet lambda_1 ~ Beta(1,m-2).
    t=sp.Symbol('t',real=True)
    a=sp.Integer(m*(m-1)); b=sp.Integer(m-2)
    root=b/a
    density=(m-2)*(1-t)**(m-3)
    # negative part computed explicitly as polynomial antiderivative
    neg=sp.Rational(m-2,m)+sp.Rational(m-1,m)*sp.integrate((b-a*t)*density,(t,0,root))
    return sp.factor(1+2*neg)

def formula(m):
    m=sp.Integer(m); a=m*m-2*m+2
    return sp.factor(2*a/m*(a/(m*(m-1)))**(m-2)-1)

def volume(m):
    m=sp.Integer(m)
    return sp.factor(2*m*(m/(m+1))**(m-1)-1)

for m in range(3,19):
    E1,E2,E12=moments(m)
    assert E2-E1**2==Q(1,m*m)
    assert E12-E1**2==-Q(1,m*m*(m-1))
    assert E2-E12==Q(1,m*(m-1))
    assert sp.simplify(direct_abs_integral(m)-formula(m))==0
    assert formula(m)>1
    assert formula(m)<volume(m)
print('INDEPENDENT_EXACT_FACET_BETA_INTEGRALS_AND_COVARIANCE_OK',16)

u=sp.Symbol('u',positive=True)
# expand with u=1/m, positive u downarrow0. check constant terms without assuming finite numerics.
q=1- u*(1-2*u)/(1-u)
logq=sp.series(sp.log(q),u,0,4)
logr=sp.series(sp.log(1/(1+u)),u,0,4)
assert sp.simplify(sp.limit((1/u-2)*sp.log(q)+1,u,0))==0
assert sp.simplify(sp.limit((1/u-1)*sp.log(1/(1+u))+1,u,0))==0
# constant corrections after leading order 2m/e.
Bplus = 2*(1/u-2+2*u)*sp.exp((1/u-2)*sp.log(q))
Vplus = 2/u*sp.exp((1/u-1)*sp.log(1/(1+u)))
assert sp.simplify(sp.limit(Bplus-2/sp.E/u,u,0))==1/sp.E
assert sp.simplify(sp.limit(Vplus-2/sp.E/u,u,0))==3/sp.E
assert sp.simplify(sp.limit(Vplus-Bplus,u,0))==2/sp.E
print('EXACT_BOUNDARY_VOLUME_ASYMPTOTIC_GAP_OK')
print('ALL_BOUNDARY_SIMPLEX_LEAST_SQUARES_CHECKS_OK')
m=sp.Symbol('m',integer=True,positive=True)
a=m*m-2*m+2
delta=sp.Rational(2,1)/(m*m*(m-1))
Rpre=sp.factor(a*(m+1)/m**3)
assert sp.simplify(Rpre-(1-1/m+2/m**3))==0
assert sp.simplify(sp.together((1-(m-2)*delta)-Rpre)*m**3*(m-1)-(m*(m-1)*(m-2)+2))==0
print('UNIVERSAL_STRICT_BOUNDARY_VS_VOLUME_CERTIFICATE_OK')
