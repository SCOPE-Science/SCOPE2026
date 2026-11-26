# Independent mathematical audit

## correctness

PASS

For odd n and p=char(F_q) not dividing n, Fourier inversion is valid and the product e_x e_y=e_{2y−x} gives c_k=c_{−k}c_{2k}. The nonzero support is invariant under both finite permutations. Multiplication of equations at k and −k, then cancellation and surjectivity of doubling on the support, give c_{−k}c_k=1 and c_{2k}=c_k². On order-r indices, if −1=2^{d_r/2} modulo r the seed relation t^{2^{d_r/2}}=t^{−1} also closes the doubling cycle; otherwise the negated doubling cycle is disjoint and independently given by inversion, with closure t^{2^{d_r}−1}=1. Frobenius covariance c_{qk}=c_k^q is both necessary and sufficient by inversion. The quotient of the order-r residues by H_r has q-cycles of common length s_r. On each cycle, propagation gives one zero choice or a seed solving both t^{N_r}=1 and t^{q^{s_r}−ε_r2^{a_r}}=1. The gcd is prime to p: N_r is odd if p=2, and the second exponent is a unit modulo p if p is odd. Thus the number of nonzero choices is the stated gcd, even when the exponent difference vanishes in characteristic two. Independent cycles and c_0=0 or 1 give the formula and inverse. Direct exact enumeration in the original basis independently gave 12, 16 and 80 at (n,q)=(5,4),(7,3),(9,2).

## originality

FAIL

Published record 4a113244be17 gives the same full count and Fourier parametrization for the same multiplication and the same range of odd n and coprime finite fields. Its global splitting-field gcd factor is redundant, and its orbit product is identical to the frozen divisor product after grouping by order r; the equivalence is proved below. This is established statement-level coverage, not an inference from title, date, or common use of Fourier methods. The record-path dates do not establish authorial priority or provenance.

## value

FAIL

The arithmetic classification is a worthwhile invariant of a natural algebra. But the incremental assertion in this submission is the same known classification in divisor notation: the exponent just counts same-order cycles and the gcd simplification follows immediately from closure. Neither supplies a further mathematical invariant or substantive new range, obstruction, application or algorithmic result. There is no isolated surviving valuable claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
