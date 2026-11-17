# Sharp universal two-level spectral stability for monotone Lipschitz functional calculus

## Finding
Let \(f:\mathbb R\to\mathbb R\) be nondecreasing and \(L\)-Lipschitz, where \(0\le L<\infty\). For every pair of complex Hermitian \(2\times2\) matrices \(A,B\),
\[
\boxed{\|f(A)-f(B)\|_{\mathrm{op}}\le \frac{2L}{\sqrt3}\|A-B\|_{\mathrm{op}}.}
\]
The coefficient \(2/\sqrt3\) is the **smallest universal coefficient** even when the class is restricted to real symmetric matrices and \(L=1\). It is approached by distinct pairs for the single fixed function \(f(t)=\max\{t,0\}\). In dimension one the corresponding universal coefficient is \(1\); this is a genuine two-level spectral amplification.

## Assumptions and scope
The spectral functional calculus is \(f(A)=U\operatorname{diag}(f(\lambda_1),f(\lambda_2))U^*\) for a unitary diagonalization of the Hermitian input; this is independent of the eigenbasis. The norm throughout is the induced matrix operator (largest singular-value) norm, not the Frobenius norm and not the largest absolute entry. The functions may be unbounded and nonsmooth, but are globally Lipschitz and nondecreasing. No matrix-operator-monotonicity hypothesis is imposed on \(f\). Constants added to \(f\) cancel from all differences. For \(L=0\), the assertion is immediate. Dimension \(2\) is exact; no claim for higher matrix sizes is made.

## Proof
**1. The divided-difference derivative.** By scaling, take \(L=1\). First suppose \(f\) is smooth and nondecreasing, with \(0\le f'(x)\le1\). At a Hermitian matrix with distinct eigenvalues \(\lambda_1,\lambda_2\), a unitary change of basis reduces its Fréchet derivative to
\[
D f_A\!\begin{pmatrix}a&z\\\overline z&c\end{pmatrix}
=\begin{pmatrix}u a&w z\\w\overline z&v c\end{pmatrix},\quad
u=f'(\lambda_1),\quad v=f'(\lambda_2),\quad
w=\frac{f(\lambda_1)-f(\lambda_2)}{\lambda_1-\lambda_2}.
\]
Here \(a,c\in\mathbb R\), \(z\in\mathbb C\), and monotonicity plus scalar nonexpansiveness ensures \(0\le u,v,w\le1\). When the eigenvalues coincide, the derivative is simply \(f'(\lambda_1)H\), with the same bound. This derivative is the standard two-level divided-difference formula; it can also be obtained directly by differentiating the spectral polynomial interpolation of a smooth \(f\).

**2. A universal bound for three-parameter Schur multipliers.** For \(u,v,w\in[0,1]\), define the real-linear map on Hermitian matrices
\[
M_{u,v,w}:\begin{pmatrix}a&z\\\overline z&c\end{pmatrix}
\longmapsto\begin{pmatrix}u a&w z\\w\overline z&v c\end{pmatrix}.
\]
Its induced operator-norm bound is convex in the three parameters. Expressing each parameter triple as a convex combination of the eight vertices of \([0,1]^3\) reduces the bound to the eight zero-one masks. With \(w=0\), all four masks are coordinate-diagonal projections of norm at most \(1\); the \((u,v,w)=(0,0,1)\) mask retaining only off-diagonal entries also has norm \(1\); \((1,1,1)\) is the identity. The only potentially larger masks are \((1,0,1)\) and \((0,1,1)\), which have identical norm by coordinate exchange.

**3. Exact exceptional-mask norm.** The closed unit ball of the real normed space of Hermitian \(2\times2\) matrices is the convex hull of its Hermitian-unitary extreme points. They are \(\pm I\) and the traceless involutions
\[
H=\begin{pmatrix}a&z\\\overline z&-a\end{pmatrix},\qquad a\in[-1,1],\quad |z|^2=1-a^2.
\]
The mask \((1,0,1)\) sends the latter to \(\begin{psmallmatrix}a&z\\\overline z&0\end{psmallmatrix}\); its spectral norm is
\[
\frac{|a|+\sqrt{a^2+4|z|^2}}2
=\frac{s+\sqrt{4-3s^2}}2,\qquad s=|a|\in[0,1].
\]
This function has derivative \(\tfrac12-\frac{3s}{2\sqrt{4-3s^2}}\), positive for \(s<1/\sqrt3\) and negative for \(s>1/\sqrt3\). Its unique maximum is
\[
\frac{1/\sqrt3+\sqrt3}2=\frac2{\sqrt3}.
\]
The two scalar unitaries have output norms \(1\), so the exceptional mask has exactly this induced norm. By Step 2, \(\|Df_A\|_{\mathrm{op}\to\mathrm{op}}\le2/\sqrt3\) for every smooth monotone 1-Lipschitz \(f\), irrespective of \(A\).

**4. Global bound and nonsmooth extension.** Integrate the derivative along the affine Hermitian segment \(B+t(A-B)\), \(0\le t\le1\). This yields the stated global bound for smooth \(f\). For an arbitrary nondecreasing 1-Lipschitz \(f\), let \(f_\varepsilon=f*\varphi_\varepsilon\) be convolution with a nonnegative smooth compactly supported probability kernel. Then \(f_\varepsilon\) is smooth, nondecreasing, 1-Lipschitz, and converges uniformly to \(f\) on each compact interval (in fact with global error bounded by a constant times \(\varepsilon\)). Applying the smooth estimate and passing to the two fixed finite spectra of \(A,B\) gives the claimed inequality. Scaling gives arbitrary \(L\).

**5. Sharpness.** Set \(f(t)=t_+=\max\{t,0\}\), and for each \(\varepsilon>0\) put
\[
A_\varepsilon=\begin{pmatrix}1&0\\0&-\varepsilon\end{pmatrix},\qquad
H=\begin{pmatrix}1/\sqrt3&\sqrt{2/3}\\\sqrt{2/3}&-1/\sqrt3\end{pmatrix}.
\]
The matrix \(H\) has \(H^2=I\), so \(\|H\|_{\mathrm{op}}=1\). The positive-part map is differentiable at \(A_\varepsilon\) and its derivative in direction \(H\) is
\[
Df_{A_\varepsilon}(H)=
\begin{pmatrix}1/\sqrt3&(1+\varepsilon)^{-1}\sqrt{2/3}\\
(1+\varepsilon)^{-1}\sqrt{2/3}&0\end{pmatrix}.
\]
Consequently,
\[
\lim_{\varepsilon\downarrow0}\lim_{\delta\downarrow0}
\frac{\|f(A_\varepsilon+\delta H)-f(A_\varepsilon)\|_{\mathrm{op}}}
{\|\delta H\|_{\mathrm{op}}}
=\frac2{\sqrt3}.
\]
Both limits use strictly distinct finite real symmetric inputs whenever \(\delta>0\). Thus no smaller universal coefficient is possible. The statement is about a sharp supremum, not finite-pair attainment.

## Verification
Run `python3 verify.py` beside this document (Python 3 standard library only). The checker tests all eight Schur mask vertex bounds against 4,808 Hermitian-unitary samples, evaluates the exact critical-unitary formula, confirms the positive-part sharpness approach at three parameters, and checks 1,500 deterministic random real-symmetric input pairs. The report ends in `ALL_TWO_LEVEL_FUNCTIONAL_CALCULUS_CHECKS_PASS`. These are corroborating finite checks; the full continuum and complex-Hermitian inequalities are established in the five proof steps above.

## Relationship to prior work
The Aleksandrov–Peller survey develops operator-Lipschitzness and divided-difference Schur multipliers in arbitrary dimensions, where scalar Lipschitzness by itself does not imply dimension-free operator Lipschitzness. The Daleskii–Krein differential formula and semidefinite projection derivatives are classical ingredients, not claimed as discoveries. Carlsson's results for isotropic Hermitian matrix functions establish the sharp **Frobenius**-norm Lipschitz bound (constant one for a scalar 1-Lipschitz function), a different input/output norm from the present spectral norm. Existing sharp entrywise and independent-coordinate \(2\times2\) positive-part estimates do not imply the spectral-norm coefficient and do not cover all monotone Lipschitz scalar functions. The new assertion is the exact universal \(2/\sqrt3\) coefficient in the two-level **spectral operator norm**, with a single positive-part sharpness family. A negative literature search does not establish publication priority.

## Limitations
The uniform bound assumes scalar monotonicity and applies only to complex Hermitian matrices of size two. For arbitrary non-monotone scalar Lipschitz functions the same coefficient is not asserted. No optimal constant or dimension-free estimate is claimed for matrices of size three or larger; the positive-part map is not operator-Lipschitz uniformly over unrestricted dimension. Historical priority remains provisional, including potentially unindexed norm-specific Schur multiplier calculations.

## References
1. A. B. Aleksandrov and V. V. Peller, *Operator Lipschitz functions*, arXiv:1611.01593v1, publicly submitted 2016-11-05. https://arxiv.org/abs/1611.01593.
2. J. Malick and H. S. Sendov, *Clarke generalized Jacobian of the projection onto the cone of positive semidefinite matrices*, Set-Valued Anal. **14** (2006), 273–293, DOI: 10.1007/s11228-005-0005-1. Author manuscript: https://www.stats.uwo.ca/faculty/hssendov/Publications/CGJPCPSDM.pdf.
3. M. Carlsson, *A Daleskii–Krein theorem for Hermitian matrix-functions based on vector-fields*, arXiv:1811.08358v1 (2018). https://arxiv.org/abs/1811.08358.
4. M. Carlsson, *Lipschitz continuity for isotropic matrix functions*, Linear Algebra Appl. **624** (2021), 259–266, DOI: 10.1016/j.laa.2021.04.006.
