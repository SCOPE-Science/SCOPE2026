# Sharp cubic spherical-harmonic concentration on an octant: a double optimal eigenspace

## Finding
Let \(S^2=\{(x,y,z):x^2+y^2+z^2=1\}\) have surface measure \(d\sigma\), let \(\Omega=\{(x,y,z)\in S^2:x,y,z\ge0\}\), and let \(\mathcal H_3\) be the seven-dimensional complex space of spherical harmonics of exactly degree three. For every nonzero \(f\in\mathcal H_3\), define the octant energy fraction
\[
Q(f)=\frac{\int_\Omega |f|^2\,d\sigma}{\int_{S^2}|f|^2\,d\sigma}.
\]
The complete spectrum of its concentration operator is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\displaystyle\frac{\pi-3}{8\pi}&1\\[4pt]
\displaystyle\frac{30\pi-5-\sqrt{6505}}{240\pi}&1\\[4pt]
\displaystyle\frac{30\pi+25-\sqrt{4045}}{240\pi}&2\\[4pt]
\displaystyle\frac{30\pi-5+\sqrt{6505}}{240\pi}&1\\[4pt]
\displaystyle\frac{30\pi+25+\sqrt{4045}}{240\pi}&2.
\end{array}
\]
The table is in strictly increasing order. Consequently the **sharp** energy inequality is
\[
\boxed{\frac{\pi-3}{8\pi}\le Q(f)\le\frac{30\pi+25+\sqrt{4045}}{240\pi}},
\]
and the sharp ratio of the upper to lower concentration levels is
\[
\frac{30\pi+25+\sqrt{4045}}{30(\pi-3)}=43.0455699116\ldots.
\]
The bottom eigenspace is the unique complex line spanned by \((x-y)(x-z)(y-z)\), while the top eigenspace is a two-dimensional complex space in the standard permutation-symmetry representation of the three coordinate axes. In particular, a maximally concentrated pure cubic is **not unique up to complex scaling**, whereas the least concentrated one is.

## Assumptions and scope
The region is the closed positive **surface octant**, not the solid octant or a union of octants. Its area fraction is \(1/8\). Boundary great-circle arcs have measure zero. The harmonic degree is exactly three (not the low-pass band through degree three), coefficients may be complex, and all integrals use the same unnormalized surface measure so that the quotient is independent of normalization. The concentration operator is the self-adjoint compression of multiplication by \(\mathbf1_\Omega\) to \(\mathcal H_3\) in the full-sphere \(L^2\) inner product. All eigenspaces and bounds refer to this operator.

## Proof
**1. A full cubic harmonic basis.** Write \(r^2=x^2+y^2+z^2\) and introduce the harmonic homogeneous cubics
\[
\begin{aligned}
P_1&=x(5x^2-3r^2),&P_2&=y(5y^2-3r^2),&P_3&=z(5z^2-3r^2),\\
B_1&=x(y^2-z^2),&B_2&=y(z^2-x^2),&B_3&=z(x^2-y^2),\\
W&=xyz.
\end{aligned}
\]
Their Euclidean Laplacians vanish. They are linearly independent, and \(\dim\mathcal H_3=7\), so they form a basis after restriction to the sphere.

**2. Exact regional moments.** For nonnegative integers \(a,b,c\) the unnormalized positive-octant monomial integral is
\[
\int_\Omega x^a y^b z^c\,d\sigma
=\frac{\Gamma((a+1)/2)\Gamma((b+1)/2)\Gamma((c+1)/2)}{4\Gamma((a+b+c+3)/2)}.
\]
This follows by using a Gaussian radial integral on the positive Euclidean orthant in two ways. On the full sphere the same integral is zero if any exponent is odd, and otherwise equals eight times the displayed positive-octant moment. Expanding the products of the seven cubics yields a diagonal full-sphere Gram matrix \(G\), in the displayed basis:
\[
G=\operatorname{diag}\left(\frac{16\pi}{7},\frac{16\pi}{7},\frac{16\pi}{7},
\frac{16\pi}{105},\frac{16\pi}{105},\frac{16\pi}{105},\frac{4\pi}{105}\right).
\]
Set \(E_i=P_i/\sqrt{16\pi/7}\), \(F_i=B_i/\sqrt{16\pi/105}\), and \(U=W/\sqrt{4\pi/105}\). These seven functions are orthonormal on the full sphere. Let \(K\) be their octant Gram matrix. With \(J=\begin{pmatrix}0&-1&1\\1&0&-1\\-1&1&0\end{pmatrix}\) and \(\mathbf 1=(1,1,1)^T\), the four nontrivial blocks of \(K\) are
\[
\begin{aligned}
K_{EE}&=\left(\frac18+\frac1{48\pi}\right)I_3-\frac1{48\pi}\mathbf1\mathbf1^T,\\
K_{FF}&=\left(\frac18+\frac3{16\pi}\right)I_3-\frac3{16\pi}\mathbf1\mathbf1^T,\\
K_{EF}&=\frac{3\sqrt{15}}{80\pi}J,\qquad K_{EU}=-\frac{\sqrt{15}}{20\pi}\mathbf1,\\
K_{FU}&=0,\qquad K_{UU}=\frac18.
\end{aligned}
\]
Here \(K_{FE}=K_{EF}^T\) and \(K_{UE}=K_{EU}^T\). These blocks follow solely from the exact gamma moments and fix all normalization constants.

**3. Permutation-symmetry decomposition.** Let \(E_0=(E_1+E_2+E_3)/\sqrt3\) and \(F_0=(F_1+F_2+F_3)/\sqrt3\). Since \(J\mathbf1=0\), the one-dimensional alternating sector spanned by \(F_0\) is invariant, with eigenvalue \(\lambda_A=(\pi-3)/(8\pi)\). Since \(B_1+B_2+B_3=-(x-y)(x-z)(y-z)\), this also identifies the unique least-concentrated line once the ordering is established.

The two-dimensional permutation-invariant sector spanned by \(E_0,U\) has symmetric matrix
\[
K_{\mathrm{triv}}=\begin{pmatrix}
\frac18-\frac1{24\pi}&-\frac{3\sqrt5}{20\pi}\\
-\frac{3\sqrt5}{20\pi}&\frac18
\end{pmatrix}.
\]
Its eigenvalues are \(\lambda_{T\pm}=(30\pi-5\pm\sqrt{6505})/(240\pi)\), each simple.

On the two-dimensional zero-sum subspace \(V=\{u\in\mathbb C^3:\sum u_i=0\}\), the remaining four-dimensional sector is \(V_E\oplus V_F\) with operator
\[
\begin{pmatrix}aI_V&kJ|_V\\-kJ|_V&bI_V\end{pmatrix},\quad
 a=\frac18+\frac1{48\pi},\quad b=\frac18+\frac3{16\pi},\quad k=\frac{3\sqrt{15}}{80\pi}.
\]
Since \(J^2=-3I\) on \(V\), its characteristic polynomial is \(\big((\lambda-a)(\lambda-b)-3k^2\big)^2\). Its two distinct eigenvalues are \(\lambda_{V\pm}=(30\pi+25\pm\sqrt{4045})/(240\pi)\), each of complex multiplicity two. In particular, the top space is given explicitly, in the normalized harmonic basis, by all vectors
\[
\sum_{i=1}^3u_i E_i-\frac{k}{\lambda_{V+}-b}\sum_{i=1}^3(Ju)_iF_i,
\qquad u\in V.
\]
The alternating, invariant, and standard sectors have dimensions \(1+2+4=7\); therefore the spectrum is complete.

**4. Strict ordering and sharpness.** The elementary integer bounds \(80<\sqrt{6505}<81\) and \(63<\sqrt{4045}<64\) imply
\[
0<\lambda_A<\lambda_{T-}<\lambda_{V-}<\lambda_{T+}<\lambda_{V+}<1.
\]
Indeed the differences, after multiplying by \(240\pi\), between successive levels are \(85-\sqrt{6505}\), \(30+\sqrt{6505}-\sqrt{4045}\), \(\sqrt{6505}+\sqrt{4045}-30\), and \(30+\sqrt{4045}-\sqrt{6505}\), respectively. Positivity of \(\lambda_A\) uses \(\pi>3\), and the upper bound \(\lambda_{V+}<1\) follows from \(\pi>3\) and \(\sqrt{4045}<64\). The variational min-max principle now yields the sharp bounds and equality spaces stated above.

## Verification
Run `python check_exact.py` with SymPy installed and `python check_numeric.py` with NumPy installed, from this folder. The former independently integrates all 49 polynomial Gram entries by the gamma formula, checks harmonicity, the full-sphere normalization, the factored characteristic polynomial, five strict eigenvalue levels and the alternating eigenvector. It returned `EXACT_OCTANT_CUBIC_PASS 7 harmonic modes; 49 Gram entries; 5 eigenvalues`. The latter builds the octant Gram matrix without using monomial moments, by 64-point Gauss-Legendre quadrature in each of the two spherical angular coordinates (4096 nodes), and checks its spectrum; the maximum eigenvalue error was \(4.31\times10^{-16}\). The analytical proof, not finite quadrature, establishes exactness.

## Relationship to prior work
Slepian's spherical spatiospectral concentration problem and its integral-matrix formulation are established by Simons, Dahlen, and Wieczorek (2004). Michel, Plattner, and Seibert (2021) develop general spin-weighted Slepian bases and commuting operators for spherical caps; they do not derive an octant cubic spectrum. Grasshorn Gebhardt and Doré (2021) treat Laplacian-adapted harmonic analysis for arbitrary sky masks, a related but different spectral operator; they explicitly describe the general-mask problem as requiring numerical calculation. Roddy and McEwen (2023) develop Slepian wavelets for incomplete manifolds using region-concentration matrices, not this evaluated octant spectrum. Previously reported exact quadratic orthant spectra concern degree two, and low-pass octant spectra through degree two do not contain the exact-degree-three harmonic sector. Neither a generic matrix construction nor any of these lower-degree results supplies the five evaluated cubic eigenvalues or the two-dimensional optimal eigenspace by implication alone.

## Limitations
The theorem concerns a single spherical octant on \(S^2\), only pure cubic spherical harmonics, and noiseless energy fractions. It does not determine higher-degree spectra, arbitrary spherical triangles, full low-pass cubic bands, or discrete sampling stability. The concentration eigenvalue ratio is not a noise-model-dependent reconstruction bound. Historical priority is provisional: an unindexed specialist table or derivation of octant cubic moments might cover this exact spectrum. No independent audit has been performed.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, first public 2004-08-31, https://arxiv.org/abs/math/0408424.
2. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first public 2021-03-26, https://arxiv.org/abs/2103.14650.
3. H. S. Grasshorn Gebhardt, O. Doré, *Harmonic analysis of isotropic fields on the sphere with arbitrary masks*, arXiv:2109.13352v1, first public 2021-09-27, https://arxiv.org/abs/2109.13352.
4. P. J. Roddy, J. D. McEwen, *Slepian Scale-Discretised Wavelets on Manifolds*, arXiv:2302.06006v1, first public 2023-02-12, https://arxiv.org/abs/2302.06006.
