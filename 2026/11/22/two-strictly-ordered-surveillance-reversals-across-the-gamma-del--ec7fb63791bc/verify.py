"""Reproduce the exact two-surveillance-stream classification and numerical diagnostics.

Requires Python 3.10+ standard library only. The analytic global argument is in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import exp, factorial


def poly(j, z):
    return sum((z**i) / factorial(i) for i in range(j + 1))


def values(m, a, r, t):
    b = m * a
    L = (b / (b + r))**m
    J = 1.0 - exp(-b * t) * poly(m - 1, b * t) + L * exp(-b * t) * poly(m - 1, (b + r) * t)
    Jp = r * L * exp(-b * t) * poly(m - 1, (b + r) * t)
    return J, Jp


def bisect(fun, lo, hi, n=80):
    v0 = fun(lo)
    assert v0 * fun(hi) < 0, (lo, hi, v0, fun(hi))
    for _ in range(n):
        mid = (lo + hi) / 2.0
        if fun(mid) * v0 > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def run():
    tests = 0
    # Exact rational coefficient checks for the key log-slope-ratio derivative.
    # For a=1, r=1, j=k-1: (q-c)P_{k-2}(z) - c z^{k-1}/(k-1)!.
    for k in range(2, 41):
        q, c = k + 1, k - 1
        coeff = [Fraction(q-c, factorial(i)) for i in range(k-1)] + [Fraction(-c, factorial(k-1))]
        assert all(v > 0 for v in coeff[:-1]) and coeff[-1] < 0
        tests += len(coeff)
    # Exact polynomial identity for J_m' = r L_m exp(-m a t) P_{m-1}((m a+r)t).
    for a, r in [(Fraction(1), Fraction(1)), (Fraction(2, 3), Fraction(5, 4))]:
        for m in range(1, 21):
            b = m*a
            L = (b/(b+r))**m
            for i in range(m):
                neg_poly = -b**i/Fraction(factorial(i))
                pos_poly = L*(b+r)**i/Fraction(factorial(i))
                # derivative of exp(-bt) times the combined polynomial
                left = -b*(neg_poly+pos_poly)
                if i+1 < m:
                    left += (-b**(i+1) + L*(b+r)**(i+1))/Fraction(factorial(i))
                right = r*L*(b+r)**i/Fraction(factorial(i))
                assert left == right, (m, i, left, right)
                tests += 1
    for a in (0.2, 1.0, 4.0):
        for r in (0.12, 0.5, 1.0, 3.0, 10.0):
            for k in range(2, 13):
                Lk = (k*a/(k*a+r))**k
                L1 = a/(a+r)
                assert Lk < L1
                count = lambda t: values(k,a,r,t)[0] - values(1,a,r,t)[0]
                growth = lambda t: (values(k,a,r,t)[1]/values(k,a,r,t)[0]
                                    -values(1,a,r,t)[1]/values(1,a,r,t)[0])
                hi = 10.0/a
                tc = bisect(count, 1.e-5/a, hi)
                tg = bisect(growth, 1.e-5/a, hi)
                assert 0 < tc < tg
                assert count(tc*.9) < 0 < count((tc+tg)/2)
                assert growth(tc*.5) > 0 > growth(tg*1.2)
                j0, jp0 = values(k,a,r,0)
                assert abs(jp0 / j0 - r) < 2.e-10
                tests += 7
    # Independent high precision brackets for k=2, a=r=1.
    with localcontext() as ctx:
        ctx.prec = 85
        def F(t):
            return t.exp()-Decimal(10)/9-Decimal(4)*t/3
        def G(t):
            return Decimal(9)*(2*t).exp()-Decimal(8)*(1+3*t)*t.exp()-1+6*t
        a=Decimal('0.74240778603337'); b=Decimal('0.74240778603338')
        c=Decimal('1.60428846844183'); d=Decimal('1.60428846844184')
        assert F(a) < 0 < F(b), (F(a),F(b))
        assert G(c) < 0 < G(d), (G(c),G(d))
        tests += 4
    print('PASS', tests, 'assertions; exact coefficient signs; 165 two-crossing samples; k=2 rigorous decimal brackets')

if __name__ == '__main__':
    run()
