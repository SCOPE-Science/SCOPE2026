# Review of sharp signed Aztec-diamond divisibility

## Correctness — PASS

The Kasteleyn determinant represents every edge-signed domino sum up to a global sign, including zero values. Its reduction modulo two is the fixed Kronecker product of two full-rank rectangular bidiagonal matrices, of binary rank \(n^2\) in dimension \(n(n+1)\); the resulting \(2^n\) determinant divisibility is unconditional. The diagonal-row/diagonal-column complement is invertible modulo two by an explicit row-sum and kernel argument. The top Boolean finite-difference coefficient is consequently odd after dividing by \(2^n\), proving sharpness and odd witness parity. Walsh inversion excludes odd gcd factors. Definitions, dimensions, signs, and all integer quantifiers were checked; exact finite experiments provide corroboration only.

## Originality — PASS under bounded literature comparison

The closest known result is Barkley–Liu, Theorem 3.5 and Example 6.10 (arXiv:1911.08102), which proves divisibility of the *unsigned* Aztec-diamond tiling number using channel dimensions, and, by its general Lemma 2.9, also implies the common \(2^n\) lower bound for every independently signed Kasteleyn determinant. It does not establish sharpness or the odd number of exact-valuation signings in a fixed small subfamily. Elkies–Kuperberg–Larsen–Propp (arXiv:math/9201305) derive unsigned tiling statistics, while Brualdi–Kirkland (2003) calculate an unsigned-count Kasteleyn determinant. Chhita–Duits (2023) treat arbitrary weights for dimer correlations, without stating the exact common divisor across all binary weightings. Related searchable mathematical records involving noncrossing perfect matchings, complete-graph perfect-matchings, and torus domino-tiling flip metrics do not dominate this graph-specific result. Search incompleteness remains a historical-priority risk; no global uniqueness certificate is asserted.

## Mathematical value — PASS

The classical unsigned count is a power of two with exponent \(n(n+1)/2\). The proved universal signed divisor has the smaller **exact** exponent \(n\), and there is a parity-certified family of sharp assignments for every order. This identifies a natural arithmetic Fourier invariant of an infinite family of planar dimer systems, rather than a single small-instance census. The tensor-rank and complementary-minor proof also supplies a reusable way to separate lower-bound and attainability questions for Kasteleyn-type Fourier sums.

## Limits and risk

No general statement about the number of zero Walsh frequencies, their multiplicities, or signed determinant magnitude distributions follows. Existing general Kasteleyn formulas may encode the result implicitly, but the inspected passages do not state or directly imply the exact all-signing gcd without the complementary-minor argument. Independent validation and exhaustive historical priority checking were not performed.

Self-review: passed. Independent audit: not yet performed.
