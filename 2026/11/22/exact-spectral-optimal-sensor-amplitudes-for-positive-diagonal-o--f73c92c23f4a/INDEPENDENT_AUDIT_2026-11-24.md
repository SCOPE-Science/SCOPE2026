# Independent mathematical audit

## correctness

PASS

With times 0,…,N the phase-free frame matrix is DCD for D=diag(|g_i|). C=VVᵀ with V_ik=a_i^k. For each minor, the Cauchy–Binet terms are products of positive generalized Vandermonde determinants (ordinary Vandermonde on the ordered positive nodes times a Schur polynomial with nonnegative coefficients and at least one positive monomial). N+1≥n ensures nonempty sums. Cofactors give the strict checkerboard sign of C⁻¹, hence H>0 entrywise. For an independent certificate, let p_i=|g_i|² and t>0. When p has full support, W≥tI iff diag(p)≥tH by inversion, congruence and the checkerboard signature. If any p_i vanishes, the smallest eigenvalue is zero. The all-ones test gives t≤1/L. The proposed p attains it because diag(r)−H is the positive semidefinite weighted graph Laplacian with quadratic form (1/2)∑ H_ij|x_i−x_j|². Equality forces (diag(p)−tH)1=0, so exactly p=r/L; phases are immaterial. In the three-mode example, the columns of V⁻¹ are coefficients of 8x²−10x+3, −16x²+16x−3 and 8x²−6x+1; applying the checkerboard signs to their coefficient Gram gives the displayed H and L=2097. When the horizon is shorter the rank is at most N+1; when two modes coincide their projected orbit spans at most one direction. Both listed degeneracies give zero.

## originality

PASS

Pass for the exact discrete finite-horizon E-optimal allocation, including uniqueness and validity at every admissible horizon. The row-sum form and its sign argument are not new as general design ideas: Chen–Belabbas explicitly have the exact analogous law for the infinite continuous-time Cauchy kernel, and the same-day finite continuous-time result deploys essentially the same argument for an exponential integral kernel. Neither inspected statement contains the finite discrete kernel. The remaining distinct content is the exact allocation for every consecutive finite discrete horizon and the needed strict inverse-sign proof for that family, not a new general optimization principle.

## value

PASS

Finite consecutive observations under a unit-energy constraint are a natural sensor-design problem. The exact worst-mode bound and unique amplitude allocation give a horizon-specific benchmark down to the minimum number of observations without performing a sensor optimization. A continuous integral or infinite-time limit need not give the same amplitudes for the actual discrete horizon; the inverse-sign certificate explains why an exact simple law still works there.

The dated certificate retains the supplied scientific assessment, sources and limitations.
