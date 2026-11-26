# Independent mathematical audit

## correctness

PASS

There are Σ_k binom(5,k)²k!=1546 matchings including the empty one. I reproduced the signed multiplier at each row-profile using a different formula: for a column subset C, the kth elementary symmetric function of the five signed row sums over C counts assignments of k distinct rows to columns in C, allowing repeated columns. Inclusion–exclusion over subsets of each k-column target forces bijections and gives the signed matching sum over all sizes. All 376,992 unordered row profiles, with multiplicities 5! divided by the product of the row-multiplicity factorials, account for all 2²⁵ signs. The replay matches all 187 signed CSV entries (1,183,200 zeros, rank 32,371,232, moduli 2 through the maximum 1546 at the extremes, hence ratio 773). The calculation marks the individual zero frequencies and transforms their indicator, using the constant full-set transform to obtain the complement's unnormalized absolute sum 25,902,311,232. Averaging any projection over translations preserves its range and its restriction to that range and cannot raise either endpoint norm. The averaged projection is uniquely the Fourier-support multiplier 1_S. Its counting kernel has ℓ¹ norm 2⁻²⁵ times the computed sum, attaining the ℓ¹ operator norm on a delta and the ℓ∞ operator norm on a translating kernel's sign vector. Normalizing the measure does not change these induced norms. The Finding's phrase 'zero frequency multiplicity' means multiplicity of eigenvalue zero, not the trivial frequency, which has value 1546.

## originality

PASS

The supported distinct advances are the signed histogram for all partial matchings of the 5-by-5 square and the computed optimal range-projection constant. Unsigned rook counting, other board shapes, size slices, and the same-board perfect-matching spectrum were compared; none of the established results provides the two claimed exact invariants. The averaging argument and standard convolution diagonalization are not novelty claims.

## value

PASS

The all-matchings indicator on a complete square board is canonical and its Fourier zero set governs exact recoverability. The sharp endpoint projection constant quantifies a distinct stability cost of projecting arbitrary data to the recoverable subspace; it cannot be read off from the spectral condition ratio. Together the full signed table and sharp norm give substantive exact benchmark data for finite-board results beyond the three-row family and the perfect-matching slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
