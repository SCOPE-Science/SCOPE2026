# Sharp two-equator frames for quadratic spherical harmonics: generic injectivity and an optimal oblique angle

## Finding
Let \(d\ge3\) and \(\mathcal H_2(S^{d-1})\) be the complex restrictions of trace-free homogeneous quadratic polynomials. Given unit vectors \(u,v\) with \(c=|u\cdot v|\in(0,1)\), define the equators \(E_u=\{x\in S^{d-1}:u\cdot x=0\}\) and \(E_v\) similarly. Each equator carries normalized uniform surface measure; the observation squared norm is the arithmetic mean of its two squared trace norms. The input norm uses normalized measure on \(S^{d-1}\). Denote the resulting positive Gram operator by \(C_{d,c}\).

Set
\[
K_d=\frac{d(d+2)}{d^2-1},\quad T_d(c)=\frac{3(1+c^2)}4+\frac1{2d},\quad D_d(c)=\frac{d+1}{2d}c^2,
\qquad h_\pm=\frac{T_d(c)\pm\sqrt{T_d(c)^2-4D_d(c)}}2.
\]
Its complete spectrum is \(K_d\) times the following multiset:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1&(d-2)(d-1)/2-1\quad(d\ge4)\\
(1+c)/2&d-2\\
(1-c)/2&d-2\\
3(1-c^2)/4&1\\
h_+&1\\
h_-&1.
\end{array}
\]
For \(d=3\) the first row is absent. All eigenvalues are positive. Thus **two nonparallel, nonorthogonal equatorial traces determine every pure quadratic harmonic**, whereas either coincident or orthogonal equators have a nonzero kernel.

The sharp smallest Gram eigenvalue is
\[
\lambda_{\min}(C_{d,c})=K_d\min\left\{h_-(d,c),\frac{1-c}{2}\right\}.
\]
It has a **unique** maximum at
\[
\boxed{c_d^*=\frac{\sqrt{3d^2+6d+4}-2}{3d}},\qquad
\lambda_{\min}^{\mathrm{opt}}=K_d\frac{1-c_d^*}{2}.
\]
This is an angular design theorem: the optimal acute angle between the normals has cosine \(c_d^*\), which increases from \(5/9\) at \(d=3\) to \(1/\sqrt3\) as \(d\to\infty\). The same angle uniquely minimizes the singular-value condition number. For \(d\ge4\) this minimum is \(\sqrt{2/(1-c_d^*)}\), tending to \(\sqrt{3+\sqrt3}\). For \(d=3\) the minimum is \(5/\sqrt6\).

## Assumptions and scope
The data are **function-valued full equatorial traces**, not the scalar great-circle integrals of the Funk transform. Quadratics can be complex; the real trace-free symmetric matrix proof complexifies without changing the eigenvalues. The two equators have equal unit-probability surface weights. The main spectral formulas hold for every real \(d\) that is an integer at least \(3\), every pair of normals with \(0<c<1\), and continuous, noiseless observations. Equal-probability normalization is essential to the displayed constants. No finite-sample, higher-degree or unequal-weight claim is made.

## Proof
**Fourth moments and normalization.** Identify a harmonic as \(p_A(x)=x^\top A x\), with \(A\) complex symmetric and \(\operatorname{tr}A=0\). The complexification is obtained from the real symmetric calculation by polarization. For real \(A\), the normalized whole-sphere energy is
\[
\int_{S^{d-1}}p_A^2=\frac{2\|A\|_F^2}{d(d+2)}.
\]
Writing \(P_n=I-nn^\top\), the uniform fourth-moment identity in the \((d-1)\)-dimensional hyperplane gives
\[
\int_{E_n}p_A^2=\frac{2\|P_nAP_n\|_F^2+[\operatorname{tr}(P_nAP_n)]^2}{(d-1)(d+1)}
=\frac{2\|A\|_F^2-4\|An\|^2+3(n^\top An)^2}{d^2-1}.
\]
Consequently the normalized two-trace Gram form on trace-free symmetric matrices is
\[
\frac{\langle C_{d,c}A,A\rangle_F}{K_d}=
\|A\|_F^2-\|Au\|^2-\|Av\|^2+
\frac34[(u^\top Au)^2+(v^\top Av)^2]
\]
for input matrices with Frobenius inner product, with \(K_d=d(d+2)/(d^2-1)\). Polarization yields the full bilinear Gram form.

**Invariant blocks.** Orient the normals so that \(u\cdot v=c\). Let \(e_+,e_-\) be their normalized sum and difference and let \(W=\operatorname{span}\{u,v\}^{\perp}\) have dimension \(m=d-2\). Put \(p=(1+c)/2\), \(q=(1-c)/2\); then \(u=\sqrt p\,e_++\sqrt q\,e_-\) and \(v=\sqrt p\,e_+-\sqrt q\,e_-\). The trace-free symmetric matrices split orthogonally into four invariant sectors: trace-free symmetric matrices supported on \(W\); mixed \(e_+\)-to-\(W\) matrices; mixed \(e_-\)-to-\(W\) matrices; and matrices supported on the \(e_+,e_-\) block with scalar \(W\)-diagonal trace correction. In addition the \(e_+e_-\) mixed matrix is a one-dimensional odd sector. Substitution in the preceding quadratic form gives respective normalized eigenvalues \(1\), \((1-c)/2\), \((1+c)/2\), and \(3(1-c^2)/4\). The first sector has dimension \(m(m+1)/2-1\) and exists only if \(m\ge2\). The two mixed sectors each have dimension \(m\).

For the remaining even sector, write \(A=\operatorname{diag}(a,b,-(a+b)I_W/m)\). Its Frobenius norm and normalized Gram numerator are respectively the quadratic forms represented by
\[
G=\begin{pmatrix}1+1/m&1/m\\1/m&1+1/m\end{pmatrix},\qquad
H=G-2\begin{pmatrix}p&0\\0&q\end{pmatrix}
+\frac32\begin{pmatrix}p^2&pq\\pq&q^2\end{pmatrix}.
\]
Direct determinant expansion gives
\[
\operatorname{tr}(G^{-1}H)=T_d(c),\qquad
\det(G^{-1}H)=D_d(c),
\]
so the remaining eigenvalues are \(h_+,h_-\). This proves the entire spectrum and multiplicities (summing to \(d(d+1)/2-1\)).

**Ordering and rank.** The identities \(T_d>0\), \(D_d>0\), and \(T_d^2-4D_d\ge0\) follow from the positive generalized two-dimensional matrix above; its eigenvalues are strictly positive for \(c>0\). Also \(h_-\) is below \((d+1)/(2d)\), because the characteristic polynomial at that point equals \((c^2-1)(d+1)/(8d)<0\). Differentiation of its quadratic equation yields
\[
h_-'(c)=\frac{c\big((d+1)/d-3h_-/2\big)}{h_+-h_-}>0.
\]
The odd eigenvalue satisfies \(3(1-c^2)/4>(1-c)/2\). The plus mixed eigenvalue and the \(W\) eigenvalue are also larger. This proves the formula for \(\lambda_{\min}\). At \(c=0\), \(h_-=0\); at \(c=1\), \((1-c)/2=0\). The kernel vectors can also be seen directly as trace-free products of the two orthogonal normals and as products of the one repeated normal with any perpendicular coordinate, respectively. No other pair of distinct hyperplanes can have a vanishing harmonic quadratic: a quadratic vanishing on both hyperplanes must be proportional to their defining linear forms' product, whose Laplacian is twice their inner product.

**Sharp angle.** Substitute \(r=(1-c)/2\) into the even-sector characteristic polynomial:
\[
 r^2-T_d(c)r+D_d(c)=\frac{(c+1)(3dc^2+4c-d-2)}{8d}.
\]
The single positive zero is \(c_d^*\) above. At \(c=0\), \(h_-<r\); at \(c=1\), \(r<h_-\). The strict increase of \(h_-\) and the strict decrease of \(r\) make their lower envelope uniquely maximal at this crossing.

For \(d\ge4\), the \(W\)-block makes \(K_d\) the top eigenvalue. All other normalized eigenvalues are at most one: in particular the even characteristic polynomial at one is \((1-c^2)(d-2)/(4d)>0\), with root sum less than two. Hence condition-number minimization is identical to maximization of the smallest eigenvalue. For \(d=3\), \(h_+\) is the top normalized eigenvalue: it exceeds \(3/4+1/(2d)=11/12\), the plus mixed value and the odd value. On \(0<c\le c_d^*\), \(h_+/h_-\) strictly decreases because \(D_d/T_d^2\) strictly increases: \(D_d/T_d^2\) is proportional to \(c^2/(3/4+1/(2d)+3c^2/4)^2\), whose maximizing squared \(c\) would exceed one. On \(c\ge c_d^*\), \(h_+\) strictly increases (differentiate the quadratic equation and use \(h_+>11/12>8/9\)), so \(2h_+/(1-c)\) strictly increases. At \(d=3\) and \(c=5/9\), direct substitution gives \(h_+=25/27\) and \(h_-=2/9\), giving the stated sharp condition number. The high-dimensional limit follows by evaluating \(c_d^*\) as \(d\to\infty\).

## Verification
The standalone script `check_two_equators.py` constructs a Frobenius-orthonormal trace-free matrix basis, independently evaluates the equatorial fourth moments with projection matrices, diagonalizes the resulting full Gram matrix in dimensions \(3\) through \(11\), and compares to every proposed eigenvalue including boundary tests. It also tests the optimal angle over a 97-dimensional range. It passed 593 assertions with NumPy. These finite checks supplement the exact identity-based proof; they do not certify all dimensions.

## Relationship to prior work
Quellmalz, Weissinger, Hubmer and Erchinger (arXiv:2303.05179, first submitted March 9, 2023) study a frame decomposition for the **scalar Funk–Radon transform**, which integrates a function over each of a continuum of great circles. The present operator instead observes **the entire restricted function on just two equators**; scalar averaging is a different operator and the cited frame decomposition does not provide the displayed two-normal matrix spectrum or optimal angle. Michel, Plattner and Seibert (arXiv:2103.14650, first submitted March 26, 2021) develop spherical Slepian concentration over **positive-area caps**, including spin-weighted tensor harmonics. A pair of measure-zero equatorial traces, with their own normalized measures, is not a cap-compression instance. General spherical polynomial interpolation results likewise do not settle these sharp frame eigenvalues. A closely related analysis for **mutually orthogonal** equators shows that two orthogonal traces have a kernel; it does not imply either generic two-trace injectivity or the angle-optimal spectral constants here. Searches did not establish historical uniqueness of the formulas; an implicit older restriction-theoretic derivation remains possible.

## Limitations
Exact statements are confined to pure homogeneous harmonic quadratics, **equal** equator weights, function-valued continuous traces, and integer \(d\ge3\). Higher harmonic degree, general unoriented weighted circles, and point-sampling designs require new arguments. The proof gives finite-dimensional spectral stability, not robustness of any specific discretization. No independently conducted mathematical validation is claimed; originality remains provisional pending additional specialist review.

## References
- M. Quellmalz, L. Weissinger, S. Hubmer, and P. D. Erchinger, *A Frame Decomposition of the Funk-Radon Transform*, arXiv:2303.05179 (first public version 2023-03-09), https://arxiv.org/abs/2303.05179.
- V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first public version 2021-03-26), https://arxiv.org/abs/2103.14650.
- K. Ivanov and P. Petrushev, *Irregular sampling of band-limited functions on the sphere*, Applied and Computational Harmonic Analysis (2015), DOI:10.1016/j.acha.2014.05.001 (comparison with sampling from scattered points).
