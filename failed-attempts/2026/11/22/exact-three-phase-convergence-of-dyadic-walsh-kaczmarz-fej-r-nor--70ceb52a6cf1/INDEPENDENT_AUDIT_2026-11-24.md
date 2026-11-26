# Independent mathematical audit

## correctness

PASS

The Finding is correct with the stated normalization. The Walsh transform of the weight N−2ʲ−k on block j has support on the zero and one-bit prefixes, so cells with first two one-bits a<b have no later contribution. Summing gives 3A_N/2ᵃ=3·2ᵃ−2^(2(b−a)−1)−1. For a≥1 the expression is strictly negative exactly when 2(b−a)−1≥a+2; for a=0, b=1 the expression is zero and for b≥2 it is negative. This yields the stated strict threshold. Each cell has measure 2^(−b−1), and the kernel has integral one, so its absolute integral is one plus twice its negative mass. Independent symbolic summation checked the all-m≥1 phase expressions and direct weighted character sums checked n=1,…,9. The frozen proof's intermediate evaluation ∑_{b=2}^{n−1}2ᵇ=2ⁿ−4 only holds for n≥2, not n=1. At n=1 the two kernel values are 3/2 and 1/2, so L₁=1 and the stated m=0 formula separately gives deficit 1/3; n=2 also gives L₂=1. Thus the written derivation needs this boundary qualification, but the Finding itself holds. Positive phase limits give the asserted sharp uniform exponent.

## originality

FAIL

Blahota's accessible July 2026 full text gives an exact dyadic norm representation and exactly the mod-three summands needed to obtain all three displayed formulas. The difference is an elementary geometric summation, not the derivation of a new quantitative invariant. This goes beyond the qualitative overlap acknowledged in the frozen record.

## value

FAIL

A three-phase law would be informative if the qualitative limit were all that was known. Here the precise phase behavior is obtained by summing the prior explicit geometric terms; independent verification and a more compact presentation add no distinct scientific result. Correcting the n=1 proof boundary would not repair this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
