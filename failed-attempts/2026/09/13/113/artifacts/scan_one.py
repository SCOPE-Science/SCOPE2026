"""Focused scan: one (l,k,skip) at a time, auto-extending prime list until fit verifies."""
import sympy as sp
import sys
sys.path.insert(0, '.')
from chi_count import chi_at_p, fit_chi

t = sp.Symbol('t')
PRIMES = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]


def chi_poly_auto(l, k, skip):
    S = list(range(-k + 1, k + 1))
    # good primes: p not dividing any nonzero difference of S-values nor
    # collapsing x_i+x_j sums: need 2k values distinct mod p and no wrap on sums.
    # Safe: p > 4k. Try progressively larger windows.
    # Good primes need affine agreement: empirically chi(p)=(p-1)(p-b)^l and single
    # aff-slice avoids collapse; auto-detect: keep primes where FULL count agrees
    # with the freeness formula (t-1)(t-b)^l, then fit deletions on same primes.
    b = 2 * k * l
    full_pts = [(p, chi_at_p(l, k, p, None)) for p in PRIMES]
    good = [p for p, v in full_pts if v == (p - 1) * (p - b) ** l]
    assert len(good) >= l + 3, (l, k, good)
    good = good[:max(l + 4, 9)]
    for w in [l + 2, l + 3, l + 4, len(good)]:
        pts = [(p, chi_at_p(l, k, p, skip)) for p in good[:w]]
        coeff, ok = fit_chi(pts, l + 1)
        if ok and all(sp.Integer(c).q == 1 for c in coeff):
            # verify on ALL good primes available
            coeff = [int(c) for c in coeff]
            poly = sum(c * t ** j for j, c in enumerate(coeff))
            if all(sum(c * (p ** j) for j, c in enumerate(coeff)) == chi_at_p(l, k, p, skip) for p in good):
                return sp.expand(poly)
    # RANSAC fallback
    import itertools
    pts = [(p, chi_at_p(l, k, p, skip)) for p in good]
    deg = l + 1
    for combo in itertools.combinations(range(len(pts)), deg + 1):
        sub = [pts[i] for i in combo]
        coeff, _ = fit_chi(sub, deg)
        if all(sum(coeff[j] * (sp.Integer(p) ** j) for j in range(deg + 1)) == v for p, v in pts):
            if all(sp.Integer(c).q == 1 for c in coeff):
                return sp.expand(sum(int(c) * t ** j for j, c in enumerate(coeff)))
    raise RuntimeError(f'no fit l={l} k={k} skip={skip}')


def show(l, k):
    b = 2 * k * l
    S = list(range(-k + 1, k + 1))
    got = chi_poly_auto(l, k, None)
    assert sp.expand(got - (t - 1) * (t - b) ** l) == 0, (l, k, got)
    print(f'l={l} k={k} FULL ok b={b}', flush=True)
    reps = [('c', m) for m in S] + [('d', m) for m in S] + [('s', m) for m in S] + [('z',)]
    for r in reps:
        skip = (r[0], r[1]) if r[0] != 'z' else ('z',)
        chi = chi_poly_auto(l, k, skip)
        Q = sp.simplify(chi / (t - 1))
        Qb = int(Q.subs(t, b))
        lin, rest = [], None
        fl = sp.factor_list(chi)
        print(f'  skip={r}: Q(b)={Qb:+d} chi={chi} factors={fl}', flush=True)


if __name__ == '__main__':
    l = int(sys.argv[1]); k = int(sys.argv[2])
    show(l, k)
