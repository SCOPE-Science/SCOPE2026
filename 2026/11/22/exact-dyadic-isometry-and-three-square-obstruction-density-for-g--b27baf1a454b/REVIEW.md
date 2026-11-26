# Independent mathematical audit

## correctness

PASS

The exponential generating function e^(−z)/(1−z)^3 gives the stipulated recurrence and G₀=1, G₁=2. Applying (1+D)²/2 to the ordinary derangement EGF gives the exact reduction in the record. For x=2t or 1+2t, the j-th falling factorial has at least floor(j/2) factors with all coefficients even, so the two interpolants are integral restricted series. Modulo eight the even branch needs terms j≤4, the odd j≤5; multiplying their respective residues 1+4t+4t² and 2t+4t² by P(2t) and P(1+2t) gives the normalized differences K₀≡t and K₁≡1+t coefficientwise mod two. Integral restricted series have integral difference quotients by factoring t^j−u^j and taking the convergent sum, so the affine leading units give exact same-parity distances; opposite-parity values are already distinct mod two. This proves bijectivity and least period at every modulus. Legendre gives the disjoint progressions; for X>2 and 2^(L−1)<X≤2^L, all omitted strata beyond 2j+3>L lie in one class mod 2^(L−2), at most O(1) indices. Each included class has O(1) counting error, and the geometric density sum is 1/6. The bounded endpoint X≤2 is immediate, avoiding a negative exponent in the displayed tail proof. Direct EGF evaluation in the independent checker verifies all five example classes and permutation/period mod 2048; the analytic argument gives all exponents.

## originality

PASS

Ulas's parameter-two obstruction progression n=2 mod 8 is covered, but the exact classification, global dyadic isometry and density with discrepancy are not covered by the inspected statements. The strong distinct same-day generalized-derangement result explicitly excludes parameter two and addresses an odd branch. Its reference to the separately solved stronger v=2 result is consistent with the frozen target, not evidence for an independently identified equivalent record.

## value

PASS

The result answers Ulas's obstruction and density questions for a natural first even parameter. The complete progression law goes beyond the previously visible 1/8 lower bound, with a 1/6 exact density and quantitative error. The isometry is a separately useful structural fact controlling every dyadic fiber, not just the chosen number-theoretic application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
