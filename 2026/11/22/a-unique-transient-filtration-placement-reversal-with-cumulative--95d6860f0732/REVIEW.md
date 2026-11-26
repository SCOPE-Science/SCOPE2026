# Independent mathematical audit

## correctness

PASS

With x=s+v, the filter-placement cofactors differ by (x+2k)(x+k)−k²−(x+k)²=kx; the end-to-end inverse numerator is k² in both cases. Thus the transform of Δ=f₂−f₁ is pk³(s+v)/(D₁D₂). Removing uniform loss multiplies both impulse responses by e^{vt}; use H equal to the convolution of six one-sided exponentials at the positive eigenvalues of M_j−vI (positivity follows from the path energy and one pinned vertex). The transform then gives Δ=pk³e^{−vt}H′. Convolution preserves log-concavity; H is positive and analytic for t>0 by the finite exponential-polynomial inversion, also for repeated eigenvalues. Its log derivative is strictly decreasing: equality at two times forces an affine log on an interval and hence everywhere, impossible since H∼t⁵/5! at zero. Because H vanishes at zero and infinity, it has exactly one maximum, and H′ changes sign there from positive to negative; this also shows why uniform v does not alter the crossing time. Integrating by parts gives pk³[e^{−vT}H(T)+v∫₀ᵀe^{−vt}H(t)dt]>0 at finite T, equivalent to the stated constant-source step response. Its infinite limit is pk³v/(D₁(0)D₂(0)), so the limit ties exactly when v=0. On a two-room path reflection interchanges end placements and transpose symmetry preserves end-to-end response, giving a tie. An independent high-precision reconstruction from eigenvector products reproduced the crossing near 6.88786993360507954, the signs at times 1 and 8, and dose difference 1/156.

## originality

PASS

The closest distinct indexed result gives the same three-room determinant for arbitrary divisible sinks at steady state; this covers the forward resolvent and the infinite-horizon comparison by specialization, not the transient order. The novel claim supported by the comparisons is the universal exactly-once pointwise reversal together with the all-finite-horizon cumulative ordering. The two-room reflection tie and the use of a standard log-concavity preservation theorem are supporting ingredients, not independent originality claims. The closest application-literature full text was not accessible, which limits the priority conclusion without constituting contrary evidence.

## value

PASS

The result distinguishes two natural decisions about remote exposure: the instantaneous preferred placement reverses once, yet the cumulative ranking never reverses at a finite horizon. This is a substantive contrast, not just a transfer-function identity or one numerical reversal. The smallest path supporting the effect is motivated by exact endpoint symmetry in two rooms, and the result works uniformly in the three free physical parameters within the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
