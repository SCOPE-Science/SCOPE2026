# Independent mathematical audit

## correctness

PASS

For the integer digit gap (as required by the digit and gcd setup), grouping by the top frequency bit and last spatial bit removes the cross term with the previous spatial prefix modulo one. The only remaining twist is diagonal unitary on the lower frequencies. The product factorization is singular exactly when a level has dt divisible by b. Upon inverting, the two blocks of a selected inverse row are scalar multiples of the same lower-level row, with a unitary right twist. Its norm squared therefore multiplies by 1/(2ps²) or 1/(2(1-p)s²), as given by the two-by-two inverse. The inverse Gram diagonal equals that row norm squared. Summing the inverse masses yields the trace; the block determinants yield the stated modulus with exponent N/2 per level. The trace is minimized exactly by maximizing every sine and every p(1-p); for the largest diagonal the minimum cell mass is at most 1/N with equality only for uniform masses. All nonzero residues modulo q are attained, enough for the stated congruences; the proof's claim about all residue classes need not include zero when gcd(b,d)=1. At the even-q optimum each level block is unitary, and at odd q the mean of reciprocal squared singular values and the row normalization give the obstructions without claiming equality. Independent construction from integer residues and direct Gram solves checked 180 positive-weight nonsingular cases (max relative diagonal error 6.69e-14), 210 cases with exactly one zero-sine level, and unitary and nonunitary optima through depth 5. The all-depth proof is exact, not numerical.

## originality

PASS

Credit the previous uniform determinant law, step congruences, and parity obstruction. The weighted determinant follows from uniform by column scaling and is not a standalone novelty either. The distinct supported claim is the coordinatewise inverse law for the finite tower, its inverse-moment identity, joint A- and worst-coordinate criteria, and strengthened odd-q obstruction; these are not supplied by the checked prior statements.

## value

PASS

The coordinatewise noise-amplification law addresses the inverse problem for a natural tower, not just the volume of its sampling map. It shows exactly how smaller masses increase local estimation variance, makes the A and worst-coordinate objectives share all optimizers with explicit parity costs, and improves an instability obstruction. These provide usable design and inverse-conditioning information not determined by a known determinant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
