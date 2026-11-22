# Scientific assessment

## Correctness — PASS

Complex scalarization of the normal planar generator gives an exact sixth-degree polynomial. The curvature identity is verified from the polynomial, and the subcritical interval is controlled by an exact positive sum-of-squares decomposition. For larger scaled steps, the sign of curvature is equivalent to a one-variable rational bound with a unique maximizer, proved by a shifted-quintic sign rule. Strict Jensen and local strict concavity supply both logical directions. A rational two-atom example is checked exactly. The standalone verifier replayed successfully. No finite sampling is used as a global proof.

## Originality — PASS (best-knowledge comparison)

Inspected work on irregular-field randomized RK (Kruse–Wu, arXiv:1701.03444), deterministically stabilized RK (Sun–Shu, arXiv:1912.11596), and fixed-step random-stage RK (Bochacik et al., arXiv:2006.12131). These study different randomness or stability quantities and do not yield a universal fixed-mean curvature transition for the ordinary degree-three stability polynomial. A public indexed RK2 energy frontier is likewise not this assertion. Related primary literature could contain a hidden equivalent convex-order formulation, so priority is not independently established.

## Value — PASS

The theorem gives an exact frequency-to-damping boundary separating strict deterministic superiority under **all** fixed-mean timestep laws from a genuine randomized improvement regime, and identifies the first of the three standard explicit Taylor RK orders exhibiting this behavior. This is a structural numerical-stability question motivated by timestep variability under stochastic or adaptive integration. It is deliberately limited to single-step numerical energy; fixed-terminal-time accuracy and higher-dimensional nonnormal effects are not claimed.

Self-review: passed. Independent audit: not yet performed.
