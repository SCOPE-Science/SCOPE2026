# Independent mathematical audit

## correctness

PASS

With ||r_0||=1 and β_j>0 through k, T_j=I+iJ_j is invertible because its Hermitian part is I. Widlund residual r_j is a multiple of the next Lanczos vector, and the corner cofactor gives ||r_j||=∏_{l≤j}β_l/|D_j|. The nonzero Galerkin residuals for j=0,…,k are orthogonal and affinely span r_0−AK_k; minimizing the norm of an affine combination gives the Rapoport inverse-square sum, also verified in Higgins–Reed–Szyld Eq. (10). Equality with the min residual bound means every Widlund norm equals one. The continuant D_j=(1+ia_j)D_{j−1}+β_{j−1}²D_{j−2} then gives |z_j|=β_j for z_j=D_j/D_{j−1}, so z_j=1+ia_j+conj(z_{j−1}) and Re(z_j)=j, starting at z_1=1+ia_1. Thus β_j≥j. With the positive unit Perron vector w of B_k and its alternating-sign copy, the two Rayleigh quotients of the leading block are d±2∑β_j w_j w_{j+1}, where d is their common diagonal contribution. The larger absolute quotient is at least 2∑β_jw_jw_{j+1}≥ρ_k, with strict inequality if any coupling is greater than j. The full norm bounds this compression. B_k attains the bound by the factorial continuant and sign symmetry of its spectrum. In dimension k+1, equality forces every β_j=j and hence a_1,…,a_k=0 by the quotient recurrence; the two Rayleigh quotients then differ from ±ρ_k by a_{k+1}w_{k+1}², forcing a_{k+1}=0. Valid for exact arithmetic, common initial iterate and the specified no-breakdown setup; no near-saturation rate is established. The uploaded script was inspected, not executed: it checks canonical small cases and one explicit 2-by-2 characteristic polynomial, not the first four norm polynomials or perturbed matrices as described in RESULT.md line 29. This supplemental evidence mismatch does not affect the analytic all-k proof.

## originality

PASS

The comparison, inverse-square relation, cofactor method for the example, and the actual attaining path are acknowledged existing results and are not credited here. The distinct contribution is the universal lower bound on all couplings, its sharp norm obstruction for every saturating system, and uniqueness of the norm minimizer in minimal dimension. The strongest primary comparison, Theorems 1–3 and their proof, gives the relationship and one sharpness example but not the necessity for arbitrary Jacobi diagonals/couplings or the norm minimization. The matching local indexed hit is the assigned record itself, not independent evidence. The judgment is limited to the checked scope.

## value

PASS

A sharp example by itself does not say whether the worst comparison factor can arise with a small skew part. The theorem makes the skew spectral norm a necessary resource for exact saturation, gives an attainable barrier at each iteration, and singles out the minimal-dimensional system that uses the least such norm. This is a natural structural and extremal question following the original comparison, not just another verification of its saturating example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
