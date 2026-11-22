# Scientific review: three-class Zeckendorf parity imbalance

## Correctness (PASS)

The claim specifies the canonical nonadjacent Fibonacci digits, includes \(n=0\), uses half-open Fibonacci cutoffs, and defines the signed count by parity of the number of summands. The last-digit recursion for the weighted polynomial is exact. The period-eight Fibonacci weights modulo three give a monodromy matrix of trace eight and determinant one, so Cayley–Hamilton establishes the *infinite* second-order recurrence, not merely observed data. Direct base values \(3,23\), bounded root-one sum, and cubic-root Fourier inversion give the exact three residue biases at every stated cutoff. Distinct positive eigenvalues give the claimed exponent, and the nonzero dominant coefficient proves sharpness for these cutoffs. The standard-library checker independently verifies the transfer computation and 29,575 finite integer comparisons; these are corroboration, not proof of the infinite statement.

## Originality (PASS within inspected evidence)

The sequence and its Zeckendorf definition were previously studied by Ferrand (2007), Shallit (2022), and in OEIS A095076; none is claimed new. Shallit's paper proves a complexity theorem, not a signed arithmetic progression count. The relevant Drmota–Müllner–Spiegelhofer result is Möbius orthogonality; the Drmota–Steiner result concerns digit-sum distribution and central limit behavior; and Popoli–Stipulanti study related correlation properties. Neither these nor the inspected earlier sequence data imply an exact phase-seven three-progression imbalance recurrence, a permanent modulo-three sign pattern, or the sharp \(0.536\ldots\) Fibonacci-cutoff exponent. Newman's 1969 formula and later rarefied Thue–Morse results use *binary* digits rather than Fibonacci digits, so substitution without redoing the transfer computation is invalid. Public research-index searches for equivalences and stronger results found fixed-weight Zeckendorf slice distributions and classical binary Newman sums, both mathematically different. Historical priority in unindexed literature remains an explicit risk.

## Value (PASS)

The result quantifies a natural refinement of the long-studied Fibonacci–Thue–Morse sequence: its signed distribution along the first nontrivial arithmetic progressions. It proves persistent bias in one progression of exactly the opposite sign of the other two, despite near-total cancellation globally. The explicit growth exponent is strictly larger than one half and is sharp on Fibonacci cutoffs, a substantial structural difference that basic equidistribution, digit-sum central limit theorems, and word complexity cannot supply. This provides an exact Fibonacci-numeration analogue of the Newman phenomenon, not a disconnected numerical curiosity. Limits: no arbitrary-cutoff sharp law and no other residue modulus are claimed.

Self-review: passed. Independent audit: not yet performed.
