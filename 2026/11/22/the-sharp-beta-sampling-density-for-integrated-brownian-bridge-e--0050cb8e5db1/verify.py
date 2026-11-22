"""Reproducibility checks for optimal sampling of quadratic bridge energy.

Run: python verify.py
Requires: numpy, scipy, sympy.
The all-budget theorem is proved analytically in RESULT.md; finite checks are supplementary.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import numpy as np
import sympy as S
from numpy.polynomial.legendre import leggauss
from scipy.special import beta, betaincinv


def exact_risk(nodes):
    points = [F(0)] + list(nodes) + [F(1)]
    result = F(0)
    for a, b in zip(points[:-1], points[1:]):
        length = b - a
        result += a * (1-b) * length**3/F(3) + length**4/F(9) - 4*length**5/F(45)
    return result


def direct_gaussian_risk(nodes, quadrature_size=190):
    nodes = np.array(nodes, dtype=float)
    z, weights = leggauss(quadrature_size)
    x, weights = (z+1)/2, weights/2
    K = np.minimum(x[:,None], x[None,:]) - x[:,None]*x[None,:]
    if len(nodes):
        CX = np.minimum(x[:,None], nodes[None,:])-x[:,None]*nodes[None,:]
        KX = np.minimum(nodes[:,None], nodes[None,:])-nodes[:,None]*nodes[None,:]
        C = K-CX@np.linalg.solve(KX,CX.T)
    else:
        C = K
    return float(2*np.sum((C*C+2*C*(K-C))*np.outer(weights,weights)))


# Exact Isserlis covariance integrals on an arbitrary bridge gap.
u,v,a,L = S.symbols('u v a L', positive=True)
C = u*(L-v)/L       # u <= v
M = a*(1-a)-a*(u+v)+(1/L-1)*u*v
c2 = S.factor(2*S.integrate(S.integrate(C*C,(u,0,v)),(v,0,L)))
cm = S.factor(2*S.integrate(S.integrate(C*M,(u,0,v)),(v,0,L)))
gap = a*(1-a-L)*L**3/3 + L**4/9-4*L**5/45
assert S.simplify(c2-L**4/90)==0
assert S.simplify(2*c2+4*cm-gap)==0
print('Symbolic bridge covariance identities: PASS')

# Explicit formula for the uniform grid, all symbolic positive integers m.
m,j=S.symbols('m j',integer=True,positive=True)
q=1/m
uniform_gap=(j/m)*(1-(j+1)/m)*q**3/3+q**4/9-4*q**5/45
uniform=S.factor(S.summation(uniform_gap,(j,0,m-1)))
assert S.simplify(uniform-(5*m*m-5*m+2)/(90*m**4))==0
assert S.limit(m**2*uniform,m,S.oo)==S.Rational(1,18)
print('Uniform-grid exact symbolic formula: PASS')

# Gaussian posterior direct integration independently of the gap formula.
for nodes in [[], [F(1,2)], [F(1,3),F(2,3)], [F(3,10),F(4,5)],
              [F(1,7),F(3,7),F(5,7)]]:
    exact, direct = exact_risk(nodes), direct_gaussian_risk(nodes)
    assert abs(float(exact)-direct)<8e-6, (nodes,exact,direct)
print('Five direct Gaussian covariance quadrature comparisons: PASS')

nchecks=0
for den in range(2,10):
    for k in range(4):
        for nums in combinations_with_replacement(range(den+1), k):
            nodes=[F(v,den) for v in nums]
            assert exact_risk(nodes)>=0
            assert exact_risk(nodes)>=F(0)
            nchecks+=1
print('Exact rational nonnegative gap risks:',nchecks)

I=beta(4/3,4/3)
prev=0.
for m in [10,30,100,300]:
    points=[F(float(betaincinv(4/3,4/3,i/m))).limit_denominator(100000000)
            for i in range(1,m)]
    scaled=m*m*float(exact_risk(points))
    assert scaled>prev and scaled<I**3/3
    print('Beta-quantile grid: intervals',m,'scaled risk',format(scaled,'.12f'))
    prev=scaled
print('Sharp asymptotic constant',format(I**3/3,'.15f'))
print('Uniform asymptotic constant',format(1/18,'.15f'))
print('Relative risk improvement',format(1-6*I**3,'.12%'))
print('All supplementary tests: PASS')
