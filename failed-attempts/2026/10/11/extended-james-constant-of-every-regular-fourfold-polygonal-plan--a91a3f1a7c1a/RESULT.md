# Extended James constant of every regular fourfold polygonal plane
## Finding
For every integer \(n\ge1\), let \(X_{4n}\) be the real Banach plane whose unit ball is the Euclidean regular \(4n\)-gon circumscribed about the Euclidean unit disk. Put
\[
\alpha=\frac{\pi}{4n}.
\]
For the extended James constant introduced by Chen, Yang, Liu and Li,
\[
J_4(X)
=
\sup_{\|x\|^2+\|y\|^2=2}
\min\{\|x+y\|,\|x-y\|\},
\]
one has
\[
\boxed{
J_4(X_{4n})
=
\sqrt2\,\sec\alpha
=
\sqrt2\,\sec\!\left(\frac{\pi}{4n}\right)
}.
\tag{1}
\]

A sharp admissible pair can always be chosen from two unit-ball vertices whose Euclidean directions differ by \(\pi/2\). Their norm ratio is
\[
\frac{\|y\|}{\|x\|}=\tan\alpha.
\tag{2}
\]
Thus the square has value \(2\), the regular octagon has value
\[
2\sqrt{2-\sqrt2},
\]
and the family decreases strictly to the Hilbert value \(\sqrt2\). More precisely,
\[
J_4(X_{4n})
=
\sqrt2
+
\frac{\sqrt2\,\pi^2}{32n^2}
+
O(n^{-4}).
\tag{3}
\]

## Assumptions and scope
All scalars are real. Write
\[
e_\theta=(\cos\theta,\sin\theta).
\]
The norm may be represented as
\[
N_n(z)
=
\max_{0\le k<2n}
\left|\left\langle z,e_{2k\alpha}\right\rangle\right|.
\tag{4}
\]
Hence the unit ball is the intersection of the strips supported by the lines with outward unit normals
\[
e_{2k\alpha}.
\]
It is the regular \(4n\)-gon of inradius \(1\), and its vertices are
\[
\sec\alpha\,e_{(2k+1)\alpha},
\qquad
0\le k<4n.
\tag{5}
\]

Because the Euclidean unit disk is contained in this polygon and the polygon is contained in the Euclidean disk of radius \(\sec\alpha\), one has for every \(z\in\mathbb R^2\)
\[
N_n(z)\le |z|_2\le \sec\alpha\,N_n(z).
\tag{6}
\]

## Proof
Take any admissible pair
\[
x,y\in X_{4n},
\qquad
N_n(x)^2+N_n(y)^2=2.
\]
By the first inequality in (6),
\[
\min\{N_n(x+y),N_n(x-y)\}
\le
\min\{|x+y|_2,|x-y|_2\}.
\tag{7}
\]
The Euclidean parallelogram identity gives
\[
|x+y|_2^2+|x-y|_2^2
=2|x|_2^2+2|y|_2^2.
\]
Therefore
\[
\min\{|x+y|_2,|x-y|_2\}
\le
\sqrt{|x|_2^2+|y|_2^2}.
\tag{8}
\]
Using the second inequality in (6),
\[
\sqrt{|x|_2^2+|y|_2^2}
\le
\sec\alpha
\sqrt{N_n(x)^2+N_n(y)^2}
=
\sqrt2\,\sec\alpha.
\tag{9}
\]
Equations (7)--(9) prove
\[
J_4(X_{4n})\le\sqrt2\,\sec\alpha.
\tag{10}
\]

For equality, choose the two unit-ball vertices
\[
u=\sec\alpha\,e_\alpha,
\qquad
v=\sec\alpha\,e_{\alpha+\pi/2}.
\tag{11}
\]
They are Euclidean-orthogonal, and
\[
N_n(u)=N_n(v)=1.
\]
Set
\[
t=\tan\alpha,
\qquad
c=\sqrt{\frac{2}{1+t^2}}=\sqrt2\cos\alpha,
\]
and define
\[
x=cu,
\qquad
y=ctv.
\tag{12}
\]
Then
\[
N_n(x)^2+N_n(y)^2
=c^2(1+t^2)=2.
\tag{13}
\]
Using the complex-plane shorthand for Euclidean directions,
\[
u+tv
=
\sec^2\alpha\,e_{2\alpha},
\qquad
u-tv
=
\sec^2\alpha\,e_0.
\tag{14}
\]
Both \(e_0\) and \(e_{2\alpha}\) are facet-normal directions. Along any facet-normal ray the polygonal norm equals Euclidean length, so
\[
N_n(u+tv)=N_n(u-tv)=\sec^2\alpha.
\tag{15}
\]
Multiplying by \(c\) gives
\[
N_n(x+y)=N_n(x-y)
=c\sec^2\alpha
=
\sqrt2\,\sec\alpha.
\tag{16}
\]
Thus (10) is sharp and proves (1).

Since \(\sec\alpha\) decreases strictly as \(n\) increases, the monotonicity follows. Finally,
\[
\sec z=1+\frac{z^2}{2}+O(z^4)
\]
at \(z=0\), and substituting \(z=\pi/(4n)\) gives (3).

## Verification
The bundled `verify.py` reconstructs the norm from the facet normals in (4), checks the Euclidean sandwich, the vertex identities, the sharp pair, and the claimed value for the first forty regular \(4n\)-gons. It also checks a deterministic family of admissible pairs against the analytic upper bound.

These numerical checks are reproducibility aids. They are not a proof over all \(n\) or all admissible vectors. The infinite theorem is established by the Euclidean sandwich, parallelogram identity, and exact sharp construction above.

## Relationship to prior work
Chen, Yang, Liu and Li introduced \(J_4\) in 2022 by extending the James optimization from two unit vectors to pairs satisfying
\[
\|x\|^2+\|y\|^2=2.
\]
Their Section 4 gives an equivalent one-parameter representation, the comparison
\[
J(X)\le J_4(X)\le A(X),
\]
a bound through the modulus of smoothness, and exact values for \(L_p\) spaces and the Day--James \(\ell_\infty-\ell_1\) plane. The inspected full text gives no regular-polygon family formula.

A previously established regular-octagon calculation gives
\[
J_4(X_8)=2\sqrt{2-\sqrt2},
\]
which is the case \(n=2\) of (1). That isolated calculation uses the exact octagonal modulus of smoothness. The present proof replaces that space-specific analysis by a uniform Euclidean comparison and an all-\(n\) sharp construction.

The closest indexed regular-polygon results located by semantic search concern different invariants, including equilateral perimeter, Ptolemy constants, generalized von Neumann--Jordan profiles, and the ordinary James constant on one congruence class of regular polygons. None of those statements implies the extended-domain formula (1).

The Takahashi--Kato constant \(A(X)\) is a natural comparison because the defining source proves \(J_4(X)\le A(X)\). Its 2014 paper predates \(J_4\), so it cannot state the present theorem. Publicly accessible metadata and abstract were inspected; a full-text regular-polygon calculation of \(A(X)\), if one exists there, could supply a parallel upper estimate but would not supply the sharp \(J_4\) witness (12)--(16).

## Limitations
The theorem concerns Euclidean regular polygons with a number of sides divisible by four, up to linear isometry. It does not determine \(J_4\) for regular \((4n+2)\)-gons, arbitrary centrally symmetric polygons, or nonsymmetric convex bodies.

The proof exhibits a family of maximizers but does not classify all maximizing pairs.

The primary 2022 article does not print a regular-polygon table, and targeted semantic searches found no covering formula. Such searches cannot exclude unindexed or differently normalized work. A residual literature risk is an equivalent formula stated through the Takahashi--Kato constant or under a different affine normalization of regular polygons.

## References
1. B. Chen, Z. Yang, Q. Liu and Y. Li, “Some New James Type Geometric Constants in Banach Spaces,” *Symmetry* 14 (2022), 405, doi:10.3390/sym14020405. Published 18 February 2022.
2. Y. Takahashi and M. Kato, “On a New Geometric Constant Related to the Modulus of Smoothness of a Banach Space,” *Acta Mathematica Sinica, English Series* 30 (2014), 1526--1538, doi:10.1007/s10114-014-2782-7.
