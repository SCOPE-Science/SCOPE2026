# Scientific review

## Correctness — PASS
The statement fixes an exact planar two-branch affine map, a fixed incoming point, and a fixed outgoing threshold. The left scalar recurrence is proved using the actual initial second-coordinate value, not a spurious fixed branch: its dominant stable multiplier gives the logarithmic incoming passage, and its Jordan collision produces an additional \(n t^n\) factor and a \(\log\log(1/\mu)\) correction. At the first switching index both adjacent coordinates are \(O(\mu)\). Strict positive-coordinate monotonicity after crossing ensures that no right-branch formula is applied incorrectly. The right expanding multiplier then gives the second logarithmic contribution with an \(O(1)\) remainder. Exact rational arithmetic checks from the provided standalone checker passed for eight parameter/forcing combinations, but the proof, not the finite experiment, carries the universal quantifiers.

## Originality — PASS within inspected evidence
Simpson's *Nonsmooth folds as tipping points*, arXiv:2406.04587v1, equation (3.6) and theorem 1, establishes divergence on the virtual-fixed-point side of the fold. The previous recoverable local analysis establishes an \(O(\mu^{-1})\) first-exit bound for a more general feedback map. Both are credited; neither supplies the logarithmic first-passage coefficients or the defect-induced logarithmic–logarithmic term. The retrieved same-subject zero-determinant normal-form paper does not overlap the strict positive-determinant domain. Related Lyapunov scaling and repeated-unit-eigenvalue results study different observables and spectral conditions. Some comparisons relied on abstracts rather than complete full text, and unindexed equivalent results remain possible; publication priority is not independently established.

## Mathematical value — PASS
The natural geometric question is how long a trajectory resides near the virtual fixed points following a nonsmooth-fold tipping event. The result supplies a sharp physically iterated time and separates an open region of simple contracting spectra from a codimension-one defective spectrum, where a new universal \(\log\log(1/\mu)\) clock correction appears. This is not a finite numerical improvement to a bound: it identifies a qualitative change in the asymptotic structure of a two-dimensional transport passage and traces it to the Jordan-block transient.

## Scope and residual limits
The theorem is exact for \(0<\alpha<1\), \(h>0\), and \(0<\delta\le(1-\sqrt\alpha)^2\) with fixed initial point \((-h,0)\) and small positive \(\mu\). It makes no claim for a changing section, oscillatory left multipliers, a nonlinear perturbation, a uniform approach to the damping boundary, or a convergent constant in the \(O(1)\) remainder. The inaccessible complete text of a related 2014 repeated-unit-multiplier work is a limited bibliographic risk, not evidence of coverage.

Self-review: passed. Independent audit: not yet performed.
