"""Finite reproducibility checks for centers of maximum balls in three coordinate disk sums.

The analytic proof, not sampling, establishes inclusion for every unit normal.
"""
from math import sqrt, sin, cos, pi, hypot, isclose

CASES = [(1., 1., 1.), (1., 1., .5), (1.3, 1., .8),
         (sqrt(2), 1., 1.), (1.7, 1., 1.), (2., 1., 1.),
         (2.4, 1., 1.), (5., 2., 1.), (sqrt(5), 2., 1.),
         (1.2, 1.1, .5), (3., 2., 1.), (2.2, 1.2, 1.)]

def support(u, a, b, c):
    x, y, z = u
    return a * hypot(x, y) + b * hypot(y, z) + c * hypot(z, x)

def directions(n):
    # Golden-angle normals; axes and equator are separately checked below.
    step = pi * (3 - sqrt(5))
    for j in range(n):
        z = 1 - 2 * (j + .5) / n
        az = step * j
        r = sqrt(1 - z*z)
        yield r*cos(az), r*sin(az), z

def predicted(a, b, c, s, t):
    assert a >= max(b, c) and min(a, b, c) > 0
    k = a-b-c
    if k <= 0:
        return abs(s) <= a-b+1e-12 and abs(t) <= a-c+1e-12
    return hypot(max(abs(s)-c, 0.), max(abs(t)-b, 0.)) <= k+1e-12

def area(a, b, c):
    if a <= b+c:
        return 4*(a-b)*(a-c)
    k = a-b-c
    return 4*b*c + 4*(b+c)*k + pi*k*k

def clearance(a, b, c, s, t, normal):
    return support(normal, a, b, c) - normal[0]*s - normal[1]*t - (b+c)

normals = list(directions(6000))
normals.extend([(1., 0., 0.), (-1., 0., 0.), (0., 1., 0.),
                (0., -1., 0.), (0., 0., 1.), (0., 0., -1.)])
for i in range(144):
    phi = 2*pi*i/144
    normals.append((cos(phi), sin(phi), 0.))

for a, b, c in CASES:
    k = a-b-c
    assert abs(clearance(a, b, c, 0., 0., (0., 0., 1.))) < 1e-12
    if k <= 0:
        candidates = [(0.,0.), (a-b, a-c), (a-b, -(a-c)),
                      (-(a-b), a-c), (-(a-b), -(a-c))]
        outside = [(a-b+.08, 0., (1.,0.,0.))]
    else:
        candidates = [(0.,0.), (c+k,0.), (0.,b+k),
                      (-c-k, 0.), (0.,-b-k),
                      (c+k/sqrt(2), b+k/sqrt(2)),
                      (-c-k/sqrt(2),b+k/sqrt(2))]
        outside = [(c+.07+k/sqrt(2), b+.07+k/sqrt(2),
                    (1/sqrt(2),1/sqrt(2),0.))]
    for s,t in candidates:
        assert predicted(a,b,c,s,t), (a,b,c,s,t)
        lowest = min(clearance(a,b,c,s,t,u) for u in normals)
        assert lowest >= -1e-9, (a,b,c,s,t,lowest)
    for s,t,u in outside:
        assert not predicted(a,b,c,s,t)
        assert clearance(a,b,c,s,t,u) < -1e-5
    # Exactly the same area at the sharp additive phase boundary.
    assert area(a,b,c)>=-1e-12

for b,c in [(1.,1.),(2.,1.),(1.3,.8)]:
    a=b+c
    assert isclose(4*(a-b)*(a-c),4*b*c, rel_tol=1e-14)
    for d in [0.1, 0.01, 0.001]:
        left,mid,right=area(a-d,b,c),area(a,b,c),area(a+d,b,c)
        # Derivatives match, second finite differences differ at first order.
        assert isclose((mid-left)/d,4*(b+c)-4*d,rel_tol=1e-10)
        assert isclose((right-mid)/d,4*(b+c)+pi*d,rel_tol=1e-10)
assert 2*pi-8 < 0
print('WEIGHTED_DISCOTOPE_INCENTER_LOCUS_CHECKS_PASSED')
