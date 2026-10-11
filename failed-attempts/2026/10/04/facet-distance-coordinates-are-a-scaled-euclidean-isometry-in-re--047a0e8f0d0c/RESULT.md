# Facet-distance coordinates are a scaled Euclidean isometry in regular simplices

## Finding

Let \(\Delta_n\subset\mathbb R^n\) be a regular \(n\)-simplex, \(n\ge2\), with center \(O\), inradius \(r\), and facets \(F_0,\ldots,F_n\). For \(P\in\Delta_n\), write \(d_i(P)\) for the perpendicular distance from \(P\) to \(F_i\). Then every pair \(P,Q\in\Delta_n\) satisfies the exact metric identity
\[
\|P-Q\|^2=\frac{n}{n+1}\sum_{i=0}^{n}\bigl(d_i(P)-d_i(Q)\bigr)^2.
\]
The classical Viviani relation is
\[
\sum_{i=0}^{n}d_i(P)=(n+1)r.
\]
Together, these statements show that the full facet-distance vector is not merely constrained by a constant sum: it is an affine Euclidean coordinate system. Precisely, the map
\[
D(P)=\bigl(d_0(P),\ldots,d_n(P)\bigr)
\]
is an affine similarity from \(\Delta_n\) onto
\[
\Sigma_r=\left\{(x_0,\ldots,x_n)\in\mathbb R_{\ge0}^{n+1}:\sum_{i=0}^{n}x_i=(n+1)r\right\},
\]
and distances in \(\Sigma_r\), measured in its ambient Euclidean metric, are \(\sqrt{(n+1)/n}\) times the corresponding distances in \(\Delta_n\).

Taking \(Q=O\), so that \(d_i(O)=r\), gives the exact quadratic Viviani refinement
\[
\sum_{i=0}^{n}\bigl(d_i(P)-r\bigr)^2=\frac{n+1}{n}\|P-O\|^2,
\]
and hence
\[
\sum_{i=0}^{n}d_i(P)^2=(n+1)r^2+\frac{n+1}{n}\|P-O\|^2.
\]
Equivalently,
\[
\frac1{n+1}\sum_{i=0}^{n}d_i(P)^2=r^2+\frac{\|P-O\|^2}{n}.
\]
Thus the variance of the facet distances reconstructs the squared radial displacement from the center exactly, while differences of facet-distance vectors reconstruct every pairwise Euclidean distance exactly.

## Assumptions and scope

The simplex is Euclidean, regular, nondegenerate, and of dimension \(n\ge2\). Distances are ordinary perpendicular distances to the affine facet hyperplanes; because \(P,Q\) lie in the simplex, these are nonnegative. The theorem is scale invariant. It concerns regular simplices only; no analogous isometry is asserted for a general simplex or a general Viviani polytope.

## Proof

Translate the center to the origin. Let the vertices be \(v_0,\ldots,v_n\), let their common circumradius be \(R\), and put \(u_i=v_i/R\). Regularity gives
\[
\langle u_i,u_i\rangle=1,\qquad
\langle u_i,u_j\rangle=-\frac1n\quad(i\ne j),
\qquad
\sum_{i=0}^{n}u_i=0.
\]
The facet \(F_i\) opposite \(v_i\) is the hyperplane
\[
\langle u_i,x\rangle=-\frac{R}{n}.
\]
Therefore the inradius is \(r=R/n\), and for a point \(P\) with position vector \(p\),
\[
d_i(P)=r+\langle u_i,p\rangle.
\]
Summing over \(i\) and using \(\sum_i u_i=0\) immediately gives
\[
\sum_i d_i(P)=(n+1)r.
\]

The vertex directions form a tight frame. Indeed, for any fixed \(j\),
\[
\sum_{i=0}^{n}u_i\langle u_i,u_j\rangle
=u_j-\frac1n\sum_{i\ne j}u_i
=\left(1+\frac1n\right)u_j.
\]
Since the \(u_j\) span \(\mathbb R^n\), this proves the operator identity
\[
\sum_{i=0}^{n}u_i u_i^{\mathsf T}=\frac{n+1}{n}I_n.
\]
For \(x=p-q\),
\[
d_i(P)-d_i(Q)=\langle u_i,x\rangle.
\]
Hence
\[
\sum_{i=0}^{n}\bigl(d_i(P)-d_i(Q)\bigr)^2
=\sum_i\langle u_i,x\rangle^2
=\frac{n+1}{n}\|x\|^2,
\]
which is the asserted metric identity.

It remains to identify the image. If \(P=\sum_i\lambda_i v_i\) has barycentric coordinates \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\), then the preceding facet formula gives
\[
d_i(P)=(n+1)r\,\lambda_i.
\]
Thus \(D\) maps \(\Delta_n\) bijectively onto \(\Sigma_r\). The metric identity shows that this affine bijection is a similarity. Finally, setting \(Q=O\) gives the centered square identity; expanding it and using the constant-sum relation gives the formula for \(\sum_i d_i(P)^2\).

An explicit inverse reconstruction is also immediate from the tight-frame identity:
\[
p=\frac{n}{n+1}\sum_{i=0}^{n}\bigl(d_i(P)-r\bigr)u_i.
\]

## Verification

The proof is symbolic and covers every dimension \(n\ge2\). The bundled deterministic script `verify_simplex_facet_isometry.py` independently constructs regular simplices in their standard \((n+1)\)-coordinate realization, samples positive barycentric coordinates, computes facet distances from those coordinates, and checks the constant-sum, pairwise metric, centered variance, and inverse-reconstruction identities for dimensions \(2\) through \(12\). These finite checks are supplementary and are not used as a proof of the universal statement.

## Relationship to prior work

Viviani-type results establish constancy of the sum of distances to the sides or faces. Zhou characterizes oriented hyperplane systems for which the signed-distance sum is constant and includes regular polyhedra among the examples. De Villiers gives the three-dimensional equal-face-area tetrahedron version and related polyhedral extensions. Those inspected sources concern the first moment \(\sum_i d_i\); they do not state the pairwise squared-distance identity above, the affine-similarity interpretation of the entire facet-distance vector, or the exact centered second-moment formula.

A later article by Alhajjar and Nasta connects Viviani-type phenomena with Minkowski's theorem and higher-dimensional polytope constructions. Its inspected abstract concerns side/face displacement and higher-dimensional generalization, not metric reconstruction from facet-distance coordinates. An equivalent identity may nevertheless exist in older barycentric-coordinate or tight-frame literature under different terminology; that is the principal residual originality risk.

## Limitations

The identity depends on the regular-simplex tight-frame relation. For a nonregular simplex, facet-distance coordinates remain affine coordinates after appropriate normalization, but the ambient Euclidean metric on the coordinate hyperplane is generally anisotropic rather than a scalar multiple of the original metric. The literature search was broad but not historically exhaustive, especially for classical barycentric-coordinate formulations. No claim of independent audit or independent validation is made.

## References

1. L. Zhou, *Viviani Polytopes and Fermat Points*, arXiv:1008.1236 (first posted 6 August 2010); later published in *College Mathematics Journal* 43 (2012), 309–312.
2. M. De Villiers, *3D Generalisations of Viviani's theorem*, *The Mathematical Gazette* 97 (2013), 441–445, DOI 10.1017/S0025557200000188.
3. E. Alhajjar and M. Nasta, *Viviani’s Theorem, Minkowski’s Theorem and Equiangular Polygons*, *Mathematics Exchange* 16(1), DOI 10.33043/8V7yDC7Ay9.
