# Exact quadrupolar Slepian spectrum of a tetrahedral spherical Voronoi cell

## Finding
Let \(R\) be one spherical Voronoi cell of a regular tetrahedron on the unit sphere, and let \(\mathcal H_2\) be the five-dimensional space of exact-degree-two spherical harmonics. For every nonzero \(f\in\mathcal H_2\), set
\[
\mathcal E_R(f)=\frac{\int_R |f|^2\,d\sigma}{\int_{\mathbb S^2}|f|^2\,d\sigma}.
\]
The complete concentration spectrum has **three distinct levels**:
\[
\lambda_- =\frac14-\frac{\sqrt{219}+\sqrt3}{36\pi}\quad(\text{multiplicity }2),\qquad
\lambda_0=\frac14+\frac{\sqrt3}{9\pi}\quad(\text{multiplicity }1),\qquad
\lambda_+=\frac14+\frac{\sqrt{219}-\sqrt3}{36\pi}\quad(\text{multiplicity }2).
\]
They satisfy \(0<\lambda_-<\lambda_0<\lambda_+<1\). Thus the **sharp two-sided restriction inequality** is
\[
\lambda_-\int_{\mathbb S^2}|f|^2\,d\sigma
\le\int_R|f|^2\,d\sigma
\le\lambda_+\int_{\mathbb S^2}|f|^2\,d\sigma.
\]
Numerically the lower and upper factors are \(0.103836526588684\ldots\) and \(0.365534090332327\ldots\), respectively. The maximizing eigenspace has dimension **two**, whereas the unique axial quadrupole has the strictly smaller fraction \(0.311258766157977\ldots\).

## Assumptions and scope
Place the tetrahedral vertices at \((1,1,1)/\sqrt3\), \((1,-1,-1)/\sqrt3\), \((-1,1,-1)/\sqrt3\), and \((-1,-1,1)/\sqrt3\). The Voronoi cell around the first vertex is, up to measure-zero boundary,
\[
R=\{(x,y,z)\in\mathbb S^2:x+y\ge0,\;x+z\ge0,\;y+z\ge0\}.
\]
It is a spherical equilateral triangle with vertices \((1,1,-1)/\sqrt3\), \((1,-1,1)/\sqrt3\), \((-1,1,1)/\sqrt3\) and area \(\pi\). Every side has arc length \(\arccos(-1/3)\). All integrals use standard sphere area measure \(d\sigma\). The theorem applies to real or complex homogeneous harmonic quadratics, **not** to the full band of degrees zero through two or to arbitrary higher-degree functions.

Let \(e=(1,1,1)/\sqrt3\), \(u=(1,-1,0)/\sqrt2\), \(v=(1,1,-2)/\sqrt6\). For a variable vector \(X=(x,y,z)\), write \(t=e\cdot X\), \(a=u\cdot X\), \(b=v\cdot X\), \(r^2=|X|^2\), and define the harmonic quadratics
\[
Q_0=(3t^2-r^2)/2,\quad Q_1=\sqrt3\,ta,\quad Q_2=\sqrt3\,tb,\quad
Q_3=\tfrac{\sqrt3}{2}(a^2-b^2),\quad Q_4=\sqrt3\,ab.
\]
The restrictions \(\sqrt5 Q_j\) constitute an orthonormal basis on the whole sphere under the probability measure \(d\sigma/(4\pi)\).

## Proof
The four Voronoi cells partition the sphere into congruent spherical triangles, so \(\operatorname{area}(R)=\pi\). Standard fourth moments of the uniform sphere, \(\mathbb E[(w\cdot X)^4]=1/5\) and \(\mathbb E[(w\cdot X)^2(w'\cdot X)^2]=1/15\) for orthonormal \(w,w'\), establish the asserted basis orthonormality.

The concentration matrix in this basis is \(M_{ij}=\frac5{4\pi}\int_R Q_iQ_j\,d\sigma\). Its **exact** evaluation gives
\[
M=\begin{pmatrix}
Z&0&0&0&0\\
0&A&0&0&C\\
0&0&A&C&0\\
0&0&C&B&0\\
0&C&0&0&B
\end{pmatrix},
\]
where
\[
Z=\frac14+\frac{\sqrt3}{9\pi},\qquad
A=\frac14+\frac{11\sqrt3}{54\pi},\qquad
B=\frac14-\frac{7\sqrt3}{27\pi},\qquad
C=-\frac{\sqrt6}{27\pi}.
\]
For completeness, this evaluation can be checked without numerical integration as follows. Every product \(p=Q_iQ_j\) is homogeneous of degree four and admits a unique harmonic decomposition \(p=h_4+r^2h_2+cr^4\). Writing \(\Delta\) for the Euclidean Laplacian,
\[
c=\frac{\Delta^2p}{120},\qquad h_2=\frac{\Delta p-20cr^2}{14},\qquad h_4=p-r^2h_2-cr^4.
\]
On the unit sphere, \(\Delta_{\mathbb S^2}h_\ell=-\ell(\ell+1)h_\ell\) for \(\ell=2,4\). The spherical divergence theorem consequently yields the **finite boundary formula**
\[
\int_R p\,d\sigma=\pi c-\frac16\sum_{E\subset\partial R}\int_E\partial_\nu h_2\,ds
-\frac1{20}\sum_{E\subset\partial R}\int_E\partial_\nu h_4\,ds.
\]
Each great-circle edge has a constant outward tangent normal \(\nu\) equal to one of \(-(1,1,0)/\sqrt2\), \(-(1,0,1)/\sqrt2\), \(-(0,1,1)/\sqrt2\). If \(w,w'\) are its endpoint unit vectors, parameterize it by \(w\cos s+z\sin s\), where \(z=(w'+w/3)/(2\sqrt2/3)\) and \(0\le s\le\arccos(-1/3)\). The integrands \(\partial_\nu h_2\) and \(\partial_\nu h_4\) become linear and cubic trigonometric polynomials, respectively. Integrating these elementary terms gives the displayed entries \(Z,A,B,C\) exactly; `exact_tetra_slepian.py` implements the entire symbolic calculation from these formulas.

The matrix splits into a scalar block \(Z\) and two identical blocks \(\begin{psmallmatrix}A&C\\ C&B\end{psmallmatrix}\). The block eigenvalues are
\[
\frac{A+B}2\pm\sqrt{\frac{(A-B)^2}4+C^2}
=\frac14+\frac{-\sqrt3\pm\sqrt{219}}{36\pi}.
\]
Moreover \(\lambda_+-Z=(\sqrt{219}-5\sqrt3)/(36\pi)>0\), and \(Z-\lambda_-=(\sqrt{219}+5\sqrt3)/(36\pi)>0\), since \(219>75\). This proves the sharp extremes and multiplicities.

In the above basis, the maximizing eigenspace is the span of \(Q_1+\kappa Q_4\) and \(Q_2+\kappa Q_3\), with
\[
\kappa=\frac{25\sqrt3-3\sqrt{219}}{4\sqrt6}.
\]
The minimizing eigenspace is the other eigenline in each two-by-two block, and the axial line \(\mathbb C Q_0\) has concentration \(\lambda_0\).

## Verification
Run `python exact_tetra_slepian.py` with SymPy installed to verify the harmonic decomposition, every symbolic boundary integral, the exact five-by-five matrix and the three eigenvalue expressions. Run `python verify_tetra_numeric.py` with NumPy and SciPy installed for a separate numerical integration directly in spherical coordinates (without boundary formulas). The latter attains maximum matrix error less than \(8\times10^{-11}\) in the tested environment. All checks use the included code; no partial enumeration is used to infer an infinite statement.

## Relationship to prior work
The spherical Slepian framework of Simons, Dahlen and Wieczorek defines concentration on arbitrary regions. Bates, Khalid and Kennedy provide numerical methods for arbitrary masks and an analytic treatment of coordinate-rectangle masks. Roddy and McEwen motivate Slepian functions and wavelets on observed subregions of manifolds. These general constructions do **not themselves state** the present exact three-level spectrum for a tetrahedral *Voronoi* triangle, the double extremal eigenspace, or the closed sharp factors. Published calculations for *unions of tetrahedron-centered circular caps*, polar sectors and orthants use geometrically different masks and do not immediately imply the integral matrix here. No claim is made that the abstract Slepian eigenproblem or symmetry-based block reduction is new.

## Limitations
Only the pure degree-two space and one regular-tetrahedral Voronoi cell are treated. The result is a closed exact low-degree benchmark, not a general high-bandlimit algorithm or a statement about noise distribution. Priority against unindexed older exact spherical-polygon harmonic tables has not been independently certified. The separate numerical quadrature corroborates but is not the proof; the proof is the exact boundary identity and matrix evaluation.

## References
- P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on Manifolds*, first public 2023-02-12, https://arxiv.org/abs/2302.06006.
- F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, https://arxiv.org/abs/math/0408424.
- A. P. Bates, Z. Khalid and R. A. Kennedy, *Efficient Computation of Slepian Functions for Arbitrary Regions on the Sphere*, https://arxiv.org/abs/1608.05479.
- A. P. Bates, Z. Khalid and R. A. Kennedy, *Slepian Spatial-Spectral Concentration Problem on the Sphere: Analytical Formulation for Limited Colatitude-Longitude Spatial Region*, https://arxiv.org/abs/1608.03031.
