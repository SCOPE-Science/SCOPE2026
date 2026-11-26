"""Independent checks for Fourier-zero rigidity of symmetric simplex projections.
Run: python check_tetrahedral_zeros.py. Requires sympy, scipy, numpy.
The finite checks corroborate an analytic theorem; they do not prove all parameter cases.
"""
from fractions import Fraction
from math import sin, pi
import numpy as np
import sympy as sp
from scipy.integrate import tplquad

x,z,a=sp.symbols('x z a', real=True)
# Independently compute the divided-difference character sum for knots (-1,-a,a,1).
knots=[-1,-a,a,1]
E=sp.symbols('E0:4')
d=sp.factor(sum(E[i]/sp.prod(knots[i]-knots[j] for j in range(4) if j!=i) for i in range(4)))
assert sp.simplify(d - (E[3]-E[0])/(2*(1-a*a)) -(E[1]-E[2])/(2*a*(1-a*a)))==0
print('Divided-difference knot coefficients: PASS')

# Two independent power series: moment of a Dirichlet(1,1,1,1) convex sum,
# versus closed-form 6(sin(az)-a sin z)/(a(1-a^2)z^3).
for k in range(13):
    h=sum(a**(2*j) for j in range(k+1))
    coeff=(-1)**k * sp.Rational(6,sp.factorial(2*k+3))*h
    from_sines=(-1)**k*sp.Rational(6,sp.factorial(2*k+3))*(1-a**(2*k+2))/(1-a*a)
    assert sp.cancel(coeff-from_sines)==0
print('Dirichlet moments vs. closed-form Fourier transform: 13 exact coefficients PASS')

# The exceptional class a=1-2/m has a Chebyshev numerator with precisely m-1
# simple roots in [-1,1]. Check small m independently using Sturm interval isolation.
for m in range(3,15):
    q=sp.Poly(m*sp.chebyshevu(m-3,x)-(m-2)*sp.chebyshevu(m-1,x),x)
    assert q.degree()==m-1
    assert q.eval(1)==q.eval(-1)==0
    assert sp.gcd(q,q.diff()).degree()==0
    # Exact sign variations at -1 and +1 give interior simple zeros.
    c=int(sp.polys.polytools.count_roots(q,-1,1))
    assert c==m-1,(m,c)
print('Exceptional Chebyshev polynomial: exact Sturm root counts for m=3..14 PASS')

# Laguerre defect at z=2*pi/(1-a) is negative for a outside the integer family.
for u in [sp.Rational(1,4),sp.Rational(2,5),sp.Rational(4,7),sp.Rational(5,9)]:
    X=float(2*sp.pi/(1-u)); v=float(u)
    f=np.sin(v*X)-v*np.sin(X)
    fp=v*(np.cos(v*X)-np.cos(X))
    fpp=v*(-v*np.sin(v*X)+np.sin(X))
    defect=fp*fp-f*fpp
    predicted=-v*(1-v)**2*np.sin(X)**2
    assert abs(defect-predicted)<1e-12 and predicted< -1e-6
print('Strict Laguerre obstruction at four nonexceptional ratios: PASS')

# Independently integrate the uniform simplex density in barycentric coordinates.
for a0,t in [(0.2,0.7),(0.4,2.3),(0.6,3.1),(0.75,4.6),(0.85,1.8)]:
    integral=6*tplquad(
        lambda w3,w2,w1:np.cos(t*(-w1-a0*w2+a0*w3+1-w1-w2-w3)),
        0,1,lambda w1:0,lambda w1:1-w1,
        lambda w1,w2:0,lambda w1,w2:1-w1-w2,
        epsabs=1e-9,epsrel=1e-9)[0]
    closed=6*(np.sin(a0*t)-a0*np.sin(t))/(a0*(1-a0*a0)*t**3)
    assert abs(integral-closed)<3e-10,(a0,t,integral,closed)
print('5 independent tetrahedron integral evaluations: PASS')
print('ALL CHECKS PASSED')
