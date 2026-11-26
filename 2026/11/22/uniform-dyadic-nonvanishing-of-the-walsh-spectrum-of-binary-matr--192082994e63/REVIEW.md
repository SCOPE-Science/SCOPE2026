# Independent mathematical audit

## correctness

PASS

For the character on all matrices at C of rank r, invertibility can be imposed by subspace Möbius inversion of the kernel indicator. The inner sum over matrices annihilating U vanishes unless the row space of C lies in U, and otherwise is 2^{n(n−dim U)}. Summing over dimensions by the Gaussian binomial theorem gives the factor (−1)^r 2^{binom(n,2)}∏_{j=1}^{n−r}(2^j−1). Averaging the full transform over the n diagonal frequencies imposes zero diagonal, giving W=2^{n(n−3)/2}s_B for n≥3. For every fixed B, the parity of the number of invertible diagonal completions is the sum of the multilinear determinant over the Boolean cube, i.e. the coefficient of the full diagonal product, which is 1. The rank factor after removing 2^{binom(n,2)} is (−1)^{n−1} modulo 4 for all deficient ranks (only j=1 gives +1 modulo 4), and (−1)^n at full rank. Hence s_B≡2 mod 4. This yields the stated congruence even for negative Walsh values. At n=2 there is a single matrix, yielding ±1. Counting Walsh diagonalization gives all the rank, determinant and inverse-norm claims.

## originality

PASS

The supported distinct claim is the uniform exact two-adic valuation at all off-diagonal frequencies, not the unsigned count, the general rank transform, or the character projection technique. A fixed off-diagonal frequency and its entire affine family of diagonal completions are essential to the comparison.

## value

PASS

The exact invariant distinguishes all spectrum coefficients from zero in one theorem, including characters for which neither the zero-frequency count nor a common divisibility bound rules out cancellation. This proves invertibility of a natural additive convolution on a matrix restriction and determines the two-adic valuation of its whole determinant and a quantitative inverse norm bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
