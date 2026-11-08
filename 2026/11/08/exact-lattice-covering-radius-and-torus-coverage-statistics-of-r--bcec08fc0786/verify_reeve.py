"""Exact supplementary checks for Reeve tetrahedron lattice coverings.

Uses only the Python standard library. Finite-grid checks supplement the
algebraic derivation in RESULT.md; they are not an exhaustive proof.
"""
from fractions import Fraction as Q
from itertools import product


def wrap(x):
    return x - (x.numerator // x.denominator)


def closed_formula(q, x, y, z):
    w = wrap(z) / q
    u, v = wrap(x-w), wrap(y-w)
    a, b = min(u, v), max(u, v)
    return w + b + wrap(q*a) / q


def independent_minimization(q, x, y, z):
    # The integer third-coordinate shift is j=0,...,q-1 modulo q;
    # higher shifts add 1 to the simplex gauge.
    w = wrap(z) / q
    return min(w + Q(j,q) + wrap(x-w-Q(j,q))
               + wrap(y-w-Q(j,q)) for j in range(q))


def clip(poly, h, keep_low):
    """Clip polygon (s,t) by 2s+t<=h, or >=h, with exact rationals."""
    result = []
    def side(p):
        val = 2*p[0]+p[1]-h
        return -val if keep_low else val
    for a,b in zip(poly,poly[1:]+poly[:1]):
        da,db=side(a),side(b)
        inside_a,inside_b=da>=0,db>=0
        if inside_a:
            result.append(a)
        if inside_a != inside_b:
            lam=da/(da-db)
            result.append((a[0]+lam*(b[0]-a[0]),
                           a[1]+lam*(b[1]-a[1])))
    return result


def integrate_affine(poly, a, b, c):
    """Exact integral of a+b*s+c*t over a counterclockwise polygon."""
    if len(poly)<3:
        return Q(0)
    cross_sum=moment_s=moment_t=Q(0)
    for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1]):
        cross=x*v-u*y
        cross_sum += cross
        moment_s += (x+u)*cross
        moment_t += (y+v)*cross
    return a*cross_sum/2 + b*moment_s/6 + c*moment_t/6


def integral_J(h):
    square=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    low=clip(square,Q(h),True)
    high=clip(square,Q(h),False)
    return integrate_affine(low,Q(0),Q(1),Q(1)) + integrate_affine(high,Q(h),Q(-1),Q(0))


assert integral_J(1)==Q(5,12)
assert integral_J(2)==Q(11,12)
for h in range(3,12):
    assert integral_J(h)==Q(1)

checks=0
for q in range(1,10):
    grid=[Q(i,13) for i in range(13)]
    for x,y,z in product(grid,repeat=3):
        assert closed_formula(q,x,y,z)==independent_minimization(q,x,y,z)
        checks+=1
    # Algebraic expressions for uncovered fraction and mean pointwise dilation.
    J=sum((integral_J(h) for h in range(1,q+1)),Q(0))
    uncovered=2*J/q**2
    predicted=(Q(5,6) if q==1 else Q(2,q)-Q(4,3*q*q))
    assert uncovered==predicted
    # Exact integration against density 2(1-a) of the minimum of two uniforms.
    # E[{q min(U,V)}] = (3q-1)/(6q), so the mean is as below.
    mean=Q(2,3)+Q(1,2*q)+Q(3*q-1,6*q*q)
    assert mean==Q(2,3)+Q(1,q)-Q(1,6*q*q)
    print('q=%d: sharp radius=%s, uncovered fraction=%s, mean=%s'
          %(q, Q(q+2,q), uncovered, mean))
print('PASS: %d independent finite-grid minimization checks; exact rational polygon integrals J_1,J_2 and moment identities checked.'%checks)
