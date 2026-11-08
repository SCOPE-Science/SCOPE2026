# Mathematical review

## Correctness — PASS
The unique John ellipsoid is invariant under the residual-barycentric affine symmetry. Under an orthogonal splitting its support inequalities are exactly \(s\le c\), \(s\le h-c\), and \(s^2+n(n-1)\rho^2\le(n-c)^2\); optimizing the determinant proves both branches and the sharp threshold. All contact statements and derivative claims follow from equalities of these explicit constraints. The accompanying standard-library verifier checks the formulas in finite dimensions and rational truncation parameters; an independent scipy nonlinear solve corroborated them numerically. Finite checks are auxiliary; the proof is analytic and holds for all \(n\ge2\) and real \(0<h\le n\).

## Originality — PASS (provisional priority)
The one-capped arbor family appears in Chapoton and in Athanasiadis–Xiao–Yan; their focus is combinatorial/lattice geometry. The especially close result on one-vertex simplex truncations is a mixed-volume profile, not an inscribed ellipsoid; the three-phase capped-hypercube John formula treats a different H-polytope. The high-relevance full texts of both mathematical records and available arbor manuscript sections were compared to this exact claim. Multiple searches against earlier mathematical records and published literature found no covering theorem. This is evidence of noncoverage in material examined, not an absolute uniqueness certificate. The main residual risk is an unindexed equivalent simplex-frustum/optimal-design result.

## Mathematical value — PASS
A natural parameterized class of simplex truncations has a nontrivial, sharp interval in which its maximal ellipsoid is unchanged. The exact volume, contact transition, and \(C^1\)-but-not-\(C^2\) regularity distinguish the result from a routine special case of John's theorem. The result also solves the invariant for the canonical one-capped arbor polytope in every dimension.

## Scope and limitations
The ambient Euclidean metric is fixed, and the theorem does not treat oblique or multiple truncations. Mathematical historical priority and all-dimensional proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
