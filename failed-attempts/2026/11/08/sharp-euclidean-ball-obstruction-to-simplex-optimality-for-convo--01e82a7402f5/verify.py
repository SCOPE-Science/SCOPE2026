"""Numerical checks for sharp ball-versus-simplex convolution cutoff.

Requires Python 3 and scipy. Running this file directly performs supplementary
numerical checks of the exact formulas; it does not certify the infinite-dimensional
assertions, which have analytic proofs.
"""
import math
from scipy.optimize import brentq
from scipy.special import betainc, gammaln

def c_n(n):
    return 0.5 * math.exp((gammaln(2*n + 1) - 2 * gammaln(n + 1)) / n)

def lens_mass(n, r):
    return betainc((n + 1) / 2, 0.5, 1 - r * r)

def root_data(n):
    c = c_n(n)
    def f(r):
        mass = lens_mass(n, r)
        return c * (1 - mass ** (1 / n)) - r
    r = brentq(f, 0.5, 0.84, xtol=1e-14)
    s = 1 - r / c
    return c, r, s

def main():
    count = 0
    C = (2**27 / (3**18 * math.pi**7)) ** (1 / 30)
    for n in (2, 3, 4, 5, 8, 16, 32, 64, 128, 256, 512, 768):
        c, r, s = root_data(n)
        assert 0 < r < 1 and 0 < s < 1
        assert abs(lens_mass(n, r) ** (1 / n) - s) < 1e-10
        sp = (c*c - 1) / (c*c + 1)
        assert s > sp
        for j in range(1, 70):
            rr = 0.5 + (0.84 - 0.5) * j / 70
            a = c * (1 - lens_mass(n, rr) ** (1 / n)) - rr
            if rr < r - 1e-7:
                assert a < 0
            if rr > r + 1e-7:
                assert a > 0
            count += 1
        count += 3
        print(f"n={n:3d}: r={r:.10f}; s={s:.10f}; published_s={sp:.10f}")
    c2, r2, s2 = root_data(2)
    assert abs(s2 - 0.41078748993) < 1e-9
    assert abs(s2*s2 - 0.16874636188) < 1e-9
    count += 2
    for n in (128, 256, 512, 768):
        c, r, s = root_data(n)
        rpred = 0.8 - (3/(25*n)) * math.log(512*math.pi*n/729)
        spred = 0.6 + (-7*math.log(n) + math.log(2**27/(3**18*math.pi**7))) / (50*n)
        # Diagnostics plus loose asymptotic sanity tests. Neither is a proof.
        assert abs(r-rpred) < 0.0005
        assert abs(s-spred) < 0.0005
        theta_scaled = math.exp(n*math.log(s/0.6)+(7/30)*math.log(n))
        assert abs(theta_scaled-C) < 0.08
        count += 3
        print(f"n={n:3d}: corrected_r_err={r-rpred:.8g}; corrected_s_err={s-spred:.8g}; theta_constant={theta_scaled:.9f}")
    print(f"PASS: {count} supplementary numerical comparisons")

if __name__ == "__main__":
    main()
