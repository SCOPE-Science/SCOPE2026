# Arithmetic–harmonic contrast controls the complete BRAS spectrum on metric stars

## Finding
Let \(k\ge3\) metric-graph arms of positive lengths \(\ell_1,\ldots,\ell_k\) meet at one hub. Discretize every arm by one conforming piecewise-linear finite element, retaining the hub and all leaf degrees of freedom. Let \(M\) be the assembled *consistent* mass matrix, \(B\) the original multiplicity-averaged broken-space additive Schwarz (BRAS) approximate inverse, and \(J=\operatorname{diag}(M)^{-1}\) the Jacobi inverse. Then the entire spectrum, counting algebraic multiplicity, is
\[
\operatorname{spec}(BM)=\left\{1,1,\underbrace{\tfrac43,\ldots,\tfrac43}_{k-2},\frac{4}{3k^2}\left(\sum_{i=1}^k\ell_i\right)\left(\sum_{i=1}^k\frac1{\ell_i}\right)\right\},
\]
where the repeated \(4/3\) level coalesces with the last eigenvalue when all arms are equal. Moreover,
\[
\kappa_2(B^{1/2}MB^{1/2})=\frac{4}{3k^2}\left(\sum_i\ell_i\right)\left(\sum_i\ell_i^{-1}\right),\qquad
\operatorname{spec}(JM)=\{\tfrac12,\underbrace{1,\ldots,1}_{k-1},\tfrac32\},\quad\kappa_2(J^{1/2}MJ^{1/2})=3.
\]
Here the symmetric-preconditioned condition numbers are equivalently the ratios of extreme positive eigenvalues of \(BM\) and \(JM\), respectively.

Writing \(R=(\max_i\ell_i)/(\min_i\ell_i)\), the **sharp uniform contrast safeguard across all metric stars** is
\[
R\le R_*:=\frac{7+3\sqrt5}{2}=6.854101966\ldots.
\]
Under this restriction BRAS is never worse conditioned than Jacobi; for \(R<R_*\) it is strictly better. This contrast bound is sharp even among genuinely branched stars: four arms of lengths \((1,1,R,R)\) give equality at \(R=R_*\) and BRAS strictly worse for every \(R>R_*\). No step-size, PDE solution, or conjugate-gradient running-time statement is asserted.

## Assumptions and scope
Each arm is a separate length-parametrized interval of length \(\ell_i>0\) with a common continuous hub value and a separate leaf value. No boundary degrees of freedom are eliminated. The local element mass is exactly
\[
M_i=\frac{\ell_i}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
The injection \(P\) copies each conforming value to its element-local copies, and its multiplicity matrix is \(D=P^\mathsf{T}P=\operatorname{diag}(k,1,\ldots,1)\) in hub-first ordering. The BRAS definition used here is exactly
\[
B=D^{-1}P^\mathsf{T}\operatorname{diag}(M_1^{-1},\ldots,M_k^{-1})PD^{-1}.
\]
This is the *original multiplicity weighting*, not local-mass weighting. All matrices are exact real matrices and all condition numbers refer to positive eigenvalue ratios under symmetric preconditioning, not the nonsymmetric Euclidean singular-value condition number of \(BM\).

## Proof
Put \(L=\operatorname{diag}(\ell_1,\ldots,\ell_k)\), \(e=(1,\ldots,1)^\mathsf{T}\), \(a=L^{-1}e\), \(h=Le\), \(S=e^\mathsf{T}h\), \(T=e^\mathsf{T}a\), and \(\mu=4ST/(3k^2)\). Direct assembly and inversion of the positive local mass blocks give
\[
M=\frac16\begin{pmatrix}2S&h^\mathsf{T}\\h&2L\end{pmatrix},\qquad
B=2\begin{pmatrix}2T/k^2&-a^\mathsf{T}/k\\-a/k&2L^{-1}\end{pmatrix}.
\]
These formulas also show positive definiteness: \(M\) is the Gram matrix of the linearly independent global nodal basis, and \(B\) is the sum of positive local inverse quadratic forms under a full-column-rank injection. Multiplication gives
\[
BM=\begin{pmatrix}
\mu-\tfrac13&\tfrac{2T}{3k^2}h^\mathsf{T}-\tfrac{2}{3k}e^\mathsf{T}\\
\tfrac23e-\tfrac{2S}{3k}a&\tfrac43I-\tfrac1{3k}ah^\mathsf{T}
\end{pmatrix}.
\]
The two independent vectors \((0,a)^\mathsf{T}\) and \((1,-2e+(2S/k)a)^\mathsf{T}\) are fixed by \(BM\), by substitution in this displayed formula. If the lengths are not all equal, \(e\) and \(h\) are linearly independent. Therefore the \((k-2)\)-dimensional subspace \(\{(0,z)^\mathsf{T}:e^\mathsf{T}z=h^\mathsf{T}z=0\}\) consists of \(4/3\)-eigenvectors. The trace equals \(\mu+2+4(k-2)/3\), so the last eigenvalue is \(\mu\). Since \(BM\) is similar to the symmetric positive-definite matrix \(B^{1/2}MB^{1/2}\), it is diagonalizable. When all lengths coincide, continuity of characteristic polynomials (or direct substitution in the block formula) gives the same multiset. By Cauchy–Schwarz, \(ST\ge k^2\), with equality only for equal lengths. Thus \(\mu\ge4/3>1\), proving the exact BRAS condition number.

For Jacobi, the diagonally symmetrized mass matrix is
\[
J^{1/2}MJ^{1/2}=I_{k+1}+\frac12\begin{pmatrix}0&v^\mathsf{T}\\v&0_{k\times k}\end{pmatrix},\qquad
v_i=\sqrt{\ell_i/S},\qquad \|v\|_2=1.
\]
Its spectrum is exactly \(\{1/2,1^{(k-1)},3/2\}\), giving condition number \(3\).

For the contrast threshold, let \(m=\min_i\ell_i\), \(M_*=\max_i\ell_i=Rm\), and \(X=S/k\), \(Y=T/k\). Since \((\ell_i-m)(M_*-\ell_i)\ge0\), each arm satisfies \(\ell_i+mM_*/\ell_i\le m+M_*\). Averaging and applying AM–GM gives
\[
4mM_*XY\le (X+mM_*Y)^2\le(m+M_*)^2,
\]
whence \(\mu\le(R+1)^2/(3R)\). Equality holds for any even number of arms split equally between \(m\) and \(M_*\), in particular for four arms. The inequality \((R+1)^2/(3R)\le3\) is equivalent to \(R^2-7R+1\le0\). Its only root at or above one is \(R_*=(7+3\sqrt5)/2\), giving the stated sharp all-star comparison.

## Verification
The accompanying `check_star.py` uses standard-library exact rational arithmetic to assemble the global mass and original BRAS matrices independently from local element blocks. It compares the full characteristic polynomials of \(BM\) and \(JM\) with the claimed factorizations for 53 rational instances (degrees three through seven, including unequal arms). It also confirms exact equal-arm and four-/six-arm balanced two-length examples, including \(\kappa(BM)=121/30>3\) for \(\ell=(1,1,10,10)\). The checker exits with an assertion failure on any discrepancy. These finite diagnostics corroborate but do not replace the arbitrary-degree algebraic proof above.

## Relationship to prior work
Krzysik, Southworth, and Wimmer introduce precisely the multiplicity-weighted broken-space inverse, prove general positive-definiteness and spectral-projector bounds, and report condition-number improvements over diagonal scaling on tested two- and three-dimensional meshes. The present result specializes the algebra to a metric-star finite-element mass matrix and **evaluates every eigenvalue and the sharp competing Jacobi criterion**, neither of which follows numerically from their general projector expression without a separate star-specific spectral calculation. The classical scalar Kantorovich inequality explains the final maximum/minimum-arm contrast estimate once the exact spectrum has been derived; it is not claimed as a new inequality.

A separate alternating-periodic one-dimensional mass-mesh analysis identifies deterioration for periodic degree-two meshes with a two-length pattern. It neither treats a variable-degree hub nor supplies the full arbitrary-arm star spectrum; the geometries and threshold statements are different. No claim is made of uniqueness among all preconditioner comparisons, and equivalent unpublished or inaccessible analyses could predate this exact formula.

## Limitations
The classification assumes one linear element per metric-graph arm, an uneliminated central and leaf degree of freedom, and original multiplicity-based BRAS. It does not cover subdivided stars, general trees, higher-order elements, mass-lumping, local-mass-weighted variants, or the cost of applying a preconditioner. The contrast safeguard is uniform across all stars, not the sharp fixed-degree restriction for every individual odd \(k\). The related primary arXiv preprint was only accessible in indexed text excerpts of its definitions and spectral theory during the literature comparison; its inaccessible parts, together with later presentations on strongly nonuniform meshes, remain residual priority risks. These limitations do not enter the algebraic proof.

## References
1. O. A. Krzysik, B. S. Southworth, and G. A. Wimmer, *Broken-space Additive Schwarz Mass Inverse Approximations and (Block) Preconditioning*, arXiv:2607.12138, first released 2026-07-13. https://arxiv.org/abs/2607.12138
2. B. S. Southworth, *BRoken-Space Additive Schwarz (BRAS) for Mass Matrix Preconditioning*, FEM@LLNL seminar, 2026-09-15. https://mfem.org/seminar/
3. *Kantorovich inequality*, classical scalar bound for positive numbers. https://en.wikipedia.org/wiki/Kantorovich_inequality
4. *MetricGraph* documentation, finite-element mass and stiffness assembly on metric graphs. https://davidbolin.github.io/MetricGraph/reference/metric_graph.html
