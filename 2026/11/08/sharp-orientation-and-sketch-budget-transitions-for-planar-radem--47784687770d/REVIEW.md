# Scientific review

## Correctness — PASS
For each nonzero probe the Nyström residual is a positive-semidefinite rank-one matrix. Cayley–Hamilton gives its exact trace from a Rayleigh denominator. Rademacher signs have only two projective directions, making the best-of-\(m\) law an exact two-point order statistic. Strict convexity gives the global orientation maximum; the circle integral gives the Gaussian baseline. Finite independent exact-rational and direct matrix checks pass (33,062 assertions). The infinite-parameter claims are proved analytically, not inferred from finite tests.

## Originality — PASS, qualified
The closest checked literature is Saibaba–Międlar (2023), Sections 1–3 and Appendix D, and Dereziński–Liang–Liao–Mahoney (2020), Introduction and Theorem 1. The former gives non-Gaussian Nyström sufficient conditions for multi-column sketches and the latter gives approximate high-stable-rank expected-projection expressions. Neither inspected result explicitly gives the exact planar best-of-independent-singletons rotation minimax law, its sharp maximizer exchange, or the precise \(m\)-versus-\(\kappa\) Gaussian-comparison boundary. A specialist exact-example precedent cannot be excluded by searches and remains the principal risk. A previously established Gaussian rank-one planar formula is used only as a comparison, not presented as a separate novelty.

## Value — PASS
Rademacher and Gaussian sketches are often compared as alternatives, while small sketch budgets can be strongly orientation dependent. The exact worst-case performance and minimal number of independent singletons required to match one Gaussian's expected error provide a complete natural numerical-linear-algebra benchmark, clarifying the finite-size limits of approximate distribution universality. The result is deliberately restricted to the smallest nontrivial SPD dimension and does not claim a better total matvec cost.

## Boundaries
All arithmetic and random probes are exact; the method keeps one candidate, not all candidate columns. The expectation is of the unsquared residual norm. High-dimensional, finite-precision, cost-equivalent and squared-error extensions are unproved. Publication precedence is not exhaustively certified.

Self-review: passed. Independent audit: not yet performed.
