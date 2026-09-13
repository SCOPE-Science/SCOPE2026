"""Inspect the (3,3) residue classes that DO have an integer root in Q."""
import sympy as sp
import sys
sys.path.insert(0, '.')
from cert_table import good_primes, chi_certified
t = sp.Symbol('t')
l, k = 3, 3
gp = good_primes(l, k)
S = list(range(-k + 1, k + 1))
for m in S:
    for tag, skip in [('c', ('c', m)), ('d', ('d', m)), ('s', ('s', m))]:
        chi, Q, coeff = chi_certified(l, k, skip, gp)
        fl = sp.factor_list(chi)
        lin = [(f, e) for f, e in fl[1] if sp.Poly(f, t).degree() == 1]
        print(f'{tag}_m{m}: chi={chi} linears={lin} full_fl={fl}')
