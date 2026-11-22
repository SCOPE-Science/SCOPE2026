# A sharp noncommuting stability frontier for restarted two-level optimization

## Finding
Let \(F\) and \(\Psi\) be real symmetric matrices satisfying \(0\prec F\prec I\) and \(0\prec\Psi\prec I\), with no commutation assumption. In the one-sweep, FCF-relaxed two-level iteration described below, let \(V_j\) denote the linear map from the initial error to the last coarse point after \(j\) coarse intervals. Then
\[
 V_j=F+\sum_{k=0}^{j-2}\Psi^k(F^2-F),\qquad
 V_\infty=(I-\Psi)^{-1}(F-\Psi)F.
\]
(The sum is empty for \(j=1\).) All eigenvalues of \(V_\infty\) are real and strictly less than \(1\), and the repeated-restart iteration \(x^{(r+1)}=V_\infty x^{(r)}\) converges to zero from every initial error if and only if
\[
 \boxed{\ \Psi\prec (I+F^2)(I+F)^{-1}.\ }
\]
If the difference on the right is merely positive semidefinite and singular, the limiting restart map has eigenvalue \(-1\). If the difference is not positive semidefinite, it has an eigenvalue strictly less than \(-1\).

This boundary has a sharp two-dimensional angular form. For
\[
 F=\operatorname{diag}(1/2,3/4),\quad
 \Psi_\theta=R_\theta\operatorname{diag}(4/5,7/8)R_\theta^{\mathsf T},\quad
 R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\]
the limiting restart is convergent from every start exactly when \(\sin^2\theta<2/15\). Both component propagators remain symmetric, positive definite and strictly contractive at every angle. At \(\theta=\pi/4\), the restart spectral radius exceeds \(1\) while at \(\theta=0\) it equals \(3/4\).

## Assumptions and scope
Work in any finite-dimensional real Euclidean space, with strict Loewner inequalities in the standard inner product. Let \(m\ge2\) be the number of fine steps per coarse interval. The homogeneous fine propagator \(\Phi\) has \(\Phi^m=F\) and the coarse propagator is \(\Psi\). Begin the first approximation on each new trajectory by copying the initial error to all coarse points; apply one exact two-level MGRIT sweep with FCF relaxation and exact coarse-grid solve; use the last corrected coarse point as the next restart's initial error. The error origin is the fixed point of the underlying affine iteration, so homogeneous error propagation suffices.

The setting allows \(\Psi F\ne F\Psi\). It is realizable by standard strictly convex quadratic models: for \(m=2\), set \(\Phi=F^{1/2}\), an exact unit-step gradient-descent propagator for positive definite Hessian \(I-\Phi\), and \(\Psi=(I+2B)^{-1}\), an implicit/proximal coarse propagator with positive definite Hessian \(B=(\Psi^{-1}-I)/2\). The fine and coarse quadratic models need not have identical eigenspaces. The theorem concerns the long-trajectory limit of a single sweep followed by repeated restarts, not convergence of MGRIT inner iterations to a fixed trajectory.

## Proof
**Endpoint recurrence.** At the beginning of each sweep, all coarse-point errors equal the input \(x\). After FCF relaxation, the first coarse error is \(Fx\), and every later coarse error is also \(Fx\). Consequently, the defect of the exact fine-grid C-point equations at the first coarse point vanishes, while each later defect equals \((F^2-F)x\). The exact coarse correction is forward substitution in the lower-bidiagonal coarse matrix with subdiagonal \(-\Psi\). Thus the corrected errors obey \(V_1x=Fx\), \(V_jx=\Psi V_{j-1}x+(F-\Psi)Fx\), equivalently
\[
 V_j=F+\sum_{k=0}^{j-2}\Psi^k(F^2-F).
\]
Since \(\|\Psi\|_2<1\), this converges in operator norm to
\[
 V_\infty=F-(I-\Psi)^{-1}F(I-F)
 =(I-\Psi)^{-1}(F-\Psi)F.
\]
No factors have been commuted in deriving these identities.

**Real spectrum and sharp equivalence.** Define \(D=F(I-F)\succ0\) and \(C=I-\Psi\succ0\). The similarity
\[
 D^{1/2}V_\infty D^{-1/2}
 =F-D^{1/2}C^{-1}D^{1/2}=:H
\]
makes the spectrum real. Since \(H\prec F\prec I\), every eigenvalue is below \(1\). Therefore \(\rho(V_\infty)<1\) exactly when \(H\succ-I\), or equivalently
\[
 I+F\succ D^{1/2}C^{-1}D^{1/2}.
\]
Taking the Schur complement of \(C\) in the symmetric block matrix with diagonal blocks \(I+F,C\) and off-diagonal \(D^{1/2}\) gives the equivalent condition
\[
 C\succ D^{1/2}(I+F)^{-1}D^{1/2}.
\]
The factors \(D^{1/2}\), \(F\), and \((I+F)^{-1}\) commute since they are functions of \(F\). Hence this becomes
\[
 I-\Psi\succ F(I-F)(I+F)^{-1}
 \quad\Longleftrightarrow\quad
 \Psi\prec (I+F^2)(I+F)^{-1}.
\]
In the non-strict comparison, congruence and Schur complements preserve the number of negative or zero eigenvalues, proving the boundary statement about \(-1\), including multiplicities.

**Exact angle threshold.** The matrix in the boxed inequality is \(G=\operatorname{diag}(5/6,25/28)\). Direct multiplication gives
\[
 \operatorname{tr}(G-\Psi_\theta)=\frac{43}{840}>0,\qquad
 \det(G-\Psi_\theta)=\frac{2-15\sin^2\theta}{3360}.
\]
For symmetric \(2\times2\) matrices, strictly positive trace and determinant characterize positive definiteness. At zero angle \(V_\infty=-3I/4\). At \(\theta=\pi/4\),
\[
 V_\infty=\begin{pmatrix}-9/8&9/32\\3/8&-15/32\end{pmatrix},
 \qquad\operatorname{spec}(V_\infty)=\left\{\frac{-51\pm3\sqrt{97}}{64}\right\}.
\]
The smaller eigenvalue is below \(-1\), proving actual divergence along a nonzero eigenvector. Both \(F\) and \(\Psi_\theta\) retain eigenvalues in \((0,1)\) for all angles. A nontrivial eigenspace rotation requires dimension at least two, so this obstruction is dimension-minimal.

## Verification
Run \(\texttt{python3 check.py}\) with Python 3 standard library. The standalone checker uses exact rational arithmetic, confirms the matrix identities and angular determinant, and checks the endpoint recurrence independently by explicit coarse-defect forward substitution for \(1\le j\le7\) over 1,400 seeded randomly selected strictly contractive positive-definite two-by-two examples, giving 9,800 finite endpoint checks. It also independently compares the Loewner test with the Schur test on those cases. The dimension-independent theorem and the strict boundary follow from the preceding analytic proof, not from those finite checks.

## Relationship to prior work
Araújo, Krzysik and De Sterck introduce multi-trajectory restarted MGRIT optimization, and derive a long-trajectory endpoint formula under their simultaneously diagonalizable fine/coarse assumption [1, Section 4.5]. The endpoint setup is theirs. The contribution here is the noncommuting symmetric-positive-definite extension, an all-dimensional necessary-and-sufficient Loewner-order criterion, and an exact angle-driven loss of restart stability. Southworth [2] supplies broad temporal approximation conditions for convergence of MGRIT/Parareal *inner space-time error iterations*, including noncommuting propagators. Those inner-iteration bounds are distinct from the repeated-restart last-point map studied here, and are not asserted to be new. No claim is made that other temporal-approximation estimates cannot be specialized to recover this result.

## Limitations
Only constant linear propagators that are symmetric positive-definite contractions, exact two-level coarse solves, FCF relaxation, and the long-trajectory endpoint limit are considered. The explicit angle threshold is for one specified two-dimensional pair. The result does not cover finite precision, changing coarse models, stochastic errors, general nonsymmetric propagators, or computational speedup. The source assumes simultaneous diagonalization whereas the present theorem deliberately allows rotated coarse eigenspaces. It does not establish historical priority against unindexed or unavailable earlier work. It has not received independent mathematical audit.

## References
[1] G. H. M. Araújo, O. A. Krzysik, H. De Sterck, *Multi-Trajectory Parallel-in-Iteration Optimization*, arXiv:2611.03621v1 (first public November 2, 2026), https://arxiv.org/abs/2611.03621 .

[2] B. S. Southworth, *Necessary Conditions and Tight Two-level Convergence Bounds for Parareal and Multigrid Reduction in Time*, arXiv:1810.07292v5, https://arxiv.org/html/1810.07292v5 .

[3] Y. Jin, Q. Lin, Z. Zhou, *Optimizing Coarse Propagators in Parareal Algorithms*, arXiv:2311.15320, https://arxiv.org/abs/2311.15320 .
