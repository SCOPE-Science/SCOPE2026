# Scientific review: optimal fixed-angle mixing on the rotation group

## Correctness

**PASS.** The one-step law is central and inversion symmetric, so Schur's lemma and the \(\mathrm{SO}(3)\) character formula give the exact norm as the supremum of normalized character moduli. The first and third spins balance at the sole real solution of \((6c+1)^3=-35\). Elementary rational bounds control spin two and all spins at least four at that angle. A four-interval covering proof using only the first three spins gives a strict global lower bound elsewhere. All endpoints and equality cases are addressed. The independent finite numerical checks are supplemental; they are not used as a proof of an infinite statement.

## Originality

**PASS against accessible prior statements, with residual priority risk.** Rosenthal's 1994 foundational study specifies exactly the same conjugacy-class rotation step and character tools, but its theorems address total-variation cutoff estimates in variable group dimension. Hough and Jiang's 2012 full accessible preprint studies fixed-angle uniform-plane walks and asymptotic mixing as group dimension grows, not the all-spin, dimension-three, unique minimizing-angle problem. Al-Dayel and Deshmukh's 2023 open article uses continuous-time Brownian heat kernels and a geometric expectation rather than angle optimization. Related mathematical records on compact-group Fourier norms, rotation covariance, and discrete graph mixing do not state or imply the exact radical optimizer. A different earlier optimization of the same character sequence could imply the result and cannot be categorically excluded without a specialist literature review.

## Value

**PASS.** The result is an exact natural design principle for a single-angle random rotation walk on a compact noncommutative group. Its sharp angle and contraction factor are nonobvious radicals, and the two binding sectors have opposite Fourier signs; all infinitely many higher sectors are strictly inactive. This supplies the precise minimax \(L^2\) geometric contraction at every iteration count, not a mere numerical or routine low-spin estimate. The design restriction is explicit: this is not a claim about arbitrary step-law mixtures or total-variation mixing from a point mass.

## Sources and limits

Primary material: Rosenthal, *Random Rotations: Characters and Random Walks on SO(N)* (1994), https://probability.ca/jeff/ftpdir/rots.pdf ; Hough–Jiang, *Cut-off phenomenon in the uniform plane Kac walk* (2012), https://arxiv.org/abs/1211.2031 ; Al-Dayel–Deshmukh, *The Heat Equation on Submanifolds in Lie Groups and Random Motions on Spheres* (first published April 20, 2023), https://doi.org/10.3390/math11081958. Relevant portions were read and compared at the level of statements and implications. Exact historical priority and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
