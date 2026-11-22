"""Independent algebraic and floating-point diagnostics for a quartic SAV midpoint gap.

Run: python check_quartic_sav.py   (Python 3 standard library only)
Numerical diagnostics are not substitutes for the analytic proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt


def poly_mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] += v * w
    return c


def test_algebra():
    # In the indeterminate s, (s-1)^2 (3s^2-4s-2).
    assert poly_mul([Q(1), Q(-2), Q(1)], [Q(-2), Q(-4), Q(3)]) == [Q(-2), Q(0), Q(9), Q(-10), Q(3)]
    # Differentiation of the proposed antiderivative can be done by clearing
    # the positive denominator: integral_0^u t(1-t)/(1+t)^(5/2) dt.
    # With s=sqrt(1+u), the antiderivative is -2(s-1)^2(3s^2-4s-2)/(3s^3).
    # Setting P(s)=3s^4-10s^3+9s^2-2, its derivative in s is
    # (-2/3)*(s*P'(s)-3*P(s))/s^4.
    p = [Q(-2), Q(0), Q(9), Q(-10), Q(3)]
    deriv = [Q(i) * p[i] for i in range(1, len(p))]
    sderiv = [Q(0)] + deriv
    diff = [sderiv[i] - 3 * (p[i] if i < len(p) else 0) for i in range(len(sderiv))]
    # This numerator equals 3(s^2-1)(s^2-2), as it must
    # after factoring out -2/3. Explicit polynomial equivalence:
    assert diff == [Q(6), Q(0), Q(-9), Q(0), Q(3)]
    # Since d/du = (2s)^(-1) d/ds, this says dI/du = u(1-u)/(1+u)^(5/2).
    assert [(-Q(1,3))*w for w in diff] == [Q(-2), Q(0), Q(3), Q(0), Q(-1)]


def f(x, c):
    return sqrt(c + x**4 / 4)


def fp(x, c):
    return x**3 / (2 * f(x, c))


def coeff(x, c):
    s = sqrt(1 + x**4 / (4*c))
    return -c**1.5 * (s-1)**2 * (3*s*s-4*s-2)/(3*s**3)


def step(x, r, h, c):
    # Solve the one-dimensional midpoint equation by monotone bisection.
    lo, hi = x/2, x
    for _ in range(52):
        z = (lo+hi)/2
        rhs = h*r*z**3/(f(z,c) + 0.5*h*fp(z,c)*z**3)
        # 2(x-z) = rhs; left side decreases with z.
        if 2*(x-z) > rhs:
            lo = z
        else:
            hi = z
    z = (lo+hi)/2
    xn = 2*z-x
    rn = r + fp(z,c)*(xn-x)
    assert 0 < xn < x and rn > 0
    assert abs((rn*rn-r*r)+(xn-x)**2/h) < 1e-9*max(1, r*r)
    return xn, rn


def simulate(x0,h,c=1,stop=0.06):
    x, r = x0, f(x0,c)
    steps = 0
    while x > stop:
        x,r = step(x,r,h,c)
        steps+=1
        if steps>200000:
            raise RuntimeError('diagnostic did not reach target')
    return r-f(x,c), x, steps


def test_numbers():
    c=1.0
    crit = (4*c*(5+4*sqrt(10))/9)**0.25
    assert abs(coeff(crit,c)) < 1e-13
    for initial in (0.8, 2.0):
        a=coeff(initial,c)
        d1, x1, k1=simulate(initial,0.05,c)
        d2, x2, k2=simulate(initial,0.025,c)
        assert d1*a>0 and d2*a>0
        assert abs(d2/0.025**2-a) < abs(d1/0.05**2-a)+1e-8
        print('x0=', initial,'A=',format(a,'.12g'),'h=.025 estimate=', format(d2/0.025**2,'.12g'),'steps=',k2)
    d1, _, _=simulate(crit,0.05,c)
    d2, _, _=simulate(crit,0.025,c)
    assert abs(d2/0.025**4-d1/0.05**4)<0.1
    print('critical ratio: h=.05',d1/0.05**4,'h=.025',d2/0.025**4)

if __name__=='__main__':
    test_algebra()
    test_numbers()
    print('PASS: exact rational polynomial identity and numerical diagnostics')
