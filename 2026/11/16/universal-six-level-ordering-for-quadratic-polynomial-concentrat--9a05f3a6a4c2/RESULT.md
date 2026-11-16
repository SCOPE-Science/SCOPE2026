# Universal six-level ordering for quadratic-polynomial concentration in a central ball slab

## Finding
Let \(d\ge2\), let \(B_d=\{x\in\mathbb R^d:\|x\|\le1\}\) carry normalized Lebesgue measure, and let \(\Pi_2^d\) be the complex polynomials of total degree at most two, with the \(L^2(B_d)\) inner product. For \(0<a<1\), put \(S_a=\{x\in B_d:|x_1|\le a\}\). Let \(T_{d,a}\) be the compression of multiplication by \(\mathbf1_{S_a}\) to \(\Pi_2^d\); thus \(\langle T_{d,a}f,f\rangle=\int_{S_a}|f|^2/\operatorname{vol}(B_d)\).

Set \(q=(d+1)/2\), \(t=a^2\), and write
\[
F_{p,r}(t)=\frac{B_t(p,r)}{B(p,r)},\qquad B_t(p,r)=\int_0^t u^{p-1}(1-u)^{r-1}\,du.
\]
Define the real symmetric matrices
\[
G=\begin{pmatrix}1&m_1\\m_1&m_2\end{pmatrix},\qquad
H=\begin{pmatrix}M_0&M_1\\M_1&M_2\end{pmatrix},
\]
where \(m_1=1/(d+2)\), \(m_2=3/((d+2)(d+4))\), and
\[
M_j=\frac{B_t(j+\frac12,q)}{B(\frac12,q)}\quad(j=0,1,2).
\]
Let \(\lambda_-<\lambda_+\) be the generalized eigenvalues of \(Hv=\lambda Gv\). The **complete spectrum**, with multiplicities, is
\[
\begin{array}{c|c}
\text{Eigenvalue}&\text{Multiplicity}\\\hline
\lambda_-&1\\
F_{3/2,q}(t)&1\\
F_{3/2,q+1}(t)&d-1\\
F_{1/2,q+1}(t)&d-1\\
F_{1/2,q+2}(t)&d(d-1)/2\\
\lambda_+&1
\end{array}
\]
and the displayed order is **strict for every** \(d\ge2\) and \(0<a<1\). Thus no spectral crossing occurs as the width or dimension varies. In particular the sharp minimum and maximum of
\[
\frac{\int_{S_a}|f|^2\,dx}{\int_{B_d}|f|^2\,dx},\qquad 0\ne f\in\Pi_2^d,
\]
are precisely \(\lambda_-\) and \(\lambda_+\); each equality case is a unique complex line contained in \(\operatorname{span}_{\mathbb C}\{1,x_1^2\}\).

For each fixed \(d\), the sharp thin-slab concentration condition number satisfies
\[
\boxed{\displaystyle
\frac{\lambda_+(d,a)}{\lambda_-(d,a)}
\sim\frac{405}{8(d+1)(d+4)}a^{-4}\quad(a\downarrow0).}
\]

## Assumptions and scope
The ambient ball is real and uniformly weighted, and \(\Pi_2^d\) includes degrees zero, one and two (not just homogeneous harmonics). Polynomial coefficients can be complex; the operator is defined using the normalized \(L^2\) form. The measure normalization cancels in energy ratios. No boundary point \(a=0\) or \(a=1\) is included in the six-strict-level assertion. The result applies simultaneously to every integer \(d\ge2\), with exact multiplicities before taking the limiting slab width.

## Proof
**1. Conditional beta measure.** If \(X\) is uniform in \(B_d\), then \(U=X_1^2\) has the beta distribution \(\mathrm{Beta}(1/2,q)\). Conditional on \(X_1=z\), the transverse vector \(Y=(X_2,\ldots,X_d)\) is uniform in the \((d-1)\)-ball of radius \(\sqrt{1-z^2}\). Consequently the average of any transverse quadratic \(Y^TAY\), given \(z\), equals \((1-z^2)\operatorname{tr}(A)/(d+1)\). Its centered conditional quadratic form
\[
Q_A(z,Y)=Y^TAY-\frac{\operatorname{tr}(A)}{d+1}(1-z^2)
\]
is orthogonal, both on the full ball and on every centered slab, to every polynomial in \(z\) of degree at most two and every transverse linear polynomial. For real symmetric \(A,B\), the full conditional fourth-moment calculation gives
\[
\mathbb E[Q_AQ_B\mid z]=\frac{2(1-z^2)^2}{(d+1)(d+3)}\left(\operatorname{tr}(AB)-\frac{\operatorname{tr}(A)\operatorname{tr}(B)}{d+1}\right).
\]
The bracket is positive definite on symmetric matrices, by \((\operatorname{tr}A)^2\le(d-1)\operatorname{tr}(A^2)\); the complex result follows by sesquilinearity. Hence this entire \(d(d-1)/2\)-dimensional sector has concentration eigenvalue \(F_{1/2,q+2}(t)\). Injectivity of \(A\mapsto Q_A\) follows from its quadratic part in \(Y\).

**2. Complete orthogonal sectors.** Reflection in \(z\) and rotations of the transverse variables give, simultaneously for both forms, the direct orthogonal decomposition
\[
\Pi_2^d
=\operatorname{span}\{1,z^2\}
\oplus\operatorname{span}\{z\}
\oplus\operatorname{span}\{Y_j\}_{j=1}^{d-1}
\oplus\operatorname{span}\{zY_j\}_{j=1}^{d-1}
\oplus\{Q_A:A=A^T\}.
\]
The dimensions sum to \(\binom{d+2}{2}\), and all summands are invariant under the concentration compression. The first is the generalized pair \((H,G)\), because \(U\sim\mathrm{Beta}(1/2,q)\). The other four blocks are scalar: their conditional squared norms carry factors respectively \(z^2\), \((1-z^2)\), \(z^2(1-z^2)\), and \((1-z^2)^2\). This yields exactly the beta-CDF ratios and multiplicities displayed above.

**3. Universal strict ordering and extremizers.** For \(0<t<1\), the beta CDF \(F_{p,r}(t)\) strictly decreases when \(p\) increases with \(r\) fixed, and strictly increases when \(r\) increases with \(p\) fixed. Both assertions follow directly by reweighting a positive beta density by the strictly increasing function \(u\), or the strictly decreasing function \(1-u\), respectively. Hence
\[
F_{3/2,q}(t)<F_{3/2,q+1}(t)<F_{1/2,q+1}(t)<F_{1/2,q+2}(t).
\]
On the even block, the Rayleigh quotient of the polynomial \(u\) equals \(F_{5/2,q}(t)\). By the min-max principle,
\[
\lambda_-\le F_{5/2,q}(t)<F_{3/2,q}(t).
\]
Likewise, the Rayleigh quotient of \(1-u\) equals \(F_{1/2,q+2}(t)\), so \(\lambda_+\ge F_{1/2,q+2}(t)\). Equality is impossible: if \(1-u\) were an eigenvector, its localized inner product with \(u-c\), where \(c\) is the mean of \(u\) under the full positive measure \((1-u)d\mathrm{Beta}(1/2,q)\), would have to vanish, yet it is strictly negative on \(0<u<t\) because the conditional mean below \(t\) is strictly less than \(c\). Thus \(\lambda_+>F_{1/2,q+2}(t)\). All six levels are strictly ordered. Both even eigenvalues are simple; their eigenspaces are the unique extremizing complex lines. All eigenvalues lie strictly between zero and one, since a nonzero polynomial cannot vanish on an open part of either region.

**4. Sharp thin-slab constant.** Write \(\mathcal B=B(1/2,q)\). As \(a\downarrow0\),
\[
M_0\sim\frac{2a}{\mathcal B},\qquad
M_1\sim\frac{2a^3}{3\mathcal B},\qquad
M_2\sim\frac{2a^5}{5\mathcal B}.
\]
Also \(\det G=2(d+1)/((d+2)^2(d+4))\). The largest eigenvalue is asymptotic to \(2a\,(G^{-1})_{00}/\mathcal B\), and the product of the two eigenvalues is \(\det H/\det G\). Since \(\det H\sim16a^6/(45\mathcal B^2)\), direct substitution yields
\[
\lambda_+\sim\frac{3(d+2)}{(d+1)\mathcal B}a,
\qquad
\lambda_-\sim\frac{8(d+2)(d+4)}{135\mathcal B}a^5.
\]
Their quotient is the asserted sharp \(a^{-4}\) law.

## Verification
The included `verify_exact.py` builds the complete ten-by-ten full-monomial Gram pair by **exact rational integration** for \(d=3\), \(a=1/2\). Its determinant factors exactly into the predicted six sectors; the even characteristic polynomial is
\[
8192\lambda^2-8132\lambda+443.
\]
Independent `verify_numeric.py` integrates full monomial moments by numerical quadrature rather than evaluating the reduced incomplete-beta blocks; all 24 dimension-width tests spanning \(d=2,3,4,5,8,10\) matched the complete predicted multisets within \(2\times10^{-10}\). It also checks the asymptotic condition-number constant using 80-digit arithmetic for dimensions \(2,3,8\). These finite checks supplement, but do not replace, the proof of the all-dimensional theorem.

To reproduce, from the directory containing the scripts run `python verify_exact.py` and `python verify_numeric.py`. Dependencies: Python 3, NumPy, SciPy, SymPy and mpmath; neither script reads external data.

## Relationship to prior work
Gerhards and Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543 (first public 7 August 2023), define this polynomial-degree concentration problem and analyze large-bandwidth eigenvalue distributions and general Remez bounds. Their main text and Appendix B do not present this degree-two centered-slab spectrum or its all-dimensional strict ordering. Gilbert and Slepian's *Doubly Orthogonal Concentrated Polynomials* (1977) studies one-dimensional nested intervals, with emphasis on high-degree asymptotics; its accessible abstract does not settle the transverse multiplicity or ordering here. Khalid, Kennedy and McEwen (arXiv:1403.5553) treat Fourier-Bessel and Fourier-Laguerre rather than degree-polynomial bandwidths.

Other published results for quadratic half-ball restrictions and arbitrary **radial** ball masks are relevant but distinct: a one-sided half-ball is not the two-sided central slab, and a radial mask depends on \(\|x\|\) rather than one normal coordinate. Published equatorial-belt concentration calculations on \(S^2\) involve surface spherical harmonics rather than volume polynomials. The beta stochastic-order argument and explicit six-sector hierarchy above do not follow as stated from these geometrically different classifications. Standard Jacobi moments and representation-theoretic block reductions are used as tools, not claimed as original discoveries.

## Limitations
The theorem concerns degree at most two and centered coordinate slabs only; it does not assert analogous strict order for higher degrees, displaced slabs, arbitrary weights, or Fourier-Laguerre bandwidths. The asymptotic condition-number formula is for fixed dimension as the slab shrinks and is not uniform in dimension. The value of \(\lambda_+\) and \(\lambda_-\) at general positive width is specified by an explicit two-by-two generalized eigenproblem, not by a rational elementary expression. Priority remains provisional: a more general weighted-Jacobi or multivariate-polynomial theorem might implicitly include this result, and full access to some older specialized concentration papers was unavailable. No independent mathematical validation is claimed.

## References
1. C. Gerhards and X. Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543, 7 August 2023, https://arxiv.org/abs/2308.03543 .
2. E. N. Gilbert and D. Slepian, *Doubly Orthogonal Concentrated Polynomials*, SIAM Journal on Mathematical Analysis (1977), https://doi.org/10.1137/0508022 .
3. Z. Khalid, R. Kennedy and J. D. McEwen, *Slepian Spatial-Spectral Concentration on the Ball*, arXiv:1403.5553 (2014), https://arxiv.org/abs/1403.5553 .
4. *Universal half-energy multiplicity and an exact quadratic half-ball Slepian spectrum*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-universal-half-energy-multiplicity-and-an-exact-quadratic-half-b--84c98dd847a8 .
5. *Two sharp angular transitions and spectral camouflage for quadratic ball concentration*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-sharp-angular-transitions-and-spectral-camouflage-for-quadra--996a7a7bbc19 .
6. *Narrow equatorial belts: sharp Slepian spectral hierarchy*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-narrow-equatorial-belts-sharp-slepian-spectral-hierarchy--9a85b4c3346c .
