"""Verify quartic counterexample disproving the degree-sum bound <= 12.

X = P dx + Q dy with P = -2y, Q = -5x^4  (Hamiltonian of H = y^2 - x^5).
f_c = y^2 - x^5 - c, c in {0,1,2}: each deg 5, X(f_c) = 0 (cofactor 0).
Checks: max degree 4, gcd(P,Q)=1, finite singularities, invariance,
degrees/total, irreducibility over QQ (factor_list), distinctness.
"""
import json
from sympy import symbols, Poly, degree, gcd, groebner, factor_list, diff

x, y = symbols('x y')
P = -2*y
Q = -5*x**4
cs = [0, 1, 2]
fs = [y**2 - x**5 - c for c in cs]

res = {}
res['P'] = str(P)
res['Q'] = str(Q)
res['max_deg'] = max(Poly(P, x, y).total_degree(), Poly(Q, x, y).total_degree())
res['gcd_PQ'] = str(gcd(Poly(P, x, y), Poly(Q, x, y)))
G = groebner([P, Q], x, y, order='lex')
res['groebner_singular_locus'] = [str(g) for g in G.polys]
sols = G.triangular_solve() if hasattr(G, 'triangular_solve') else None
res['triangular_solve'] = str(sols)

inv = []
for c, f in zip(cs, fs):
    Xf = (P*diff(f, x) + Q*diff(f, y)).expand()
    inv.append({'c': c, 'f': str(f), 'Xf': str(Xf),
                'cofactor': 0, 'deg': Poly(f, x, y).total_degree(),
                'factor_list': str(factor_list(f, x, y))})
res['invariants'] = inv
res['total_degree_3_fibers'] = sum(d['deg'] for d in inv)
# pairwise non-associate check: f_c - f_c' is nonzero constant
res['differences'] = {f"{a}_vs_{b}": str((fs[i]-fs[j]).expand())
                      for k, (i, a) in enumerate(zip(range(3), cs))
                      for j, b in zip(range(3), cs) if j > i}
print(json.dumps(res, indent=2))
