# Three exact tangential concentration levels on cubical spherical cells

## Finding
Let \(d\ge 2\) be an integer, let \(\sigma\) be probability surface measure on \(S^{d-1}\subset\mathbb R^d\), and put
\[
 C_d=\{x\in S^{d-1}:x_1\ge |x_j|\text{ for }2\le j\le d\}.
\]
For the tangent-vector space \(\mathcal V_d\) defined below, the concentration operator \(T_d=P_{\mathcal V_d}\mathbf1_{C_d}|_{\mathcal V_d}\) has **exactly three strictly ordered eigenvalues**
\[
0<\lambda_{-,d}<\lambda_{0,d}<\lambda_{+,d}<1,
\]
with respective multiplicities \(d-1\), \(1+\binom{d-1}{2}\), and \(d-1\). Thus \(\dim\mathcal V_d=d(d+1)/2\), and these eigenvalues give the sharp minimum and maximum of \(\int_{C_d}|F|^2d\sigma/\int_{S^{d-1}}|F|^2d\sigma\) for all nonzero \(F\in\mathcal V_d\).

Let \(X\sim\sigma\), \(M_d=\max_{1\le i\le d}|X_i|\), \(s_d=\mathbb E M_d\), and \(t_d=\mathbb E M_d^2\). Define
\[
a_d=\frac{d-2+t_d}{2(d-1)^2},\quad b_d=\frac{1+(d-2)t_d}{4(d-1)},\quad c_d=\frac{s_d}{2\sqrt{2(d-1)}},\quad \lambda_{0,d}=\frac{1-t_d}{2(d-1)}.
\]
Then \(\lambda_{-,d}\) and \(\lambda_{+,d}\) are exactly the smaller and larger eigenvalues of \(\begin{pmatrix}a_d&c_d\\c_d&b_d\end{pmatrix}\). The two moments are expressible by **one-variable integrals**:
\[
s_d=\frac{\Gamma(d/2)}{\sqrt2\,\Gamma((d+1)/2)}\int_0^\infty\!\left[1-\operatorname{erf}(z/\sqrt2)^d\right]dz,
\quad t_d=\frac2d\int_0^\infty\!z\left[1-\operatorname{erf}(z/\sqrt2)^d\right]dz.
\]
In every dimension \(\operatorname{tr}T_d=(d+1)/4\). As \(d\to\infty\), the complete sharp edge asymptotics are
\[
\lambda_{+,d}\sim \frac{\log d}{2d},\qquad \lambda_{0,d}\sim\frac1{2d},\qquad\lambda_{-,d}\sim\frac1{4d\log d},\qquad \frac{\lambda_{+,d}}{\lambda_{-,d}}\sim 2(\log d)^2.
\]

## Assumptions and scope
For the standard basis \(e_i\), put \(G_i(x)=e_i-x_i x\) and \(K_{ij}(x)=x_i e_j-x_j e_i\) for \(i<j\). The complex vector space \(\mathcal V_d=\operatorname{span}_{\mathbb C}\{G_i,K_{ij}:1\le i\le d,\;1\le i<j\le d\}\) is equipped with the Hermitian \(L^2(S^{d-1},\sigma;\mathbb C^d)\) inner product. All fields are tangent; the \(G_i\) are spherical gradients of linear harmonics and the \(K_{ij}\) are infinitesimal rotation fields. This is a *continuous observation* problem, not a finite set of samples. The theorem covers \(d=2\), where the relevant fields are tangent to the circle, and all larger dimensions. Eigenvalue multiplicities include possible complex coefficients. No assumption of real-valued input is needed.

## Proof
**1. Global orthogonal frame.** By \(\mathbb E X_i=0\) and \(\mathbb E X_iX_j=\delta_{ij}/d\), the fields \(G_i\) are mutually orthogonal with norm squared \((d-1)/d\), the \(K_{ij}\) are mutually orthogonal with norm squared \(2/d\), and all global \(G\)-to-\(K\) cross inner products vanish. Consequently
\[
\widehat G_i=\sqrt{\frac d{d-1}}G_i,\qquad \widehat K_{ij}=\sqrt{\frac d2}K_{ij}
\]
form a complete orthonormal basis of \(\mathcal V_d\).

**2. All local moments by one maximum.** Signed-permutation symmetry partitions the sphere, outside measure-zero ties, into \(2d\) congruent cells. Thus \(A=\mathbb P(X\in C_d)=1/(2d)\). Conditional on membership in this cell, \(X_1=M_d\); the conditional distribution of the absolute coordinate maximum is unchanged. Therefore
\[
\mathbb E[X_1\mathbf1_{C_d}]=A s_d=:m,\quad \mathbb E[X_1^2\mathbf1_{C_d}]=A t_d=:q,
\quad \mathbb E[X_j^2\mathbf1_{C_d}]=A\frac{1-t_d}{d-1}=:p\ (j>1).
\]
All other first and off-diagonal second local moments vanish by independent sign changes of coordinates \(2,\ldots,d\).

**3. Exact block diagonalization.** The identities
\(G_i\cdot G_j=\delta_{ij}-x_ix_j\),
\(K_{ij}\cdot K_{kl}\) obtained by multiplying their displayed components, and
\(G_a\cdot K_{ij}=\delta_{aj}x_i-\delta_{ai}x_j\)
show that the localized Gram matrix in the normalized frame consists of the scalar block \(\lambda_{0,d}\) on \(\widehat G_1\), an identical scalar block on each \(\widehat K_{jk}\) with \(2\le j<k\le d\), and \(d-1\) identical \(2\times2\) blocks on \(\operatorname{span}\{\widehat G_j,\widehat K_{1j}\}\), \(j=2,\ldots,d\):
\[
\begin{pmatrix}
\frac d{d-1}(A-p)&\frac d{\sqrt{2(d-1)}}m\\
\frac d{\sqrt{2(d-1)}}m&\frac d2(q+p)
\end{pmatrix}
=\begin{pmatrix}a_d&c_d\\c_d&b_d\end{pmatrix}.
\]
The protected scalar from both isolated types equals \(\frac d{d-1}(A-q)=dp=\lambda_{0,d}\). This proves all multiplicities, completeness, and the exact spectrum.

**4. Universal strict order.** Since \(M_d>1/\sqrt d\) almost surely away from a null set, \(dt_d>1\). Direct subtraction gives
\[
a_d-\lambda_{0,d}=\frac{dt_d-1}{2(d-1)^2}>0,\quad
b_d-\lambda_{0,d}=\frac{dt_d-1}{4(d-1)}>0.
\]
Moreover,
\[
\det\left(\begin{pmatrix}a_d&c_d\\c_d&b_d\end{pmatrix}-\lambda_{0,d}I\right)
=\frac{(dt_d-1)^2-(d-1)^2s_d^2}{8(d-1)^3}<0,
\]
because
\[
(d-1)s_d-(dt_d-1)=\mathbb E[(1-M_d)(dM_d+1)]>0.
\]
Thus the two matrix eigenvalues lie on opposite sides of \(\lambda_{0,d}\). Positivity of the smallest and strict boundedness of the largest by one follow because a nonzero analytic tangent-vector field cannot vanish identically on either open set \(C_d^\circ\) or \((S^{d-1}\setminus C_d)^\circ\). The trace equals \(\dim\mathcal V_d\) times the cell fraction, because the sum of squared basis-field norms is rotation-invariant; equivalently sum the listed blocks to obtain \((d+1)/4\).

**5. One-dimensional moment evaluation.** Let \(N_1,\ldots,N_d\) be independent standard Gaussians, \(R=(\sum N_i^2)^{1/2}\), and \(Z=\max_i|N_i|\). Then \(N/R\) is uniform on the sphere and independent of \(R\), whence \(Z=RM_d\) with independent factors. Since \(\mathbb P(Z\le z)=\operatorname{erf}(z/\sqrt2)^d\), tail integration gives \(\mathbb E Z=\int_0^\infty\mathbb P(Z>z)dz\) and \(\mathbb E Z^2=2\int_0^\infty z\mathbb P(Z>z)dz\). Divide by \(\mathbb E R=\sqrt2\Gamma((d+1)/2)/\Gamma(d/2)\) and \(\mathbb E R^2=d\) respectively.

**6. Sharp large-dimensional edges.** Standard Gaussian tail inequalities give, with \(L=\log d\),
\(\mathbb E Z^2\sim2L\) and \(\operatorname{Var}Z\to0\). For completeness, choose cutoffs \(\sqrt{2L\pm4\log L}\). A union bound makes the upper-tail second moment tend to zero, while \((1-u)^d\le e^{-du}\) and the Gaussian lower-tail bound make the lower failure probability exponentially small in a positive power of \(L\). The cutoff interval has width \(O(\log L/\sqrt L)\), so \(\mathbb E(Z-\sqrt{2L})^2\to0\), proving these assertions. Stirling's ratio gives \(\mathbb E R=\sqrt d(1+O(1/d))\). Substitution yields
\[
a_d\sim(2d)^{-1},\quad b_d\sim L/(2d),\quad
\det\begin{pmatrix}a_d&c_d\\c_d&b_d\end{pmatrix}
=\frac{1+\operatorname{Var}Z+o(1)}{8d^2}\sim\frac1{8d^2}.
\]
The determinant expansion follows directly after inserting \(s_d=\mathbb E Z/\mathbb E R\), \(t_d=\mathbb E Z^2/d\); all discarded terms are \(O(L^2/d^3)\). The two matrix eigenvalues are therefore asymptotic to \(b_d\) and \(\det/b_d\), while \(\lambda_{0,d}\sim1/(2d)\), proving all edge and condition-number statements.

## Verification
The complete standalone script `verify_spectrum.py` independently constructs all normalized tangent fields, samples the entire spherical Gram matrix with scrambled Sobol–Gaussian directions, and compares its sorted eigenvalues with the one-variable integral formulas at \(d=2,3,4,6\). Its largest observed absolute eigenvalue discrepancy was \(0.000408\), below the predeclared tolerance \(0.0018\). It also checks trace, region probability, symbolic block determinant and trace identities, and the exact \(d=3\) moments
\[
s_3=\frac{3\sqrt2}{\pi}\arctan\frac1{\sqrt2},\qquad t_3=\frac13+\frac2{\pi\sqrt3}.
\]
These tests corroborate, but do not replace, the all-dimensional analytic proof. At \(d=3\) the sorted levels are approximately \(0.004813332293\), \(0.0747785174\), and \(0.420408150277\), each of multiplicity two.

## Relationship to prior work
Plattner–Simons (2013 preprint; 2014 journal) formulated general spherical vector Slepian concentration and its tangential Gram matrix, treating polar caps explicitly. Michel–Plattner–Seibert (first public March 26, 2021) gave a spin-weighted approach and commuting constructions for caps. Those general frameworks can in principle be used to build a matrix for the three-dimensional cell, but their inspected statements do not give the present evaluated cubical-cell spectrum, its dimension-independent three-level ordering, or its sharp large-dimensional law. The sphere's scalar quadratic-harmonic spectrum on the same cubical cells is a different operator, and it does not determine the mixed gradient–rotation first moment used here. The cubed-sphere geometry is natural in spherical-grid modeling; no numerical-discretization theorem is asserted.

## Limitations
This treats only the specified finite-dimensional tangent-gradient and rotation-field space, a single signed-coordinate-dominant cell, and uniform probability measure. It does not classify higher vector harmonic degrees, weighted observations, all unions of cells, vector-valued sample recovery, or arbitrary spherical regions. The numerical tests are finite and are not independent mathematical certification. Exhaustive historical priority against unindexed publications is not established.

## References
- A. Plattner and F. J. Simons, *Spatiospectral concentration of vector fields on a sphere*, **Applied and Computational Harmonic Analysis** 36 (2014), 1–22. DOI: 10.1016/j.acha.2012.12.001; preprint arXiv:1306.3201 (2013).
- V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1 (March 26, 2021); **Analysis and Applications** 20 (2022), 947–988.
- C. Chen, X. Li, F. Xiao, and X. Shen, *A nonhydrostatic atmospheric dynamical core on cubed sphere using hybrid multi-moment finite-volume/finite difference methods*, arXiv:2202.13368 (February 27, 2022), background on the observation geometry only.
