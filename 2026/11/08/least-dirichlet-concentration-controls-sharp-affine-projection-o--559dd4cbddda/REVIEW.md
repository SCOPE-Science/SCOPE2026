# Self-review

## Correctness — PASS

The projection kernel follows from the exact positive Dirichlet Gram matrix and its explicit inverse. Convexity reduces all evaluation norms to vertices; strict sign disagreement of two vertex kernels on an interior open set excludes all mixed vertices and nonvertex maximizers. Exact beta truncated first moments establish the constant, and a conditional-Dirichlet splitting applies a strictly kink-crossing Jensen inequality to prove the full \(L_T(a)\) order. Equality inputs come from the sign of the vertex kernel; the centered mean-one identity gives the positivity defect. The fixed-shape gamma limit uses a uniform second-moment bound. The attached checker supplies exact and floating-point independent spot checks, not an infinite certificate.

## Originality — PASS, qualified

The known uniform-volume affine projector constant (published-finding corpus `2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34`) is recovered and specifically excluded from claimed novelty. Waldron's full 2007 technical report gives the general weighted Jacobi-simplex projection framework, but not the sharp endpoint norm's strict least-concentration rule or the full nonuniform equality classification. Hangelbroek et al. (arXiv:1005.2424) discuss uniform projection bounds in a different kernel-manifold setting. Exact published-finding corpus searches covering Dirichlet, beta convex order, affine projection norms, positivity and vertex selection returned no stronger equivalent; a failed search is not proof of priority. Full text of the uniform-volume published record was not retrievable during this review, which remains a documented bibliographic risk; its published exact special case is treated as prior.

## Mathematical value — PASS

Arbitrary nonuniform Dirichlet densities are a natural multivariate Jacobi family. In this setting, a seemingly multidimensional operator-norm optimization reduces sharply to the single *least concentrated* barycentric coordinate. This strict ordering is valid for all dimensions and positive real weights, with complete equality cases, sharp undershoot, exact beta formula and asymptotic gamma coefficient. It identifies which geometric vertex controls least-squares instability under heterogeneous weighting, rather than merely computing another low-dimensional example. It is not a claim about higher-degree approximation.

## Residual scientific risks

A pre-existing general convex-order theorem can subsume the **strict ordering lemma**; the claimed contribution is its sharp application to the weighted projection norm and full optimizer classification, rather than inventing beta aggregation. An unindexed general Jacobi-projector Lebesgue-constant theorem may dominate this result. Primary preprints inspected do not establish that stronger implication. Independent mathematical validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
