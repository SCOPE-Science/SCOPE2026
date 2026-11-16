# Complete quadratic-polynomial concentration reduction on a two-coordinate quarter-ball

## Finding

Let \(d\ge3\), let \(B_d=\{x\in\mathbb R^d:\|x\|\le1\}\), and set
\[
Q_d=B_d\cap\{x_1\ge0,\ x_2\ge0\}.
\]
Write \(\mathcal P_2(B_d)\) for all complex-valued polynomials of total degree at most two, with the \(L^2(B_d)\) inner product for normalized volume. The self-adjoint concentration operator \(T_d\) is defined by
\[
\langle T_df,g\rangle_{B_d}=\int_{Q_d}f\overline g\,d\mu_d,
\qquad d\mu_d=\frac{dx}{\operatorname{vol}(B_d)}.
\]
The complete spectrum, *as a multiset*, is
\[
\boxed{\operatorname{Spec}(T_d)
=\Lambda_{4,d}\ \uplus\ \Lambda_{A,d}\ \uplus\
 \Lambda_{V,d}^{[d-2]}\ \uplus\
 \left\{\frac14\left(1-\frac2\pi\right)\right\}^{[d-2]}
 \uplus\ \left\{\frac14\right\}^{[\binom{d-1}{2}]} .}
\tag{1}
\]
Here \(\Lambda_{4,d}\) consists of four **specified generalized eigenvalues** of explicit four-by-four matrices; \(\Lambda_{A,d}\) and \(\Lambda_{V,d}\) each consist of two ordinary eigenvalues of explicit two-by-two matrices below. A bracketed exponent means that each member of the indicated multiset is repeated that number of times, and \(\uplus\) counts all repetitions, including possible cross-block coincidences. Thus (1) determines all \(\binom{d+2}{2}\) eigenvalues from matrices of size at most four in every dimension.

Define
\[
c_d=\frac{(d+2)\sqrt{d+4}\,\Gamma(1+d/2)}{8\sqrt{2\pi}\,\Gamma((d+5)/2)},\qquad
A_d=\begin{pmatrix}\frac14(1-\frac2\pi)&c_d\\c_d&\frac14\end{pmatrix},\qquad
V_d=\begin{pmatrix}\frac14&2c_d\\2c_d&\frac14(1+\frac2\pi)\end{pmatrix}.
\]
Then \(\Lambda_{A,d}=\operatorname{Spec}(A_d)\) and \(\Lambda_{V,d}=\operatorname{Spec}(V_d)\). In particular their four eigenvalues are given explicitly by
\[
\frac{1-1/\pi}{4}\pm\sqrt{c_d^2+\frac1{16\pi^2}},\qquad
\frac{1+1/\pi}{4}\pm\sqrt{4c_d^2+\frac1{16\pi^2}}.
\tag{2}
\]
For the remaining four eigenvalues, put \(z=(x_1,x_2)\) and choose the polynomial basis
\[
b_0(z)=1,\qquad b_1(z)=x_1+x_2,\qquad
b_2(z)=x_1^2+x_2^2,\qquad b_3(z)=x_1x_2.
\]
Define the completely explicit two-variable moments, for nonnegative integers \(a,b\), by
\[
m_d(a,b)=\frac{\Gamma(1+d/2)\,\Gamma((a+1)/2)\,\Gamma((b+1)/2)}{\pi\,\Gamma(1+(d+a+b)/2)}.
\tag{3}
\]
Expand \(b_i(z)b_j(z)=\sum_{a,b}h^{ij}_{ab}x_1^a x_2^b\), with uniquely determined integer coefficients \(h^{ij}_{ab}\). The four-by-four matrices are
\[
(G_d)_{ij}=\sum_{\substack{a,b\text{ even}}}h^{ij}_{ab}m_d(a,b),\qquad
(K_d)_{ij}=\frac14\sum_{a,b\ge0}h^{ij}_{ab}m_d(a,b),\quad 0\le i,j\le3.
\tag{4}
\]
Then \(G_d\) is positive definite and \(\Lambda_{4,d}\) is the multiset of roots of \(\det(K_d-\lambda G_d)=0\). Equations (1)–(4) are an exact all-dimensional algebraic-and-gamma-function spectral classification, not an approximation or an algorithm that grows with \(d\).

The operator has exact trace
\[
\operatorname{tr}(T_d)=\frac14\binom{d+2}{2}.
\tag{5}
\]
In dimension four the sharp minimum and maximum energy fractions are approximately \(0.001494346479621\) and \(0.871488123330396\). These numerical illustrations are not used to prove (1).

## Assumptions and scope

The ambient measure is uniform Lebesgue volume on the full solid ball, not surface area on its boundary. There is no radial or harmonic-degree restriction other than total polynomial degree at most two. The region cuts **exactly the first two coordinates**, not all \(d\) coordinates. Complex coefficients are allowed, but all basis matrices are real symmetric. Boundaries have zero volume. The dimension requirement is \(d\ge3\). The quotient \(\int_{Q_d}|f|^2/\int_{B_d}|f|^2\) for nonzero \(f\in\mathcal P_2(B_d)\) is bounded sharply by the smallest and largest eigenvalues in (1), respectively; the corresponding eigenspaces give all equality functions.

## Proof

**Step 1: exact moments.** If \(\alpha\in\mathbb Z_{\ge0}^d\), beta or Gaussian integration gives the normalized absolute ball moment
\[
\mathbb E_{B_d}\prod_{j=1}^d|x_j|^{\alpha_j}
=\frac{\Gamma(1+d/2)}{\Gamma(1+(d+|\alpha|)/2)}
 \prod_{j=1}^d\frac{\Gamma((\alpha_j+1)/2)}{\Gamma(1/2)}.
\tag{6}
\]
A signed monomial integrates to zero over the full ball if any exponent is odd. Over \(Q_d\) it integrates to zero if any exponent among the last \(d-2\) coordinates is odd; otherwise its restricted integral is precisely one quarter of the corresponding absolute moment (6). The factor is one quarter because signs of the first two coordinates are independent and equiprobable, conditional on their absolute values. Formulae (3) and (4) follow immediately.

**Step 2: orthogonal polynomial decomposition.** Let \(y=(x_3,\ldots,x_d)\), and \(m=d-2\). The following decomposition is algebraically direct and orthogonal for *both* the full and restricted inner products:

* The four-dimensional space spanned by \(1\), \(x_1+x_2\), \(x_1^2+x_2^2\), and \(x_1x_2\).
* The two-dimensional space spanned by \(x_1-x_2\) and \(x_1^2-x_2^2\).
* For each residual coordinate \(3\le j\le d\), the two-dimensional space spanned by \(x_j\) and \((x_1+x_2)x_j\), and the one-dimensional space spanned by \((x_1-x_2)x_j\).
* The residual quadratic space consisting of the polynomial
  \[
  p(x)=|y|^2-\frac{d-2}{d}(1-x_1^2-x_2^2)
  \tag{7}
  \]
  together with all trace-free homogeneous quadratics in \(y\).

To justify the last statement, conditional on \(z=(x_1,x_2)\), the vector \(y\) is uniformly distributed on the \((d-2)\)-ball of squared radius \(1-|z|^2\). Consequently
\[
\mathbb E(|y|^2\mid z)=\frac{d-2}{d}(1-|z|^2),
\]
so \(p\) has conditional mean zero, and every trace-free quadratic in \(y\) has conditional mean zero by rotational symmetry. The residual quadratic block is mutually orthogonal to the other blocks and to its own different irreducible rotational sectors. Every member is even in the first two coordinates; therefore on this entire block the restricted and full quadratic forms differ by exactly \(1/4\). Its dimension is
\[
1+\left[\frac{(d-2)(d-1)}2-1\right]=\binom{d-1}2.
\]
The other blocks are pairwise orthogonal: swapping \(x_1,x_2\) separates symmetric from antisymmetric scalar terms, and sign changes and rotations among the residual coordinates separate the vector modes. Since the mask \(Q_d\) is invariant under all these symmetries, orthogonality holds for both forms. The listed dimensions sum to \(\binom{d+2}{2}\), so this exhausts the polynomial space. For \(d=3\), the trace-free residual sector is empty but \(p\) remains nonzero.

**Step 3: evaluate nontrivial blocks.** On the scalar symmetric sector, (6) gives (4). On the scalar antisymmetric sector, the full Gram form is diagonal; normalizing each basis vector with respect to the full Gram form gives precisely \(A_d\). Similarly, the normalized Gram forms on the vector symmetric and antisymmetric sectors yield \(V_d\) and the singleton \(\frac14(1-2/\pi)\). In each calculation the mixed integral uses
\[
\mathbb E_{B_d}|x_1|^3=\frac{\Gamma(1+d/2)}{\sqrt\pi\,\Gamma((d+5)/2)},
\quad \mathbb E_{B_d}|x_1x_2|=\frac{2}{\pi(d+2)},
\quad \mathbb E_{B_d}|x_1x_2|x_j^2=\frac{2}{\pi(d+2)(d+4)}.
\]
The off-diagonal normalized entries are exactly \(c_d\) and \(2c_d\), respectively. The spectral theorem for an orthogonal direct sum proves (1) and the eigenvalue formulas (2). All Gram forms are positive definite because the basis polynomials are linearly independent on the ball.

**Step 4: sharp bounds and trace.** For nonzero \(f\), its restricted energy fraction is the Rayleigh quotient of the finite-dimensional self-adjoint \(T_d\), hence the min and max in (1) are *attained and sharp*. The reproducing kernel of the full total-degree-two polynomial space has a radial diagonal by rotational invariance. Since \(Q_d\) selects exactly one quarter of every orthant pair in the first two signs, integrating this diagonal gives \(\operatorname{tr}(T_d)=\frac14\dim\mathcal P_2(B_d)\), proving (5).

## Verification

The standalone program `verify.py` recomputes the entire \(\binom{d+2}{2}\)-by-\(\binom{d+2}{2}\) monomial concentration spectrum independently from (6), and compares it to all the reduced blocks for every integer dimension from three through twelve. It checks the two analytic two-by-two blocks, the protected quarter eigenvalue and conditional orthogonality, all multiplicities, and the trace. A separate 90-point product Gaussian quadrature in polar coordinates integrates the scalar four-by-four quarter-disk block without using the gamma moment table; at dimension four its maximum entry error was \(1.72\times10^{-15}\). The separate `exact_check.py` also verified seven normalized block identities symbolically (with exact gamma and \(\pi\) expressions) in dimensions three, four, five, and eight. All checks passed. Such finite checks corroborate, but are not substituted for, the all-dimensional proof above.

## Relationship to prior work

Gerhards and Huang, first posted August 7, 2023, investigate spectral shapes and asymptotic eigenvalue distributions for polynomial and Fourier–Jacobi concentration on balls. Their full-text discussion of total-degree polynomial bandwidth and the asymptotic theorem for Lipschitz domains do not specify the fixed quadratic, two-coordinate, all-dimensional spectral decomposition (1). Khalid, Kennedy and McEwen use Fourier–Bessel and Fourier–Laguerre rather than total-degree polynomial bandwidth, so their ball-region symmetry reductions do not imply this spectrum. Published related exact results for a *single half-ball* and for *pure quadratic harmonics on a spherical quarter-wedge* have materially different operators: neither determines the mixed-radial, constant, and linear sectors of the solid-volume problem here. A separately recorded earlier full-positive-orthant volume result concerns positivity of all coordinates and does not imply the two-coordinate wedge for \(d\ge3\). The one-dimensional classical concentrated-polynomial problem supplies historical background, not the claimed block spectrum.

## Limitations

The theorem is for total polynomial degree at most two and for two orthogonal coordinate halfspaces only; it does not assert formulas for other intersection angles, weighted volumes, higher polynomial bands, or surface-only measurements. Formula (4) presents a generalized four-by-four characteristic equation rather than radicals for its roots. The presentation identifies the quarter-energy eigenspace of the residual block; possible accidental eigenvalue coincidences across different blocks are *already counted* by multiset union and are not excluded. Numerical intervals are illustrative. Independent external mathematical audit and an exhaustive historical priority determination have not been performed.

## References

1. C. Gerhards and X. Huang, *Spatiospectral localization within the ball—studies on the influence of the spectral shape*, arXiv:2308.03543, initial public submission 2023-08-07, https://arxiv.org/abs/2308.03543 ; HTML https://arxiv.org/html/2308.03543v5.
2. Z. Khalid, R. A. Kennedy and J. D. McEwen, *Slepian Spatial-Spectral Concentration on the Ball*, arXiv:1403.5553, 2014, https://arxiv.org/abs/1403.5553.
3. E. N. Gilbert and D. Slepian, *Doubly Orthogonal Concentrated Polynomials*, SIAM Journal on Mathematical Analysis (1977), https://doi.org/10.1137/0508022.
4. Published indexed findings: *Universal half-energy multiplicity and an exact quadratic half-ball Slepian spectrum*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-universal-half-energy-multiplicity-and-an-exact-quadratic-half-b--84c98dd847a8 ; *Exact spectral staircase for quadratic spherical quarter-wedge concentration*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-spectral-staircase-for-quadratic-spherical-quarter-wedge-c--e0da39681828 (indexed statements compared; full GitHub texts inaccessible in this investigation).
