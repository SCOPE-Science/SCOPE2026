# Independent mathematical audit

## correctness

PASS

On the precisely specified 16 nodes (south pole plus 3,5,7 longitudes on distinct latitude rings), unitary angular Fourier block-triangularization of harmonics through degree three reduces squared determinant to Q=∏_{j=1}^3(1−x_j²)^{j(j+1)} ∏_{0≤i<j≤3}|x_j−x_i|^{2(2i+1)}, x0=−1, up to a positive height-independent C4. The log Hessian is negative definite and bounded above by −4I in each of six convex height order chambers, so each has a unique interior optimizer. In the inspected exact-rational CHECKER.py, six 1e−10 grid points have ||∇log Q||²<1e−15, and rational inequalities Q(q_better)>Q(q_worse)(1+||g_worse||²/4) rigorously compare all five adjacent chamber optima. Independent Fraction arithmetic verified the order 231>321>132>312>213>123 and 4.77011<D_best/D_runner_up<4.77012. The winning coordinates (x1,x2,x3)≈(0.8685804158,−0.6042361642,0.2022056534) are within 1e−8 of the unique optimum. Numeric 16×16 direct harmonic determinants corroborate the factorization and independence from independent ring rotations, not the infinite-domain optimality argument.

## originality

PASS

The determinant factorization and one optimum per chamber are decisively prior and credited. The six-chamber exact global ranking for the smallest nontrivial three-ring case, its unique winning 5,7,3 order and sharp 4.77011–4.77012 gap survive the stronger all-bandwidth result and the sampled prior numerical-stability literature.

## value

PASS

The D-optimal ordering is a mathematically motivated unknown design choice for the standard minimum-size spherical-harmonic sample architecture. The strict all-chamber exact comparison (global rather than local within a chamber) and factor-4.77 separation quantify how choice of ring-height ordering affects full interpolation determinant; a useful nontrivial finite-level design fact rather than arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
