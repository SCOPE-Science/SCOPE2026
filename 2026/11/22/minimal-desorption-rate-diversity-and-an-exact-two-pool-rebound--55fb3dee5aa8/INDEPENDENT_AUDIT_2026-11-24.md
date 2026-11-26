# Independent mathematical audit

## correctness

PASS

Summing pool inventories and uptake within each equal-desorption class gives a closed system of size m+1 without losing any information in C(t). With the positive scaling T=diag(1,√(a_b/b)), T⁻¹MT is the symmetric arrowhead Q with zᵀQz=−vz₀²−Σ_b(√a_b z₀−√b z_b)². Thus it is negative definite. Repeated eigenvalues would permit an eigenvector with no air coordinate; distinct pool diagonals force such a vector to be supported on at most one pool, and its nonzero air coupling rules it out. The finite sum for C′ has at most m zeros counted with multiplicity by Rolle induction; the dominant coefficient of C is strictly positive by positivity of the Perron eigenvectors and the nonnegative nonzero initial state (m=0 is just one decaying mode). Therefore C′ is eventually negative. The initial and eventual negative signs mean each positive component uses two endpoint incidences; if two positive components share an endpoint, its zero has even order at least two, so the multiplicity count still applies to the headline bound. In the two-pool case the reduced derivative bracket −p+qu−ru^κ has negative endpoints. Convexity when r≤0, or monotonicity when q≤0<r, excludes an increase; otherwise strict concavity gives the stated interior maximum and threshold, with equality giving a tangency only when the interior conditions hold. For the witness, K=10M has characteristic polynomial X³+14X²+32X+10. The air moments s_j=e₁ᵀKʲx₀ start (2,−1,20) and satisfy its recurrence. An independent exact rational evaluation of Σ_{j=0}^N s_{j+1}t^j/(10^{j+1}j!) gave P₁₀(1)=138133084986931/22680000000000000 and an error bound 1977326743/245953125000000 using the geometric tail bound for x=7t/5, namely 7x^(N+1)/[(N+1)!(1−x/(N+2))]. At t=5, N=40 gives P≈−0.017612582204117346 with an exact rational bound less than 1.12·10⁻¹⁴. Exact comparisons certify the signs −,+,− at 0,1,5; the zero count gives exactly one rebound, not just sampled nonmonotonicity.

## originality

PASS

Reversible storage equations, exponential mode decompositions, and the Chebyshev zero bound are known ingredients. The supported quantitative distinction is the autonomous star's exact desorption-class bound with a sharp two-class onset, the necessary-and-sufficient three-mode test, and a certified witness with positive rates and admissible initial loads. The strongest inspected model antecedent includes independent storage media and many decay modes but does not give that shape classification in the relevant passages. The inspected two-sink empirical model is layered, not a two-pool star. This comparison does not claim priority for storage models or prove exhaustive novelty.

## value

PASS

For post-emission model interpretation, duplicating storage compartments at the same release rate cannot account for the observed shape, while heterogeneous stored inventories can. This is a motivated exact minimality result: the positive-rate rational witness proves genuine feasibility, and the phase threshold distinguishes parameter and initial-state regimes rather than merely observing a numerical peak. This can serve as a benchmark for diagnosing modeled transients without assuming a second source pulse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
