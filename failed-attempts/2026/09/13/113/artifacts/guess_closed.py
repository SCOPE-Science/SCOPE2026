"""Guess closed forms: fit each chi coefficient as polynomial in k (per class, l=3)."""
import sympy as sp
import sys
sys.path.insert(0, '.')
from scan_one import chi_poly_auto

t, K = sp.symbols('t K')

CASES = {
    'C_top': lambda k: ('c', k),
    'C_mid': lambda k: ('c', 0),
    'D_top': lambda k: ('d', k),
    'D_mid': lambda k: ('d', 0),
    'S_bot': lambda k: ('s', -k + 1),
    'Z': lambda k: ('z',),
}


def polyfit(vals, deg=None):
    # vals: list of (k, v); fit polynomial in k of minimal degree, verify exact
    ks = [sp.Integer(k) for k, v in vals]
    vs = [sp.Integer(v) for k, v in vals]
    n = len(vals)
    for d in range(n):
        V = sp.Matrix([[k ** j for j in range(d + 1)] for k in ks])
        rhs = sp.Matrix(vs)
        if V.rows == d + 1:
            c = V.LUsolve(rhs)
        else:
            # overdetermined: solve first d+1 rows, verify rest
            c = V[:d + 1, :].LUsolve(rhs[:d + 1, :])
        if all(sum(c[j] * (k ** j) for j in range(d + 1)) == v for k, v in zip(ks, vs)):
            return sum(c[j] * K ** j for j in range(d + 1))
    return None


for tag, mk in CASES.items():
    ks = [1, 2, 3, 4]
    chis = [chi_poly_auto(3, k, mk(k)) for k in ks]
    polys = [sp.Poly(c, t) for c in chis]
    print(f'=== {tag} ===')
    for j in range(5):
        vals = [(k, int(p.nth(j))) for k, p in zip(ks, polys)]
        f = polyfit(vals)
        print(f'  coeff t^{j}: {vals} -> {f}')
