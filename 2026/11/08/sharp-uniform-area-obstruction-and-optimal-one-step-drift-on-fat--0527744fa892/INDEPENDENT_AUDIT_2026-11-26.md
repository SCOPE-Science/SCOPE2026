# Independent mathematical audit

## correctness

PASS

Since βL=L+1 and L≥2, at least one digit is legal everywhere. All three inverse points (w+q_i)/β exist; the normalized-area transfer density is β^−2 times the sum of the three selection weights. The sets of additional eligible digits at inverse points 0, 1 and 2 are, respectively, {1 if x>1, 2 if y>1}, {0 if x+y<L−1, 2 if y>1}, and {0 if x+y<L−1, 1 if x>1}, away from the partition lines. Thus the origin and upper corner regimes have weights 3−2p and 1+2p on positive-area sets, including at β=3/2. Equality to β² would force p=1/2 and β=√2. At √2, the seven nonempty cells in the frozen order have weights 3−2p, 3, 1+u, 2, 1+t, 1+2p, 1+s. The second cell is a triangle with leg 2−√2, giving positive excess (2−√2)²/[2(1+√2)²]=17−12√2. No other cell contributes positive excess when p=1/2, independent of the triple coin; otherwise the first or sixth adds strictly positive excess. TV of probabilities is the mass of the positive part, and kernel contraction plus the triangle inequality gives the stationary bound, not a sharp stationary distance. The frozen decimal script was inspected, not rerun; the table and radical identity are exact. On the background existence assertion, the 2022 paper states the endpoint for a fair coin only. Its proof method extends to biased p: at β=3/2 the triple cell is a singleton of zero area, and the least- and greatest-admissible maps with constant probabilities p and 1−p represent the position kernel a.e. For any fixed n the common itinerary refinement consists of finitely many convex polygonal interiors; all boundary lines are horizontal, vertical or slope −1 since every branch is a positive dilation and translation. Their minimum corner angle is uniformly bounded below by π/4, giving the uniform positive angular parameter a in the paper's Theorem 5.1, while the minimum segment length δ_n is positive for each finite refinement. The n-step branch probabilities sum to one and every inverse derivative is β^−n times the identity, so c_n in that inequality can be taken 2β^−n for n large. A block iterate has variation coefficient c_n(1+1/a)<1. Its Cesàro averages of normalized area have uniformly bounded BV norm and an L¹-convergent subsequence by BV compactness. The limit is fixed for the block iterate by L¹ contraction, and averaging its first n one-step iterates yields a one-step AC stationary law. This establishes the background existence at the endpoint without attributing biased-coin coverage to Remark 5.8.

## originality

PASS

The model and AC-existence machinery are prior work. The distinct verified claim is all-parameter flat-density exclusion and the exact optimized one-step TV defect with its full minimizer family. The half-bound is a consequence, not an independently novel contraction principle.

## value

PASS

Normalized area is the natural reference probability in this random expanding system. Ruling it out throughout the fat regime is a useful constraint on invariant densities. At the Jacobian-two scale, the exact positive defect and all coin minimizers distinguish binary bias from the wholly free triple coin, quantitatively beyond an existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
