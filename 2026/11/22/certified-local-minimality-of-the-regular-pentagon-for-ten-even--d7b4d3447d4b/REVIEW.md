# Self-review

## Correctness — PASS

The regular-pentagon statement is fully quantified for all ten even exponents and neighboring convex labeled pentagons modulo similarities. The triangulation formula follows by binomial expansion and the beta-integral on each oriented triangle; the double-distance moment follows by binomial expansion of the even power. Dihedral symmetry plus scale invariance proves exact stationarity, and differentiating the quotient at stationarity yields the displayed normalized six-by-six Hessian. All positivity conclusions rest on the self-contained exact-integer interval implementation and its ten rational pivot tests, not on floating-point quadrature. The smallest certified pivot is \(>1/5\). Positive definiteness in a local similarity chart and smooth Taylor expansion prove a strict local minimum. Independent floating-point tensor quadrature provides only a secondary cross-check. A code-implementation error remains a reproducibility risk until independently reviewed.

## Originality — PASS (priority risk remains)

The central comparison is with Bogosel–Bucur–Fragalà (2023), arXiv:2302.11677v1, §3.1: they already report numerical *positive* transverse Hessians for exactly the same exponents and pentagon case. This observation is **not** new; their paper does not exhibit certified interval pivot inequalities or a proof of strict local minimality for the ten-exponent pentagon case. The claim advances numerical evidence to a formally replayable finite exact-arithmetic positivity argument. The 2021/2022 Bonacini–Cristoferi–Topaloglu work applies to triangles and quadrilaterals and decreasing kernels. The 2024 validated Faber–Krahn work handles a different Dirichlet eigenvalue. Published research searches and exact claim comparisons uncovered no rigorous dominating result; historical priority against unindexed sources and possible additional versions remains open.

## Mathematical value — PASS

It resolves a specific, literature-motivated proof gap spanning ten exponents for a canonical five-sided geometry. The certificate separates true local stability from numerical optimizer/Hessian evidence and supplies exact checkable inequalities on every nonsimilarity mode. The result is a local benchmark for nonlocal polygon energies; it does not solve the global nonlocal isoperimetric problem nor all exponents/side counts.

## Scope and verification limitations

Only the listed ten even exponents, sufficiently nearby nondegenerate convex pentagons, and the displayed mathematical functional are covered. There is no global claim, no assertion of uniqueness among all polygons, and no third-party mathematical certificate. Independent audit would need to review the beta-moment formula, quotient-Hessian identity, code and rational interval execution.

Self-review: passed. Independent audit: not yet performed.
