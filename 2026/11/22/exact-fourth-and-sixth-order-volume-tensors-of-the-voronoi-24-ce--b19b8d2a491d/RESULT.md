# Exact fourth- and sixth-order volume tensors of the Voronoi 24-cell

## Finding
Let \(D_4=\{z\in\mathbb Z^4:\sum_i z_i\text{ is even}\}\), let \(V\) be its unscaled Euclidean Voronoi cell, and let \(X\) be uniform on \(V\) with respect to normalized four-dimensional volume. Write \(S=\|X\|_2^2\). The exact radial moments through degree six are
\[
\operatorname{vol}_4(V)=2,\qquad
\mathbb E S=\frac{13}{30},\quad
\mathbb E S^2=\frac3{14},\quad
\mathbb E S^3=\frac{289}{2520},\quad
\operatorname{Var}(S)=\frac{167}{6300}.
\]

The **complete directional fourth-moment tensor is rotationally isotropic**: for every \(u\in\mathbb R^4\),
\[
\boxed{\mathbb E\langle X,u\rangle^4=\frac3{112}\|u\|_2^4.}
\]
The covariance is \(\mathbb E(XX^{\mathsf T})=(13/120)I_4\). Thus the standardized fourth directional moment is the same in *every* nonzero direction, namely \(2700/1183\).

The sixth tensor is also explicit, but no longer isotropic. For every \(u=(u_1,u_2,u_3,u_4)\in\mathbb R^4\), put
\[
A_6=\frac{251}{26880},\qquad B_6=\frac{403}{241920},\qquad C_6=\frac5{6912}.
\]
Then
\[
\boxed{
\begin{aligned}
\mathbb E\langle X,u\rangle^6={}&A_6\sum_i u_i^6
 +15B_6\sum_{i\ne j}u_i^4u_j^2\\
 &+90C_6\sum_{i<j<k}u_i^2u_j^2u_k^2.
\end{aligned}}
\]
In particular, with \(e_1,e_2\) the first two coordinate unit vectors,
\[
\boxed{\mathbb E\langle X,e_1\rangle^6
-\mathbb E\left\langle X,\frac{e_1+e_2}{\sqrt2}\right\rangle^6
=\frac{61}{80640}>0.}
\]
Thus fourth-order rotational isotropy is exact while sixth-order rotational isotropy fails. These assertions hold for the entire solid Voronoi cell, not just its vertices or boundary.

## Assumptions and scope
The lattice uses the conventional Euclidean normalization: its minimal nonzero vector length is \(\sqrt2\), its covolume is \(2\), and its Voronoi covering radius is \(1\). No rescaling or unit-covolume convention is implicit. The probability law is volume-uniform; boundaries have zero measure. Tensor coordinates are the standard orthonormal coordinates of \(\mathbb R^4\). Moments are with respect to the origin, which is the symmetry center. The sixth-order identity is a complete homogeneous polynomial identity for *every* real direction \(u\), not merely an evaluation at two directions.

## Proof
**1. Voronoi inequalities and a chamber simplex.** The \(24\) shortest vectors of \(D_4\) are \(\pm e_i\pm e_j\) for \(1\le i<j\le4\). Their perpendicular-bisector inequalities define
\[
P=\{x\in\mathbb R^4:|x_i|+|x_j|\le1\text{ for all }i<j\}.
\]
In the nonnegative sorted chamber \(x_1\ge x_2\ge x_3\ge x_4\ge0\), the entire system reduces to \(x_1+x_2\le1\). That chamber is the four-simplex with vertices
\[
0,\quad e_1,\quad\frac{e_1+e_2}{2},\quad
\frac{e_1+e_2+e_3}{2},\quad\frac{e_1+e_2+e_3+e_4}{2}.
\]
All these chamber vertices lie in the convex hull of the \(24\) unit vectors
\[
\mathcal U=\{\pm e_i:1\le i\le4\}
\cup\{(\pm\tfrac12,\pm\tfrac12,\pm\tfrac12,\pm\tfrac12)\},
\]
where the latter set includes all \(16\) independent sign patterns. Conversely, all vectors in \(\mathcal U\) satisfy every pair inequality, so \(P=\operatorname{conv}\mathcal U\). In particular \(\|x\|_2\le1\) for \(x\in P\). Every lattice vector not among the \(24\) shortest has length at least \(2\). For such a vector \(z\), Cauchy–Schwarz yields \(\langle x,z\rangle\le\|z\|_2\le\|z\|_2^2/2\), so its Voronoi bisector contributes no additional inequality. Therefore \(V=P\), and the signed coordinate-permutation group partitions \(V\), apart from null sets, into exactly \(16\cdot24=384\) copies of the displayed simplex.

**2. Exact integral over the chamber.** Let \(\Delta_4=\{t_i\ge0:\sum_{i=1}^4t_i\le1\}\). Its affine map onto the chamber is
\[
\begin{aligned}
x_1&=t_1+(t_2+t_3+t_4)/2, &x_2&=(t_2+t_3+t_4)/2,\\
x_3&=(t_3+t_4)/2, &x_4&=t_4/2.
\end{aligned}
\]
The absolute Jacobian is \(1/8\), and the chamber volume is \((1/8)/4!=1/192\); hence \(\operatorname{vol}_4(V)=384/192=2\). For any polynomial \(F\) even in each coordinate and symmetric under coordinate permutations, the normalized expectation becomes
\[
\mathbb E F(X)=24\int_{\Delta_4}F(x(t))\,dt.
\]
Every monomial is evaluated *exactly*, using the Dirichlet simplex integral
\[
\int_{\Delta_4}t_1^{a_1}t_2^{a_2}t_3^{a_3}t_4^{a_4}\,dt
=\frac{a_1!a_2!a_3!a_4!}{(a_1+a_2+a_3+a_4+4)!}
\quad(a_i\in\mathbb Z_{\ge0}).
\]
Expanding the stated affine map and applying this rule gives the following independently checkable table. Every entry is an expectation (not an unnormalized integral):

| Symmetric even polynomial \(F\) | \(\mathbb E F(X)\) |
| --- | ---: |
| \(\sum_i X_i^2\) | \(13/30\) |
| \((\sum_i X_i^2)^2\) | \(3/14\) |
| \((\sum_i X_i^2)^3\) | \(289/2520\) |
| \(\sum_i X_i^4\) | \(3/28\) |
| \(\sum_{i<j}X_i^2X_j^2\) | \(3/56\) |
| \(\sum_i X_i^6\) | \(251/6720\) |
| \(\sum_{i\ne j}X_i^4X_j^2\) | \(403/20160\) |
| \(\sum_{i<j<k}X_i^2X_j^2X_k^2\) | \(5/1728\) |

Since coordinate permutations act transitively on single indices, ordered distinct pairs, and unordered triples, divide the respective last five entries by their orbit sizes \(4,6,4,12,4\). This yields
\[
\mathbb E X_1^4=\frac3{112},\quad
\mathbb E X_1^2X_2^2=\frac1{112},\quad
\mathbb E X_1^6=\frac{251}{26880},\quad
\mathbb E X_1^4X_2^2=\frac{403}{241920},\quad
\mathbb E X_1^2X_2^2X_3^2=\frac5{6912}.
\]
The radial moment and variance formulas follow by expanding powers of \(\sum_i X_i^2\). In particular \(3/14-(13/30)^2=167/6300\).

**3. A geometric fourth-order isotropy identity.** Signed coordinate permutations preserve \(V\), so all odd-coordinate moments vanish, all diagonal fourth moments equal \(A=\mathbb E X_1^4\), and all distinct-pair even fourth moments equal \(B=\mathbb E X_1^2X_2^2\). The orthogonal Hadamard transformation
\[
H=\frac12\begin{pmatrix}
1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix}
\]
permutes the \(24\) vertices \(\mathcal U\), hence preserves their convex hull \(V\) and its volume measure. It sends \(e_1\) to \((1/2,1/2,1/2,1/2)\). Applying invariance to the fourth power of this projection gives \(A=(4A+36B)/16\), equivalently \(A=3B\). Therefore
\[
\mathbb E\langle X,u\rangle^4=A\sum_i u_i^4+6B\sum_{i<j}u_i^2u_j^2
=A\left(\sum_i u_i^2\right)^2.
\]
The exact value \(A=3/112\) from the table completes the fourth-tensor statement. Similarly the covariance is scalar by symmetry and its trace is \(13/30\), so it equals \((13/120)I_4\), giving the stated standardized directional fourth moment.

**4. Sixth-order tensor and failure of isotropy.** By signed symmetry, only even exponent patterns contribute to \(\mathbb E\langle X,u\rangle^6\). The partitions \(6\), \(4+2\), and \(2+2+2\) have multinomial coefficients \(1,15,90\), respectively. The corresponding orbit moments are precisely \(A_6,B_6,C_6\) from step 2, proving the complete sixth-order formula. The axial and two-coordinate-diagonal evaluations are
\[
\mathbb E X_1^6=\frac{251}{26880},\qquad
\mathbb E\left(\frac{X_1+X_2}{\sqrt2}\right)^6
=\frac{A_6+15B_6}{4}=\frac{173}{20160}.
\]
Their difference is \(61/80640>0\), although both directions are unit vectors. This rules out rotational isotropy at degree six and finishes the proof.

## Verification
The attached `verify.py` uses only Python 3's standard library. It implements rational sparse-polynomial arithmetic and checks all eight symmetric-moment table entries in **two independently parametrized integration coordinates**: an affine Dirichlet four-simplex and a product unit cube whose Jacobian is \(a^2c(1-a)/8\). It checks the exact fourth/sixth tensor coefficients, variance and anisotropy gap, the 24 explicitly enumerated unit vertices, and that the Hadamard matrix maps their set to itself. The two rational integrations agree entry by entry and all asserted constants pass. This is a finite exact-algebra verifier of the displayed integral evaluations; the proof that the integration domain is the Voronoi cell and that the identities hold in every direction is given analytically above.

## Relationship to prior work
Conway and Sloane computed the regular 24-cell's Euclidean Voronoi geometry and exact **second moment**, including the familiar value \(13/30\) in this normalization, but their evaluated results do not provide the solid fourth/sixth tensors or the degree-six directional obstruction. Liu established the global four-dimensional lattice quantizer optimum for **quadratic** distortion at \(D_4\), not the higher error moments. Ordentlich studies lattice radial distributions and general moment bounds; the cited early numerical evaluations of the \(D_4\) radial function and the general random-lattice bounds do not evaluate the present exact volume moments or directional sixth tensor.

The published *Exact deep-hole radial tail of the \(D_4\) Voronoi 24-cell* supplies an exact high-radius tail only for squared radius exceeding \(3/4\), not the global volume moments or any directional tensor. The published FCC/BCC directional-kurtosis comparison concerns **three-dimensional** Voronoi cells, and the published cube–octahedron fourth-isotropy transition concerns **three-dimensional** interpolating solids. Standard symmetry theory already explains that the regular 24-cell can have an isotropic fourth-order volume tensor; the newly evaluated content here is its exact uniform-solid fourth and sixth coefficients, global squared-distortion variance, and explicit sixth-order anisotropy gap. General polynomial-on-simplex integration is an established method and is not claimed as new.

## Limitations
Only the unscaled \(D_4\) cell's uniform **solid-volume** moments through total degree six are determined. No claim is made of fourth-moment optimality among lattices, stochastic dominance, a complete radial CDF, classification of sixth-moment extremal directions, or corresponding formulas for arbitrary deformed 24-cells. The moment identities are exact, but priority against unindexed classical moment tables remains provisional. A historical reference mentions numerical plots of the \(D_4\) radial distribution; its complete underlying computational data were not inspected. No independent audit has been performed.

## References
1. T. Liu, *The optimal four-dimensional lattice quantizer and bounds from Voronoi facets*, arXiv:2611.00100v1, first public 2026-10-26; https://arxiv.org/html/2611.00100v1.
2. J. H. Conway and N. J. A. Sloane, *Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization*, IEEE Transactions on Information Theory 28 (1982), 211–226, DOI: 10.1109/TIT.1982.1056483; lawful author copy https://neilsloane.com/doc/Me82.pdf.
3. O. Ordentlich, *The Voronoi Spherical CDF for Lattices and Linear Codes: New Bounds for Quantization and Coding*, arXiv:2506.19791, first public 2025-06-24; https://arxiv.org/html/2506.19791.
4. *Exact deep-hole radial tail of the \(D_4\) Voronoi 24-cell*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-deep-hole-radial-tail-of-the-d-4-voronoi-24-cell--0c95835f8670.
5. *An exact directional-kurtosis crossover between FCC and BCC quantization cells*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-exact-directional-kurtosis-crossover-between-fcc-and-bcc-quan--a679f2d22ab5.
6. *A unique fourth-order isotropic body in the cube–octahedron intersection family*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-unique-fourth-order-isotropic-body-in-the-cube-octahedron-inte--b7144dfb179e.
