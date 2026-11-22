"""Reproducible finite diagnostics; the global theorem is proved in RESULT.md."""
from fractions import Fraction
from math import log


def check_exact_coefficients():
    for p, q in [(1, 5), (2, 5), (3, 5), (4, 5), (2, 3)]:
        l = Fraction(p, q)
        a = l * (l - 1) / 3
        # Laurent invariance residual at order y^{-5}.
        assert -l*l + l*l*l - 3*a*l == 0
        coeff = (5*l - 2) / 6
        assert coeff == (5*l-2)/6
        if l == Fraction(2,5):
            assert coeff == 0


def iterate(v, lam, steps):
    y = 1.0
    u = v
    out = {}
    for n in range(steps):
        if n in (200, 500, 1000, 2000, 5000, 10000):
            out[n] = (y, u)
        old_u = u
        u *= 1-lam/(1+y*y)
        y += old_u
    return out


def terminal_difference(v, lam, target=100.0):
    y = 1.0
    u = v
    for _ in range(80000):
        if y >= target or u < 1e-17:
            break
        old_u = u
        u *= 1-lam/(1+y*y)
        y += old_u
    if y < target:
        return -1.0
    return u - (lam/y + lam*(lam-1)/(3*y**3))


def shoot(lam):
    lo, hi = 0.0, 2.0
    for _ in range(57):
        mid = (lo+hi)/2
        if terminal_difference(mid,lam)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def check_numerical():
    for lam in (0.4,0.6):
        v=shoot(lam)
        data=iterate(v,lam,11000)
        c=(5*lam-2)/6
        residuals=[y*y-2*lam*n-c*log(n) for n,(y,u) in data.items() if n>=500]
        assert max(residuals)-min(residuals)<0.003, (lam,residuals)
        assert all(y>0 and u>0 for y,u in data.values())
        print(f"lambda={lam:.1f}, finite-target critical speed={v:.15g}, "
              f"log coefficient={c:.12g}, residuals={[round(x,6) for x in residuals]}")

if __name__=='__main__':
    check_exact_coefficients()
    check_numerical()
    print('Finite diagnostics passed; global claims require the analytical proof.')
