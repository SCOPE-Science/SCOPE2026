# Scientific review

## Correctness
PASS. The Hardy-orbit decomposition and Szegő Cauchy determinant give the exact finite objective. Identity (7) gives a global, not local, reflection reduction using \(AC\ge b^2\); log differentiation then yields a strictly increasing-versus-decreasing equation and the unique maximizer. Substituting \(\epsilon=1-r^2\) and \(\delta=\sin^2\theta_*\) into this exact equation yields the sharp quarter-power boundary law. The code independently tests finite identities and examples, but is not used in lieu of these continuous arguments.

## Originality
PASS relative to inspected sources. Aguilera–Carando [1] proves existence of orbit frames and gives orthonormal generators, not determinant designs of three raw kernels with constrained nonidentical moduli. The closest public result [2] optimizes all points on **one common circle**; its full RESULT.md explicitly excludes mixed radii. The new global mixed-radius optimizer and quarter-power collapse are not implications of that equiradial statement. Searches covered pseudohyperbolic Fekete problems, unequal-radius Szegő Gram determinants, prescribed-modulus node placement, and quarter-power boundary clustering. No known exact same-domain implication was found; unindexed classical Fekete theory is the main residual risk.

## Value
PASS. This solves the natural first non-equiradial D-optimal design for unorthogonalized orbit generators of a finite Blaschke multiplier. It determines all maximizing configurations, an explicit reproducible scalar equation, and a counterintuitive quarter-power clustering regime near the unit circle. The result is about a geometrically constrained infinite Riesz basis, not an arbitrary finite matrix slice.

## Limits and closest literature
The optimization is determinant-only and restricted to the three radii \((r,r,s)\); larger mixed-radius designs and frame condition-number optimization are not settled. The Cauchy determinant and orbit decomposition are established ingredients. Relevant sources are [1] A. Aguilera and D. Carando, arXiv:2606.00912v1 (30 May 2026); [2] *Sharp determinant stability and conditioning of concentric Szegő orbit frames* (public mathematical record, 11 October 2026); [3] T. Karvonen, S. Särkkä and K. Tanaka, arXiv:1912.07316.

Self-review: passed. Independent audit: not yet performed.
