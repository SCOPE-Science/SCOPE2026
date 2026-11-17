# Self-review

## Correctness — PASS

The theorem concerns all bi-infinite real data with finite discrete variation and the precisely defined conservative affine-exact two-secant slope class. The Hermite derivative is a Bernstein-nonnegative quadratic (with its sign reversed for decreasing cells), hence each output has variation equal to sampled variation. A finite one-secant decrement forces both neighboring knot slopes to change by at least the decrement for every admissible limiter; each neighboring cubic bump has variation \(8/27\), while the central cell has at least one decrement of variation. This proves the universal lower bound. For minmod, differentiating along a data segment produces a selector with local coefficients in \([0,1]\); the central perturbation kernel is a convex combination of four nonnegative unit-integral kernels, while each side contributes at most \(8/27\). The explicit finite-support witness attains \(43/27\). The standalone exact-identity and random-rational checker passed.

## Originality — PASS (qualified)

Hyman's 1982 report, Williamson–Rasch's 1987 full text and Edelman–Micchelli's 1987 scanned article were inspected for the relevant slope constraints, interpolation representations and competing stronger statements. They address construction, slope admissibility, qualitative data sensitivity and approximation accuracy, not the exact global two-input variation minimax optimization stated here. The closest previously recorded harmonic-mean cubic Hermite result has coefficient \(59/27\) for a selector outside this unit-capped class and does not imply the present universal optimum. Targeted published-record and scholarly searches for the formula, minmod aliases and norm equivalents found no covering record. An unindexed equivalent remains a real historical risk; negative retrieval is not itself a novelty proof.

## Mathematical value — PASS

This proves an operator-class **impossibility-and-attainability** statement, not merely another constant for a fixed cubic. It identifies a sharp quantitative cost of combining exact affine reproduction with conservative shape constraints: every method in the class preserves variation of each signal yet must amplify some two-data perturbation by at least \(43/27\); the simple minmod rule is provably minimax. Such perturbation stability is relevant when sampling data are noisy or updated. The one-input vs two-input distinction cannot be read from ordinary monotonicity tests and the class theorem does not follow from the harmonic-mean case.

## Limits and closest literature

The conservative unit cap is essential; the result does not claim global minimax among all monotone cubic schemes, minmod uniqueness, or mesh-independent extension to nonuniform knots. The archival Hyman document's exact original day of public circulation is not independently known; the recorded source date refers to its explicitly day-verified online publication. Primary paper material inspected was not independently audited.

Self-review: passed. Independent audit: not yet performed.
