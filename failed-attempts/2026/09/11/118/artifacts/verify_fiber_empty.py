"""Verify the empty-fiber disproof for Bad(1/2,1/2) cap L0, L0: y=x/2+1/3.

Checks (stdlib only, exact rational arithmetic where claimed):
 1. Resonant identity: for q=6m, ||q(t/2+1/3)|| = ||3mt|| exactly (shift by
    integer 2m vanishes), for exact rational sample points.
 2. Doubling bound: max(||2theta||,||theta||) <= 2||theta|| over a dense
    rational grid of fractional parts (exact Fraction arithmetic).
 3. Threshold lemma: m > 24/c^2 turns Dirichlet approximants ||mu||<1/m into
    fiber violations 2||mu|| < c/sqrt(6m); verified arithmetically.
 4. End-to-end violation certificates: for exact rational test slopes,
    exhibit an explicit m with max(||6mt||,||3mt||) < c/sqrt(6m).
"""
from fractions import Fraction
import math


def dist_to_int_frac(x: Fraction) -> Fraction:
    f = x - math.floor(x)  # fractional part in [0,1), exact
    if f > Fraction(1, 2):
        return Fraction(1, 1) - f
    return f


def test_resonant_identity():
    samples = [Fraction(1, 7), Fraction(22, 13), Fraction(-5, 3),
               Fraction(0, 1), Fraction(355, 113) - 3]
    for t in samples:
        for m in [1, 2, 3, 7, 11, 50]:
            q = 6 * m
            y = t / 2 + Fraction(1, 3)
            lhs = dist_to_int_frac(q * y)
            rhs = dist_to_int_frac(Fraction(3 * m, 1) * t)
            assert lhs == rhs, f"identity fail t={t} m={m}: {lhs} vs {rhs}"
            assert (q * Fraction(1, 3)).denominator == 1  # q/3 = 2m integer
    print("identity: OK (||q(t/2+1/3)|| = ||3mt|| for q=6m, exact)")


def test_doubling_bound():
    N = 2000
    worst = Fraction(0)
    for k in range(N):
        th = Fraction(k, N)
        d1 = dist_to_int_frac(th)
        d2 = dist_to_int_frac(2 * th)
        m = max(d1, d2)
        assert m <= 2 * d1, f"doubling fail theta={th}"
        if d1 > 0:
            r = m / d1
            if r > worst:
                worst = r
    print(f"doubling: OK (max(||2th||,||th||) <= 2||th|| on {N}-grid, "
          f"worst ratio {float(worst):.4f})")


def test_threshold_lemma():
    for c in [Fraction(1, 2), Fraction(1, 10), Fraction(1, 100)]:
        thr = Fraction(24, 1) / (c * c)  # m > 24/c^2
        for m in [int(thr) + 1, int(thr) + 5, 10 * int(thr) + 100]:
            # violation implication: 2/m < c/sqrt(6m)
            assert 2.0 / m < float(c) / math.sqrt(6 * m)
    print("threshold: OK (m > 24/c^2 turns 1/m Dirichlet hit into violation)")


def dirichlet_violation_demo():
    # Exact rational test slope u0 ~= sqrt(2); t = u0/3; search explicit m
    # with 2||m u0|| < c/sqrt(6m), which forces the fiber inequality to fail.
    u0 = Fraction(1393, 985)
    for c in [Fraction(1, 2), Fraction(1, 10), Fraction(1, 100)]:
        found = None
        for m in range(1, 5000):
            d = dist_to_int_frac(u0 * m)
            if 2.0 * float(d) < float(c) / math.sqrt(6 * m):
                t = u0 / 3
                q = 6 * m
                e1 = dist_to_int_frac(q * t)
                e2 = dist_to_int_frac(q * (t / 2 + Fraction(1, 3)))
                assert max(e1, e2) <= 2 * d  # doubling + identity
                if float(max(e1, e2)) < float(c) / math.sqrt(q):
                    found = (m, float(d), float(max(e1, e2)),
                             float(c) / math.sqrt(q))
                    break
        assert found is not None, f"no violation found for c={c}"
        print(f"c={float(c):.3f}: violation at m={found[0]}, "
              f"||mu||={found[1]:.3e}, fiber max={found[2]:.3e} "
              f"< c/sqrt(q)={found[3]:.3e}")

    # Float illustration of the mechanism for irrational slopes (demo only)
    for t, name in [(math.sqrt(2), "sqrt2"), (math.pi, "pi")]:
        c = 0.1
        u = 3 * t
        for m in range(1, 20000):
            d = abs(m * u - round(m * u))
            if 2 * d < c / math.sqrt(6 * m):
                q = 6 * m
                e1 = abs(q * t - round(q * t))
                e2 = abs(q * (t / 2 + 1 / 3) - round(q * (t / 2 + 1 / 3)))
                assert max(e1, e2) < c / math.sqrt(q) + 1e-9
                print(f"t={name}, c={c}: violation m={m}, "
                      f"max={max(e1, e2):.3e} < {c / math.sqrt(q):.3e}")
                break


if __name__ == "__main__":
    test_resonant_identity()
    test_doubling_bound()
    test_threshold_lemma()
    dirichlet_violation_demo()
    print("VERIFY_OK")
