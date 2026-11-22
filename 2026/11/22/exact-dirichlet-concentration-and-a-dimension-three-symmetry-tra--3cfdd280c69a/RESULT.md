# Exact Dirichlet concentration and a dimension-three symmetry transition on spherical lunes

## Finding
Let \(d\ge3\), and let \(\mathcal H_2(d)\) be the complex vector space of restrictions to \(S^{d-1}\) of homogeneous harmonic quadratic polynomials. Fix \(0<L<\pi\), write \(\phi=\arg(x_1+i x_2)\), and define the spherical lune
\[
E_L=\{x\in S^{d-1}:-L/2<\phi<L/2\}.
\]
The null set \(x_1=x_2=0\) is irrelevant. Equip \(\mathcal H_2(d)\) with the **Dirichlet** inner product
\[
\langle f,g\rangle_D=\int_{S^{d-1}}\nabla_S f\cdot\overline{\nabla_S g}\,d\sigma,
\]
where \(\sigma\) is probability surface measure, and define \(T_{d,L}\) by
\[
\langle T_{d,L}f,g\rangle_D=\int_{E_L}\nabla_S f\cdot\overline{\nabla_S g}\,d\sigma.
\]
For \(p=L/(2\pi)\), \(u=\sin L/L\), \(v=u\cos L\), \(a=\sqrt{(d-2)/d}\), and \(b=1/d\), its **complete** spectrum, with multiplicity, is
\[
\begin{array}{c|c}
\text{Dirichlet concentration eigenvalue}&\text{multiplicity}\\\hline
p\left(1-bv+\sqrt{b^2v^2+a^2u^2}\right)&1\\
p\left(1-bv-\sqrt{b^2v^2+a^2u^2}\right)&1\\
p(1+2bv)&1\\
p\left(1+\frac{d-2}{2d}u\right)&d-2\\
p\left(1-\frac{d-2}{2d}u\right)&d-2\\
p&\frac{d(d-3)}2.
\end{array}
\]
Coincident eigenvalues are counted additively; the last row is absent in dimension three.

Set \(L_*=\arccos\sqrt{3/8}\). In dimension three, the **maximizing** eigenspace is the one-dimensional \(2x_1x_2\) sector for \(0<L<L_*\) and the upper eigenline of the planar-radial block for \(L_*<L<\pi\), with a two-dimensional tie at \(L_*\). The **minimizing** eigenspace is the lower planar-radial eigenline for \(0<L<\pi-L_*\) and the one-dimensional \(2x_1x_2\) sector for \(\pi-L_*<L<\pi\), with a two-dimensional tie at \(\pi-L_*\). For every \(d\ge4\) and every \(0<L<\pi\), the upper and lower planar-radial eigenlines are respectively the unique maximizer and minimizer: **there are no interior symmetry transitions**.

The sharp squared gradient-observation condition number is the ratio of these extremal eigenvalues. In the narrow-lune limit,
\[
\kappa_d(L)\sim
\begin{cases}
4L^{-2},&d=3,\\
\dfrac{12(d-1)^2}{d(d+2)}L^{-2},&d\ge4.
\end{cases}
\]
The eigenvalue formulas, eigenvectors, strict ordering, and asymptotics hold for every stated dimension and aperture, not merely at tested parameters.

## Assumptions and scope
Write \(x=(\sqrt r\cos\phi,\sqrt r\sin\phi,y)\), where \(r=x_1^2+x_2^2\) and \(y\in\mathbb R^{d-2}\). All complex harmonics are handled by complexifying real symmetric trace-free matrices; the displayed multiplicities are complex dimensions. A harmonic is \(f_A(x)=x^{\mathsf T}Ax\), with \(A=A^{\mathsf T}\) and \(\operatorname{tr}A=0\). The full-sphere Dirichlet norm is
\[
\|f_A\|_D^2=\frac{4}{d+2}\operatorname{tr}(AA^*).
\]
The aperture restriction \(0<L<\pi\) excludes the trivial half-sphere degeneracy at \(L=\pi\). No boundary conditions are imposed on the lune: the operator is **concentration of gradients of globally defined harmonics**, not a regional Dirichlet-Laplacian eigenproblem.

## Proof
**1. Exact conditional moment identity.** Uniform probability measure on \(S^{d-1}\) has independent uniform longitude \(\phi\), squared planar radius \(r\sim\mathrm{Beta}(1,(d-2)/2)\), and transverse direction uniform on \(S^{d-3}\) (the symmetric two-point set if \(d=3\)). Thus
\[
\mathbb E r=\frac2d,\qquad\mathbb E r^2=\frac8{d(d+2)}.
\]
For trace-free symmetric matrices \(A,B\),
\[
\nabla_Sf_A=2(Ax-(x^{\mathsf T}Ax)x),\quad
\nabla_S f_A\cdot\nabla_S f_B=4\left(x^{\mathsf T}ABx-(x^{\mathsf T}Ax)(x^{\mathsf T}Bx)\right).
\]
Spherical second and fourth moments give \(\mathbb E_{S^{d-1}}\nabla_S f_A\cdot\nabla_S f_B=4\operatorname{tr}(AB)/(d+2)\). Complex conjugation on the second factor yields the Hermitian version.

**2. Block decomposition.** Put \(m=d-2\) and
\[
Z=r-2/d,\quad C=x_1^2-x_2^2,\quad S=2x_1x_2.
\]
The orthogonal source decomposition is
\[
\operatorname{span}\{Z,C,S\}\oplus
\bigoplus_{j=3}^{d}\operatorname{span}\{2x_1x_j,2x_2x_j\}
\oplus \{y^{\mathsf T}By:B=B^{\mathsf T},\operatorname{tr}B=0\}.
\]
The last summand has dimension \(m(m+1)/2-1=d(d-3)/2\). Use the full-sphere Dirichlet-orthonormal versions of \(Z,C,S\). Conditioning on longitude and using the preceding moment formula produces the pointwise (in \(\phi\)) normalized gradient Gram density
\[
G_0(\phi)=
\begin{pmatrix}
1&a\cos2\phi&a\sin2\phi\\
a\cos2\phi&1-\frac2d\cos4\phi&-\frac2d\sin4\phi\\
a\sin2\phi&-\frac2d\sin4\phi&1+\frac2d\cos4\phi
\end{pmatrix},\quad a=\sqrt{\frac{d-2}{d}}.
\]
Each mixed pair has pointwise density
\[
G_{\rm mix}(\phi)=I_2+\frac{d-2}{2d}
\begin{pmatrix}\cos2\phi&\sin2\phi\\\sin2\phi&-\cos2\phi\end{pmatrix}.
\]
A transverse trace-free quadratic has constant conditional normalized gradient energy density \(1\). Reflection symmetry and the transverse orthogonal group eliminate cross-block terms. These identities may also be checked directly using \(\mathbb E[r(1-r)]=2(d-2)/(d(d+2))\) and the usual fourth moments on the transverse sphere; no finite numerical calculation is required.

**3. Integrate exactly.** Angular integration over \([-L/2,L/2]\), divided by \(2\pi\), uses
\[
\frac1L\int_{-L/2}^{L/2}\cos2\phi\,d\phi=u,
\quad\frac1L\int_{-L/2}^{L/2}\cos4\phi\,d\phi=v,
\]
and the two sine averages vanish. The three-dimensional block splits as the \(2\times2\) block
\[
K_{ZC}=p\begin{pmatrix}1&au\\au&1-2bv\end{pmatrix}
\]
and the scalar \(S\)-block \(p(1+2bv)\). The mixed blocks give \(p(1\pm(d-2)u/(2d))\), and the transverse block gives \(p\). Diagonalizing \(K_{ZC}\) yields the displayed spectrum. The multiplicities sum to
\[
3+2(d-2)+\frac{d(d-3)}2=\frac{(d-1)(d+2)}2=\dim\mathcal H_2(d).
\]

**4. Exact extremal ordering.** Set \(t=\cos L\in(-1,1)\), and write \(R=\sqrt{b^2t^2+a^2}\). The two normalized eigenvalues of \(K_{ZC}\) are \(1+u(-bt\pm R)\). Since \(a>1/2=b+(d-2)/(2d)\) for every integer \(d\ge3\), and \(R\ge a\), the upper one strictly exceeds both mixed branches and the transverse eigenvalue, while the lower one strictly falls below them. Hence only the \(S\)-block can compete at either extremum. Its normalized eigenvalue is \(1+2but\), so
\[
\lambda_+-\lambda_S=pu(R-3bt),\qquad
\lambda_--\lambda_S=-pu(R+3bt).
\]
When \(t>0\), the first difference vanishes precisely if \(a^2=8b^2t^2\); when \(t<0\), the second vanishes precisely under the same condition. This reduces to \(t^2=d(d-2)/8\). An interior solution is possible **only** when \(d=3\), with roots \(\pm\sqrt{3/8}\). Their strict signs on the complementary intervals give the complete sharp extremizer classification, including both two-dimensional ties. Each planar-radial extremal eigenvalue is simple because \(au>0\).

**5. Positivity and narrow-aperture law.** For a nonzero quadratic harmonic, its tangential gradient cannot vanish on any open patch; otherwise analyticity and connectedness force a global constant, impossible in positive exact degree. Thus every eigenvalue lies strictly between zero and one. Taylor expansion gives
\[
\lambda_-/p=\frac{d+2}{6(d-1)}L^2+O_d(L^4),
\]
while \(\lambda_+/p\to2(d-1)/d\) and \(\lambda_S/p\to(d+2)/d\). Inserting the already-proved extremal ordering gives precisely the two asserted sharp condition-number constants.

## Verification
The standalone `check_lune_gradient.py` does **not** insert the spectral blocks into its Gram matrix. It builds all trace-free symmetric quadratic matrices, orthonormalizes them in the exact source Dirichlet form, then computes the localized gradient products from independently derived conditional radial/transverse second and fourth moments. Each longitude integrand has Fourier order at most four, so its 16-point discrete Fourier transform determines the angular integral without Fourier aliasing; the code integrates those coefficients analytically. For dimensions \(d=3,4,5,7,9\) and ten aperture values (including both transition angles), all 50 full sorted spectra agree with the theorem within \(3\times10^{-12}\); the 200 programmed assertions pass. The analytic moment identities and inequalities, not the finite tests, prove the all-parameter claims.

## Relationship to prior work
Michel, Plattner and Seibert (2021) develop the general vector/scalar Slepian construction and normalized tangential harmonic gradients, with cap-specific commuting operators. Simons, Dahlen and Wieczorek (2004) formulate general regional spherical concentration, and Aslam and Khalid (2020) develop a spatial-Slepian transform. These general frameworks do not state the present all-dimensional Dirichlet-gradient lune spectrum or its unique dimension-three transition pair. Bates, Khalid and Kennedy (2016/2017) supply an exact limited-longitude scalar Slepian matrix, while Nafees, Khalid and Kennedy (2020) call a two-region **difference of scalar energies** a "differential" Slepian problem; neither uses function derivatives. Published exact-degree quadratic *scalar-value* lune spectra (2026) are especially close geometrically, but their observation is \(|f|^2\), not \(|\nabla_Sf|^2\), and their two symmetry-transition apertures \(\arccos(\pm2/d)\) exist in **every** dimension. In contrast the derivative observation has two interior transitions **only** in dimension three. Green's formula relates the two types of energy through an additional nonvanishing boundary-flux term on a lune; it does not equate their spectra. Seto, Wei and Zhu (2020) study the distinct Dirichlet boundary-value eigenproblem on spherical lunes.

## Limitations
The theorem addresses degree exactly two, uniform spherical probability measure, full tangential-gradient energy, and a symmetric lune with \(0<L<\pi\). It does not cover mixed-degree spaces, directional-only gradients, or arbitrary regions. The finite checker is supplementary, not a proof. An independently published equivalent or a stronger theorem implicitly determining these derivative eigenvalues may remain unindexed; independent scientific review is not performed. Full text of all possible historical sources cannot be guaranteed.

## References
1. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1, first posted 2021-03-26, Sections 2–4. https://arxiv.org/html/2103.14650v1
2. A. Aslam and Z. Khalid, *Spatial-Slepian Transform on the Sphere*, arXiv:2010.07266v1, first posted 2020-10-14, Sections II–III. https://arxiv.org/html/2010.07266v1
3. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1, first posted 2004-08-31, general regional concentration and cap sections. https://arxiv.org/html/math/0408424v1
4. S. Seto, G. Wei and X. Zhu, *Fundamental gaps of spherical triangles*, arXiv:2009.00229v1, first posted 2020-09-01, Section 2. https://arxiv.org/html/2009.00229v1
5. *Sharp quadratic spherical-lune concentration and its dimension-dependent optimizer transition*, published result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-quadratic-spherical-lune-concentration-and-its-dimension-d--03bb0ccb58c4
6. *Two sharp symmetry switches for quadratic spherical harmonics on a lune*, published result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-sharp-symmetry-switches-for-quadratic-spherical-harmonics-on--440750a519f4
7. A. P. Bates, Z. Khalid and R. A. Kennedy, *Slepian Spatial-Spectral Concentration Problem on the Sphere: Analytical Formulation for Limited Colatitude-Longitude Spatial Region*, arXiv:1608.03031v1, first posted 2016-08-10, equations (8)–(12). https://arxiv.org/abs/1608.03031
8. W. Nafees, Z. Khalid and R. A. Kennedy, *Differential and Weighted Slepian Concentration Problems on the Sphere*, IEEE Transactions on Signal Processing 68 (2020), DOI 10.1109/TSP.2020.2983644, equations (14),(16),(21)–(27). https://zubairkhalid.org/papers/J18.pdf
