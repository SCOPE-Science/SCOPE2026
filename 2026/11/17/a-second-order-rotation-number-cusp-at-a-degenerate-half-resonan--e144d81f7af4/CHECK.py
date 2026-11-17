"""Reproduce the exact quadratic bottleneck identities and supplementary drift tests.

Requires Python 3 and sympy. All numerical tests supplement, not replace, the proof.
"""
import math
import sympy as s

x, eps, u, a, c = s.symbols('x eps u a c', real=True)
v = a * (1 + s.cos(4 * s.pi * x)) + c * s.sin(2 * s.pi * x)
vp = s.diff(v, x)
vpp = s.diff(vp, x)


def jet(center):
    shift = center + eps * u
    first = eps * (v + v.subs(x, x + s.Rational(1, 2)))
    second = eps**2 * vp.subs(x, x + s.Rational(1, 2)) * v
    third = (eps**3 / 2) * vpp.subs(x, x + s.Rational(1, 2)) * v**2
    ex = 0
    for term in (first, second, third):
        ex += s.series(term.subs(x, shift), eps, 0, 4).removeO()
    P = s.expand(s.simplify(ex).coeff(eps, 3))
    A = s.simplify(P.coeff(u, 2))
    B = s.simplify(P.coeff(u, 1))
    C = s.simplify(P.coeff(u, 0))
    K = s.factor(C - B**2 / (4 * A))
    return P, A, B, C, K

p1, A1, B1, C1, K1 = jet(s.Rational(1, 4))
p2, A2, B2, C2, K2 = jet(s.Rational(3, 4))
assert s.simplify(A1 - 16 * s.pi**2 * a) == 0
assert s.simplify(A2 - A1) == 0
assert s.simplify(B1 - 4 * s.pi**2 * c * (4 * a + c)) == 0
assert s.simplify(B2 - 4 * s.pi**2 * c * (c - 4 * a)) == 0
assert s.simplify(C1 - 2 * s.pi**2 * c**2 * (4 * a + c)) == 0
assert s.simplify(C2 - 2 * s.pi**2 * c**2 * (4 * a - c)) == 0
K = s.pi**2 * c**2 * (16 * a**2 - c**2) / (4 * a)
assert s.simplify(K1 - K) == 0
assert s.simplify(K2 - K) == 0


def drift(e, aa, cc, xx):
    def vfun(t):
        return aa * (1 + math.cos(4 * math.pi * t)) + cc * math.sin(2 * math.pi * t)
    y = xx + 0.5 + e * vfun(xx)
    return e * (vfun(xx) + vfun(y))

# The return displacement equals the second-step forcing plus first-step forcing.
# Check sign-definiteness on sampled grids away from transition ratios.
tests = 0
for aa, cc in [(1, -3), (1, -1), (1, 0.5), (1, 1), (1, 3), (2, 3)]:
    for e in [0.008, -0.008, 0.003, -0.003]:
        samples = [drift(e, aa, cc, k / 2000) for k in range(2000)]
        assert min(e * val for val in samples) > 0, (aa, cc, e, min(samples), max(samples))
        tests += len(samples)
for aa, cc in [(1, 5), (2, -9)]:
    for e in [0.008, -0.008, 0.003, -0.003]:
        samples = [drift(e, aa, cc, k / 4000) for k in range(4000)]
        assert min(samples) < 0 < max(samples)
        tests += len(samples)
for e in [0.1, 0.02, -0.03]:
    assert abs(drift(e, 1, 0, 0.25)) < 1e-12

# Independently confirm the formal coefficient from the Gaussian integral.
coef = s.simplify(s.sqrt(A1*K) / (4*s.pi))
assert s.simplify(coef.subs({a:1,c:1}) - s.pi*s.sqrt(15)/2) == 0
print('PASS exact symbolic jets, identical completed-square minima and coefficient')
print('PASS', tests, 'supplementary sampled sign comparisons')
print('Critical coefficient at a=c=1:', float(coef.subs({a:1,c:1})))
