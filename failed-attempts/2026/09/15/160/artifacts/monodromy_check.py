"""Bounded recovery test: chart-dependence of wall vectors under skeleton monodromy.

Model: 2D integral-affine focus-focus monodromy around singular locus of Sk(U),
M = [[1,1],[0,1]] (standard focus-focus). A wall contact vector u in the character
lattice N=Z^2 parallel-transported around Sing becomes M*u. If M*u != u, then the
monomial z^{-u} and wall direction are chart-dependent: a global identity
f^an_x = f^log_x for all x off Sing has no canonical meaning without a torus
trivialization fixing the lattice identification.

This reproduces the concrete obstruction to dropping the dense-torus hypothesis
by pure formal manipulation.
"""
import json
import os

M = [[1, 1], [0, 1]]

def apply(M, u):
    return [M[0][0]*u[0] + M[0][1]*u[1], M[1][0]*u[0] + M[1][1]*u[1]]

vectors = [[1, 0], [0, 1], [1, 1], [2, -1], [-1, 3], [0, 0]]
rows = []
for u in vectors:
    v = apply(M, u)
    rows.append({"u": u, "M*u": v, "fixed": (u == v)})

nontrivial = [r for r in rows if not r["fixed"]
              and not (r["u"] == [0, 0])]
print("focus-focus monodromy M = [[1,1],[0,1]]")
for r in rows:
    print(r)
print(f"non-fixed nonzero vectors: {len(nontrivial)}/{len(rows)-1}")
assert nontrivial, "expected chart-dependence"
# The zero vector is trivially fixed; every nonzero vector with u[1]!=0 moves.
assert all(r["u"][1] != 0 for r in nontrivial)
print("RESULT: chart-dependence confirmed; canonical global lattice ID fails without torus chart.")

out = {"M": M, "rows": rows,
       "result": "M*u != u for generic contact orders: monomials z^{-u} are chart-dependent"}
os.makedirs(os.path.dirname(__file__), exist_ok=True)
with open(os.path.join(os.path.dirname(__file__), "monodromy_check_result.json"), "w") as f:
    json.dump(out, f, indent=2)
