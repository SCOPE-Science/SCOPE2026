# Independent mathematical audit

## correctness

PASS

A swap changes exactly its two coordinates, so legal swap locations count distinct neighbors. With L=n−2 and Y_i indicating unequal second neighbors, the two end swaps contribute Y₁+Y_L, and each internal swap contributes Y_iY_{i+1}. Each profile of weight w lifts to q(q−1)(q−2)^w proper words, so profile indicators are independent Bernoulli(p) under the uniform word law. Weighting the initial and terminal bits and adjacent products yields (1), and the 2×2 resolvent gives (2). One zero kills at least two terms even for L=1, while the profiles 1^j0^{L−j} give all degrees 0≤j≤L−1; all ones give L+1. Zero degree forces zero ends and an independent interior set, giving the stated path recurrence. The only nonzero covariances involve overlapping products and endpoint/product pairs; for L=1 the same Bernoulli variable is counted twice, and for L=2 both distinct ends covary with the single product. The mean and variance formulas and handshake edge formula follow. Independent direct swap enumeration using set membership confirmed finite distributions, support, mean and variance.

## originality

FAIL

Exact coverage by a distinct indexed result is established, not priority or direction of derivation. Resultary 4d7ccc34519c gives the very same graph, degree identity and transfer polynomial in a broader parameter range. Subtracting the n=2 term in the length series and relabeling states yields the assigned generating function. Explicit wording of the support gap and edge total does not recover originality: both are immediate from the matching profile identity and polynomial/mean.

## value

FAIL

The legal-swap degree distribution is a natural invariant of a proper-coloring path, but this submission adds no substantive scientific information beyond the broader exact result. The stated support and edge count are direct consequences of the already evaluated same invariant, not a distinct classification or consequence needing new work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
