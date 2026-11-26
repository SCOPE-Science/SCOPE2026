# Independent mathematical audit

## correctness

PASS

For full-dimensional Z in dimension d≥3 represented by at most d+1 segments, use the Steiner-normalized area sum S=Σ a_i a_j sin θ_ij. Setting B=Σ w_ij sin²θ_ij, expansion gives A=A_*−Q/2 and B=B_*−E/2: tr(T²) includes the weighted squared inner products, and the diagonal terms cancel in L²−tr(T²). The angular weighted variance gives AB−S²=AH. Subtracting AB from A_*B_* gives the displayed identity and both nonnegative lower bounds, by writing the difference as A_*E/2+BQ/2 or B_*Q/2+AE/2. At equality Q=E=0, so all d+1 lengths are positive/equal, and the unit-direction Gram matrix is (d+1)/d times the orthogonal projection off a one-dimensional kernel. Its diagonal one forces all kernel magnitudes to be 1/√(d+1); column signs turn that kernel into the all-ones direction, and all signed off-diagonals equal −1/d. Conversely the simplex attains the bound. Sign changes just translate the zonotope. The checked zonotope convention gives mean width 2κ_(d−1)L/(dκ_d), so fixing L is equivalent to fixing mean width. RESULT.md lines 45–86 give an exact replay; verify.py is finite corroboration only and was not executed in the review.

## originality

PASS

The distinct result is the sharp fixed-mean-width maximum allowing unequal generator lengths, plus an exact quantitative defect identity. No separate originality credit is given for the equilateral maximum, the wedge-area formula, or the characterization of a real unit-norm tight frame with d+1 columns as signed simplex directions.

## value

PASS

This settles a concrete intermediate-index case of the fixed-mean-width problem when generator lengths are unrestricted. The equality and exact defect decomposition also distinguish geometric mechanisms of near equality: the squared deficit controls length dispersion and isotropy independently. The result does not extrapolate to higher intrinsic volumes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
