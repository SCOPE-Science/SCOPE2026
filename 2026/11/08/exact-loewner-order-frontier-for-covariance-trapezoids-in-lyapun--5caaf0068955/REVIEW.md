# Scientific assessment

## Correctness — PASS

The constant-input specialization is derived from the explicit IF-SSPRK2 tableau of Zhang–Lan–Jing, Eq. (5). An entrywise Peano-kernel identity reduces stepwise Loewner overestimation to positivity of the second-congruence derivative. Rank-one forcing and the maximal-cyclic-vector lemma force a quadratic annihilating polynomial; an explicit two-by-two determinant condition yields the necessary and sufficient \(4a\ge b^2\) criterion. An exact completion-of-squares identity establishes sufficiency, including the equality boundary. The Hurwitz corollary follows from the roots of the quadratic. `verify.py` performs exact-rational checks and supplementary finite numerical tests. The proof, not the tests, establishes the quantified claims.

## Originality — PASS, with literature limitations

The closely relevant 2026 source proves positive semidefinite **output** and a norm-error estimate, not a one-sided comparison of output with the exact integral, nor a classification of the drift. Dieci–Eirola (1994) preserve positivity for different numerical constructions; Koskela–Mena (2017) compare solutions for different data rather than quadrature and exact solution with identical data. Searches for Loewner order of Lyapunov trapezoids, exponential-congruence convexity, and quadratic minimal-polynomial criteria identified no dominating theorem. The potentially relevant 1996 Dieci–Eirola monotonicity paper could only be compared at bibliographic level, so historical priority remains a material risk; no claim of independent novelty certification is made.

## Mathematical value — PASS

The question concerns reliable **one-sided covariance bounds**, stronger than positive-semidefinite numerical output, in an integrating-factor integrator designed for covariance/Lyapunov evolution. The theorem gives a complete, dimension-free structural classification, a sharp stable-drift impossibility result, a rank-one counterexample at every sufficiently small step, and a meshwise consequence in the positive cases. The square-zero exceptional family and the stable anisotropic obstruction distinguish this from a routine scalar quadrature observation. It does not establish comparable results for nonlinear or time-varying forcing.

Self-review: passed. Independent audit: not yet performed.
