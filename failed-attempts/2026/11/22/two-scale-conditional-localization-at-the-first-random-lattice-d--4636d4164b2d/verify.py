"""Independent numerical checks for the conditional two-scale location theorem.
Standard-library only. Numerical quadrature is corroboration, not the proof.
"""
import math
from fractions import Fraction

# Exact enumeration of squared distances to square corners, independently
# of the order-statistic formulas used in the proof.
checks = 0
for i in range(1, 67):
    for j in range(1, 65):
        s = Fraction(i, 205)
        t = Fraction(j, 207)
        eps = Fraction((i * 23 + j * 17) % 120 + 1, 2048)
        squared = sorted((s + Fraction(a, 2))**2 +
                         (t + Fraction(b, 2))**2
                         for a in (-1, 1) for b in (-1, 1))
        n = sum(z <= Fraction(1, 2) + eps for z in squared)
        triple = s*s+t*t+abs(s-t) <= eps
        quad = s*s+t*t+s+t <= eps
        assert (n >= 3) == triple
        assert (n == 4) == quad
        assert (n == 3) == (triple and not quad)
        checks += 3

A = 4 / (3 * math.sqrt(2))

def midpoint(f, a, b, n=240000):
    h = (b-a) / n
    return h*sum(f(a+(k+0.5)*h) for k in range(n))

def region_areas(eps):
    ymax = 2 / (1+math.sqrt(1+4*eps))
    # 'H' is the limit parabolic cap. 'H_eps' its finite-scale subset.
    h = midpoint(lambda y: 2*(math.sqrt(max(0,(1-y-0.5*eps*y*y)/2))
                          -math.sqrt(eps)*y/2), 0, ymax)
    k = midpoint(lambda x:
                max(0, 2*(1-x-eps*x*x) / (
                    1+math.sqrt(1+4*eps*(1-x-eps*x*x)))),
                0, ymax)
    return h,k

for eps in (0.01,0.0025,0.0004,0.0001):
    H, K = region_areas(eps)
    assert 0 < H < A and 0 < K < .5
    # Four-corner area inside (X,Y) variables is sqrt(eps)*K.
    H3 = H-math.sqrt(eps)*K
    assert 0 < H3 < H
    tv_ge3 = 1-H/A
    tv_exact3 = 1-H3/A
    tv_four = 1-2*K
    c_ge3 = 3*math.sqrt(2)/8
    c_exact3 = 3*math.sqrt(2)/4
    c_four = 4/3
    print("REPORT",eps,tv_ge3/math.sqrt(eps),tv_exact3/math.sqrt(eps),tv_four/eps);assert abs(tv_ge3/math.sqrt(eps)-c_ge3) < 2*math.sqrt(eps)+0.0003
    assert abs(tv_exact3/math.sqrt(eps)-c_exact3) < 2*math.sqrt(eps)+0.0003
    assert abs(tv_four/eps-c_four) < 3*eps + 0.0003
    checks += 6

# The limit cap has area 4/(3 sqrt(2)), triangular square limit area 1/2.
assert abs(A - midpoint(lambda x: 2*(1-2*x*x),0,1/math.sqrt(2),100000))<1e-8
checks += 1
print(f"GEOMETRIC_TWO_SCALE_CHECKS_PASSED {checks}")
