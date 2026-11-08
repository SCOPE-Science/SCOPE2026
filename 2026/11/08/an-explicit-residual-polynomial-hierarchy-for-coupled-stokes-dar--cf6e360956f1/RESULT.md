# An explicit residual-polynomial hierarchy for coupled Stokes–Darcy block preconditioning

## Finding
Let \(K\) be the three-block saddle-point matrix and \(Q_\alpha\) its ideal coupled preconditioner defined below. For every positive \(\alpha\), the nonnormal right-preconditioned operator \(T_\alpha=KQ_\alpha^{-1}\) admits the explicit residual polynomials
\[
 p_m(t)=(1-t^2)(1-t)^{m-2},\qquad m=2,3,\ldots.
\]
Their exact values on \(T_\alpha\) have only the last block row nonzero, and yield an unconditional residual estimate for exact-arithmetic, unrestarted GMRES:
\[
 \frac{\|r_m\|_2}{\|r_0\|_2}\le M_\alpha\left(\frac{\alpha}{\mu+\alpha}\right)^{m-1}\quad(m\ge2).
\]
Here \(\mu>0\) is the smallest eigenvalue of the symmetric part of the positive-real second Schur complement, and \(M_\alpha\) is an explicitly defined block-operator norm. The same factor bounds one full cycle of restarted GMRES with restart length \(m\). For every fixed matrix and \(m\ge2\), this estimate is \(O(\alpha^{m-1})\) as \(\alpha\downarrow0\). The \(O(\alpha)\) order for two steps is in general unimprovable, even in dimension three.

## Assumptions and scope
All spaces are real Euclidean spaces. Let \(d,v,p\) be positive integers, \(A_d\in\mathbb R^{d\times d}\) be nonsingular, \(A_s\in\mathbb R^{v\times v}\), \(G\in\mathbb R^{v\times d}\), and \(B\in\mathbb R^{p\times v}\) have full row rank. Put
\[
 S_1=A_s+GA_d^{-1}G^T,\qquad S_2=BS_1^{-1}B^T.
\]
Assume the symmetric part \(H(S_1)=(S_1+S_1^T)/2\) is positive definite. This implies that \(S_1\) and \(S_2\) are nonsingular and \(H(S_2)\succ0\). Set \(\mu=\lambda_{\min}(H(S_2))>0\). Define, for any \(\alpha>0\),
\[
 K=\begin{bmatrix}A_d&G^T&0\\G&-A_s&B^T\\0&B&0\end{bmatrix},\quad
 Q_\alpha=\begin{bmatrix}A_d&G^T&0\\0&S_1&-B^T\\0&B&\alpha I_p\end{bmatrix},\quad T_\alpha=KQ_\alpha^{-1}.
\]
Define the dimension-compatible matrices
\[
 X=GA_d^{-1},\qquad Z=BS_1^{-1},\qquad E_\alpha=\alpha(S_2+\alpha I_p)^{-1},
\]
and the explicitly computable factor
\[
 M_\alpha=\left\|\begin{bmatrix}-ZX&E_\alpha Z&2I_p-E_\alpha\end{bmatrix}\right\|_2,
 \qquad q_\alpha=\frac{\alpha}{\mu+\alpha}<1.
\]
The residual \(r_m\) refers to the original right-preconditioned system \(KQ_\alpha^{-1}y=b\) in the ordinary Euclidean norm, with an arbitrary initial guess and initial residual \(r_0\). The corresponding physical solution is \(x=Q_\alpha^{-1}y\). No inexact block inverses, flexible preconditioning, or rounding error is included.

## Proof
**1. Positivity and invertibility.** The standard inverse identity, valid for nonsymmetric real matrices, gives
\[
 H(S_1^{-1})=S_1^{-T}H(S_1)S_1^{-1}\succ0.
\]
Consequently \(H(S_2)=BH(S_1^{-1})B^T\succ0\) because \(B\) has full row rank. For every \(\alpha>0\), \(S_2+\alpha I_p\) is nonsingular. For \(u=(S_2+\alpha I_p)^{-1}w\),
\[
 (\mu+\alpha)\|u\|_2^2\le u^T(S_2+\alpha I_p)u\le\|u\|_2\|w\|_2,
\]
so \(\|E_\alpha\|_2\le q_\alpha<1\). Block elimination also makes \(Q_\alpha\) invertible.

**2. Exact right-preconditioned block identity.** Directly multiplying \(K\) by the block inverse of \(Q_\alpha\) gives
\[
 T_\alpha=\begin{bmatrix}I_d&0&0\\X&-I_v&0\\0&E_\alpha Z&I_p-E_\alpha\end{bmatrix}.
\]
In particular, for \(m=2\),
\[
 I-T_\alpha^2=\begin{bmatrix}0&0&0\\0&0&0\\-E_\alpha ZX&E_\alpha^2 Z&E_\alpha(2I_p-E_\alpha)\end{bmatrix}.
\]
Since
\[
 I-T_\alpha=\begin{bmatrix}0&0&0\\-X&2I_v&0\\0&-E_\alpha Z&E_\alpha\end{bmatrix},
\]
induction by right multiplication with \(I-T_\alpha\) gives for every integer \(m\ge2\) the exact identity
\[
 \boxed{p_m(T_\alpha)=
 \begin{bmatrix}
 0&0&0\\0&0&0\\
 -E_\alpha^{m-1}ZX&E_\alpha^m Z&E_\alpha^{m-1}(2I_p-E_\alpha)
 \end{bmatrix}.}
\]
No diagonalizability or normality is used. Equivalently, the nonzero row is
\(E_\alpha^{m-1}\begin{bmatrix}-ZX&E_\alpha Z&2I_p-E_\alpha\end{bmatrix}\).

**3. GMRES residuals and restarts.** Since \(p_m(0)=1\) and \(\deg p_m=m\), its action on \(r_0\) is an admissible GMRES residual candidate. Thus residual minimization gives
\[
 \|r_m\|_2\le\|p_m(T_\alpha)r_0\|_2\le\|E_\alpha^{m-1}\|_2 M_\alpha\|r_0\|_2
 \le M_\alpha q_\alpha^{m-1}\|r_0\|_2.
\]
Every new cycle of restarted GMRES of length \(m\) starts with a new residual but the same matrix, and the same polynomial is admissible. Therefore its cycle-boundary residuals \(r^{(j)}\) satisfy \(\|r^{(j)}\|_2\le(M_\alpha q_\alpha^{m-1})^j\|r^{(0)}\|_2\). For any fixed blocks, \(M_\alpha\) remains bounded as \(\alpha\downarrow0\) (indeed \(E_\alpha\to0\)), and \(q_\alpha=O(\alpha)\). Since \(q_\alpha<1\), for any fixed \(\alpha\) a sufficiently large finite restart length guarantees a contraction factor strictly smaller than one. This is a theoretical sufficient guarantee, not an assertion of mesh- or parameter-uniform restart lengths.

**4. Exact two-step obstruction.** Set \(d=v=p=1\), \(A_d=A_s=B=[1]\), and \(G=[0]\). Then \(S_1=S_2=[1]\), \(\mu=1\), and with \(e=\alpha/(1+\alpha)\),
\[
 T_\alpha=\begin{bmatrix}1&0&0\\0&-1&0\\0&e&1-e\end{bmatrix}.
\]
Choose initial residual \(r_0=(1,1,1)^T\). The distance from \(r_0\) to the two-dimensional span of \(T_\alpha r_0\) and \(T_\alpha^2r_0\), computed by a scalar Gram determinant (or a cross product), is precisely
\[
 \boxed{\|r_2\|_2^2=\frac{2\alpha^2}{1+\alpha+\alpha^2}.}
\]
Thus \(\|r_2\|_2/\|r_0\|_2\sim\sqrt{2/3}\,\alpha\), showing the two-step \(O(\alpha)\) power cannot uniformly be replaced by \(o(\alpha)\) under these assumptions. This example does not claim sharpness of the bound's numerical constant or the power at \(m>2\).

## Verification
A standalone Python 3 script, `verify.py`, uses NumPy and SymPy. It tests the explicit preconditioned block matrix, the polynomial identity through degree eight, the matrix-norm bound, and GMRES residual minimization on random positive-definite samples. It also symbolically verifies the scalar identity for twelve powers and the exact two-step residual formula. The script's supplementary assertions passed; the proof of the infinite family is the analytic induction and norm argument above, **not** the finite tests. Execute `python verify.py` in the extracted files' directory with NumPy and SymPy installed.

## Relationship to prior work
Chao and Li (2026), Theorem 8, give the ideal coupled preconditioner's block preconditioned form and its eigenvalue information and explicitly note that nonnormality prevents extracting a GMRES convergence rate from eigenvalues alone. The present observation uses that block form but supplies explicit degree-by-degree *residual-polynomial* identities, a quantitative geometric GMRES bound (including restarted cycles), and an exact first-order obstruction. It does not assert that the block preconditioner itself or the standard GMRES polynomial principle is new. Southworth, Sivas and Rhebergen (2020) establish general GMRES/Schur-complement equivalences for several two-by-two block preconditioners, motivating the polynomial approach; their general results do not state the above formula for this three-block regularized coupled operator. Greif and He (2023) investigate different block preconditioners for the same discretization. These comparisons are not a proof of historical priority.

## Limitations
The analysis requires the *ideal*, exactly inverted \(Q_\alpha\), strictly positive symmetric part of \(S_1\), and full row rank \(B\). It is not a guarantee for the source paper's inexact practical preconditioner or arbitrary three-by-three saddle-point systems. The constant \(M_\alpha\) and \(\mu\) may depend on discretization and physical parameters; mesh-independent convergence requires separate uniform estimates. The bound is sufficient, not a sharp worst-case estimate at all iterations. The scalar example proves sharpness only of the two-step asymptotic power in \(\alpha\). General historical novelty remains subject to broader literature checks and independent review.

## References
1. Z. Chao and T. Li, *An efficient coupled block preconditioner for the Marker-and-Cell discretization of the Stokes-Darcy equations*, arXiv:2610.34692v1, first public October 26, 2026. https://arxiv.org/abs/2610.34692
2. B. S. Southworth, A. A. Sivas and S. Rhebergen, *On fixed-point, Krylov, and 2 × 2 block preconditioners for nonsymmetric problems*, arXiv:1911.02664, 2020. https://arxiv.org/abs/1911.02664
3. C. Greif and Y. He, *Block Preconditioners for the Marker-and-Cell Discretization of the Stokes–Darcy Equations*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 1540–1565. https://doi.org/10.1137/22M1518384
4. F. P. A. Beik and M. Benzi, *Preconditioning techniques for the coupled Stokes–Darcy problem: spectral and field-of-values analysis*, Numerische Mathematik (2022). https://doi.org/10.1007/s00211-021-01267-8
