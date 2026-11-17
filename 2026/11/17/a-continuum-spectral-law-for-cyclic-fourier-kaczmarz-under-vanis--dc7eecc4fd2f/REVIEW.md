# Scientific review: continuum Fourier Kaczmarz cycle law

## Correctness
PASS. The normalized Fourier Gram matrix is derived directly from the finite-root orthogonality relation, and the exact Gauss–Seidel sweep formula is checked against an independently assembled triangular solve. The kernel scaling shows \(\mathcal S_2\)-convergence with a diagonal-strip error of squared order \(m^{-1}\). An explicit positive Gram-square-root similarity transfers the limit to the actual Hilbert error operator. The eigenvalue boundary condition \((z+c)e^z=c\) is derived from the integral equation, its spurious zero-exponent root is excluded, and the remaining roots are exactly the nonprincipal Lambert branches. Compact spectral approximation yields the per-cycle radius limit. Finite diagnostics are not substituted for the infinite-dimensional proof.

## Originality
PASS, with priority qualification. The closest published finite-atomic Fourier Kaczmarz result gives the *exact finite-dimensional root-polynomial rate* and proves that equal weights on a regular polygon are exactly the finite-recovery case. The new statement is not another computation of that polynomial: it identifies the critical bias scaling, a full Hilbert–Schmidt limit in both coefficient and physically correct orthonormal coordinates, the associated complete nonzero continuum spectrum, and fixed-index physical singular-value convergence. Berner–Herr–Jorgensen's Theorem 4.1 and Lemma 5.7 concern finite-atomic unconditionality and qualitative spectral-radius decay, not this limit. The closest fixed-sweep Gauss–Seidel rank-one Gram result fixes coherence independent of dimension rather than letting it shrink. Historical Volterra rank-one perturbation and continuum Gauss–Seidel references may still contain equivalent forms; publication priority is not certified.

## Mathematical value
PASS. Equal weights yield an exactly zero full-cycle error. A one-atom mass defect of order \(m^{-1}\) nevertheless yields a strictly positive per-cycle limiting spectral radius, with an entire nontrivial physical singular spectrum. This is a motivated dimension-dependent stability boundary for cyclic Fourier reconstruction rather than an arbitrary small-case constant; the Hilbert–Schmidt limit provides a reusable operator model for both spectral and transient behavior.

## Closest literature and limitations
The most relevant sources are Berner–Herr–Jorgensen, *Frame Properties of Effective Stationary Sequences*, arXiv:2611.03358 (Sections 4–5); *Regular-polygon finite-step rigidity and an explicit spectral rate for Fourier Kaczmarz recovery* (November 2026); and *A fixed-sweep Gauss–Seidel residual illusion for rank-one Gram systems* (October 2026). The claim fixes \(c>0\), deterministic Fourier order, and one distinguished mass; no parameter-uniform bound or noise result is claimed. Independent publication-priority review remains necessary.

Self-review: passed. Independent audit: not yet performed.
