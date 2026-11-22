# Review: a minimal driven-reaction covariance sign transition

## Correctness — PASS
The four-state generator is specified with every transition rate. Direct symbolic reconstruction confirms its unique stationary probability vector, the exact covariance numerator and strictly positive denominator for all \(0<t\leq1\), \(r\geq0\). All nonconstant powers of the relevant polynomial have nonnegative coefficients and the positive-degree part is strictly increasing; its sign at zero decides whether there is exactly one positive crossing. Boundary limits and the opening slope follow from substitution and the implicit function theorem. The standalone symbolic checker replayed successfully; its finite tests are not an all-domain proof.

## Originality — PASS, qualified
The initiating 2026 article explicitly calls for systematic study of the connected nearest-neighbor correlation across stationary regimes; it supplies the bond birth/death mechanism, but develops large-lattice mean field and Monte Carlo findings, not the specified two-site sign diagram. The established exact pure TASEP correlation literature omits these reactions; the 2003 exclusion-plus-Langmuir work attaches/detaches particles without the same occupied-pair requirement. Earlier closely related results for resetting exclusion systems and other mass-exchange models concern different generators. An implicit same-generator finite-state computation cannot be excluded from all literature, and independent priority assessment is outstanding.

## Value — PASS
A nearest-neighbor correlation is exactly the correction that obstructs mean-field closure in the motivating physical model. The complete two-parameter minimal-bond classification distinguishes always-positive association from a unique negative-to-positive reaction-induced reversal, locating its sharp boundary at equal injection/extraction rate \(t=1/2\), and gives a definite test case for correlation-sensitive finite-size approximations. This is not evidence of corresponding macroscopic phase transitions.

## Closest literature and limitations
Chatterjee–Goswami–Mukherjee, arXiv:2611.06463v1 (2026); Derrida–Evans, J. Phys. I France 3 (1993), DOI 10.1051/jp1:1993132; Juhász–Santen, arXiv:cond-mat/0311208 (2003). This result does not treat unequal boundary rates, longer chains, hydrodynamic limits, or the special rate-normalization conventions of particular simulations.

Self-review: passed. Independent audit: not yet performed.
