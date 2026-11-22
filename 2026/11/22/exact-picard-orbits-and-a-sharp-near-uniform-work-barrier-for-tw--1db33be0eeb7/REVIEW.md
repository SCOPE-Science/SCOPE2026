# Scientific review: exact Picard orbits and a sharp near-uniform work barrier

## Correctness — PASS

The claim is confined to the specified two-invariant Gram correction with mean-value gradients and a mass-preserving predictor. Orthogonal elimination of the mass multiplier gives the displayed inversion map; the invariant subspace of the predictor-initialized iterates reduces it to one Möbius recurrence. A Cayley coordinate yields the full orbit without asymptotic approximations. The two nonsingular algebraic branches follow from collinearity and the energy constraint, with the already-feasible predictor and rank-deficient uniform predictor handled separately. The parity-sensitive exact stopping thresholds imply the asserted sharp inverse-radius limit. The finite-step oscillator example follows from the identity for a skew generator restricted to the mean-zero plane.

The supplied checker independently performs exact-rational raw Gram solves and checks the formula and both branches, together with numerical near-singularity limits and the three-evaluation oscillator predictor. Numerical tests are support, not proof; the proof in RESULT.md supplies the quantifiers and limiting argument. The corrector's interim iterates need not conserve energy, and singular starting Gram matrices are explicitly excluded from the positive-radius formula.

## Originality — PASS, with historical-priority qualification

Pu and Ran (2026, arXiv:2605.30827v1), Sections 2 and 4 and Algorithm 1, specify the method and its fixed-point solve. They prove conservation and order properties and give numerical efficiency experiments. The exact Picard orbit, its distant algebraic branch, the sharp fixed-accuracy inner iteration cost, and a finite-step loss of Gram rank in a conservative oscillator were not found in that full-text comparison.

Norton et al. (2013, arXiv:1302.2713v1), Sections 1, 4 and its multiple-integral example, give a much broader projection/discrete-gradient equivalence and local existence results but do not analyze this predictor-initialized map or its cost. Norton and Quispel (2013, arXiv:1301.4717v1), Section 4, give a different linearly implicit quadratic-integral method explicitly designed to avoid nonlinear solves; their result does not imply the particular method's Picard work law. Published mathematical-record searches found adjacent projection and fixed-point results, but no theorem with the same update and threshold. Equivalence with a standard radial projection is acknowledged rather than claimed as new.

Residual risks: fractional-linear iterations are classical; a source outside the consulted corpus may have analyzed this particular correction map. The originality judgment is a comparison of mathematical implications of accessible literature, not proof of universal priority.

## Value — PASS

The finding addresses the actual algorithmic cost of enforcing two physically natural invariants, linear mass and Euclidean energy. It distinguishes a cheap explicit nearest-point correction from the prescribed implicit Picard implementation: the latter can make unbounded intermediate excursions and needs a sharply quantified number of inner steps as a predictor loses its mean-zero component. The bound is realized by a concrete explicit Runge--Kutta predictor for a conservative oscillator, not an arbitrary unmotivated parameter slice. This matters for larger-step implementation, stopping rules and monitoring of Gram conditioning; it does not assert poor behavior for every predictor or suggest that the corrector's asymptotic branch is new.

## Scope and limitations

Results use exact arithmetic, a quadratic invariant, a linear invariant, mean-value discrete gradients and mass-preserving predictors. They do not establish global convergence of an outer method, finite-precision robustness, arbitrary nonlinear multi-invariant behavior, or large-step accuracy of the explicit example. The inner Picard cost can be avoided by direct radial normalization in this special case.

Self-review: passed. Independent audit: not yet performed.
