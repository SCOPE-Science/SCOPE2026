# Sharp quadratic-harmonic concentration on a spherical cube face

## Finding
Let \(R=\{(x,y,z)\in\mathbb S^2:x\ge |y|,\ x\ge |z|\}\), one of the six equal-area geodesic-square faces of the standard cubed sphere. Let \(\mathcal H_2\) be the complex five-dimensional space of restrictions to \(\mathbb S^2\) of homogeneous harmonic quadratic polynomials on \(\mathbb R^3\). The self-adjoint concentration operator \(T_R:\mathcal H_2\to\mathcal H_2\) is defined by
\[
\langle T_R f,g\rangle_{\mathbb S^2}=\int_R f\overline g\,d\sigma.
\]
Its complete spectrum, in decreasing order, is
\[
\boxed{\frac16+\frac{\sqrt3}{4\pi}\quad(1),\qquad
\frac16+\frac{\sqrt3}{9\pi}\quad(2),\qquad
\frac16-\frac{2\sqrt3}{9\pi}\quad(1),\qquad
\frac16-\frac{\sqrt3}{4\pi}\quad(1).}
\]
Parentheses denote multiplicity. The corresponding eigenspaces are, respectively, the spans of \(3x^2-1\), of \(xy,xz\), of \(yz\), and of \(y^2-z^2\), where every polynomial is evaluated on the unit sphere.

Consequently, for **every nonzero complex** \(f\in\mathcal H_2\),
\[
\boxed{\frac16-\frac{\sqrt3}{4\pi}\ \le\
\frac{\int_R|f|^2\,d\sigma}{\int_{\mathbb S^2}|f|^2\,d\sigma}\ \le\
\frac16+\frac{\sqrt3}{4\pi}.}
\]
Equality on the left occurs precisely for nonzero complex scalar multiples of \(y^2-z^2\), and on the right precisely for nonzero complex scalar multiples of \(3x^2-1\). The sharp ratio of upper to lower **energy** bounds is
\[
\frac{2\pi+3\sqrt3}{2\pi-3\sqrt3}.
\]
These are exact finite-dimensional concentration constants, not statements about arbitrary functions or higher harmonic degrees.

## Assumptions and scope
The sphere is the unit Euclidean two-sphere with ordinary surface-area measure \(d\sigma\); integrals are not probability normalized. The boundary of \(R\) is irrelevant to the integrals. The harmonic projection and inner product use global full-sphere normalization. The result applies to real and complex degree-two spherical harmonics, but **not** to the full band of degrees zero through two. A rotated cube face has the same spectrum with rotated eigenfunctions.

## Proof
Write
\[
(x,y,z)=\frac{(1,u,v)}{\sqrt{1+u^2+v^2}},\qquad -1\le u,v\le1,
\]
so that \(d\sigma=(1+u^2+v^2)^{-3/2}du\,dv\). The six cube faces partition \(\mathbb S^2\) up to null boundaries, hence \(\Omega:=\int_Rd\sigma=2\pi/3\).

Set
\[
A=\int_R x^4d\sigma,\quad B=\int_Rx^2y^2d\sigma=\int_Rx^2z^2d\sigma,\quad
C=\int_Ry^4d\sigma=\int_Rz^4d\sigma,\quad E=\int_Ry^2z^2d\sigma.
\]
Thus \(A,B,C,E\) are obtained by integrating \(1,u^2,u^4,u^2v^2\), respectively, against \((1+u^2+v^2)^{-7/2}du\,dv\) over the unit square. Direct elementary evaluation gives the boundary terms
\[
T_1=2\int_{-1}^{1}(2+v^2)^{-5/2}dv=\frac{8\sqrt3}{27},\qquad
T_3=2\int_{-1}^{1}v^2(2+v^2)^{-5/2}dv=\frac{2\sqrt3}{27}.
\]
For example \(v=\sqrt2\tan\theta\) reduces both to trigonometric polynomial integrals. Integrate on the square the three total derivatives
\[
\partial_u\bigl(u(1+u^2+v^2)^{-5/2}\bigr),\quad
\partial_u\bigl(u^3(1+u^2+v^2)^{-5/2}\bigr),\quad
\partial_u\bigl(uv^2(1+u^2+v^2)^{-5/2}\bigr).
\]
The resulting exact relations are
\[
A-3B=T_1,\qquad 3B-2C+3E=T_1,\qquad B+C-4E=T_3.
\]
Since \((x^2+y^2+z^2)^2=1\), symmetry also gives \(A+4B+2C+2E=\Omega\). Solving these four linear equations yields
\[
A=\frac{2\pi}{15}+\frac{52\sqrt3}{135},\quad
B=\frac{2\pi}{45}+\frac{4\sqrt3}{135},\quad
C=\frac{2\pi}{15}-\frac{26\sqrt3}{135},\quad
E=\frac{2\pi}{45}-\frac{8\sqrt3}{135}.
\]

The five harmonic quadratics
\[
Q_0=3x^2-1,\quad Q_1=xy,\quad Q_2=xz,\quad Q_3=y^2-z^2,\quad Q_4=yz
\]
span \(\mathcal H_2\). Each pair is orthogonal on the full sphere and also on \(R\): independent reflections of \(y,z\) and interchange \(y\leftrightarrow z\) eliminate cross terms. In this order their full-sphere squared norms are
\[
\frac{16\pi}{5},\quad\frac{4\pi}{15},\quad\frac{4\pi}{15},\quad
\frac{16\pi}{15},\quad\frac{4\pi}{15},
\]
and their squared norms over \(R\) are, respectively,
\[
3A-12B+\Omega,\quad B,\quad B,\quad2(C-E),\quad E.
\]
Division gives exactly the four spectral values in the claim. Their strict order follows from the successive positive differences \(5\sqrt3/(36\pi)\), \(\sqrt3/(3\pi)\), and \(\sqrt3/(36\pi)\). Positivity of the least eigenvalue follows from \(2\pi>3\sqrt3\). Since the diagonalization holds over the complexification, the variational min–max principle gives both sharp inequalities and all equality spaces. This is a proof for every nonzero \(f\), not an inference from sampled numerical cases.

## Verification
The standalone file `verify_cube_face.py` independently checks the moment linear system, rational-radical spectrum, eigenvalue ordering and trace using exact symbolic arithmetic, then computes all 25 entries of the locally normalized concentration matrix by direct tensor Gauss–Legendre quadrature on the cubed-sphere square at orders 24, 40, 64 and 100. The maximum absolute entrywise discrepancy was below \(3\cdot10^{-15}\) in the reported runs. Execute `python verify_cube_face.py` with installed `sympy` and `numpy`. The numerical test checks the exact proof but is not its substitute.

## Relationship to prior work
Simons, Dahlen and Wieczorek established the general spherical Slepian spatial–spectral concentration eigenproblem. Roddy and McEwen extended Slepian constructions on manifolds and motivated regional localization. Simons and collaborators used gnomonic cubed-sphere patches for spherical wavelet analysis. Faham and Nasir studied cubed-sphere harmonic bases and inner products in that coordinate system. These frameworks provide the context, global harmonic machinery and square-face coordinates; none of the passages inspected provides the four exact **single-face pure-degree-two** eigenvalues and equality spaces derived here. In particular, a formula for general inner products or an orthogonal basis on the whole sphere is not a previously evaluated sharp local concentration spectrum. Related exact localization results for octants, quadrants, antipodal caps and tetrahedral triangular cells concern different regions; their spectra do not imply this one through geometric congruence or simple complementarity.

## Limitations
Only one cubed-sphere face, pure degree two and the unweighted ordinary area measure are analyzed. No results for sampling at nodes, a full harmonic band, higher degrees, noisy discrete reconstruction or stability of numerical quadrature are claimed. Priority is assessed against the inspected literature and indexed results; a previously unindexed equivalent exact cube-face calculation cannot be excluded without specialist review.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review 48 (2006); preprint https://arxiv.org/abs/math/0408424.
2. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on Manifolds*, first submitted 12 February 2023, https://arxiv.org/abs/2302.06006.
3. F. J. Simons, I. Loris, E. Brevdo, I. C. Daubechies, *Wavelets and wavelet-like transforms on the sphere and their application to geophysical data inversion*, Proc. SPIE 8138 (2011), https://geoweb.princeton.edu/people/simons/PDF/reprints/SPIE-2011.pdf.
4. M. A. A. M. Faham and H. M. Nasir, *Weakly Orthogonal Spherical Harmonics in Non-Polar Spherical Coordinates and its Application to Functions on Cubed-Sphere*, SQU Journal for Science 17(2) (2012), pp. 200–213, https://distantreader.org/stacks/journals/squjs/squjs-403.pdf.
