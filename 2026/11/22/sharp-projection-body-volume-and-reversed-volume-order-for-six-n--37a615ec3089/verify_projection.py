"""Numerical and exact endpoint checks for a six-normal projection-zonotope formula.
Requires Python 3 standard library; optional SciPy and NumPy verify convex-hull volume.
"""
import itertools
import math
from fractions import Fraction

PI = math.pi

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def dots(a,b):
    return sum(x*y for x,y in zip(a,b))

def points(phi):
    return [(math.sqrt(2/3)*math.cos(2*PI*j/3 + off),
             math.sqrt(2/3)*math.sin(2*PI*j/3 + off),
             sign/math.sqrt(3))
            for off, sign in ((0,1),(phi,-1)) for j in range(3)]

def determinant_sum(points):
    return sum(abs(det(*t)) for t in itertools.combinations(points,3))

def volume_formula(phi):
    return 32*PI**3/27*(1+2*math.cos(phi))

def explicit_volume(points):
    return 8*(PI/3)**3*determinant_sum(points)

# Every point lies on the unit sphere and the ensemble is an exact 2-design.
for j in range(32):
    phi=(PI/3)*j/31
    x=points(phi)
    assert len(x)==6
    assert all(abs(dots(v,v)-1)<2e-14 for v in x)
    assert all(abs(sum(v[k] for v in x))<2e-14 for k in range(3))
    assert all(abs(sum(v[a]*v[b] for v in x)-(2 if a==b else 0))<2e-14
               for a in range(3) for b in range(3))
    # Formula from all 20 determinants independently versus cosine closed form.
    assert abs(determinant_sum(x)-(4+8*math.cos(phi)))<3e-13
    assert abs(explicit_volume(x)-volume_formula(phi))<4e-12

# Independent convex hull of all signed generator sums, when scipy is available.
try:
    import numpy as np
    from scipy.spatial import ConvexHull
    for phi in (0.0, PI/12, PI/6, PI/4, PI/3):
        vv=points(phi)
        vertices=np.array([[sum(e*PI/3*vv[i][k] for i,e in enumerate(signs))
                            for k in range(3)] for signs in itertools.product((-1,1),repeat=6)])
        vol=ConvexHull(vertices).volume
        assert abs(vol-volume_formula(phi))<3e-10,(phi,vol,volume_formula(phi))
    print('PASS including five independent convex-hull volume calculations')
except ImportError:
    print('PASS standard-library checks; optional SciPy/NumPy hull test skipped')

# Exact dimensionless endpoint volume and quotient coefficients.
# A cube with the prescribed facet areas has volume squared 8*pi^3/27.
# The aligned triangular bipyramid has volume squared 64*pi^3/243.
assert Fraction(64, 27)/Fraction(8, 27) == 8
assert Fraction(32, 9)/Fraction(64, 243) == Fraction(27, 2)
assert Fraction(32, 9)/Fraction(64, 27) == Fraction(3, 2)

# The two volume functions are ordered in opposite directions on the twist interval.
def body_volume(phi):
    t=2*math.cos(math.pi/3-phi)
    return 4*math.pi**1.5/(9*math.sqrt(3))*(t+1)/math.sqrt(t)

previous_projection=float('inf')
previous_original=0
previous_quotient=float('inf')
for i in range(1001):
    phi=i*math.pi/3000
    vproj=volume_formula(phi)
    vbody=body_volume(phi)
    quotient=vproj/vbody**2
    assert vproj < previous_projection + 2e-12
    assert vbody > previous_original - 2e-12
    assert quotient < previous_quotient + 2e-12
    previous_projection,previous_original,previous_quotient=vproj,vbody,quotient
print('volume / pi^3 at triangular-bipyramid endpoint:',volume_formula(0)/PI**3)
print('volume / pi^3 at cubic endpoint:',volume_formula(PI/3)/PI**3)
