# Independent mathematical audit

## correctness

PASS

For b=1 the normalized entry is already a sign divided by sqrt(m); for b=2 the four equally likely signed coordinate vectors rotate under the normalized Hadamard to the four equally likely sign pairs, each with coordinate size 1/sqrt(m). Since the draw is independent per block and column, the concatenated rotated matrix is iid dense Rademacher and the Gram identity holds on this coupling. For n≥2, the inner product of two unit columns is Σ_j(b_j/m)X_j, where X_j is 0 for a noncollision and ±1 each with probability 1/(2b_j). The positive weights sum to one, so its magnitude is one iff every block has the same nonzero collision sign. Rank failure therefore has probability 2∏_j(2b_j)^−1; dense rank failure is 2^(1−m). The ratio factors into 2^(b_j−1)/b_j, each at least one with equality only at 1 or 2. The event is Gram-measurable. Counting one nonzero per block yields the stated minimal count with a width-one block for odd m. For n=1 the necessity fails, as expected and excluded by the original quantifiers.

## originality

FAIL

The earlier indexed theorem 893b68c79546 gives the same exact iff, deterministic Hadamard, and whole-Gram consequences for equal widths. The mixed-width extension is not identical wording, but it is a mechanical blockwise consequence of the prior proof. Apply its coupling separately to each 1- or 2-block at scale sqrt(b_j/m). For necessity, its one-block fourth-moment gap with ζ=1, rescaled and added using independence and equal block variances, yields ΔE[C^4]=m^−4 Σ_j b_j(b_j−1)(b_j−2), which is positive exactly when a block has b_j≥3. The alternative collapse formula is an endpoint probability of the very same prior explicit signed-collision law: all block collisions must take the same sign. The ceiling minimum and odd-row case follow immediately by counting and packing the already covered blocks. This is demonstrated precise coverage and implication, not an inference about who discovered the result first from a catalogue date.

## value

FAIL

The equal-width exact equivalence is a useful embedding fact, but it is already covered. In the new presentation the only remaining changes are the immediate independent-block composition, the elementary product at the two endpoints of that already specified collision law, and one-versus-two block packing for odd size. As scoped, there is no separately motivated nonmechanical threshold, new sketch design problem, or unknown exact statistic beyond those consequences to justify a surviving valuable repair. This does not detract from the correctness of the proof or from the previously known classification's utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
