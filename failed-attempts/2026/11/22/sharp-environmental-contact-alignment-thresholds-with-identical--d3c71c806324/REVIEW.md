# Independent mathematical audit

## correctness

PASS

The stated block matrix is irreducible and nonnegative (the final diagonal entry is zero), and has a positive Perron vector (z,w). Summing the human coordinates of the eigenvector equation gives (λ−a)Σz_i=Uw, hence λ>a; substitution in the last coordinate gives (λ−a)(λ²−Q)=aUV/n and λ²>Q. Both factors on the left are positive and strictly increasing on the claimed root interval, where the product goes from zero to infinity. Implicit differentiation there gives dλ/dQ=(λ−a)/(λ²−Q+2λ(λ−a))>0. Classical rearrangement therefore gives both extrema; ties are harmless, and comparing assignments with a strict two-pair swap when both lists are nonconstant proves strict separation. For 0<a<1 and Q<1, comparison with λ=1 yields the full trichotomy; if Q≥1 both sides are strictly above one, and if a≥1 the Perron root is strictly above one. Row sums do not depend on the permutation. The exact rational two-group products check the reversal and n=1 has only one assignment. An independent Decimal bisection of the two stated abstract cubics reproduced the quoted decimal roots to their displayed precision. RESULT.md lines 43–76, VERIFICATION.md and check.py were inspected; the packaged 5,090 finite comparisons were not rerun. The conclusion is only about the modeled spectral threshold, not realized epidemic outcomes.

## originality

FAIL

The closest local-score paper does not cover heterogeneous interlayer row sums, but this is not the strongest applicable result. Roberts–Heesterbeek (2003) give the general single-selected-coordinate threshold, including equality, by a resolvent formula. Its specialization to the final block coordinate gives the exact frozen test. Applying it to the scalar-rescaled matrix also gives the cubic determining each Perron root; comparing permutations then reduces directly to classical rearrangement. The minimal rational reversal is a worked instance of this specialization, not a separate obstruction or new invariant. This is mathematical implication from verified prior full text, not a literature-access judgment.

## value

FAIL

The toy model is a natural way to illustrate why row-sum scores are insufficient, but its exact threshold and root are direct reductions of an established threshold invariant. Permutation comparison adds the textbook rearrangement step, and the minimal example is an exact numerical illustration in the first dimension permitting a swap. No independently useful unknown exact fact remains in this frozen formulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
