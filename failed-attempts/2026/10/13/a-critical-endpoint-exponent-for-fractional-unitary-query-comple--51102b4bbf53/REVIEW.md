# Independent mathematical audit

## correctness

PASS

The cited bound is Appendix D.2 Eq. (D21) of arXiv:2610.01940v1, before restricting t away from the endpoints. The same model and uniform error convention apply. The degree/jump reduction can also be checked on H=diag(δ,δ+θ) for 0≤θ<2π−δ: starting from |+⟩, twice the output coherence is a Laurent polynomial P of degree at most 2N after N controlled forward/inverse queries, and trace-norm control of the output bounds |P(θ)−e^{itθ}| by ε. The shifted difference P(θ+δ)−e^{itδ}P(θ) is bounded by 2ε on the arc of length 2π−2δ (endpoints by continuity); at 2π−δ periodicity makes its magnitude at least 2sin(πt)−2ε. The trigonometric Remez bound used in the source has factor T_{4N}(sec(δ/2))≤exp(4Nδ) for 0<δ<1; a complex polynomial can be handled by rotating its maximum to the real axis and taking the real part. This recovers the recorded lower bound in its positive regime. The universal Theorem 1 upper bound has no fixed-endpoint restriction. For both scalings the sine term is πcε^α(1+O(ε^{2α})); the bracket in D21 is (1−α)log(1/ε)+log(πc/4)+O(ε^{2α}), independently of δ. Near an endpoint the relevant unitary has spectral arc length at most (2π−δ)min(t,1−t); centering it gives channel error at most four times the sine of one-quarter of that arc length. For α>1 this is o(ε), giving zero queries near zero and at most one near one. The critical scaling and exact optimality near one are not claimed.

## originality

FAIL

The endpoint exponent law is mechanically implied by the same-model bounds and endpoint discussion already published in arXiv:2610.01940v1. The precise α wording is not stated there, but substituting min(t,1−t)=cε^α in D21 and its universal upper bound gives the entire logarithmic branch, while its stated O(min(t,1−t)) approximation already gives the other branch. The elementary centering constant does not change the law or resolve the critical crossover.

## value

FAIL

The statement is a useful explanatory reading of prior bounds, but its two regimes follow by the same elementary substitution and little-o comparison already made available by the anchor. No nontrivial crossover threshold, uniform adaptive upper construction, or independent endpoint classification beyond those bounds is established. Clarification alone is not a distinct scientific finding here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
