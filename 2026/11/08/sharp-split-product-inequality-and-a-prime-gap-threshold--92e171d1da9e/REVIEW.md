# Independent mathematical audit

## correctness

PASS

Separation forces at least one surplus small factor. Pair the other small factors in increasing order with V: the positive integer displacements have total D=T−d≤T−1 for surplus sum T, and D≥G even when G and x are real. For one surplus t, the finite product inequality ∏(1−z_j)≥1−Σz_j, with z_j=Δ_j/v_j and v_j≥t+G, gives t(d+G)/(t+G)>(d+G)/2. For at least two, if m is the largest surplus factor then all paired small factors are ≥m+1; Bernoulli bounds the denominator distortion by (1+1/(m+1))^(T−1). The two- and three-surplus reductions are exhaustive: at fixed other inputs their left sides increase with m; the derivative of log of the right side is strictly less than (3−s)/((m+1)(m+2)) with s the sum of those inputs, in the ranges where this monotonicity is used. The other ranges follow from the displayed e, e², e³ bounds. My independent exact script verified 6 two-factor and 24 three-factor strict integer cross-multiplications and all 15 exceptional compositions, with maxima 2,21/10,21/10,2 by length. Replay: python3 /workspace/branches/review4_exact_cases.py. Appending a new largest factor w preserves the normalized lower bound since the multiplier exceeds wT/(e(T+w))≥45/(14e)>1. The t,t+1 versus 2t example obeys all hypotheses and approaches 1/2. For the prime corollary x>d ensures A lies in the prefix; any alternative with outside primes loses by the split-set inequality and any alternative without them loses by uniqueness of the product minimizer. Optimality is for integer sets, not for prime-only thresholds.

## originality

PASS

The closest distinct source has the same comparison structure and unique-maximizer application but only the coefficient 2/e³ and a weaker sufficient gap. The sharp coefficient and consequent stronger sufficient condition survive inspection of the closest primary and Resultary claims; the qualitative unboundedness theorem is not credited to this record.

## value

PASS

The constant is the optimal universal coefficient in a quantitative exchange step that already has a concrete use in distinct-prime partition optimization. The proof covers every separated distinct-integer configuration, not just the limiting two-versus-one mechanism. It removes more than a factor of five from the stated sufficient prime gap while preserving the optimizer classification; it does not claim a new qualitative prime-discrepancy theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
