# Independent mathematical audit

## correctness

PASS

An order ideal is a nested sequence of layers, each one of the six square lower ideals; conversely any such sequence defines an ideal. Using this independent enumeration and layer-major bit indexing, I reproduced the entire integer Walsh census for all six widths. Width six has 336 ideals, no zeros in degrees 0–2 and 32 triples. The orbit representatives and all four images of each agree exactly with direct parity sums, with no overlaps. Coordinate exchange preserves ideals; complement after reversal is an ideal bijection and multiplies the reversed character sum by (−1)^|S|. Complete zero counts for widths 1–6 are 6,61,680,0,107510,1414094, with least vanishing degrees 1,2,1,none,1,3. Fourier diagonalization gives rank 15363122 at width six and the singular values on the recoverable range have endpoints 2 and 336, hence condition number 168. The exact transform of the complementary frequency mask verifies that the absolute sum of the unnormalized recoverable-support kernel is 9182696964; division by 2^24 reduces to 2295674241/4194304. Convolution by the normalized kernel has ℓ¹ norm equal to its total absolute mass (test a point mass), and the same ℓ∞ norm (choose a sign vector aligned to one row). For any projection onto the range, its translation conjugates all fix that same space and all have image in it; their average remains a projection and its norm is no higher. Translation commutation diagonalizes it in the Walsh basis: identity on surviving characters, zero on lost ones. This proves the unrestricted real and complex minima. ‘32 triple orbits’ in the prior-work prose is a slip; the precise Finding, table and certificate consistently give 32 triples in eight orbits. The argument and all operators are finite-dimensional.

## originality

PASS

The closest earlier result gives the same type of exact spectral and projection calculation for a different 24-cube poset; no novelty is attributed to the Walsh algorithm or averaging. The separate same-day cube/diagram analogues do not determine this box's exact census or finite cutoff. The assessment is bounded and does not claim priority for the broad cubic-only phenomenon.

## value

PASS

The canonical 2×2×n family gives a motivated finite least-degree cutoff, separating protection of first- and second-order parity information from cubic information loss. The orbit census specifies the lost low-order observables, while the rank, restricted condition number and exact optimal endpoint amplification supply complementary recovery benchmarks. These values concern this natural family and are not a restatement of the unsigned count; no larger-width theory is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
