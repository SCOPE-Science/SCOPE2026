# Exact transverse sixth-moment stability for the hexagonal Fourier aperture

## Finding

Consider the six frequencies of the triangular-lattice root hexagon, in this fixed order,
\[
\Lambda=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))\subset\mathbb Z^2.
\]
For \(c=(c_1,\ldots,c_6)\in\mathbb C^6\setminus\{0\}\), set
\[
P_c(z,w)=c_1z+c_2z^{-1}+c_3w+c_4w^{-1}+c_5zw+c_6(zw)^{-1},
\quad
\mathcal J(c)=\frac{\int_{\mathbb T^2}|P_c|^6\,dm}{(\sum_{j=1}^6|c_j|^2)^3},
\]
where \(dm\) is Haar **probability** measure. Let \(u=6^{-1/2}(1,1,1,1,1,1)\) and let its phase-and-translation orbit be
\[
\mathcal O=\left\{6^{-1/2}\big(e^{i(\theta+\langle \lambda_j,t\rangle)}\big)_{j=1}^6:\theta\in\mathbb R,\ t\in\mathbb R^2\right\}.
\]
Then \(\mathcal J(u)=85/9\), and \(\mathcal O\) is a *strict local maximizing manifold on the coefficient unit sphere*: for every \(c\) of unit Euclidean norm sufficiently near \(\mathcal O\), equality \(\mathcal J(c)=85/9\) holds only on \(\mathcal O\).

More precisely, write a tangent perturbation \(h=x+iy\), with \(x,y\in\mathbb R^6\) and \(\sum_j x_j=0\). The coefficient of \(\varepsilon^2\) in \(\mathcal J(u+\varepsilon h)\) is
\[
Q(h)=x^TH_xx+y^TH_yy,
\]
where the complete **real-amplitude transverse spectrum** of \(H_x\) is
\[
-77/3\ (1\text{ time}),\quad-68/3\ (2\text{ times}),\quad -65/3\ (2\text{ times}),
\]
and the **phase spectrum** of \(H_y\) is
\[
0\ (3\text{ times}),\qquad-15\ (1\text{ time}),\qquad-27\ (2\text{ times}).
\]
The three zero phase directions are exactly common phase and the two torus translations; no other zero modes occur. Equivalently, writing \(d(c,\mathcal O)=\inf_{v\in\mathcal O}\|c-v\|_{\ell^2}\), the **sharp quadratic local deficit coefficient** is
\[
\boxed{\lim_{\delta\downarrow0}\inf_{\substack{\|c\|_2=1\\0<d(c,\mathcal O)<\delta}}
\frac{85/9-\mathcal J(c)}{d(c,\mathcal O)^2}=15.}
\]
It is approached by the imaginary direction \(i(1,-1,1,-1,-1,1)/\sqrt6\). This is a **local** theorem, not a claim that \(85/9\) is the global best sixth-moment constant on the entire six-dimensional space.

## Assumptions and scope

The coefficients are unrestricted complex numbers, with Euclidean normalization only when defining distance to \(\mathcal O\). Frequencies remain the six listed integer pairs, the moment order is exactly six, and the integration measure is normalized Haar measure on the continuous two-dimensional torus. A phase translation acts as \(c_j\mapsto e^{i(\theta+\langle\lambda_j,t\rangle)}c_j\); it preserves the norm and moment. The local statement concerns a neighborhood of the three-real-dimensional compact orbit \(\mathcal O\) in the unit sphere \(S^{11}\). The displayed coefficient \(15\) measures **squared Euclidean distance in coefficient space** and is the half-Hessian eigenvalue, not twice it.

## Proof

**1. Exact convolution identity.** For any frequency \(\nu\in\mathbb Z^2\), let
\[
T_\nu=\{(i,j,k)\in\{1,\ldots,6\}^3:\lambda_i+\lambda_j+\lambda_k=\nu\}.
\]
Expanding \(P_c^3\) and applying Parseval gives the finite identity
\[
\int_{\mathbb T^2}|P_c|^6\,dm=\sum_\nu\left|\sum_{(i,j,k)\in T_\nu}c_ic_jc_k\right|^2.
\tag{1}
\]
There are exactly \(216\) ordered triples and \(37\) occupied frequencies, and \(\sum_\nu |T_\nu|^2=2040\), all obtained by integer addition. At \(u\), each cubic convolution coefficient is \(|T_\nu|/(6\sqrt6)\), giving \(2040/216=85/9\).

**2. Exact quadratic Taylor coefficient.** Write \(c=u+\varepsilon h\) with \(h=x+iy\). For each \(\nu\), define
\[
d_\nu=\frac{|T_\nu|}{6\sqrt6},\qquad
b_\nu(h)=\frac16\sum_{(i,j,k)\in T_\nu}(h_i+h_j+h_k),
\]
\[
e_\nu(h)=\frac1{\sqrt6}\sum_{(i,j,k)\in T_\nu}(h_ih_j+h_ih_k+h_jh_k).
\]
The cubic convolution in (1) is exactly \(d_\nu+\varepsilon b_\nu(h)+\varepsilon^2e_\nu(h)+\varepsilon^3\sum_{T_\nu}h_ih_jh_k\). Thus its squared modulus has quadratic coefficient
\[
\sum_\nu |b_\nu(h)|^2+2\operatorname{Re}\sum_\nu d_\nu\overline{e_\nu(h)}.
\tag{2}
\]
By sixfold frequency symmetry, the first derivative of the numerator is radial, and it vanishes on \(\sum_jx_j=0\). Moreover,
\[
\sum_j|u_j+\varepsilon h_j|^2=1+\varepsilon^2\|h\|_2^2
\quad\text{on this tangent space}.
\]
Since the denominator in \(\mathcal J\) is the cube of this quantity, the quadratic coefficient of \(\mathcal J\) equals (2) minus \((85/3)\|h\|_2^2\). Cross-terms between \(x\) and \(y\) vanish because all \(d_\nu\) and convolution incidence counts are real.

**3. Exact matrices and spectral diagonalization.** Enumerating only the integer triples in (1) yields the symmetric matrices
\[
H_x=\begin{pmatrix}
-1/6&47/2&22&23&23&22\\
47/2&-1/6&23&22&22&23\\
22&23&-1/6&47/2&23&22\\
23&22&47/2&-1/6&22&23\\
23&22&23&22&-1/6&47/2\\
22&23&22&23&47/2&-1/6
\end{pmatrix},
\]
\[
H_y=\begin{pmatrix}
-23/2&-13/2&2&7&7&2\\
-13/2&-23/2&7&2&2&7\\
2&7&-23/2&-13/2&7&2\\
7&2&-13/2&-23/2&2&7\\
7&2&7&2&-23/2&-13/2\\
2&7&2&7&-13/2&-23/2
\end{pmatrix}.
\]
Their eigenspace dimensions can be verified exactly by rational row reduction of \(H_x-\mu I\) and \(H_y-\mu I\); the resulting six eigenvalues with multiplicities are \(340/3\) (radial), \(-77/3\), \(-68/3\) twice and \(-65/3\) twice for \(H_x\); and \(0\) three times, \(-15\) once, \(-27\) twice for \(H_y\). The one-dimensional radial eigenvector \((1,1,1,1,1,1)\) for \(H_x\) is **not tangent** to the coefficient sphere, so the five negative values are precisely the amplitude spectrum claimed. The three linearly independent vectors \((1,\ldots,1)\), \((\lambda_{j,1})_j\), and \((\lambda_{j,2})_j\) span \(\ker H_y\), which identifies all phase symmetry directions.

**4. Strict local maximality and optimal deficit.** Smoothness of \(\mathcal J\) on nonzero coefficient vectors, compactness of \(\mathcal O\), and orthogonal tubular coordinates along the orbit give a uniform expansion, for the Euclidean normal displacement \(h\),
\[
\frac{85}{9}-\mathcal J(c)=-Q(h)+O(\|h\|_2^3),\qquad
\|h\|_2=d(c,\mathcal O)+O(d(c,\mathcal O)^2).
\]
All normal eigenvalues are strictly negative, with largest one \(-15\). This proves a strict local maximum, and the lower limit of the deficit-to-distance ratio is at least \(15\). The imaginary normal vector \(i(1,-1,1,-1,-1,1)/\sqrt6\) has norm one, is orthogonal to all orbit tangents, and is an eigenvector with eigenvalue \(-15\). Unit normalization of \(u+\varepsilon h\) and the Taylor expansion yield the reverse bound, so the limit equals \(15\).

## Verification

Run `python3 checker.py` in this directory using only the Python standard library. It enumerates all ordered triples, rebuilds the exact rational matrices independently of the written display, checks their entries, checks every asserted eigenspace multiplicity by rational Gaussian elimination, identifies the symmetry kernel and least-stable vector, and performs supplementary small-perturbation evaluations of (1). The exact result is `HEXAGONAL_L6_LOCAL_PASS triples=216 sums=37 numerator=2040 real_bands=4 phase_bands=3 gap=15`. Finite perturbation checks serve only as corroboration; the universal local statement follows from the exact polynomial identity, rational spectral calculation and smooth Taylor argument.

## Relationship to prior work

Gonçalves and Negro (arXiv:2003.11955, first public 2020-03-26) prove local stability for continuous Euclidean Fourier restriction on the cone, paraboloid and sphere, using dispersive and geometric transformations. Their operators integrate over curved Euclidean surfaces and their theorems do not specialize to the six-character torus polynomial in (1). Ciccone and Gonçalves (arXiv:2208.09441, first public 2022-08-19) study continuous circle Fourier extension under sparse arithmetic constraints, involving Bessel-function integrals. Its \(L^6\) functional is not the present Haar-torus sixth moment. The published six-point triangular-aperture calculation `bea9cf2ed885` concerns \(L^4\) and a non-centrally-symmetric triangular frequency support \(\{(i,j):i+j\le2\}\); the present frequency support is a genuine hexagon and the assertion is a local \(L^6\) Hessian and sharp distance coefficient. The finite-field characteristic-three parabola local-sixth-moment result `158763dab4f3` concerns a distinct group and convolution geometry, so neither its quadratic bands nor its conclusion imply those here. General symmetry principles alone do not fix the numerical transverse spectrum or rule out additional unstable directions.

## Limitations

No global \(L^2\)-to-\(L^6\) sharp constant or classification of global maximizers is claimed. The coefficient \(15\) is the sharp infinitesimal **local** constant; no optimal noninfinitesimal neighborhood size is determined. The stability neighborhood depends only on this fixed six-mode model, not on a varying number of modes. Earlier unindexed equivalent computations of a hexagonal six-wave Hessian are an outstanding bibliographic risk; independent validation has not been performed.

## References

1. F. Gonçalves and G. Negro, *Local maximizers of adjoint Fourier restriction estimates for the cone, paraboloid and sphere*, arXiv:2003.11955v1, first public 2020-03-26, https://arxiv.org/abs/2003.11955.
2. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, first public 2022-08-19, https://arxiv.org/abs/2208.09441.
3. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, published-finding corpus public record `2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
4. *Exact local sixth-moment stability of the parabola in characteristic three*, published-finding corpus public record `2026/10/11/SCOPE-exact-local-sixth-moment-stability-of-the-parabola-in-characteri--158763dab4f3`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-local-sixth-moment-stability-of-the-parabola-in-characteri--158763dab4f3.
