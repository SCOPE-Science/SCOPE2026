# Scientific review

## Correctness
**PASS.** The search-line coordinate solves the exact exponential ODE \(\dot u=-2\gamma\lambda u\). Equal-magnitude opposite Hessian eigenvalues reduce the position coefficient matrix to a scalar plus a skew matrix, giving an exact integral of the squared norm. Its logarithmic derivative has one sign change precisely when \(|u_0|>1\), proving the unique peak, its height, its first return time, and the global basin and exceptional wrong eigenline. The supplied executable checks exact symbolic identities and 192 directly integrated initial-value configurations. Numerical tests are supporting evidence only; the proof covers all parameters in the domain.

## Originality
**PASS within examined evidence.** The primary Shi–Zhang–Zheng–Zhu source establishes asymptotic stability only subject to local initialization bounds. The original E–Zhou paper introduces coupled gentlest ascent but does not state the hyperbolic-secant trajectory or global amplification classification. The Bofill–Quapp–Caballero nonlinear examples discuss turning curves, while Chu–Lin investigates generalized search geometry and convergence; neither gives this quantitative balanced-quadratic pulse. Actual targeted published-record and literature searches found no equal-or-stronger statement. Residual risk: a less-indexed exact solution in older optimization/chemical-dynamics work may exist.

## Mathematical value
**PASS.** Initial eigendirection error is a central practical constraint in saddle search. This exact solvable canonical model shows that almost every search-line initialization converges even though worst-case transient position amplification is unbounded, and quantifies its sharp exponent, the full pulse and recovery times, and an exact heavy-tailed random-initialization law with an infinite-mean threshold. That separation between global attraction and transient behavior is not supplied by local asymptotic stability rates. The exact equal-curvature assumption is material; this is not a general nonlinear potential theorem.

## Closest literature and limitations
See the four cited primary works in `RESULT.md`, especially the 2026 coupled theorem and the original 2011 construction. Only the balanced planar quadratic and unaccelerated coupled flow are proved. Priorities outside examined works remain a possible risk. Computational checks are not exhaustive.

Self-review: passed. Independent audit: not yet performed.
