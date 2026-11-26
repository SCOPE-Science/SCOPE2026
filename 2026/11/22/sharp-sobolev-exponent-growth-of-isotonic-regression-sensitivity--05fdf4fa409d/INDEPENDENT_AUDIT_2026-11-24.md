# Independent mathematical audit

## correctness

PASS

In the stated unweighted Euclidean projection on a path, translation equivariance makes the gradient quotient well-defined. The chamber map Q is averaging on consecutive blocks; each gradient column of DQD⁻¹ is obtained by taking output gradients of a unit step. For adjacent blocks of lengths m,l this gives a boundary row with nonnegative ramp weights, central entry one and row sum (m+l)/2. The two contributions of an internal edge to neighboring boundary rows add to one before missing endpoint rows are discarded; a separating edge contributes one. Weighted Hölder and these column/row bounds give (n/2)^(1−1/p), including p=1; the row sum gives p=∞ directly. The finitely many closed affine cells partition each line segment into subsegments on which these estimates apply, including a segment lying on cell boundaries. Strict chambers with decreasing raw data inside pooled blocks and distinct ordered means give genuine finite witnesses: the block pattern (1,n−2,1) sends a ramp to a gradient with two equal entries (n−1)/2, yielding the lower bound, and (1,n−1) attains the infinity upper bound. The latter's row has entry one plus a further positive entry for n≥3, so its dual p-norm bound is strictly above one for p>1, even at n=3. The increasing chamber yields equality at p=1, and n=2 follows from its upper bound and the identity chamber. Dividing by (n/2)^(1−1/p) gives the uniform error at most 1/n. No complete finite interior-p formula is claimed. Read RESULT.md:3–57, VERIFICATION.md and check_isotonic_wp.py without executing uploaded code; the independent_matrix_check.py and .log in /workspace/branches/49ed2a84-f4f4-492d-aba9-c2ac3ab8e796 corroborate exact row/column sums and genuine fitted pairs for bounded n, with floating evaluation of selected p-norm ratios. The general conclusion comes from the analytic argument.

## originality

PASS

Credit the sharp uniform all-exponent leading constant with explicit finite two-sided error, the sharp infinity endpoint and the contraction/expansion transition for this two-input derivative seminorm. The TV endpoint and the Hilbert-exponent coefficient have existing coverage and are not separately credited. The available recognized value-space results and these special exponents do not supply the matching bounds uniformly over all exponents.

## value

PASS

Isotonic projection is contractive on values and in gradient TV, but the bias this suggests for stronger gradient seminorms is wrong. The exact infinity gain, failure at each p>1 even in the shortest nontrivial dimension, and quantitative all-exponent interpolation with a matching leading constant give a sharp stability benchmark for arbitrary input perturbations. Uniform relative error controls exponents varying with dimension, not just one fixed exponent at a time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
