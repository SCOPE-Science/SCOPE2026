# Scientific review: entropy boundary layers for random widths of norm balls

## Correctness — PASS

The claim fixes \(d\ge2\), the dual exponents, normalized Euclidean-sphere measure, and **full** projection widths. Hölder duality and strict power means identify all extremizers; near axes, the two competing local terms are \((2/q)\sum|z_i|^q\) and \(-\|z\|_2^2\); near diagonals, the spherical Hessian of the half-width is \((q-2)f_q I\). Tangent-area normalization gives precisely the \(2d/A_d\) and \(2^d/A_d\) factors. The limit as \(q\to2\) is a uniform first variation of the norm, and the logarithmic entropy endpoint follows from \(r^2\log(1/r^2)\), not from a quadratic approximation. The proof supplies the infinite limiting arguments, while the finite checker supplies independent diagnostic tests. The proof and checker agree on all four regimes and on the different order of limits. Independent verification is not claimed.

## Originality — PASS, provisionally

The relevant pre-2016 source Barthe–Guédon–Mendelson–Naor (2005, arXiv:math/0503650) establishes probabilistic geometry of \(\ell_p\)-balls, spherical norm moments and extremal section comparisons, not these fixed-dimensional endpoint probabilities and logarithmic entropy limit. Gorbunov–Vorontsova–Gasnikov (arXiv:1804.03722) addresses expectations and concentration. Kaufmann (2021, doi:10.15559/21-VMSTA182) addresses high-dimensional sharp large deviations, including projection lengths, but with the dimension, rather than the fixed-\(d\) width deficit or exponent distance from \(2\), tending to a limit. The exact connection between widths and dual norms is expressly treated as prior knowledge.

Indexed work on covariance signs of powers of dual-norm widths, singular-curvature chord tails, and entropy first variations of hyperplane-section volumes was also compared. These are adjacent but do not imply the claimed **full fixed-dimensional four-tail classification together with the logarithmic lower endpoint of the near-Euclidean entropy limit**. The nearby indexed research records were available chiefly through their public summaries, so an unindexed or inaccessible equivalent remains a residual priority risk. A negative search result is not proof of novelty.

## Value — PASS

Directional projection widths of norm balls are natural geometric observables. The four-case theorem determines exact rare-viewing probabilities and distinguishes the nonquadratic coordinate-contact exponent for \(p>2\) from quadratic diagonal contact. The Euclidean limit is singular rather than a trivial interpolation: its lower-tail probability acquires a logarithmic correction that is not uniform in the fixed-\(p\) extreme-width limit. These coefficients also determine the sharp number of independent random viewing directions required to observe widths within a given absolute tolerance of the optimum, using the identity \(\Pr\{\min_{j\le N}W_j>W_{\min}+\varepsilon\}=(1-F(\varepsilon))^N\). The matching tangent-ball marks explain the geometric source of each constant. It is a complete natural classification rather than an arbitrary sample of exponents.

## Closest literature and limitations

The claims are fixed-dimensional; do not infer a dimension-uniform limit or an all-scale joint \(p\to2\), \(\varepsilon\to0\) crossover. The endpoints \(p=1,\infty\) require separate arguments. The evaluated primary literature does not certify global historical novelty. Numerical diagnostics are not proof; proof details appear in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
