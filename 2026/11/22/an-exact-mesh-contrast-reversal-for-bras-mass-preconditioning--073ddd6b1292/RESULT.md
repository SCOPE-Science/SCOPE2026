# An exact mesh-contrast reversal for BRAS mass preconditioning

## Finding

Let a periodic one-dimensional continuous piecewise-linear finite-element mesh have \(n=4m\ge4\) elements, with positive element lengths alternating \(a,b,a,b,\ldots\). Put \(r=\max(a,b)/\min(a,b)\ge1\). Let \(M\) be the consistent finite-element mass matrix, \(B_{\mathrm I}\) the identity-weighted (original) broken-space additive Schwarz (BRAS) inverse, and \(B_{\mathrm D}\) its diagonal-local-mass-weighted counterpart, as defined below. Let \(J=\operatorname{diag}(M)^{-1}\). The spectral condition number is the ratio of the largest to smallest positive eigenvalue of the indicated preconditioned product.

**Exact comparison.** For every \(m\ge1\),
\[
\kappa(JM)=3,\qquad
\kappa(B_{\mathrm D}M)=\frac{3r^2+10r+3}{3(r+1)^2}\le\frac43.
\]
For \(r\ge3\),
\[
\kappa(B_{\mathrm I}M)=\left(\frac{3r+1}{r+3}\right)^2.
\]
For \(1\le r\le3\), \(\kappa(B_{\mathrm I}M)\le(3r+1)^2/(12r)\le25/9<3\). Consequently, identity-weighted BRAS is strictly better conditioned than Jacobi precisely for
\[
1\le r<r_*=1+\frac4{\sqrt3}=3.3094010767\ldots,
\]
is equally conditioned at \(r=r_*\), and is strictly **worse** for \(r>r_*\). By contrast, the diagonal-local-mass-weighted BRAS is strictly better than Jacobi at every \(r\ge1\), and its condition number tends to \(1\) as \(r\to\infty\), while that of identity-weighted BRAS tends to \(9\).

For example, at \(r=4\) on any such periodic mesh, the three condition numbers are exactly
\[
\kappa(B_{\mathrm I}M)=\frac{169}{49}>3=\kappa(JM)>\frac{91}{75}=\kappa(B_{\mathrm D}M).
\]

## Assumptions and scope

There are \(n=4m\) distinct cyclic vertices, with edge \(i\to i+1\pmod n\) of length \(h_i\). Here \(h_{2j}=a>0\), \(h_{2j+1}=b>0\), and all finite-element degrees of freedom are nodal values. The local consistent mass is
\[
M_{h}=\frac h6\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
Let \(P\) duplicate conforming nodal values into edge-local copies, let \(M_{\rm br}\) be the block diagonal matrix with local blocks \(M_{h_i}\), and put \(D=P^\mathsf TP=2I\). The original BRAS inverse is
\[
B_{\mathrm I}=D^{-1}P^\mathsf TM_{\rm br}^{-1}PD^{-1}.
\]
For the weighted variant, set \(W=\operatorname{diag}(M_{\rm br})\), \(A_W=P^\mathsf TWP\), and
\[
B_{\mathrm D}=A_W^{-1}P^\mathsf TWM_{\rm br}^{-1}WPA_W^{-1}.
\]
Both preconditioners are SPD. The conclusions concern exact arithmetic and generalized spectral conditioning of a **single** preconditioned mass solve, not wall-clock speed or performance of every possible weighted BRAS implementation. A physical periodic domain of circumference \(2m(a+b)\) realizes the mesh; simultaneous common scaling of \(a,b\) is immaterial.

## Proof

The local inverse is \(M_h^{-1}=\frac2h\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\). Direct assembly gives, at each vertex \(i\),
\[
M_{ii}=\frac{a+b}{3},\quad M_{i,i+1}=\frac{h_i}{6},\quad
(B_{\mathrm I})_{ii}=\frac1a+\frac1b,\quad (B_{\mathrm I})_{i,i+1}=-\frac1{2h_i}.
\]
Here and below unspecified matrix entries vanish and the off-diagonal formula is symmetric. Jacobi is a scalar multiple of \(I\). The constant vector and the alternating-sign vector are eigenvectors of \(M\) with eigenvalues \((a+b)/2\) and \((a+b)/6\), respectively. Every row is strictly diagonally dominant, and Gershgorin's bounds are exactly these endpoints; therefore \(\kappa(JM)=3\).

For identity-weighted BRAS, group consecutive vertices into two-node unit cells. Their Fourier phases are \(\theta_k=2\pi k/(n/2)\), \(0\le k<n/2\). Write \(c=\cos\theta_k\), \(q=r+r^{-1}\), \(t=r-r^{-1}\), and \(u=4-c\in[3,5]\). The corresponding \(2\times2\) Bloch symbols of \(M\) and \(B_{\mathrm I}\) have respective diagonals \((a+b)/3\) and \(1/a+1/b\), with upper off-diagonal entries \((a+b e^{i\theta_k})/6\) and \(-(1/a+e^{i\theta_k}/b)/2\). Multiplying these symbols and calculating trace and discriminant yields the **complete** spectrum
\[
\lambda_\pm(u)=\frac12+\frac{qu\pm t\sqrt{u^2-9}}{12},
\qquad u=4-\cos\theta_k.
\]
Since \(q^2-t^2=4\), the lower branch is \(\ge1\) for all \(u\ge3\): the function \(qu-t\sqrt{u^2-9}\) has a minimum of \(6\) on \([3,\infty)\), attained at \(u=3q/2\) (with the endpoint understood for \(t=0\)). The upper branch increases strictly in \(u\), so its largest value is at \(u=5\), namely
\[
\lambda_{\max}(B_{\mathrm I}M)=\frac{(3r+1)^2}{12r}.
\]
The phase \(\theta=\pi\), hence \(u=5\), occurs because \(n/2\) is even. For \(1\le r\le3\), the preceding lower bound yields \(\kappa(B_{\mathrm I}M)\le(3r+1)^2/(12r)\le25/9\). For \(r\ge3\), the unconstrained lower-branch minimizer \(3q/2\) is at or beyond \(5\); differentiating shows that the lower branch is decreasing up to \(u=5\). Thus its smallest eigenvalue is also attained at \(\theta=\pi\), and equals \((r+3)^2/(12r)\). Dividing gives the stated exact \(r\ge3\) condition number. Since \((3r+1)/(r+3)\) is strictly increasing, it equals \(\sqrt3\) only at \(r=1+4/\sqrt3\), proving the strict reversal and its sharpness.

For diagonal-local-mass weighting, \(A_W=(a+b)I/3\). Exact assembly yields the identity
\[
\boxed{B_{\mathrm D}=\frac8{a+b}I-\frac{12}{(a+b)^2}M.}
\]
Therefore \(B_{\mathrm D}\) commutes with \(M\). On each Bloch cell, the mass eigenvalues are \(\mu_\pm=(a+b)/3\pm|a+b e^{i\theta}|/6\). Substitution into the polynomial \(\frac8{a+b}\mu-\frac{12}{(a+b)^2}\mu^2\) gives the same eigenvalue for both signs:
\[
\lambda_{\mathrm D}(\theta)=\frac43-\frac{|a+b e^{i\theta}|^2}{3(a+b)^2}.
\]
Its minimum \(1\) is at \(\theta=0\); its maximum \(\frac43-(a-b)^2/[3(a+b)^2]\) is at \(\theta=\pi\). Both phases occur. This yields the exact weighted condition number and both asymptotic limits.

## Verification

Run `python3 verify.py` from this extracted package. The checker uses standard-library exact rational arithmetic, assembles \(M,B_{\mathrm I},B_{\mathrm D}\) independently from local element blocks, verifies the polynomial identity and extremal Bloch eigenvectors for 40 mesh/contrast combinations, and checks the rational witness at \(r=4\). These finite tests are **not** an exhaustive argument for arbitrary mesh size or irrational contrast. The preceding Bloch-symbol derivation and calculus supply that proof.

## Relationship to prior work

Krzysik, Southworth and Wimmer (2026) introduce the original multiplicity-averaged broken-space mass inverse and prove general spectral bounds, with experiments demonstrating improvements over diagonal preconditioning on several finite-element families. The September 2026 primary seminar by Southworth explicitly studies degradation of **identity weights** under graded one-dimensional meshes and advocates **diagonal-local-mass weights** as a remedy. Thus neither the possibility of grading-induced deterioration nor the weighted remedy is claimed here as new. The additional, specific claim is the exact alternating-periodic finite-grid spectral calculation, the **sharp contrast threshold** at which original BRAS overtakes Jacobi in condition number, and the exact weighted counterpart which tends to unit conditioning. The general spectral bounds do not determine these sharp crossing values or this discrete Bloch spectrum. Nearby work on Gram-based multilevel preconditioning treats a different algorithm.

## Limitations

The result is confined to scalar one-dimensional \(P_1\) consistent-mass matrices on periodic **two-periodic** meshes with a number of elements divisible by four. For other mesh lengths, boundaries, higher-order elements, nonperiodic grading, or weighted choices other than those defined above, these exact formulas may not apply. Spectral condition numbers alone do not determine real computational cost or finite-iteration CG behavior. The full July 2026 preprint could not be retrieved in this examination; comparisons use material indexed from its technical sections and the publicly available 34-page September primary seminar. Consequently, an equivalent calculation elsewhere in that full preprint or less accessible literature remains a priority risk.

## References

1. O. A. Krzysik, B. S. Southworth, G. A. Wimmer, *Broken-space Additive Schwarz Mass Inverse Approximations and (Block) Preconditioning*, arXiv:2607.12138, first public 2026-07-13, https://arxiv.org/abs/2607.12138.
2. B. S. Southworth (joint work with O. Krzysik et al.), *BRoken-Space Additive Schwarz (BRAS) for Mass Matrix Preconditioning*, FEM@LLNL seminar slides, 2026-09-15, https://mfem.org/pdf/seminar/southworth2.pdf (particularly slides 6–8, 13–15 and 20).
3. O. A. Krzysik, B. S. Southworth, G. A. Wimmer, *A black-box, multilevel algebraic preconditioning framework for conforming finite elements*, arXiv:2607.07485, first public 2026-07-08, https://arxiv.org/abs/2607.07485 (distinct Gram/LS-AMG-DD approach).
