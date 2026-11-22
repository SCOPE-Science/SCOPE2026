# A sharp square-root weighting threshold for two-cell broken-space mass preconditioning

## Finding
Consider the complete conforming piecewise-linear mass matrix on two adjacent intervals. With independent positive element-constant averaging weights, the weighted broken-space additive Schwarz (BRAS) inverse has a complete three-eigenvalue spectrum, a **unique** best relative weight, and an exact critical exponent for contrast-uniform conditioning. With interval-length ratio \(r>0\), weight ratio \(w>0\), and every node retained, its spectrum is
\[
\operatorname{spec}(B_wM)=\left\{1,1,\Lambda(r,w)\right\},\quad
\Lambda(r,w)=\frac{4(r+1)(r+w^2)}{3r(1+w)^2}
=\frac43\left(1+\frac{(w-r)^2}{r(1+w)^2}\right).
\]
The spectral condition number equals \(\Lambda(r,w)\), and is uniquely minimized over \(w>0\) by \(w=r\), at the contrast-independent value \(4/3\). In the power family \(w=r^\gamma\), \(\gamma\in\mathbb R\), uniform boundedness over all \(r>0\) holds **if and only if** \(\gamma\ge\tfrac12\). At the critical exponent, the exact global supremum is \(8/3\), approached only as the contrast diverges. Below the exponent, the condition number is unbounded.

## Assumptions and scope
Use the continuous affine finite-element space on two consecutive real intervals of respective lengths \(r>0\) and \(1\). Both exterior endpoint degrees of freedom and the single interior interface degree of freedom are retained; no essential boundary elimination is imposed. On either interval of length \(h\), the local consistent mass matrix is \(h\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}/6\). Let \(M_{\mathrm{br}}\) be the block-diagonal assembly of these two matrices, and let \(P\in\mathbb R^{4\times3}\) copy global nodal values to the two local copies of the interface. The assembled mass is \(M=P^\top M_{\mathrm{br}}P\). For any \(w>0\), define \(W=\operatorname{diag}(w,w,1,1)\), \(R_w=(P^\top WP)^{-1}P^\top W\), and \(B_w=R_wM_{\mathrm{br}}^{-1}R_w^\top\). Relative element weights alone matter; a common positive rescaling of \(W\) does not change \(B_w\). The condition number means the positive spectral ratio of \(M^{1/2}B_wM^{1/2}\) (equivalently of \(B_wM\)), not the ordinary nonsymmetric matrix two-norm.

## Proof
**Exact assembly.** In the nodal order left/interface/right, direct local assembly gives
\[
M=\frac16\begin{pmatrix}2r&r&0\\r&2(r+1)&1\\0&1&2\end{pmatrix},\qquad
B_w=\begin{pmatrix}
4/r&-2w/[r(1+w)]&0\\
-2w/[r(1+w)]&(4w^2/r+4)/(1+w)^2&-2/(1+w)\\
0&-2/(1+w)&4
\end{pmatrix}.
\]
**Two unit eigenvalues.** Put \(R_*=M^{-1}P^\top M_{\mathrm{br}}\). Both maps are exact left inverses of \(P\): \(R_wP=R_*P=I\). Thus \((R_w-R_*)P=0\). Also, \(R_*M_{\mathrm{br}}^{-1}R_*^\top=M^{-1}\), and the mixed products \((R_w-R_*)M_{\mathrm{br}}^{-1}R_*^\top\) and its transpose vanish since \(M_{\mathrm{br}}^{-1}R_*^\top=PM^{-1}\). Consequently
\[
B_w-M^{-1}=(R_w-R_*)M_{\mathrm{br}}^{-1}(R_w-R_*)^\top\succeq0.
\]
The range of \(P\) has codimension one in the broken space, so this difference has rank at most one. Therefore \(M^{1/2}B_wM^{1/2}\) has at least two eigenvalues equal to \(1\) and its remaining eigenvalue is at least \(1\). Multiplying the displayed exact matrices and taking the trace gives \(\operatorname{tr}(B_wM)=2+4(r+1)(r+w^2)/(3r(1+w)^2)\); this proves the asserted complete spectrum, including all equality cases.

**Unique optimum.** The algebraic identity
\[
\Lambda(r,w)-\frac43=\frac{4(w-r)^2}{3r(1+w)^2}
\]
is nonnegative and vanishes precisely when \(w=r\). Since the two other eigenvalues equal \(1\), the condition number is the displayed \(\Lambda\), so the minimizer is unique for each \(r>0\).

**Sharp power-weight classification.** With \(w=r^\gamma\), set \(F_\gamma(r)=(r^\gamma-r)^2/[r(1+r^\gamma)^2]\). It obeys \(F_\gamma(1/r)=F_\gamma(r)\). As \(r\to\infty\): for \(\gamma<0\), \(F_\gamma(r)\sim r\); for \(\gamma=0\), \(F_0(r)\sim r/4\); for \(0<\gamma<1\), \(F_\gamma(r)\sim r^{1-2\gamma}\) (except at \(\gamma=1\), where it is identically zero); and for \(\gamma>1\), it is asymptotic to \(r^{-1}\). Thus the supremum over contrasts is finite precisely when \(\gamma\ge\frac12\), using continuity on compact positive intervals. At \(\gamma=\frac12\), substitution \(s=\sqrt r\) yields \(F_{1/2}(r)=((s-1)/(s+1))^2<1\) at finite positive \(s\), with supremum \(1\), hence \(\sup\Lambda=8/3\). This establishes sharpness and the nonattained boundary.

**Jacobi comparison.** The mass Jacobi inverse is \(J=\operatorname{diag}(M)^{-1}\). The symmetric normalized mass has unit diagonal and two nonzero consecutive off-diagonal entries whose squared magnitudes sum to \(1/4\), for every \(r>0\). Its three eigenvalues are therefore \(1/2,1,3/2\), and \(\kappa(JM)=3\).

## Verification
The accompanying standalone \(\texttt{verify_weighted_bras.py}\) uses standard-library exact rational arithmetic to construct the two local mass blocks and their inverses independently. For 956 positive rational pairs, it checks the assembled matrices and all coefficients of the characteristic polynomial against the claimed \(1,1,\Lambda\) spectrum, together with Jacobi eigenvalue identities. It also checks the minimizer identity. Executing it returns 8,618 passing exact-rational assertions. Finite checks are reproducibility tests; the preceding algebra establishes the theorem for **all** positive real interval and weight ratios and every real power exponent.

## Relationship to prior work
Krzysik, Southworth and Wimmer introduce the unweighted BRAS construction and analyze its general preconditioned spectrum. Southworth's September 2026 technical slides extend the construction to positive weighted averaging, explain that local mass-diagonal weights mitigate grading, and establish a general spectral upper bound. Those qualitative constructions and the general rank principle are **prior work**, not claims of novelty here. The particular two-interval continuous affine model, its exact arbitrary-scalar-weight spectral formula, its unique optimizer over all positive element-constant relative weights, and its sharp critical power exponent together furnish a minimal complete parametric classification not identified in those inspected results. Related prior analyses of unweighted BRAS on periodic grids and metric stars concern different geometry or lack the free scalar-weight and exponent classification. The classic Jacobi spectral interval is included solely as a comparator, not a discovery.

## Limitations
The classification concerns exactly two affine elements, one shared interface, three retained nodal degrees of freedom, exact consistent mass matrices, positive weights constant on each element, and exact arithmetic. It does not establish global condition-number bounds for arbitrary many-element meshes, high-degree bases, nonconforming constraints or arbitrary non-diagonal local weights. The power exponent criterion is a statement about this two-element family only. The general literature may contain equivalent specializations not indexed in the inspected sources; no claim of exhaustive historical priority is made. Independent proof review has not been performed.

## References
1. O. A. Krzysik, B. S. Southworth and G. A. Wimmer, *Broken-space Additive Schwarz Mass Inverse Approximations and (Block) Preconditioning*, arXiv:2607.12138 (first public 2026-07-13). https://arxiv.org/abs/2607.12138
2. B. S. Southworth, *BRoken-Space Additive Schwarz (BRAS) for Mass Matrix Preconditioning*, FEM@LLNL seminar slides, September 2026; relevant slides 6–8 and 13–15. https://mfem.org/pdf/seminar/southworth2.pdf
3. A. J. Wathen, *Realistic Eigenvalue Bounds for the Galerkin Mass Matrix*, IMA Journal of Numerical Analysis 7 (1987), 449–457. https://doi.org/10.1093/imanum/7.4.449
