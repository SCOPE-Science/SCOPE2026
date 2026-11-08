# Scientific review: exact adjacent-degree law for uniform hypercube spanning trees

## Correctness — PASS
The claimed identity covers all integers \(d\ge3\), with every parameter and boundary defined. The weighted spanning-tree transfer-current determinant is standard. Explicit Walsh decomposition gives five exact kernel entry types, all supported by integral identities. The two uniform-star mean-zero subspaces split into \(d-2\) identical two-dimensional blocks, leaving an exact three-dimensional block; this proves the full polynomial identity. Marginal and covariance formulas follow algebraically and positivity holds by elementary inequalities. Reproducible standalone rational checks compare \(Q_3\) exhaustive enumeration (384 trees), matrix-tree determinants at numerous weights in dimensions 3–5, and exact Walsh sums through dimension 10. These finite checks are corroboration rather than the proof of all dimensions.

## Originality — PASS with historical-priority risk
Aldous (1990), Proposition 9 and the explicit cube example, concerns a **single specified vertex** degree law, not a joint law at two prescribed ambient-adjacent vertices. Nachmias–Peres (2020), Theorems 1.1–1.2, concern a **one-root local weak limit** as degree increases; this does not identify any finite-dimensional prescribed adjacent two-star distribution. Archer–Nachmias–Shalev (2021) concerns global measured-metric scaling. Burton–Pemantle provides the general transfer-current framework but not the evaluated hypercube two-star factorization. A prior exact all-pairs edge-covariance classification in this graph controls only second-order moments, not the full bivariate polynomial. The new calculation diagonalizes the entire weighted two-star kernel; it does not claim novelty for its underlying determinantal principle. published-finding corpus search and accessible record comparison found no explicit stronger covering statement. Historical-priority risk remains, especially for unindexed exact local graph statistics.

## Value — PASS
The exact distribution of neighboring degrees is a natural finite-graph statistic of the UST. It is not fixed by the well-known single-vertex law or pairwise edge correlations. The cubic-times-repeated-quadratic reduction makes an otherwise exponentially indexed weighted-tree determinant directly computable for every dimension, and the positive degree covariance supplies a structurally informative contrast to negative covariance of distinct edge indicators. This is a complete natural family-level law rather than an arbitrary small finite slice.

## Reproduction and limits
Run `python VERIFY.py` with Python 3.10+ and no third-party packages. Only the exact all-dimension mathematical argument proves the theorem; finite checks do not certify historical priority. Scope is unit-weight cubes with two ambient-adjacent vertices; independent validation is absent.

Self-review: passed. Independent audit: not yet performed.
