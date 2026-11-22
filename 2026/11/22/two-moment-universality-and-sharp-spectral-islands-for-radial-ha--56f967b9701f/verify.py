"""Finite exact-arithmetic cross-checks for the radial quadratic Toeplitz formula.

Run with Python 3: python3 verify.py
The infinite-dimensional theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as Q

checks = 0

def test(condition):
    global checks
    assert condition
    checks += 1


def beta_moments(alpha, n):
    # Squared-radius Beta(1, alpha+1) moments.
    v = [Q(1)]
    for j in range(n):
        v.append(v[-1] * Q(j+1, j+alpha+2))
    return v


def two_circle_moments(n):
    # One-quarter mass at zero and three-quarters mass at unit radius.
    return [Q(1)] + [Q(3,4)] * n


def shift_coefficient(m, j):
    # Harmonic monomial basis f_j=z^j (j>=0), f_-j=conjugate(z)^j.
    if j >= 0:
        return Q(1)
    k = -j
    return m[k] / m[k-1]


def direct_quadratic_coefficient(m, j):
    # Exact orthogonal projection coefficient of z^2 f_j onto f_(j+2).
    if j >= 0:
        return Q(1)
    k = -j
    if k == 1:
        return m[2] / m[1]
    if k == 2:
        return m[2]
    return m[k] / m[k-2]


laws = [beta_moments(k, 20) for k in (Q(-1,2), 0, 1, 2, 3, 5, 9)]
laws += [two_circle_moments(20)]
for m in laws:
    m1, m2 = m[1:3]
    rho = m2 / m1**2
    delta = m2 / m1 - m1
    test(rho > 1)
    test(delta == m1*(rho-1))
    for j in range(-18, 18):
        direct = direct_quadratic_coefficient(m, j)
        product = shift_coefficient(m, j)*shift_coefficient(m, j+1)
        test(direct - product == (delta if j == -1 else 0))
    # Test mixed-root identities throughout the admissible rational interval.
    for k in range(1, 40):
        # u is interior, v=rho*u exterior, normalized |u|=r.
        r = Q(1, rho) + (Q(1)-Q(1, rho))*Q(k,40)
        u = -r
        v = rho*u
        t = -(u+v)
        lam = -u*v
        test(abs(u) < 1)
        test(abs(v) > 1)
        test(1+Q(1,rho) < t < 1+rho)
        test(lam == -rho*t*t/(1+rho)**2)
        test(1+(rho-1)*u/(u-v) == 0)
        test((rho-1)*t/(u-v)**3 != 0)

# Classical area and a singular two-radius measure are exactly isospectral for
# every quadratic by equality of their rho parameter.
area = beta_moments(0, 20)
singular = two_circle_moments(20)
test(area[1] != singular[1])
test(area[2] != singular[2])
test(area[2]/area[1]**2 == singular[2]/singular[1]**2 == Q(4,3))

# In contrast, z^2+(5/2)z has an outlier for alpha=3 but not alpha=0.
t = Q(5,2)
rho0 = area[2]/area[1]**2
rho3 = beta_moments(3, 3)[2]/beta_moments(3, 3)[1]**2
test(not (1+1/rho0 < t < 1+rho0))
test(1+1/rho3 < t < 1+rho3)
test(-rho3*t*t/(1+rho3)**2 == Q(-375,256))
print('RADIAL_QUADRATIC_CHECK_OK', checks)
