"""Reproducible checks for scalar-complement reduced-basis Richardson stability.

The theorem is proved analytically; finite arithmetic verifies its derived identities.
Run: python verify.py  (Python 3 standard library).
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def spectral_radius(a, b, k, t):
    delta = (1-b*t)**2 + 4*k*k*t/a
    return (abs(1-b*t) + sqrt(delta))/2


def norm2(a, b, k, t):
    # Core T = [[0,-k/a],[-k*t,1-b*t]].
    x, y, z = k/a, k*t, 1-b*t
    trace = x*x + y*y + z*z
    determinant = (x*y)**2  # determinant(T.T*T) = determinant(T)**2.
    return sqrt((trace + sqrt(max(0., trace*trace-4*determinant)))/2)


def safe_roots(a, b, k):
    q = k*k/(a*a)
    K = b*b + k*k*(1-q)
    d = (1-q)*(b*b-k**4/a**2)
    if d <= 0:
        return None
    return ((b-sqrt(d))/K, (b+sqrt(d))/K)


def exact_det_identity(a, b, k, t):
    q = (k/a)**2
    K = b*b + k*k*(1-q)
    # Gram = I - TT^T in the coupled two-dimensional core.
    gram_11 = 1-q
    gram_22 = 2*b*t - (b*b+k*k)*t*t
    gram_12 = (k/a)*(1-b*t)
    lhs = gram_11*gram_22 - gram_12**2
    rhs = -q + 2*b*t - K*t*t
    assert lhs == rhs
    return lhs


# All inputs are exact rational numbers in these algebraic identities.
count = 0
for ai in range(1, 17):
    for bi in range(1, 17):
        for ki in range(0, 17):
            a, b, k = F(ai,3), F(bi,4), F(ki,6)
            if not k*k < a*b:
                continue
            for t in [F(1,10),F(1,3), F(1,1), F(3,2)]:
                exact_det_identity(a,b,k,t)
                count += 1

# Exact rational witness: a=10, b=1, k=2, t=1/5.
a,b,k,t=F(10),F(1),F(2),F(1,5)
assert exact_det_identity(a,b,k,t)>0
# Squared spectral norm is (21+5*sqrt(17))/50 < 1.
assert 21+5*sqrt(17) < 50
assert isclose(norm2(float(a),float(b),float(k),float(t))**2,
               (21+5*sqrt(17))/50,rel_tol=1e-13)
assert norm2(10.,1.,2.,1.) == 2.
assert isclose(spectral_radius(10.,1.,2.,1.),sqrt(F(2,5)),rel_tol=1e-13)

# Sharp impossibility example: a=1, k=2, b=5, rho(1/b)<1 but ||T||>=2.
assert spectral_radius(1.,5.,2.,.2)<1
assert norm2(1.,5.,2.,.2)==2.

rng=Random(732916)
for _ in range(14000):
    a = 10**rng.uniform(-1.0,1.1)
    b = 10**rng.uniform(-1.0,1.1)
    k = sqrt(a*b)*rng.uniform(0.002,.999)
    roots=safe_roots(a,b,k)
    if k<a:
        assert roots is not None
        lo,hi=roots
        assert 0 < lo < hi
        t=(lo+hi)/2
        assert norm2(a,b,k,t)<1+5e-12
        assert exact_det_identity(F(a),F(b),F(k),F(t))>0
    else:
        assert roots is None
        for t in (0.0001,1/b,1.1/b,2/b):
            assert norm2(a,b,k,t)>=1-5e-12
    opt=1/b
    assert isclose(spectral_radius(a,b,k,opt),k/sqrt(a*b), rel_tol=5e-13)
    assert isclose(norm2(a,b,k,opt),max(k/a,k/b),rel_tol=5e-13)
    for t in (opt*.3,opt*.65,opt*1.7,opt*3.5):
        assert spectral_radius(a,b,k,t)>spectral_radius(a,b,k,opt)-1e-12
    if b<=k<a:
        assert norm2(a,b,k,opt)>=1-5e-13
        assert norm2(a,b,k,(roots[0]+roots[1])/2)<1

# Exact two-step parity family: a=1, k=R, b=2R^2, t=1/b.
for R in range(1,40):
    T=((-F(0),-F(R)),(-F(1,2*R),F(0)))
    prod00=T[0][0]**2+T[0][1]*T[1][0]
    prod11=T[1][0]*T[0][1]+T[1][1]**2
    prod01=T[0][0]*T[0][1]+T[0][1]*T[1][1]
    prod10=T[1][0]*T[0][0]+T[1][1]*T[1][0]
    assert prod00==prod11==F(1,2) and prod01==prod10==0
    assert norm2(1,2*R*R,R,1/(2*R*R))==R

print(f"PASS: {count} exact rational Gram determinant identities, 14000 randomized spectral/norm cases, explicit rational and parity witnesses.")
