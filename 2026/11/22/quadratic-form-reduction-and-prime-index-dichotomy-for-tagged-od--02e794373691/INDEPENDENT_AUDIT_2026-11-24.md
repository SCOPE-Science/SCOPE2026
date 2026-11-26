# Independent mathematical audit

## correctness

PASS

The cited generating function is for the tagged total in odd-part designated-summand partitions, not the partition count or the unrestricted tagged total. Factoring its eta quotient as qE(q²⁴)P(q)/[P(q³)P(q¹²)] is exact. The product for P has constant term 1 and nonconstant terms in each factor of the form 2q^(mj); modulo four only one factor can contribute, giving twice the divisor count, which is odd precisely on squares. The shifted inverses negate those terms; Euler's pentagonal identity yields qE(q²⁴)=Σ_t(−1)^tq^((6t−1)²). The signs on pentagonal terms survive only for epsilon, since 2 and −2 coincide modulo four in the representation terms. For n≡3 modulo 4 none of the square or representation terms can contribute. For primes p≡1 modulo 4 the j in the d=3 term is even, making its count identical to the d=12 count, and their contributions cancel. For p≥5 the unique odd coordinate in the prime two-square representation contributes exactly once iff 3 does not divide it: one sign then lies in the class −1 modulo 6. The examples and small prime exclusions agree. For r≡11 modulo 12, both −1 and −3 are nonsquares, so r-divisibility of either relevant norm form forces both variables divisible by r, implying even r-valuation by descent; the square term also has even valuation. The lower relative prime density bound 1/4 follows from the prime number theorem in arithmetic progressions for p≡5 modulo 12 (ordinary Dirichlet infinitude alone is not a quantitative density proof). If infinitude of both subclasses of p≡1 modulo 12 is intended, it follows from the infinitude of primes represented by the primitive forms x²+36y² and 4x²+9y² respectively; the main residue proof does not require that result. A separately written finite expansion matched all 2000 positive coefficients, 301 primes from 5 to 2000 and 565 odd-valuation obstruction cases, as well as all 500 indices congruent to 3 modulo 4; see /workspace/branches/ca952bde-a00e-4cbc-aa60-263aec4fa262/check-notes.md. The supplied checker was inspected, not run; the finite replay does not prove the infinite statements.

## originality

PASS

The eta quotient, earlier progression congruences and integer-density lacunarity are known. The supported distinct result is the explicit all-index quadratic representation rule modulo four and the resulting Gaussian-coordinate prime classification and specific local composite obstruction.

## value

PASS

The quadratic reduction turns the known coefficient generator into an all-index arithmetic test. It both distinguishes the two residues at split primes using a natural Gaussian-coordinate invariant and gives a local vanishing criterion at composite indices; density-one lacunarity or a list of residue progressions does not answer those questions. The characterization is useful even without exact densities for both Gaussian-coordinate subclasses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
