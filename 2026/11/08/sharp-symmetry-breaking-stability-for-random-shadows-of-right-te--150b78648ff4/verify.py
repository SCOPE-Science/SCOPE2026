"""Reproducible checks of the sharp trirectangular-tetrahedron shadow stability theorem.

Requires Python 3, numpy, scipy, sympy and mpmath. Numerical tests supplement
rather than replace the analytic proof in RESULT.md.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
import sympy as sp
import mpmath as mp

A=sp.Symbol('a')
P=192*A**9-192*A**8+144*A**7+128*A**6+135*A**5-109*A**4-42*A**3+38*A**2+3*A-9
st=sp.sturm(P,A)
def variation(t):
    signs=[sp.sign(q.subs(A,t)) for q in st]
    assert all(x != 0 for x in signs)
    return sum(x!=y for x,y in zip(signs,signs[1:]))
assert (variation(sp.Rational(1,3)),variation(sp.Rational(1)))==(5,4)
mp.mp.dps=55
c=mp.mpf(1)/3
def g(t): return mp.acos(mp.sqrt(t))
def gp(t): return -1/(2*mp.sqrt(t*(1-t)))
def F(a): return 2*(g(a)+2*g((1-a)/2)-3*g(c))
def Fp(a): return 2*(gp(a)-gp((1-a)/2))
def H(a): return (a-c)*Fp(a)-2*F(a)
astar=mp.findroot(H,(mp.mpf('.78'),mp.mpf('.8')))
C=F(astar)/(mp.mpf('1.5')*(astar-c)**2)
assert mp.mpf('0.7849')<astar<mp.mpf('0.7851')
assert mp.mpf('0.5861')<C<mp.mpf('0.5863')

# Exact rational check used in the proof that the centered extension is
# strictly smaller than the minimum of the boundary ratios.
from fractions import Fraction as Q
x=Q(577,1000)
L=x+x**3/Q(6)+3*x**5/Q(40)+5*x**7/Q(112)
assert L > Q(22,7)/6 + Q(708,1000)/8

# Independent random samples for the complete three-parameter simplex.
rng=np.random.default_rng(20261101)
t=rng.dirichlet([.42,.73,1.4],size=130000)
g0=math.acos(1/math.sqrt(3))
delta=2*np.arccos(np.sqrt(t)).sum(axis=1)-6*g0
spread=((t-1/3)**2).sum(axis=1)
assert np.min(delta/np.maximum(spread,1e-30)) > float(C)-2e-12

# Monte Carlo test of the *geometric* silhouette probability, independent
# of the spherical-angle formula: project each tetrahedron onto U^perp.
def monte_carlo(a,b,c,n=18000):
    vertices=np.array([[0,0,0],[a,0,0],[0,b,0],[0,0,c]],dtype=float)
    normals=rng.normal(size=(n,3))
    normals/=np.linalg.norm(normals,axis=1)[:,None]
    threes=0
    for u in normals:
        v=np.cross(u,[0.,0.,1.])
        if np.linalg.norm(v)<1e-9: v=np.cross(u,[0.,1.,0.])
        v/=np.linalg.norm(v)
        w=np.cross(u,v)
        xy=np.stack((vertices@v,vertices@w),axis=1)
        threes+=(len(ConvexHull(xy).vertices)==3)
    inv=np.array([1/a,1/b,1/c],dtype=float)
    q=inv/np.linalg.norm(inv)
    exact=(2*np.arccos(q).sum()-np.pi)/(2*np.pi)
    err=abs(threes/n-exact)
    assert err<0.022, (a,b,c,threes/n,exact,err)
    return err
errors=[monte_carlo(*legs) for legs in [(1,1,1),(.37,1,1),(.4,.9,1.7)]]
print('VERIFY_OK sturm=(5,4) sharp_constant=',mp.nstr(C,18),
      'optimizer=',mp.nstr(astar,18),'random_simplex_tests=',len(t),
      'geometric_projection_trials=',3*18000,
      'max_projection_error=',format(max(errors),'.6f'))
