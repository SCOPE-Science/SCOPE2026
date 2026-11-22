# Exact mode-switching thresholds for blended-mass multilinear wave elements

## Finding
For every integer \(d\geq1\), every orthotope with positive side lengths \(h_1,\ldots,h_d\), every wave speed \(c>0\), and every blend \(0\leq\alpha\leq1\), the standard \(2^d\)-node tensor-product multilinear finite element has a completely explicit generalized Laplacian spectrum under the convex blend of its exact consistent and row-sum-lumped mass matrices. Its largest generalized eigenvalue moves, as \(\alpha\) increases, through **every** cardinality of alternating-coordinate mode, in a strictly ordered sequence of sharp algebraic transition parameters. The resulting critical central-difference timestep has an exact finite-dimensional formula and a sharp distinction between partially and fully consistent mass at growing dimension.

Write \(r_1\geq\cdots\geq r_d>0\) for the ordered multiset \(\{h_1^{-2},\ldots,h_d^{-2}\}\) and \(s_k=\sum_{j=1}^k r_j\). Define
\[
\Lambda_k(\alpha)=\frac{12c^2s_k}{3^k(1-\alpha)+\alpha},\qquad 1\leq k\leq d,
\]
and for \(1\leq k<d\), define
\[
\alpha_k=\frac{3^k(2s_k-r_{k+1})}{3^k(2s_k-r_{k+1})+r_{k+1}},
\qquad\alpha_0=0,\quad\alpha_d=1.
\]
Then \(0<\alpha_1<\cdots<\alpha_{d-1}<1\) and
\[
\lambda_{\max}(\alpha)=\max_{1\leq k\leq d}\Lambda_k(\alpha).
\]
On every open interval \((\alpha_{k-1},\alpha_k)\), the unique *maximizing cardinality* is \(k\); at \(\alpha_k\), precisely the adjacent cardinalities \(k\) and \(k+1\) maximize. If side lengths are repeated, modes within a given cardinality can have ties. The maximizing \(k\)-coordinate modes select the \(k\) smallest side lengths (up to ties). In the cube \(h_1=\cdots=h_d=h\),
\[
\alpha_k=\frac{(2k-1)3^k}{1+(2k-1)3^k},
\]
so the three-dimensional cell switches one-coordinate \(\to\) two-coordinate \(\to\) three-coordinate highest-frequency modes at exactly \(3/4\) and \(27/28\).

For the undamped central-difference discretization of the element wave equation, restricted to the complement of its constant mode, all solutions are power bounded for all starting pairs **exactly** when
\[
0<\Delta t<\frac{2}{\sqrt{\lambda_{\max}(\alpha)}}.
\]
At equality a top-frequency scalar recurrence has a double multiplier \(-1\) and a linearly growing solution; above equality an exponentially growing solution exists. In a cube, for every fixed \(0\leq\alpha<1\) and every \(d\),
\[
\lambda_{\max}(\alpha)\leq\frac{4c^2}{(1-\alpha)h^2},
\]
whereas \(\lambda_{\max}(1)=12dc^2/h^2\). Thus fixed partial lumping has a dimension-independent element-level CFL scale, unlike the fully consistent mass case.

## Assumptions and scope
Let \(\Omega=\prod_{j=1}^d[0,h_j]\). Label its \(2^d\) vertices by bit vectors \(\varepsilon\in\{0,1\}^d\) and take the usual tensor-product \(Q_1\) Lagrange basis \(\phi_\varepsilon\). Define the exact matrices
\[
(M_C)_{\varepsilon\eta}=\int_\Omega\phi_\varepsilon\phi_\eta\,dx,
\qquad (K)_{\varepsilon\eta}=c^2\int_\Omega\nabla\phi_\varepsilon\cdot\nabla\phi_\eta\,dx.
\]
The row-sum lumping is \(M_L=\operatorname{diag}(M_C\mathbf 1)=(|\Omega|/2^d)I\). The **single element** mass is \(M_\alpha=(1-\alpha)M_L+\alpha M_C\), and the semidiscrete system is \(M_\alpha\ddot u+Ku=0\) without essential boundary constraints. No assertion is made about a globally assembled mesh or about elastic vector stiffness. All matrices are real symmetric, and \(M_\alpha\) is positive definite. Central difference means \(M_\alpha(u^{n+1}-2u^n+u^{n-1})/\Delta t^2+Ku^n=0\). The constant mode has zero stiffness and the expected free-particle drift; the power-boundedness assertion concerns the invariant \(M_\alpha\)-orthogonal mean-zero subspace.

## Proof
**1. One-dimensional diagonalization.** On a segment of length \(h\), the exact mass and stiffness blocks are
\[
M^{(h)}=\frac h6\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
K^{(h)}=\frac1h\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
Their common eigenvectors \((1,1)^{\mathsf T}\) and \((1,-1)^{\mathsf T}\) have mass eigenvalues \(h/2\) and \(h/6\), respectively; the stiffness eigenvalues are zero and \(2/h\), respectively.

**2. Complete generalized spectrum.** Tensorizing gives \(M_C=\bigotimes_j M^{(h_j)}\) and \(K=c^2\sum_j K^{(h_j)}\otimes\bigotimes_{i\ne j}M^{(h_i)}\), with tensor-factor ordering inherited from the vertices. Every Walsh sign vector \(v_S(\varepsilon)=(-1)^{\sum_{j\in S}\varepsilon_j}\) is a simultaneous eigenvector. Set \(V=|\Omega|\). Its consistent mass eigenvalue is \((V/2^d)3^{-|S|}\), its lumped mass eigenvalue is \(V/2^d\), and its stiffness eigenvalue is
\[
\frac{V}{2^d}\,3^{-|S|}\,12c^2\sum_{j\in S}h_j^{-2}.
\]
Dividing stiffness by blended mass yields, for every subset \(S\),
\[
\lambda_S(\alpha)=\frac{12c^2\sum_{j\in S}h_j^{-2}}{3^{|S|}(1-\alpha)+\alpha},
\]
including \(\lambda_\varnothing=0\). For a fixed nonzero cardinality \(k\), the numerator is maximal on the \(k\) largest reciprocal squared side lengths, yielding \(\Lambda_k\).

**3. Sharp consecutive crossings and all-cardinality dominance.** With \(D_k(\alpha)=3^k(1-\alpha)+\alpha\), the sign of \(\Lambda_k-\Lambda_{k+1}\) equals that of
\[
3^k(2s_k-r_{k+1})(1-\alpha)-r_{k+1}\alpha,
\]
which vanishes uniquely at \(\alpha_k\), changing sign from positive to negative. To establish the strict ordering, write \(\alpha_k/(1-\alpha_k)=3^k(2s_k/r_{k+1}-1)\). Because \(s_{k+1}=s_k+r_{k+1}\) and \(r_{k+2}\leq r_{k+1}\), this odds ratio strictly increases with \(k\). Hence \(\alpha_k\) are strictly increasing. For \(\alpha\in(\alpha_{k-1},\alpha_k)\), the successive comparisons imply \(\Lambda_1<\cdots<\Lambda_k>\cdots>\Lambda_d\), with the analogous two-way tie only at a transition. For equal side lengths \(s_k=kh^{-2}\), giving the stated cube thresholds.

**4. Exact central-difference boundary.** Every nonconstant Walsh mode obeys \(z_{n+1}-(2-\lambda_S\Delta t^2)z_n+z_{n-1}=0\). Its two roots are distinct and on the unit circle exactly when \(0<\lambda_S\Delta t^2<4\); at \(\lambda_S\Delta t^2=4\), the repeated root \(-1\) has a generalized solution \(n(-1)^n\), and above 4 one root has magnitude greater than one. The finite system is diagonalized by the Walsh basis, so the largest \(\lambda_S\) gives the necessary and sufficient strict bound for power boundedness of every mean-zero starting pair. Finally, for the cube and \(\alpha<1\), use \(k/3^k\leq1/3\) to get \(\Lambda_k\leq4c^2/[(1-\alpha)h^2]\). At \(\alpha=1\), every denominator is one, and \(\Lambda_d=12dc^2/h^2\).

## Verification
The accompanying dependency-free `CHECK.py` constructs all exact tensor-product element matrices using rational arithmetic for dimensions \(1\) through \(4\), several anisotropic side-length choices, and blend parameters including the analytically derived switching boundaries. It checks every Walsh generalized eigenvalue, the maximizing-cardinality formula, every adjacent-branch comparison, and the exact three-dimensional cube boundaries. Run `python3 CHECK.py` in the same directory. The script reports `VERIFY_OK 8751`; these finite checks corroborate but do not replace the all-dimension analytical proof above.

## Relationship to prior work
Wang, Leung, Yang and Li (arXiv:2610.27715v1, 20 October 2026) develop mass-lumped, partially explicit multiscale wave time stepping and establish energy stability in decomposition-specific auxiliary spaces. They do not analyze convex consistent/lumped mixing on one tensor-product \(Q_1\) orthotope, its exact Walsh spectrum or its sequence of switching cardinalities. Voet, Sande and Buffa (arXiv:2502.00452v1, 1 February 2025) study mass lumping and stabilization in trimmed isogeometric analysis, focusing especially on low-frequency accuracy. Bioli and Voet (arXiv:2410.17857v1, 23 October 2024) derive sharp bounds for lumped-mass immersed spectra, while Deng and Calo (arXiv:1711.02979, 8 November 2017) study dispersion-minimized tensor-product spline mass. Those spectral tools and the standard CFL relationship are prior work. The contribution here is a distinct exact **finite-element mixed-mass phase diagram**, covering every dimension and anisotropic side-length vector; it is not an extension of the cited papers' stability theorems to their discretization classes.

## Limitations
The result is confined to the scalar, constant-coefficient, unassembled \(Q_1\) orthotope and an affine blend of exact consistent and row-sum-lumped masses. Its modes are element-local Walsh modes; boundary constraints, interelement assembly, numerical quadrature, distorted hexahedra, arbitrary multiscale bases, and elastic tensor couplings change the matrices. For \(\alpha>0\), the blended mass is generally not diagonal: an element-level CFL improvement does **not** by itself imply a cheap fully explicit implementation. Nor does the largest-eigenvalue result prove small dispersion error, computational optimality or an improved global simulation. Prior-art searches cannot certify universal first discovery. No independent mathematical audit has been performed.

## References
1. Y. Wang, W. T. Leung, Z. Yang, S. Li, *Multi-time-stepping splitting scheme with mass lumping for the multiscale wave equation*, arXiv:2610.27715v1 (first public 20 October 2026), https://arxiv.org/abs/2610.27715.
2. Y. Voet, E. Sande, A. Buffa, *Mass lumping and stabilization for immersogeometric analysis*, arXiv:2502.00452v1 (1 February 2025), https://arxiv.org/abs/2502.00452.
3. I. Bioli, Y. Voet, *A theoretical study on the effect of mass lumping on the discrete frequencies in immersogeometric analysis*, arXiv:2410.17857v1 (23 October 2024), https://arxiv.org/abs/2410.17857.
4. Q. Deng, V. Calo, *Dispersion-minimized mass for isogeometric analysis*, arXiv:1711.02979 (8 November 2017), https://arxiv.org/abs/1711.02979.
