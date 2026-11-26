# A sharp Euclidean safety frontier for scalar-complement reduced-basis Richardson iteration

## Finding
Let \(n\ge 2\), \(a,b>0\), \(c\in\mathbb R^{n-1}\), and \(k=\|c\|_2\) satisfy \(k^2<ab\). Define the symmetric positive-definite star matrix and Type-II additive reduced-basis inverse by
\[
A=\begin{pmatrix}a&c^\mathsf T\\c&bI_{n-1}\end{pmatrix},\qquad
B_t=\begin{pmatrix}a^{-1}&0\\0&tI_{n-1}\end{pmatrix},\qquad t>0.
\]
The fixed-step Richardson error propagation is \(T_t=I-B_tA\); the residual propagation is \(T_t^\mathsf T\). Set
\[
q=\frac{k^2}{a^2},\quad K=b^2+k^2(1-q),\quad
 t_\pm=\frac{b\pm\sqrt{(1-q)(b^2-k^4/a^2)}}{K}
\]
when \(k<a\). The following is an exact classification, in every stated dimension.

1. **Spectral convergence:** \(\rho(T_t)<1\) precisely when \(0<t<2/(b+k^2/a)\). Its unique globally optimal complementary weight is \(t_{\rm sp}=1/b\), with \(\rho(T_{t_{\rm sp}})=k/\sqrt{ab}\).
2. **Euclidean error and residual safety:** A positive weight with \(\|T_t\|_2<1\) exists precisely when \(k<a\). In that case the complete set of strictly safe weights is \(t_-<t<t_+\). Both endpoints have induced norm exactly one. If \(k\ge a\), no positive weight is strictly Euclidean contractive, even though spectrally convergent weights always exist.
3. **Spectral-optimal versus Euclidean-safe selection:** At \(t_{\rm sp}=1/b\), \(\|T_{t_{\rm sp}}\|_2=\max\{k/a,k/b\}\). Accordingly, the spectral optimum is strictly Euclidean safe exactly when \(k<\min\{a,b\}\); when \(b\le k<a\), it is not strictly safe but another positive weight is; when \(k\ge a\), none is.

The spectral/Euclidean gap can be arbitrarily large at a fixed spectral rate. For every real \(R\ge1\), set \(a=1\), \(k=R\), \(b=2R^2\), \(n=2\), and \(t=1/b\). Then
\[
T_t=\begin{pmatrix}0&-R\\-1/(2R)&0\end{pmatrix},\qquad
T_t^2=\tfrac12 I_2,
\]
so \(\rho(T_t)=1/\sqrt2\), \(\|T_t^{2j}\|_2=2^{-j}\) and \(\|T_t^{2j+1}\|_2=R2^{-j}\) for all integers \(j\ge0\), while \(\|T_s\|_2\ge R\) for **every** positive complementary weight \(s\). Thus uniform asymptotic convergence does not imply one-step nonexpansion in the Euclidean error or residual norm.

## Assumptions and scope
All matrices are real, all algebra is exact, and \(B_t\) is held fixed across iterations. The reduced space is one-dimensional, spanned by the first coordinate, and the omitted block is the isotropic SPD block \(bI_{n-1}\). The strict Schur condition \(k^2<ab\) is necessary and sufficient for positive definiteness of \(A\). The reduced inverse \(B_t\) is precisely the Type-II correction \(P(P^\mathsf T AP)^{-1}P^\mathsf T+t(I-PP^\mathsf T)\) for \(P=e_1\). No claim is made for arbitrary omitted blocks, varying bases, non-SPD systems, or floating-point arithmetic.

A strict Euclidean contraction means a worst-case contraction for **every** nonzero error (or residual) at one step, not merely asymptotic convergence of each trajectory. Because \(A\) and \(B_t\) are symmetric, the error matrix \(T_t=I-B_tA\) and residual matrix \(I-AB_t=T_t^\mathsf T\) have equal Euclidean operator norm, though their action on a particular vector can differ.

## Proof
**Orthogonal reduction.** If \(k>0\), rotate the omitted coordinates so that \(c\) becomes \((k,0,\ldots,0)^\mathsf T\). The orthogonal similarity sends \(T_t\) to the direct sum of
\[
U_t=\begin{pmatrix}0&-k/a\\-kt&1-bt\end{pmatrix}
\]
and \((1-bt)I_{n-2}\). When \(k=0\), the same reduction holds with zero coupling. The block \(U_t\) dominates both the spectral radius and operator norm of the scalar complement block, so it suffices to analyze \(U_t\).

**Exact spectral range and unique optimum.** The eigenvalues of \(U_t\) are
\[
\lambda_\pm(t)=\frac{1-bt\pm\sqrt{(1-bt)^2+4k^2t/a}}2,
\]
and hence
\[
\rho(T_t)=\frac{|1-bt|+\sqrt{(1-bt)^2+4k^2t/a}}2.
\]
Write \(\eta=k^2/a\). Positive definiteness gives \(\eta<b\). The positive eigenvalue is strictly less than one for every \(t>0\), by comparing the square root with \(1+bt\). The negative eigenvalue is strictly greater than minus one precisely when \(t(b+\eta)<2\). This establishes the spectral interval, including exclusion of its endpoints. For \(0<t<1/b\), the spectral radius is \(\lambda_+(t)\). Implicit differentiation of \(\lambda_+^2-(1-bt)\lambda_+-\eta t=0\) gives
\[
\lambda_+'(t)=\frac{\eta-b\lambda_+(t)}{\sqrt{(1-bt)^2+4\eta t}}<0,
\]
where the inequality follows because evaluating its defining polynomial at \(\eta/b\) gives \((\eta/b)(\eta/b-1)<0\). For \(t>1/b\), the spectral radius is \(-\lambda_-(t)\), and the corresponding implicit derivative shows it strictly increases. If \(k=0\), the formula reduces to \(|1-bt|\), with the same unique minimizer. Substituting \(t=1/b\) gives the asserted optimum.

**Exact Euclidean safety window.** Compute the symmetric Gram deficit
\[
I_2-U_tU_t^\mathsf T=
\begin{pmatrix}
1-q&(k/a)(1-bt)\\
(k/a)(1-bt)&2bt-(b^2+k^2)t^2
\end{pmatrix}.
\]
Its determinant is the exact quadratic
\[
\det(I_2-U_tU_t^\mathsf T)=-q+2bt-Kt^2.
\]
Strict positivity of this matrix is equivalent to \(\|U_t\|_2<1\). Its leading principal minor is \(1-q\), so \(k<a\) is necessary. Under that assumption the discriminant after completing the square is
\[
b^2-qK=(1-q)(b^2-k^4/a^2)>0,
\]
using \(b>k^2/a\). Thus the determinant is positive exactly between the two stated real roots. They satisfy \(0\le t_-<t_+\), with equality \(t_-=0\) only when \(k=0\), and the leading minor remains positive throughout. At either finite endpoint the smallest eigenvalue of the Gram deficit is zero and the other is nonnegative, yielding induced norm exactly one. If \(k\ge a\), the fixed first row of \(U_t\) gives \(\|T_t\|_2\ge k/a\ge1\) for every \(t>0\). This proves necessity and sufficiency without a finite-grid search.

**Three selection regimes.** At the spectral optimum,
\[
U_{1/b}=\begin{pmatrix}0&-k/a\\-k/b&0\end{pmatrix},
\quad \|U_{1/b}\|_2=\max\{k/a,k/b\}.
\]
The stated regimes are the disjoint exhaustive cases for \(k\ge0\) subject to \(k^2<ab\). In the intermediate case \(b\le k<a\), the spectral optimizer is not strictly safe while the positive safety interval exists; the two other regimes follow directly. Finally, the explicit family has \(k^2=R^2<2R^2=ab\), so is SPD. Direct multiplication proves the parity identities. Since the first row has norm \(R\) for every weight, its one-step norm obstruction is universal within this family.

## Verification
A standalone Python 3 program, `verify.py`, computes the characteristic polynomial, the exact Gram determinant (using rational arithmetic), the two strict thresholds, numerical operator norms, and the two-step witness. Execute `python verify.py` without external packages. It reports 12,756 exact-rational determinant cases and 14,000 seeded floating-point diagnostics, plus rational/parity witnesses. These checks test the formulas but do not replace the above proof for all dimensions, real parameters, and positive weights.

## Relationship to prior work
Fan, Hu, and Zhang (2026) define the Type-II additive reduced-basis preconditioner in equation (3.5) and give nonsingularity results; their Richardson norm bound in Proposition 3.6 treats the Type-I construction. The present result keeps their Type-II inverse, but classifies its scalar complementary weight under a one-dimensional reduced space and an isotropic omitted SPD block. The point is the exact distinction between spectral convergence and worst-case Euclidean error/residual contraction, rather than existence of a nonsingular preconditioner.

Southworth, Sivas, and Rhebergen (2019/2020) analyze block-preconditioned fixed-point and Krylov convergence through Schur complements and give formulas for block-Jacobi powers. Pearson (2020) surveys block scaling and preconditioning. These broader references provide important context; they do not state the exact complementary-weight frontier, its three regimes, or the fixed-spectral-rate unbounded transient family. General Euclidean contraction and matrix-norm tests are standard background; no novelty is claimed for the individual two-by-two determinant identity or for spectral-radius theory.

## Limitations
The complete cutoff depends on the omitted block being a scalar multiple of the identity. For general SPD omitted blocks, this two-mode orthogonal reduction does not apply. The theorem does not assess FGMRES behavior, finite-precision error, or optimality of a changing reduced basis. Originality is supported by the compared published sources rather than a proof that no earlier specialized equivalent exists.

## References
1. X. Fan, Q. Hu, and S. Zhang, *Additive reduced basis preconditioners for large-scale parametrized PDEs*, arXiv:2609.11097v1, first posted 2026-09-10, especially Section 3 and Eq. (3.5). https://arxiv.org/abs/2609.11097
2. B. S. Southworth, A. A. Sivas, and S. Rhebergen, *On fixed-point, Krylov, and two-by-two block preconditioners for nonsymmetric problems*, arXiv:1911.02664, SIAM J. Matrix Anal. Appl. 41 (2020), 871–900, DOI 10.1137/19M1298317.
3. J. W. Pearson, *Preconditioners for Krylov subspace methods: An overview*, GAMM-Mitteilungen (2020), DOI 10.1002/gamm.202000015.
