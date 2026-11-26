# Independent mathematical audit

## correctness

PASS

Normalize to [0,1]. At the midpoint z=(x+y)/2, quadraticity gives W(x)-W(y)=DW(z)(x-y) exactly. The derivative kills constants, so it suffices to test unit step directions. For a step with k right samples in a window the derivative is 2h_k/m², where h_k=(m-k)ΣR_r-kΣL_s. The full packet has h_0=h_m=0. After collapsing repeated endpoint zeros an edge-truncated packet is a consecutive part of the full packet (the text's literal subsequence language omits those repetitions, which do not affect variation). In the sign dual of its variation, the contribution of a pair of sign indices i<j is (R_i-L_{m-j+1})(σ_i-σ_j). For each fixed sign vector, the maximum over all samples is twice the number of opposite-sign pairs: every positive right coefficient can be saturated at one and every positive left coefficient at one, independently. Thus the maximum is 2 floor(m²/4). The balanced-block baseline has h_k=(m-k)min(k,floor(m/2)), rises then falls, and attains that packet variation at n=2m. Interior symmetric secants approach its derivative; appending zeros maintains the full packet. Rescaling restores b-a. The short-length statement is an upper bound only, and sharpness at longer lengths is a supremum. Inspected the proof, VERIFICATION.md and verify_variance.py without executing the script.

## originality

FAIL

Distinct contribution not established relative to verified scope coverage. The separate complete-graph cut result gives the identical upper bound by substituting the bounded-range quadratic pair kernel. Its all-crossing-pairs sharpness proof then gives the matching variance lower bound by a two-level baseline with crossing differences tending to the range endpoint, so the variance theorem is a direct specialization of the broader estimate and its sharpness mechanism. This is an implication comparison against an existing distinct record, not a determination of which same-day record came first.

## value

FAIL

A sharp path-variation coefficient of local variance is a natural invariant, but here both its value and limiting attainment reduce to the existing complete-graph theorem and its constant-crossing-slope witness. There is no separate surviving sharpness issue in the claimed regime: exact constants for truncated packets, a genuinely different boundary condition, or finite-pair attainment are not determined by the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
