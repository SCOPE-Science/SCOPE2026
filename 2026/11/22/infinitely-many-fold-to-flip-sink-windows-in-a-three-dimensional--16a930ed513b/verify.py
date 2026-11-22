"""Self-contained numerical diagnostics for an exact analytic fixed-point staircase.

No external libraries. Bisection checks selected transcendental thresholds;
proof of all-index assertions is given in the accompanying mathematical text.
"""
from math import pi, tan, sqrt, sin, cos, isfinite


def root(fn, left, right):
    fl, fr = fn(left), fn(right)
    assert isfinite(fl) and isfinite(fr) and fl * fr < 0
    for _ in range(100):
        mid = (left + right) / 2
        fm = fn(mid)
        if fm == 0: return mid
        if fl * fm <= 0:
            right, fr = mid, fm
        else:
            left, fl = mid, fm
    return (left + right) / 2


def thresholds(m):
    A = (2*m + .5) * pi
    eta = root(lambda z: tan(z) + z, A + 1.e-6, (2*m+1)*pi - 1.e-6)
    H = sqrt(1 + eta**2)
    if m == 0:
        return (1., H, 0., eta)
    zeta = root(lambda z: tan(z)-z, 2*m*pi+1.e-6, A-1.e-6)
    K = sqrt(1 + zeta**2)
    assert K < H
    return (K, H, zeta, eta)


def h(z): return z/sin(z)
def slope(z): return z*cos(z)/sin(z)

K0,H0,_,eta0 = thresholds(0)
assert K0 == 1. and 2. < H0 < 3.
k0=(K0+H0)/2
z0=root(lambda z: h(z)-k0, 1.e-8, pi-1.e-8)
assert abs(z0-k0*sin(z0)) < 1.e-12
assert abs(slope(z0)) < 1
assert abs(k0*cos(z0)) < 1

for m in (1,2,3,8,20,100):
    K,H,zeta,eta = thresholds(m)
    if m < 100:
        Knext,_,_,_ = thresholds(m+1)
        assert H < Knext
    assert 2*m*pi < zeta < (2*m+.5)*pi < eta < (2*m+1)*pi
    assert abs(tan(zeta)-zeta) < 3.e-6
    assert abs(tan(eta)+eta) < 3.e-6
    k=(K+H)/2
    u=root(lambda z: h(z)-k, 2*m*pi+1.e-7, zeta)
    v=root(lambda z: h(z)-k, zeta, (2*m+1)*pi-1.e-7)
    assert abs(u-k*sin(u)) < 3.e-10
    assert abs(v-k*sin(v)) < 3.e-10
    assert slope(u)>1
    assert -1 < slope(v) < 1
    # The true three-dimensional nonlinear map has stationary point
    # (sin(v), sin(v), v); check both its stationary equations.
    x=sin(v)
    assert abs(v-k*x)<3.e-10
    assert abs(x-sin(v))<1.e-12
    # Small nonzero delayed-feedback perturbations, with k kept fixed,
    # satisfy the four strict cubic Schur inequalities.
    p=q=1.e-5
    g=p+q-k
    c=cos(v)
    a1=g*c; a2=-q*c; a3=-p*c
    assert abs(a3)<1
    assert 1+a1+a2+a3>0
    assert 1-a1+a2-a3>0
    assert 1-a2+a1*a3-a3*a3>0
    A=(2*m+.5)*pi
    if m>=8:
        assert abs((H-K)*A-2)<.008

# Original article's displayed numerical parameters have exactly three
# real fixed points: 0 and one pair in the first sine lobe.
assert 1<3.1<thresholds(1)[0]
print('VERIFY_OK')
