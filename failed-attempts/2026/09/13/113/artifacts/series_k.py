"""Closed forms for chi of each deletion class + the Q(b) defect formulas.

Strategy: fit each deletion chi as polynomial in (k) with symbolic coefficients?
Simpler: since S = {-k+1..k}, m-values fall into symmetry classes indexed by
j = distance from the "free end". Parametrize m = k - j (top end classes) and
m = interior. Collect Q(b) and chi-ceofficients across k for fixed class to
guess polynomial-in-k closed form, then GUIDE the proof (not substitute for it).

Here: tabulate for l=3: class C_edge (m=k), C_0 (m=0-ish interior), D_edge (m=k),
D_0, Z; print chi coefficients + Q(b) as functions of k.
"""
import sympy as sp
import sys
sys.path.insert(0, '.')
from scan_one import chi_poly_auto

t = sp.Symbol('t')


def series(l, ks, tag, mk_skip):
    print(f'--- l={l} class {tag} ---')
    for k in ks:
        skip = mk_skip(k)
        chi = chi_poly_auto(l, k, skip)
        Q = sp.simplify(chi / (t - 1))
        b = 2 * k * l
        print(f'k={k} skip={skip} Q(b)={int(Q.subs(t, b))} chi={chi}', flush=True)


if __name__ == '__main__':
    series(3, [1, 2, 3, 4], 'C_top(m=k)', lambda k: ('c', k))
    series(3, [1, 2, 3, 4], 'C_mid(m=0)', lambda k: ('c', 0))
    series(3, [1, 2, 3, 4], 'D_top(m=k)', lambda k: ('d', k))
    series(3, [1, 2, 3, 4], 'D_mid(m=0)', lambda k: ('d', 0))
    series(3, [1, 2, 3, 4], 'S_bot(m=-k+1)', lambda k: ('s', -k + 1))
    series(3, [1, 2, 3, 4], 'Z', lambda k: ('z',))
