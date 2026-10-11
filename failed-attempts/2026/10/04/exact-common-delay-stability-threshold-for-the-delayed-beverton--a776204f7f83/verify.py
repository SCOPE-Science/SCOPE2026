import cmath
import math


def chi(lam, tau, P, Q):
    return lam * lam + P * lam * cmath.exp(-lam * tau) + Q * cmath.exp(-2 * lam * tau)


def threshold(P, Q):
    D = P * P - 4.0 * Q
    if D >= 0.0:
        return math.pi / (P + math.sqrt(D))
    return math.asin(P / (2.0 * math.sqrt(Q))) / math.sqrt(Q)


def assert_close(a, b, tol=1e-11):
    if abs(a - b) > tol:
        raise AssertionError((a, b, abs(a-b)))

# Figure 2 parameters from Huang--Long--Shan.
s201 = math.sqrt(201.0)
x1 = (-9.0 + s201) / 10.0
x2 = (-11.0 + s201) / 8.0
m1, b, m2, c1, c2 = 0.5, 1.2, 0.6, 0.4, 0.5
assert abs(1.0 / (1.0 + x1) - m1 - c1 * x2) < 1e-12
assert abs(b / (1.0 + x2) - m2 - c2 * x1) < 1e-12
P = x1 / (1.0 + x1) ** 2 + b * x2 / (1.0 + x2) ** 2
Q = b * x1 * x2 / ((1.0 + x1) ** 2 * (1.0 + x2) ** 2) - c1 * c2 * x1 * x2
D = P * P - 4.0 * Q
if not (P > 0.0 and Q > 0.0 and D > 0.0):
    raise AssertionError((P, Q, D))
tc = threshold(P, Q)
assert_close(tc, 3.590488585197299, 2e-13)
alpha2 = (P + math.sqrt(D)) / 2.0
lam = 1j * alpha2
if abs(chi(lam, tc, P, Q)) > 2e-12:
    raise AssertionError(chi(lam, tc, P, Q))
if not (2.0 < tc < 4.0):
    raise AssertionError(tc)

# Complex-quadratic-root representative case P=Q=1.
P2, Q2 = 1.0, 1.0
tc2 = threshold(P2, Q2)
assert_close(tc2, math.pi / 6.0, 1e-14)
lam2 = 1j * math.sqrt(Q2)
if abs(chi(lam2, tc2, P2, Q2)) > 2e-12:
    raise AssertionError(chi(lam2, tc2, P2, Q2))

# Algebraic factorization at a generic complex test point.
lt = 0.23 + 0.71j
tt = 0.83
y = lt * cmath.exp(lt * tt)
lhs = cmath.exp(2 * lt * tt) * chi(lt, tt, P2, Q2)
rhs = y * y + P2 * y + Q2
if abs(lhs - rhs) > 1e-12:
    raise AssertionError((lhs, rhs))

# Positive crossing direction at both representative critical roots.
for omega, tau in [(alpha2, tc), (1.0, tc2)]:
    deriv = omega * omega / (1.0 + 1j * omega * tau)
    if not deriv.real > 0.0:
        raise AssertionError(deriv)

print('VERIFY_OK')
