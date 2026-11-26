#!/usr/bin/env python3
"""Independent finite checks for a cube-plus-simplex boundary theorem.
Runs from the standard Python scientific stack; only numerical tests are claimed.
"""
import itertools, math
import numpy as np
from scipy.spatial import ConvexHull

def expected(n,t):
    v=sum(math.comb(n,k)*t**k/math.factorial(k) for k in range(n+1))
    s=n*sum(math.comb(n-1,k)*t**k/math.factorial(k) for k in range(n))
    s+=sum(math.comb(n,k)*math.sqrt(k)*t**(k-1)/math.factorial(k-1) for k in range(1,n+1))
    return v,s

def vertices(n,t):
    cube=np.array(list(itertools.product((0.,1.),repeat=n)))
    return np.vstack([cube]+[cube+t*np.eye(n)[i] for i in range(n)])

num=0
for n in (2,3,4,5):
    for t in (.4,1.,2.):
        hull=ConvexHull(vertices(n,t))
        v,s=expected(n,t)
        assert abs(hull.volume-v)<3e-7*max(v,1),(n,t,hull.volume,v)
        assert abs(hull.area-s)<3e-7*max(s,1),(n,t,hull.area,s)
        num+=1

# Test all named facet normal offsets and their rank using vertices.
from itertools import combinations
for n in (2,3,4,5):
    pts=vertices(n,1.)
    for k in range(1,n+1):
        for S in combinations(range(n),k):
            a=np.zeros(n);a[list(S)]=1
            vals=pts@a
            assert np.max(vals)<=k+1+1e-10
            on=pts[np.abs(vals-(k+1))<1e-10]
            assert np.linalg.matrix_rank(on-on[0],tol=1e-9)==n-1
    for i in range(n):
        on=pts[np.abs(pts[:,i])<1e-10]
        assert np.linalg.matrix_rank(on-on[0],tol=1e-9)==n-1
print('CUBE_SIMPLEX_BOUNDARY_CHECK_PASS',num,'hull volume+area pairs, all subset facet ranks through dimension 5')

# Check the exact critical polynomial, then evaluate its coefficients and root.
import sympy as sp
z=sp.symbols('z')
v3=1+3*z+sp.Rational(3,2)*z**2+z**3/6
s3=6+(6+3*sp.sqrt(2))*z+(sp.Rational(3,2)+sp.sqrt(3)/2)*z**2
f3=sp.expand(3*sp.diff(s3,z)*v3-2*s3*sp.diff(v3,z))
r2, r3 = sp.sqrt(2), sp.sqrt(3)
claimed = (9*(r2-2) + (-9+3*r3+9*r2)*z
           + (3+6*r3-sp.Rational(9,2)*r2)*z**2
           + sp.Rational(3,2)*(1+r3-r2)*z**3)
assert sp.expand(f3-claimed) == 0
coeff=[sp.N(sp.expand(f3).coeff(z,j),30) for j in range(4)]
assert float(coeff[0])<0 and all(float(c)>0 for c in coeff[1:])
from scipy.optimize import brentq
root=brentq(sp.lambdify(z,f3,'numpy'),0,2,xtol=1e-14)
quot=float(sp.lambdify(z,s3/v3**sp.Rational(2,3),'numpy')(root))
assert abs(root-0.428630637733420)<3e-12
assert abs(quot-5.762637024562115)<3e-12
print('CUBE_SIMPLEX_SHARP_ISOPERIMETRY_PASS',root,quot)
