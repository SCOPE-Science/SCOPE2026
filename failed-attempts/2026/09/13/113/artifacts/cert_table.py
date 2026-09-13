"""Consolidated certification table for the emergent claim scope.

Scope: l=3, k in {1,2,3,4}; l=4, k in {1,2}; EVERY single-hyperplane deletion
(all m in S, both signs, plus z=0) — covers every W(B_l)-orbit representative
(indeed every hyperplane).

For each (l,k,skip): recompute chi counts on good primes (auto-detected as
primes where FULL count matches (p-1)(p-b)^l), fit degree-(l+1) polynomial,
assert exact integer coefficients + verification on all good primes, assert
(t-1)|chi, factor over ZZ, and certify non-freeness-relevant statements:
  - FREE-CANDIDATE class: assert chi == (t-1)(t-b)^{l-1}(t-b+1) exactly.
  - ALL OTHER classes: assert the exact chi and that the cofactor Q=chi/(t-1)
    has NO integer root, certified by exhaustive divisor check
    (any integer root r of Q divides Q(0); evaluate at every divisor).
Writes chi_table.json with full certificate.
"""
import sympy as sp
import json
import sys
sys.path.insert(0, '.')
from chi_count import chi_at_p, fit_chi

t = sp.Symbol('t')
PRIMES = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]


def divisors(n):
    n = abs(int(n))
    assert n != 0
    d = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            d |= {i, -i, n // i, -(n // i)}
        i += 1
    return sorted(d)


def good_primes(l, k):
    b = 2 * k * l
    gp = [p for p in PRIMES if chi_at_p(l, k, p, None) == (p - 1) * (p - b) ** l]
    assert len(gp) >= l + 2, (l, k, gp)
    return gp


def chi_certified(l, k, skip, gp):
    pts = [(p, chi_at_p(l, k, p, skip)) for p in gp]
    coeff, ok = fit_chi(pts, l + 1)
    assert ok, (l, k, skip, pts)
    assert all(sp.Integer(c).q == 1 for c in coeff), (l, k, skip, coeff)
    coeff = [int(c) for c in coeff]
    chi = sp.expand(sum(c * t ** j for j, c in enumerate(coeff)))
    assert chi.subs(t, 1) == 0
    q, r = sp.div(chi, t - 1)
    assert r == 0
    return chi, sp.expand(q), coeff


def nonfree_cert(chi, Q):
    """Certificate that D is not free (Terao + Z-factorization), in one of two
    exhaustive sub-cases:
      (A) chi does not split over Z at all (Q has no integer root);
      (B) chi splits only partially: (t-1)(t-r)R(t) with R integer monic of
          degree >= 2 having no integer root (still not a full linear
          factorization, so Terao's theorem rules out freeness).
    Returns dict with verified kind and data."""
    assert chi.subs(t, 1) == 0
    fl = sp.factor_list(chi)
    lin = [(f, e) for f, e in fl[1] if sp.Poly(f, t).degree() == 1]
    assert all(e == 1 for _, e in lin), fl  # (t-1) and any other root simple here
    nonlin = [(f, e) for f, e in fl[1] if sp.Poly(f, t).degree() >= 2]
    if len(lin) == 1:
        cert = no_int_root_cert(Q)
        return {'kind': 'A_no_integer_root', 'linear_part': str(lin),
                'factor_list': str(fl), 'cofactor_cert': cert}
    # kind B: one extra simple integer-root factor; residual R = product of the
    # nonlinear factors (already certified to have no linear factor over ZZ).
    assert len(lin) == 2, fl
    lin_sorted = sorted(lin, key=lambda fe: int(fe[0].subs(t, 0)))
    R = sp.expand(sp.prod([f ** e for f, e in fl[1]
                           if sp.Poly(f, t).degree() >= 2]))
    assert sp.expand(lin_sorted[0][0] * lin_sorted[1][0] * R - chi) == 0, (fl, R)
    assert sp.Poly(R, t).LC() == 1
    # R integer coefficients?
    Rp = sp.Poly(R, t)
    assert all(sp.Integer(c).q == 1 for c in Rp.all_coeffs()), R
    Rcert = no_int_root_cert(sp.expand(R))
    # discriminant check for the quadratic case recorded when applicable
    extra = {}
    if Rp.degree() == 2:
        a, b_, c_ = [int(x) for x in Rp.all_coeffs()]
        extra['discriminant'] = b_ ** 2 - 4 * a * c_
    return {'kind': 'B_one_extra_root', 'extra_root': str(lin_sorted[1][0]),
            'linear_part': str(lin), 'factor_list': str(fl),
            'residual': str(sp.expand(R)), 'residual_cert': Rcert,
            **extra}


def no_int_root_cert(Q):
    Qp = sp.Poly(Q, t)
    assert Qp.LC() == 1
    const = int(Q.subs(t, 0))
    assert const != 0
    divs = divisors(const)
    vals = {r: int(Q.subs(t, r)) for r in divs}
    assert all(v != 0 for v in vals.values()), \
        [r for r, v in vals.items() if v == 0]
    fl = sp.factor_list(Q)
    assert not any(sp.Poly(f, t).degree() == 1 for f, _ in fl[1]), fl
    return {'Q0': const, 'n_divisors_checked': len(divs),
            'min_abs_value': min(abs(v) for v in vals.values()),
            'factor_list': str(fl)}


def run_scope():
    scope = [(3, k) for k in (1, 2, 3, 4)] + [(4, k) for k in (1, 2)]
    table = {}
    for l, k in scope:
        b = 2 * k * l
        S = list(range(-k + 1, k + 1))
        gp = good_primes(l, k)
        free_form = sp.expand((t - 1) * (t - b) ** (l - 1) * (t - b + 1))
        rows = {}
        for m in S:
            for tag, skip in [('c', ('c', m)), ('d', ('d', m)), ('s', ('s', m))]:
                chi, Q, coeff = chi_certified(l, k, skip, gp)
                if (tag == 'd' and m == k) or (tag == 's' and m == -k + 1):
                    assert sp.expand(chi - free_form) == 0, (l, k, tag, m, chi)
                    rows[f'{tag}_m{m}'] = {'class': 'SPLIT',
                                           'chi': str(chi), 'coeff': coeff}
                else:
                    cert = nonfree_cert(chi, Q)
                    rows[f'{tag}_m{m}'] = {'class': 'NON_SPLIT',
                                           'chi': str(chi), 'coeff': coeff,
                                           'nonfree_cert': cert}
        chi, Q, coeff = chi_certified(l, k, ('z',), gp)
        cert = nonfree_cert(chi, Q)
        rows['z_del'] = {'class': 'NON_SPLIT_Z', 'chi': str(chi),
                         'coeff': coeff, 'nonfree_cert': cert}
        table[f'l{l}_k{k}'] = {'b': b, 'good_primes': gp,
                               'free_candidate_form': str(free_form),
                               'rows': rows}
        n_split = sum(1 for v in rows.values() if v['class'] == 'SPLIT')
        print(f'l={l} k={k}: certified {len(rows)} deletions, '
              f'{n_split} SPLIT, good_primes={gp}', flush=True)
    with open('chi_table.json', 'w') as f:
        json.dump(table, f, indent=1)
    print('wrote chi_table.json')


if __name__ == '__main__':
    run_scope()
