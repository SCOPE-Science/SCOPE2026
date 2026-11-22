# Scientific review

## Correctness — PASS
For all \(n\le2\), KKT reduction to the sole inactive-coordinate test \(c\max(b_2,0)/(d+t)-b_1\ge0\) proves an endpoint interval because its derivative has constant sign. In the three-dimensional example, positive leading minors prove strict convexity; the exact inverse has first component \((t-1/2)(t-1)/D(t)\) and the remaining two components stay positive. On the interval where the first coordinate vanishes, the explicit boundary solution has nonnegative reduced gradient and satisfies complementary slackness. A separate exact symbolic script reconstructs the algebra and enumerates all supports at nine rational parameters. Finite computations do not substitute for these analytic arguments. The strict signs at three parameter values also prove robustness, while the spectral eigenvalue formula proves strict condition-number improvement.

## Originality — PASS, qualified
The 2026 nonnegative conjugate-gradients work solves fixed-parameter nonnegative quadratics and analyzes spectral regularization, but it does not classify coordinate support through a ridge parameter sweep. The 2002 and 2004 nonnegative Tikhonov papers supply numerical methods without the two-versus-three coordinate phase boundary. Nearby mathematical-record results concern ridge sketch preconditioning, fixed-step Gauss–Newton contraction, or transient active-face identification, none of which implies this constrained optimizer support statement. Conventional \(\ell_1\)-path entry/exit results use a different penalty. Searches cannot exclude unindexed examples, unpublished observations, or equivalent formulas hidden in broader complementarity literature.

## Value — PASS
A dimension-minimal, robust loss-and-regain counterexample is a concrete obstruction to reusing a supposedly nested active set during nonnegative ridge continuation. The phenomenon survives positive forcing and occurs during strictly improving spectral conditioning; the two-dimensional theorem identifies exactly when nesting really is guaranteed. The complete finite-dimensional classification and closed rational transition values are more informative than a single numerical warning.

## Scope and residual risks
No all-dimensional classification is claimed, and the problem's mixed-sign off-diagonal matrix may not represent every application-specific positivity structure. A literature-index search and substantial comparisons cannot establish priority conclusively; independent validation has not yet been performed.

Self-review: passed. Independent audit: not yet performed.
