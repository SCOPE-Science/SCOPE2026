"""Full deletion scan l=3, k=1..4 (primes all > 2k+1); verify integer-root structure."""
import sympy as sp
import sys
sys.path.insert(0, '.')
from chi_count import chi_at_p, fit_chi

t = sp.Symbol('t')

PRIMES = [23, 29, 31, 37, 41, 43, 47, 53, 59]

GOOD = {1: 4, 2: 6, 3: 8, 4: 10, 5: 12, 6: 14}  # min p: S values distinct mod p


def chi_poly(l, k, skip):
    S = list(range(-k + 1, k + 1))
    pts = [(p, chi_at_p(l, k, p, skip)) for p in PRIMES if p >= GOOD[k]]
    coeff, ok = fit_chi(pts, l + 1)
    assert ok, (l, k, skip, pts, coeff)
    assert all(sp.Integer(c).q == 1 for c in coeff), coeff
    coeff = [int(c) for c in coeff]
    return sp.expand(sum(c * t ** j for j, c in enumerate(coeff)))


def analyze(l, k):
    b = 2 * k * l
    S = list(range(-k + 1, k + 1))
    full = (t - 1) * (t - b) ** l
    got_full = chi_poly(l, k, None)
    assert sp.expand(got_full - full) == 0, (l, k, got_full, full)
    print(f'l={l} k={k}: FULL ok, b={b}')
    # distinct orbit reps: coord (any m: conjecture uniform), diff m, sum m, z
    # scan every m to check orbit uniformity
    reps = [('c', m) for m in S] + [('d', m) for m in S] + [('s', m) for m in S] + [('z',)]
    for r in reps:
        skip = (r[0], r[1]) if r[0] != 'z' else ('z',)
        chi = chi_poly(l, k, skip)
        assert (chi.subs(t, 1)) == 0
        Q = sp.simplify(chi / (t - 1))
        assert sp.Poly(Q, t).LC() == 1
        Qp = sp.Poly(Q, t)
        # values at b
        Qb = int(Q.subs(t, b))
        # factorization over ZZ
        fac = sp.factor(chi)
        roots = sp.Poly(chi, t).all_roots() if False else None
        # integer roots via trial
        lin = sp.factor_list(chi)
        print(f'  skip={r}: Q(b)={Qb:+d} chi={chi} factor={fac} factor_list={lin}')
    print()


if __name__ == '__main__':
    for k in [1, 2, 3, 4]:
        analyze(3, k)
