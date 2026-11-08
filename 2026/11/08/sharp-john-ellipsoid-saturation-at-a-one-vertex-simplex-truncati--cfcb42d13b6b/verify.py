"""Exact supporting-hyperplane and determinant checks for a one-vertex truncated simplex.

Requires only Python 3 standard library. These finite tests corroborate, not establish,
the mathematical proof of the all-dimensional optimization theorem.
"""
from fractions import Fraction as Q
from math import factorial, gamma, pi, sqrt, log
from itertools import product

checks = 0

def verify(n, h):
    global checks
    assert isinstance(h,Q) and n>=2 and 0 < h <= n
    alpha=Q(n,n+1)
    cutoff=2*alpha
    if h <= cutoff:
        c=s=h/2
        r2=(Q(n)-h)/Q(n-1)
    else:
        c=s=alpha
        r2=alpha
    assert r2>0 and s>0
    checks += 1
    # First coordinate's two supporting hyperplanes.
    assert c-s == 0 and c+s <= h
    checks += 2
    # The n interchangeable barycentric coordinates have the same exact
    # coordinate-support variance; each lower facet is tangent.
    b=(Q(n)-c)/n
    variance=s*s/(n*n)+r2*Q(n-1,n)
    assert variance == b*b, (n,h,variance,b*b)
    checks += 1
    if h <= cutoff:
        assert c+s == h
    elif h < n:
        assert c+s < h
    checks += 1
    # Exact relation between Euclidean coordinate covariance determinant
    # and these symmetry-adapted axes (Jacobian factor 1/sqrt(n)).
    # det(C_x)=s^2*r2^(n-1)/n (purely rational).
    det=s*s*r2**(n-1)/n
    assert det>0
    checks += 1
    return c,s,r2

# Rational exact support checks at 550+ sizes/parameters.
for n in range(2,102):
    a=Q(n,n+1);cut=2*a
    hs=[Q(1,100),Q(1,2),Q(1),cut-Q(1,100),cut,cut+Q(1,100),Q(n)]
    for h in hs:
        if 0<h<=n: verify(n,h)

# Independent numerical determinant profiling, deliberately *not* substituting
# the optimal-shape formula into candidate test points.
# Each test fixes a possible center, then sweeps many feasible first-axis radii.
# A nontrivial candidate with larger determinant would contradict the formula.
for n in [2,3,4,5,8,12]:
    cut=2*n/(n+1)
    for h in [0.15,0.9,1.,cut-0.01,cut,cut+0.01,(cut+n)/2,n]:
        c0,s0,r20=verify(n,Q(str(h)))
        target=float(s0*s0*r20**(n-1))
        for i in range(1,100):
            c=h*i/100
            for j in range(1,25):
                s=min(c,h-c)*j/25
                if s<=0:continue
                rr=((n-c)**2-s*s)/(n*(n-1))
                assert rr>0
                trial=s*s*rr**(n-1)
                assert trial <= target*(1+3e-12),(n,h,c,s,trial,target)
                checks+=1

# The saturation volume is C^1 but not C^2.  At the cutoff the left
# second logarithmic derivative is strictly negative, the right is zero.
for n in range(2,102):
    cut=Q(2*n,n+1)
    left_second_log=-1/(cut*cut)-Q(n-1,2)/(Q(n)-cut)**2
    assert left_second_log < 0
    assert 1/cut-Q(n-1,2)/(Q(n)-cut)==0
    checks+=2

print('VERIFY_OK',checks,'exact/finite assertions')
