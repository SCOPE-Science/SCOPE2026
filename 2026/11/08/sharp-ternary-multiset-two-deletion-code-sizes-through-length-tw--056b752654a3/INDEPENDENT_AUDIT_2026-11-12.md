# Independent mathematical audit

## correctness

PASS

PASS: common two-deletion unordered output iff d(u,v)=L1(u-v)/2 <=2; code iff conflict-graph independent set distance>=3. Each of 15 rows n6..20 in actual s3_cert.json was independently verified by BigInt exact rational arithmetic: witness length/uniqueness and distance>=3, positive-weight dual cliques pairwise dist<=2, every simplex vertex coverage>=1, dual_cost equality and < optimum+1, and residue-class counts. Integer optimum squeezed between witness size and floor of rational cover cost. No floating-point or solver trust required; outside n6..20 not asserted.

## originality

PASS

PASS best-of-knowledge: a complete exact n=6..20 table for ternary multiset codes correcting precisely TWO deleted elements is a natural finite coding invariant. The older exhaustive n-t=2 small-survivor regime varies t with n, and the 2026 multiset-profile graph theorem solves ONE deletion (distance>=2), not the required distance>=3 graph; neither implies the fifteen current exact maxima.

## value

PASS

PASS: finite-length exact optimum of natural ternary two-deletion correcting codes is important for choosing codebooks when asymptotic formulas are inconclusive. Fifteen rigorously certified maxima and non-cyclic improvements offer genuinely unknown natural integer invariants without requiring a general n formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
