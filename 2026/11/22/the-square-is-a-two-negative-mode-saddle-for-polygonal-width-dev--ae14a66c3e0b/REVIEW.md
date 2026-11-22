# Self-review

## Correctness — PASS

A complete local similarity gauge reduces all nearby labeled convex quadrilaterals to four parameters; the exact Akiyama–Kamae edge-pair width kernel is expanded through quadratic order. Opposite-edge contributions are uniformly cubic, not improperly omitted constants. The resulting exact perimeter and second-moment Hessians give two strictly positive and two strictly negative eigenvalues. Both the analytic identity and an independent 56-shape direction-by-direction projection quadrature are checked with the extracted `verify.py`. Limit: this establishes only local second-order behavior; sign statements on the quadratic cone are deliberately excluded.

## Originality — PASS, with historical priority risk

Akiyama–Kamae (2022) establishes the width-deviation kernel and poses the four-sided global optimization problem but does not give the four-dimensional square Hessian in its inspected full text. Two published parallelogram-width reconstruction studies establish formulas and positive comparisons only on the centrally symmetric submanifold and cannot imply the two strictly negative transverse eigenvalues. Exact phrasing and mathematical implications, including aliases such as projection-length variance and squared coefficient of variation, were compared with literature, indexed mathematical findings and accessible prior claims. Unindexed later local analyses may exist; this is not a claim of unique global priority.

## Mathematical value — PASS

The open all-quadrilateral deviation problem has a canonical candidate, the square; the exact local Morse index, decomposed by central symmetry, rules it out as even a local minimum and identifies a sharp quadratic perturbation threshold in the full shape-moduli space. This is a motivated, structural stability classification, not merely one numerical counterexample, a reparameterization or a claim to solve the global optimizer. The previously known parallelogram minimum is only context.

Self-review: passed. Independent audit: not yet performed.
