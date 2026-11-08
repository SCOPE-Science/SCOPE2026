"""Independent exact and sampling checks for pairwise-distance ellipsoid inverse."""
from fractions import Fraction
from math import factorial, gamma, pi
from itertools import product
import random
import sympy as sp


def ball_vol(dim):
    return sp.pi**(sp.Rational(dim,2))/sp.gamma(sp.Rational(dim,2)+1)


def radial_constant(dim,k):
    d=sp.Integer(dim)
    out=d*ball_vol(dim-1)*2**(dim+2*k)/((d+2*k)*ball_vol(dim))*sp.beta(sp.Rational(dim+2*k+1,2),sp.Rational(dim+1,2))
    return sp.simplify(sp.expand_func(out))


def poly_from_moments(dim,moments):
    t=sp.Symbol('t')
    g=sum(sp.rf(sp.Rational(dim,2),k)/sp.factorial(k) * moments[k-1]/radial_constant(dim,k)*t**k for k in range(1,dim+1)) + 1
    return sp.series(g**(-2),t,0,dim+1).removeO().expand()


def moments_from_axes(lambdas):
    dim=len(lambdas);t=sp.Symbol('t')
    g=sp.prod((1-sp.sympify(z)*t)**(-sp.Rational(1,2)) for z in lambdas)
    series=sp.series(g,t,0,dim+1).removeO().expand()
    return [sp.simplify(series.coeff(t,k)*sp.factorial(k)/sp.rf(sp.Rational(dim,2),k)*radial_constant(dim,k)) for k in range(1,dim+1)]

for d in [2,3,4,5]:
    lambdas=[sp.Integer(j*j+2*j+1) for j in range(1,d+1)]
    mom=moments_from_axes(lambdas)
    t=sp.Symbol('t')
    recovered=poly_from_moments(d,mom)
    expected=sp.prod((1-z*t) for z in lambdas).expand()
    assert sp.simplify(recovered-expected)==0, (d,recovered,expected)
    assert sp.simplify(radial_constant(d,1)-sp.Rational(2*d,d+2))==0
    assert sp.simplify(radial_constant(d,2)-sp.Rational(4*d*(d+3),(d+2)*(d+4)))==0
    ratio=sp.simplify(mom[1]/mom[0]**2)
    assert sp.Rational((d+3)*(d+2),d*(d+4)) <= ratio < sp.Rational(3*(d+3),d+4)

# Monte Carlo checks in dimensions 2, 3, and 5 for two independent ball points.
random.seed(30217)
def sample_ball(d):
    g=[random.gauss(0,1) for _ in range(d)]
    n=sum(v*v for v in g)**.5
    r=random.random()**(1/d)
    return [r*v/n for v in g]

for d in [2,3,5]:
    lam=[float((j+1)**2) for j in range(d)]
    m=moments_from_axes([sp.Integer((j+1)**2) for j in range(d)])
    n=90000
    sums=[0.,0.]
    for _ in range(n):
        u=sample_ball(d);v=sample_ball(d)
        q=sum(lam[i]*(u[i]-v[i])**2 for i in range(d))
        sums[0]+=q;sums[1]+=q*q
    pred=[float(m[j]) for j in range(2)]
    obs=[s/n for s in sums]
    assert abs(obs[0]/pred[0]-1)<0.027,(d,obs,pred)
    assert abs(obs[1]/pred[1]-1)<0.055,(d,obs,pred)

print('ELLIPSOID_DISTANCE_INVERSE_OK exact_dimensions=2,3,4,5 calibration=8 simulation_dimensions=2,3,5 samples_each=90000')
