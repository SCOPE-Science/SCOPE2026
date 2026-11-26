# Independent mathematical audit

## correctness

PASS

The difference y_i=x_i XOR x_(i+3) removes exactly the forbidden abcabc, including at n<6. Its image is precisely orbit-wise even parity, of codimension gcd(n,3); the orthogonality and inverse multiplicity cancel. The signed closed pair walk is uniquely indexed by each marked y even at short periods. If 3 divides n, three one-negative and three two-negative sign patterns reduce by cyclic trace to QP^2 and Q^2P; the factor 3 cancels n=3m in the zeta logarithm. Independently built 32-state overlap adjacency and evaluated det(I-zA) by exact Bareiss elimination at 33 distinct integers, proving the degree-at-most-32 denominator identity; recovered all 18 listed coefficients, and independently checked direct bitmask counts for n=1..14 (replay /workspace/branches/replay-cyclic.py). A fixed word of a rotation lifts from circumference gcd(n,rotation); this gives Burnside and least-period decomposition with the stated totient and Möbius weights. The other P roots are a complex pair of modulus rho^(-1/2), the signed and cyclotomic factors have unit reciprocal roots, the quadratic-in-z^3 factor gives reciprocals of modulus at most (1+sqrt(2))^(1/3), and the last factor gives cubes of reciprocals satisfying x^3+x^2+x-1=0, hence reciprocals of modulus at most 2^(1/3). These bounds are strictly below the simple dominant rho; proper powers contribute only O(poly(n) 2^(n/2)).

## originality

PASS

Within inspected evidence the explicit degree-24 factorization, marked counts for just half-length three, and the resulting orbit/growth census are distinct. General zeta rationality, the linear derivative correspondence, and the stronger avoidance restriction discussed in the related same-day catalogue entry are not credits for this exact factorization.

## value

PASS

The length-six binary exclusion is a natural fixed-length duplication constraint on periodic points. The compact factorization makes the cyclic closure contribution visible and identifies the exact asymptotic and primitive orbit census, not just a generic finite-state representation or a short list. This can be used to compare simultaneous and single-length restrictions and count periodic orbits at arbitrary periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
