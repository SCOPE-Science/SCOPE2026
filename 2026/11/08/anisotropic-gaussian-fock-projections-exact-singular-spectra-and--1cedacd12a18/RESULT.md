# Anisotropic Gaussian Fock projections: exact singular spectra and a rational–irrational counting transition

## Finding
For a Gaussian-kernel projection from a possibly nonradial Gaussian \(L^2\) space into an anisotropic Gaussian Fock space, all singular values are products of finitely many eigenvalues of a concrete positive matrix. In complex dimension two this creates a sharp arithmetic dichotomy: the second-order logarithmic eigenvalue-counting coefficient exists precisely when the two log-decay rates have irrational ratio. The rational case instead has macroscopic staircase jumps of exactly computable size.

Let \(H=2tI-A\) and, when \(H>0\),
\[
Q=t^2 B^{-1/2}H^{-1}B^{-1/2},\qquad
\kappa=\frac{t^d}{\sqrt{\det A\det H}}.
\]
The operator is bounded exactly when \(H>0\) and \(Q\le I\). In that case its norm is \(\kappa\). If the eigenvalues of \(Q\) are \(q_1,\ldots,q_d\), with multiplicities, the complete eigenvalue multiset of \(P_tP_t^*\) is
\[
\left\{\kappa^2\prod_{j=1}^d q_j^{\nu_j}:\nu\in\mathbb N_0^d\right\}.
\]
The operator is compact precisely when all \(q_j<1\); in that case its singular values and Schatten sums are
\[
s_\nu=\kappa\prod_jq_j^{\nu_j/2},\qquad
\sum_\nu s_\nu^p=\kappa^p\prod_j(1-q_j^{p/2})^{-1},\quad p>0.
\]
For \(d=2\) and \(q_1,q_2<1\), put \(a=-\tfrac12\log q_1\), \(b=-\tfrac12\log q_2\) and
\[
N(R)=\#\{\nu\in\mathbb N_0^2:s_\nu>\kappa e^{-R}\}.
\]
Then \(N(R)\sim R^2/(2ab)\). The refined dichotomy is
\[
\begin{array}{ll}
\displaystyle N(R)=\frac{R^2}{2ab}+\frac{R}{2a}+\frac{R}{2b}+o(R),&a/b\notin\mathbb Q,\\
\displaystyle\lim_{R\to\infty}\frac{N(R)-R^2/(2ab)}R\ \text{does not exist},&a/b\in\mathbb Q.
\end{array}
\]
If \(a=cp,b=cq\) with \(c>0\) and coprime integers \(p,q\ge1\), then for every integer \(N\ge1\),
\[
N(cpqN)=\frac{pq}{2}N^2+\frac{p+q-1}{2}N,
\]
and crossing the threshold \(cpqN\) adds exactly \(N+1\) counted eigenvalues.

## Assumptions and scope
For integer \(d\ge1\), take \(t>0\) and Hermitian positive-definite \(A,B\in M_d(\mathbb C)\), not necessarily commuting. Set
\[
d\mu_A(w)=\frac{\det A}{\pi^d}\exp(-w^*Aw)\,dV(w),
\quad \mathcal F_B^2=\{g\text{ entire}:\int|g|^2d\mu_B<\infty\}.
\]
On compactly supported \(L^2(\mu_A)\) inputs define
\[
(P_tf)(z)=\left(\frac t\pi\right)^d\int_{\mathbb C^d}e^{t z\cdot\overline w}f(w)e^{-t|w|^2}\,dV(w).
\]
A bounded extension is understood to take values in \(\mathcal F_B^2\); all products and eigenvalue multiplicities refer to that extension. In the logarithmic count \(R>0\), strict inequality is used, so boundary eigenvalues are not counted. The two-dimensional refined law requires strict compactness, not merely boundedness.

## Proof
**1. The necessary Gaussian margin.** Evaluation at zero is a continuous functional on \(\mathcal F_B^2\). The linear functional \(f\mapsto(P_tf)(0)\) on the source has Riesz representative proportional to \(\exp[-w^*(tI-A)w]\). Its squared \(L^2(\mu_A)\) norm is proportional to
\[
\int_{\mathbb C^d}e^{-w^*(2tI-A)w}\,dV(w).
\]
It is finite exactly when \(H=2tI-A\) is positive definite. Thus boundedness forces \(H>0\).

**2. Exact positive operator.** Under \(H>0\), Gaussian integration and the reproducing identity for the target imply, first for holomorphic polynomials \(g\),
\[
(P_t^*g)(w)=\frac{t^d}{\det A}e^{-w^*(tI-A)w}g(tB^{-1}w),
\]
\[
(P_tP_t^*g)(z)=\frac{t^{2d}}{\det A\det H}\,g(t^2B^{-1}H^{-1}z).
\]
The second formula follows from the Gaussian reproducing identity
\[
\frac{\det H}{\pi^d}\int e^{v\cdot\overline w}h(w)e^{-w^*Hw}\,dV(w)=h(H^{-1}v)
\]
for entire polynomials \(h\). The Hermitian matrix \(Q=t^2B^{-1/2}H^{-1}B^{-1/2}\) is positive definite. Under the unitary change of coordinates \(\zeta=B^{1/2}z\), followed by a unitary eigenbasis change, the operator \(g\mapsto g(t^2B^{-1}H^{-1}z)\) becomes composition with \(\operatorname{diag}(q_1,\dots,q_d)\) on standard Fock space. Normalized monomials are then an orthonormal eigenbasis. Consequently the quadratic form of \(P_tP_t^*\) on polynomials is bounded if and only if every \(q_j\le1\). Since the kernel defines densely defined operators on compactly supported inputs, the bound yields a bounded extension of \(P_t\); the eigenvalue of the constant monomial proves \(\|P_t\|=\kappa\). This also proves the eigenvalue multiset for all matrix parameters, with no simultaneous diagonalization assumption on \(A,B\).

**3. Compactness, singular values and exact Schatten sums.** If any \(q_j=1\), the monomials in that coordinate give an orthonormal sequence on which \(P_tP_t^*\) has eigenvalue \(\kappa^2\); hence it is noncompact. If all \(q_j<1\), diagonal eigenvalues converge to zero outside finite sets, proving compactness. Taking square roots and summing separate geometric series gives the stated singular multiset and every \(S_p\) sum.

**4. The two-dimensional counting dichotomy.** Writing \(s_{m,n}=\kappa e^{-am-bn}\) yields the exact lattice identity
\[
N(R)=\#\{(m,n)\in\mathbb N_0^2:am+bn<R\}.
\]
Elementary comparison of this lattice triangle with unit squares proves \(N(R)=R^2/(2ab)+O(R+1)\). For irrational \(a/b\), let \(M=\lfloor R/a\rfloor\) and \(\theta=R/a-M\). Summing the numbers of nonnegative integers \(n\) satisfying \(bn<R-am\) gives
\[
N(R)=\sum_{m=0}^{M}\frac{R-am}{b}+(M+1)-\sum_{m=0}^{M}\left\{\frac{R-am}{b}\right\}-E_R,
\]
where \(0\le E_R\le1\) counts a possible exact boundary equality. Because \(a/b\) is irrational, rotation by \(a/b\) on the circle is uniquely ergodic; its fractional-part averages are \(1/2+o(1)\), uniformly in the initial phase \(R/b\). The arithmetic-progression sum is exactly
\[
\sum_{m=0}^{M}\frac{R-am}{b}=\frac{R^2}{2ab}+\frac R{2b}+\frac{a}{2b}\theta(1-\theta).
\]
Together with \(M+1=R/a+O(1)\), this establishes the claimed two-term asymptotic.

For rational \(a/b=p/q\) with \(p,q\) coprime write \(a=cp,b=cq\). At \(R_N=cpqN\), integer points in the closed triangle with vertices \((0,0),(qN,0),(0,pN)\) number \(pqN^2/2+(p+q+1)N/2+1\), by Pick's theorem (or by a direct floor sum). Exactly \(N+1\) are on the sloping hypotenuse; removing them gives the displayed strict count. At \(R_N+\varepsilon_N\) with any \(0<\varepsilon_N<c\), all those \(N+1\) boundary points enter and no higher level does. Choose \(\varepsilon_N\downarrow0\). The difference of the normalized second-order remainders across these two sequences converges to \(1/(cpq)>0\), because the smooth area term changes by \(o(R_N)\). Therefore the normalized second-order remainder has no limit.

## Verification
The standalone script `verify.py` uses exact rational arithmetic to check a genuinely noncommuting two-variable Gaussian covariance example: \(t=2\), \(A=\bigl(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\bigr)\) and \(B=\bigl(\begin{smallmatrix}3&1\\1&5\end{smallmatrix}\bigr)\). It reproduces the positive composition matrix, trace, determinant, norm and Hilbert–Schmidt identity, and exhaustively checks selected rational lattice threshold counts. These finite tests check algebra, not the irrational infinite limiting argument, which is proved above.

For a concrete irrational example take \(t=1\), \(A=I_2\), \(B=\operatorname{diag}(e^2,e^{2\sqrt 2})\); then \(\kappa=1\), \(a=1\), \(b=\sqrt2\), and the linear counting coefficient is \((1+1/\sqrt2)/2\). Replacing the second diagonal entry with \(e^4\) gives \(a=1,b=2\), whose staircase has \(N(2N)=N^2+N\) and jumps by \(N+1\).

## Relationship to prior work
Fang and Tien (arXiv:2610.41461v1, first posted 2026-10-30) classify boundedness and compactness for scalar Gaussian mixed-norm Fock projections. Their complete available text gives no singular-value list, anisotropic matrix classification or rational-versus-irrational logarithmic counting law. Sang and Zhao (arXiv:2610.28279v1) study a different analytic-Fock-to-analytic-Fock Gaussian operator in one variable and compute its Hilbert–Schmidt norm and Schatten membership. Dong and Zhu (arXiv:2509.16672v1) explicitly compute singular values for a different two-parameter canonical operator on a single one-variable Fock space. The classical Gaussian reproducing identity and integer-lattice theory are acknowledged proof ingredients, not new discoveries. The distinct assertion here is the off-diagonal, noncommuting-covariance spectral identification together with its sharp two-variable spectral-counting phase law.

## Limitations
The refined two-term counting theorem is established only in complex dimension two; the general-dimensional exact singular product formula does not itself supply higher-dimensional second-order lattice asymptotics. The theorem concerns positive-definite Gaussian weights and the displayed isotropic integral kernel, not arbitrary Gaussian integral operators with quadratic holomorphic multipliers. The irrational case has an \(o(R)\) remainder, without an effective rate. The rational case precludes a pointwise linear correction but admits special-subsequence formulae. Literature searches cannot guarantee publication priority; earlier equivalent Gaussian-second-quantization formulas and lattice-counting applications remain a residual risk. No independent audit has been performed.

## References
1. X. Fang and P. T. Tien, *Fock Projections between Gaussian Mixed-Norm Spaces: Full-Range Boundedness and Compactness*, arXiv:2610.41461v1 (2026-10-30), https://arxiv.org/abs/2610.41461.
2. Y. Sang and L. Zhao, *Gaussian Integral Operator between Fock Spaces*, arXiv:2610.28279v1 (2026-10-20), https://arxiv.org/abs/2610.28279.
3. X. Dong and K. Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672v1 (2025-09-20), https://arxiv.org/abs/2509.16672.
4. K. Zhu, *Analysis on Fock Spaces*, Graduate Texts in Mathematics 263, Springer (2012), for standard Fock reproducing kernels.
5. G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, for classical lattice counting and elementary equidistribution background.
