# Self-review

## Correctness — PASS
The explicit model is taken from Oliveira (2026), Section 8.4. Substituting equal deviations yields the exact cubic–quintic orbit equation \(t(b+3t^2+t^4)=0\). The two-step Jacobian trace and determinant were recomputed from both implicit next-state derivatives; their exact polynomial factorizations give the complete Schur inequalities and show that the nonzero branches are attracting precisely for \(b<(419-39\sqrt{1241})/800\). The central branch is attracting for all negative \(b\). The two exceptional nonregular step parameters are excluded from forward linearization. An exact reduction and an implicit-function argument yield the unequal-deviation branch at the critical point. Symbolic certificates and four sample numerical checks reproduce the identities. The argument concerns local forward branches only, not a global multivalued solution selection.

## Originality — PASS, with historical-priority limits
The closest source, Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1, Section 8.4, supplies the recurrence and local cusp/fold equations, but not the nonlocal attracting threshold or its transverse symmetry-breaking branch. Targeted published-result searches for the same recurrence, both critical parameters, Floquet multiplier \(+1\), two-cycle cusp, and aliases found no equivalent published claim. Results on other cubic maps, replicators, or generic fold/cusp theory do not imply this model-specific exact boundary. Accessible historical results were compared for scientific implication, not merely title match. Unindexed older calculations remain a residual priority risk; a failed search is not a guarantee of absolute novelty.

## Mathematical value — PASS
The original local cusp analysis does not reveal which periodic states are observable as locally attracting forward solutions away from the degenerate point. A sharp global-in-amplitude threshold, the coexistence of at least three sinks, and the unequal-deviation branch crossing identify a concrete and dynamically meaningful change within precisely that motivating recurrence. The algebraic parameter is forced by the transverse multiplier, not an arbitrarily chosen slice invariant: zero bias is the natural reflection-symmetric axis of the source cusp.

## Boundaries and references
The result is not a full orbit census or global basin theorem. A forward step is not locally defined at two specified exceptional parameter values. Its exact algebraic calculation is reproducible using the packaged checker. The source preprint, arXiv:2611.03336v1, was read directly through Section 8.4, and closest indexed results were compared. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
