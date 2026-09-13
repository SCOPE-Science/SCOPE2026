"""Prove no integer root: certify each irreducible cubic/quartic factor has none.

For Qbar(t) = Q(t) after removing known linear factors: if it has an integer
root r, then r | Qbar(0). Enumerate divisors and evaluate. Cross-check Q has
no root by evaluating at all divisors + factor_list has no linear factor
(already shown by Z-factorization). Also prove irreducibility claims where
needed by rational-root + quadratic-factor exclusion (evaluate: if the cubic
is irreducible over Z it suffices that no integer root; quartic needs ruling
out product of two quadratics — do integer undetermined-coefficient search).
"""
import sympy as sp

t = sp.Symbol('t')

CASES = {
    # (l,k,skip): chi coefficients low->high, from verified fits
    'l3k1_c':   [191, -289, 115, -18, 1],
    'l3k1_d0':  [196, -295, 116, -18, 1],
    'l3k1_z':   [201, -301, 117, -18, 1],
    'l3k2_c0':  [1647, -2061, 449, -36, 1],
    'l3k2_d0':  [1646, -2060, 449, -36, 1],
    'l3k2_dmid':[1618, -2029, 446, -36, 1],
    'l3k2_z':   [1713, -2137, 459, -36, 1],
    'l4k1_c':   [-3753, 5654, -2264, 394, -32, 1],
    'l4k1_d0':  [-3844, 5772, -2293, 396, -32, 1],
    'l4k1_z':   [-3991, 5968, -2346, 400, -32, 1],
}


def divisors(n):
    n = abs(int(n))
    if n == 0:
        return None
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, -i, n // i, -(n // i)}
    return sorted(d)


def certify_no_int_root(coeff, label):
    p = sum(c * t ** j for j, c in enumerate(coeff))
    const = coeff[0]
    divs = divisors(const)
    vals = [(r, int(p.subs(t, r))) for r in divs]
    bad = [r for r, v in vals if v == 0]
    # also bound check: any integer root must divide const, so this is exhaustive
    print(f'{label}: const={const} ndiv={len(divs)} min|val|={min(abs(v) for _, v in vals)} integer_roots={bad}')
    assert not bad
    fl = sp.factor_list(p)
    lin = [f for f, e in fl[1] if sp.Poly(f, t).degree() == 1]
    assert not lin, (label, fl)
    print(f'   factor_list={fl}')
    return fl


for label, coeff in CASES.items():
    # divide by (t-1) first
    q, r = sp.div(sum(c * t ** j for j, c in enumerate(coeff)), t - 1)
    assert r == 0
    certify_no_int_root(sp.Poly(q, t).all_coeffs()[::-1], label + ' Q')
print('ALL CERTIFIED: no integer root in any Q above')
