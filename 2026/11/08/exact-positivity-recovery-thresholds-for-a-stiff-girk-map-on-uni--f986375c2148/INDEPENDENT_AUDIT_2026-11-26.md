# Independent mathematical audit

## correctness

PASS

The RK determinant is 1−2z+2z² and the numerator is 1−z. The matrix denominator is invertible because its diagonal is D=1+2h+2h² on transient states and 1 on the absorbing state. The transient block is F(−hI+hN) with N nilpotent; equivalently its bands are the coefficients of (1+h−hx)/(D−(2h+4h²)x+2h²x²). Conservation F(hQ)1=1 gives the remaining column. A fresh exact denominator-clearing check verified the proposed entries and row sums for every n=2,3,4,5, including the −7/625 witness at h=1/2. Sizes two and three use only nonnegative entries. For h>0 in size four the only obstruction is the factor 2h²+2h−1 in B4; in size five the first-row B5 is negative throughout 0<h<1/√2. At and beyond 1/√2 both tails are nonnegative and the order-three transient band is positive (4h⁴+16h³+12h²−1>0); the lower bands are nonnegative as well. At h=0 the update is the identity. These are sign proofs including both threshold equalities, not a sampled classification.

## originality

PASS

The tableau and its spectral damping are known, as is the matrix-function machinery. The checked prior results on the same chain use materially different rational maps, and the closest source using the identical map analyzes drag/gyromotion eigenmodes rather than the defective birth chain. The exact finite-dimensional recovery sets and the stiff-window witness are distinct on the inspected evidence; this is not a priority certification.

## value

PASS

This is a bounded but motivated diagnostic for a stiff update already used in the literature. It identifies the smallest chain that exhibits a negative entry in the specified stiff window and the exact recovery boundary, despite damped scalar modes. The absorbing-tail sign and its separation from spectral damping are useful information not supplied by the prescribed stiffness condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
