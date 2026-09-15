"""Sparse-degeneracy lemma for plain flag algebras on this problem.

If m = c*n^{3/2}, the 3-uniform edge density is p(n) = 6m/n^3 = 6c/sqrt(n) -> 0.
Any fixed 3-graph F with e(F) >= 1 has homomorphism density t(F,H) <= p(n) -> 0
(up to constants), so the flag-algebra limit object is the edgeless (zero) graphon.
Consequences: every standard (dense) flag-algebra inequality converges to 0 >= 0
at the relevant scale; it cannot separate Construction H (~0.1924 n^{3/2}) from any
other o(n^3) family, nor resolve an eps*n^{3/2} stability statement.
"""
import math

c = 1 / (3 * math.sqrt(3))
print(f"{'n':>10} {'m~c n^1.5':>12} {'p(n)=6m/n^3':>14} {'eps*n^1.5 / n^3':>18}")
for n in [10**3, 10**4, 10**5, 10**6, 10**9, 10**12]:
    m = c * n**1.5
    p = 6 * m / n**3
    scale = 0.01 * n**1.5 / n**3  # eps=0.01 stability scale as density
    print(f"{n:>10} {m:>12.3f} {p:>14.3e} {scale:>18.3e}")

# analytic bound: t(edge,H) = p -> 0; for fixed F with e>=1 edges,
# t(F,H) <= t(edge,H) = p (by averaging/monotonicity of homomorphism densities
# for subgraphs: each edge-constraint can only lower the count). Hence all -> 0.
ns = [10**6, 10**12]
for n in ns:
    p = 6 * c / math.sqrt(n)
    assert 0 < p < 1e-2, n
print("PASS: edge density -> 0 (zero-graphon limit); dense flag algebras vacuous here")
