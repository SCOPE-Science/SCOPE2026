"""Finite numerical consistency checks for the spherical first-band theorem.

These calculations are supplementary only; the full theorem is established analytically.
"""
import cmath
import math
import random

PI = math.pi


def j0(z):
    return 1.0 if z == 0 else math.sin(z) / z


def j1(z):
    if z == 0:
        return 0.0
    if abs(z) < 0.001:
        return z / 3 - z**3 / 30 + z**5 / 840
    return math.sin(z) / z**2 - math.cos(z) / z


def h(z):
    if z == 0:
        return 0.0
    if z < 0.001:
        return z / 3 + z**3 / 45 + 2 * z**5 / 945
    return 1 / z - math.cos(z) / math.sin(z)


def dh(z):
    if z == 0:
        return 1 / 3
    if z < 0.001:
        return 1 / 3 + z**2 / 15 + 2 * z**4 / 189
    return 1 / math.sin(z)**2 - 1 / z**2


def vecnorm(v):
    return math.sqrt(sum(t * t for t in v))


def y(x, kappa=1):
    r = vecnorm(x)
    if r == 0:
        return (0., 0., 0.)
    return tuple(h(kappa * r) * t / r for t in x)


def dot(a, b):
    return sum(s * t for s, t in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def subtract(a,b):
    return tuple(u-v for u,v in zip(a,b))


def project_atom(x):
    r = vecnorm(x)
    if r == 0:
        return (1+0j, 0j, 0j, 0j)
    a, b = j0(r), j1(r)
    return (complex(a),) + tuple(1j * math.sqrt(3) * b * q/r for q in x)


def inner(p,q):
    return sum(u.conjugate()*v for u,v in zip(p,q))


def bisect(level, left, right, iters=110):
    # Assumes monotone h on the interval.
    assert h(left) < level < h(right)
    for _ in range(iters):
        middle=(left+right)/2
        if h(middle) < level:
            left=middle
        else:
            right=middle
    return (left+right)/2


def main():
    random.seed(20261111)
    checks = 0
    # Direct angular quadrature of the plane-wave zeroth and first moments.
    n=4096
    for z in [0.2,1.7,2.9,3.8,5.2,7.6]:
        # composite trapezoid (endpoints have half-weight)
        vals=[cmath.exp(1j*z*(-1+2*j/n)) for j in range(n+1)]
        integral0=sum((0.5 if j in (0,n) else 1)*v for j,v in enumerate(vals))/n
        integral1=sum((0.5 if j in (0,n) else 1)*(-1+2*j/n)*v for j,v in enumerate(vals))/n
        assert abs(integral0-j0(z))<2e-6
        assert abs(integral1-1j*j1(z))<2e-6
        checks += 2
    for _ in range(250):
        z=3.05*random.random()
        assert h(z)+1e-12 >= z/3
        assert dh(z)+1e-12 >= 1/3
        checks += 2
    for _ in range(250):
        x=[random.uniform(-1,1) for _ in range(3)]
        x=tuple(t*2.4/3**0.5 for t in x)
        x2=[random.uniform(-1,1) for _ in range(3)]
        x2=tuple(t*2.4/3**0.5 for t in x2)
        # Both norms strictly below pi.
        assert vecnorm(subtract(y(x),y(x2)))*3+1e-10>=vecnorm(subtract(x,x2))
        checks +=1
    for _ in range(100):
        x=tuple(random.uniform(-2,2) for _ in range(3))
        x2=tuple(random.uniform(-2,2) for _ in range(3))
        r1,r2=vecnorm(x),vecnorm(x2)
        p,q=project_atom(x),project_atom(x2)
        numerical=(inner(p,p)*inner(q,q)-abs(inner(p,q))**2).real
        ya,yb=y(x),y(x2)
        formula=3*j0(r1)**2*j0(r2)**2*(vecnorm(subtract(ya,yb))**2+3*vecnorm(cross(ya,yb))**2)
        assert abs(numerical-formula)<1e-10
        checks +=1
    for n in range(1,5):
        lo,hi=n*PI+1e-4,(n+1)*PI-1e-4
        for t in [0.1,0.5,1.0,2.0]:
            neg=bisect(-t,lo,hi)
            pos=bisect(t,lo,hi)
            assert lo<neg<pos<hi
            assert abs(h(neg)+t)<1e-10 and abs(h(pos)-t)<1e-10
            # Identical projective coordinate +t along the first coordinate,
            # with antipodal directions across opposite signs of h.
            assert abs(h(neg)*(-1)-h(pos))<1e-10
            checks +=3
    # Exact nonzero-mean / pure-degree-one exceptional distinction.
    for n in range(1,5):
        z=n*PI
        assert abs(j0(z))<1e-14 and abs(j1(z))>0.01
        checks +=1
    print(f'CHECK_OK spherical_moment_quadrature=12 first_band_inequalities=500 '
          f'inverse_distance=250 gram_identity=100 global_shell_alias=48 '
          f'pure_degree_one=4 total={checks}')


if __name__=='__main__':
    main()
