# Scientific assessment of the all-bandwidth spherical ring determinant theorem

## Correctness — PASS

The defined complex spherical harmonics, full-area normalization, ring populations, latitude range, and scalar determinant are explicit in `RESULT.md`. A unitary angular DFT makes the evaluation matrix block triangular by harmonic order, and each diagonal block is an associated-Legendre derivative Vandermonde matrix. Its squared determinant produces every constant and exponent in the product. The logarithmic Hessian is a sum of negative endpoint and squared-gap terms, strictly negative in every nonzero direction. Each ordering chamber has an interior maximizer because the log determinant tends to minus infinity on its boundary. The 387 checker assertions are supplementary and were executed on the packaged checker, not substituted for proof.

## Originality — PASS relative to inspected sources

Khalid–Kennedy–McEwen (2014) and Nafees et al. (2017) establish the ring scheme and per-order recovery blocks, and optimize their condition numbers rather than the all-bandwidth determinant. Dell'Accio et al. (May 2026) study constrained interpolation–regression under rank assumptions, not the explicit ring-design landscape. Haines (December 2024) treats spherical-design regression optima under other feasible constraints. The earlier exact nine-node quadratic determinant is a proper special case and is not claimed as a new special case. Actual semantic searches against a mathematical results repository did not identify the all-bandwidth closed determinant plus exact chamber-maxima count. A classical implicit weighted-Fekete or collocation factorization is a residual bibliographic priority risk; database absence is not a proof of novelty.

## Value — PASS

The statement solves a naturally constrained, minimum-cardinality spherical sampling design problem in all harmonic bandwidths: it gives a closed volume criterion, an exact interpolation/noninterpolation boundary, invariance to all ring phases, and a complete classification of the critical points in the height-ordering cells. Each otherwise nonconvex chamber becomes a strictly concave optimization with a unique solution and an explicit stationarity system. This gives a structural and reproducible design certificate distinct from a routine test of a single determinant or a condition-number bound.

## Scope and remaining risks

The globally best permutation of ring heights is not identified for arbitrary bandwidth, and D-optimal volume is not condition-number optimality. The derivation builds on known order-by-order factorization; literature on weighted Fekete nodes could contain an equivalent full design theorem. Independently audit the algebraic normalization and bibliographic priority before external reliance.

Self-review: passed. Independent audit: not yet performed.
