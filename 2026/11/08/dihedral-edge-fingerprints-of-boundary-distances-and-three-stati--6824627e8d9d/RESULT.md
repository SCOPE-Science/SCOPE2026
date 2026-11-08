# Dihedral-edge fingerprints of boundary distances and three-statistic reconstruction of boxes

## Finding

Let \(P\subset\mathbb R^3\) be a three-dimensional compact convex polyhedron with nonempty interior, with polygonal faces, surface area \(S>0\), edges \(e\), edge lengths \(\ell_e\), and interior dihedral angles \(0<\theta_e<\pi\). Let \(X,Y\) be independent points sampled uniformly from the surface-area measure on \(\partial P\), and put \(F_P(r)=\Pr(\|X-Y\|\le r)\). Then

\[
F_P(r)=\frac{\pi r^2}{S}+\frac{4r^3}{3S^2}\sum_e\ell_e\left(\frac{\pi-\theta_e}{\sin\theta_e}-1\right)+O_P(r^4)\qquad(r\downarrow0).
\]

Thus the Euclidean boundary-pair distance law determines both surface area and a nonnegative, dihedral-angle-weighted total edge length. The correction is strictly positive for every nondegenerate convex polyhedron.

For a rectangular box with side lengths \(a,b,c>0\), write \(s_1=a+b+c\), \(s_2=ab+bc+ca\), \(s_3=abc\), and \(S=2s_2\). In the exact interval \(0\le r<\min(a,b,c)\),

\[
F_P(r)=\frac{\pi r^2}{S}+\frac{8(\pi-2)s_1r^3}{3S^2}+\frac{3(1-\pi)r^4}{S^2}.
\]

If \(M_2=\mathbb E\|X-Y\|^2\), then

\[
M_2=\frac{s_1^2s_2-2s_2^2+2s_1s_3}{6s_2}.
\]

Consequently the three statistics \(c_2=\lim_{r\downarrow0}F_P(r)/r^2\), \(c_3=\lim_{r\downarrow0}(F_P(r)-c_2r^2)/r^3\), and \(M_2\) determine the unordered triple \(\{a,b,c\}\) uniquely. In fact, with \(S=\pi/c_2\),

\[
s_2=S/2,\qquad s_1=\frac{3S^2c_3}{8(\pi-2)},\qquad s_3=\frac{6s_2M_2-s_1^2s_2+2s_2^2}{2s_1},
\]

and the sides are exactly the three positive real roots, counting multiplicity, of \(t^3-s_1t^2+s_2t-s_3=0\).

## Assumptions and scope

Distance is ambient *Euclidean chord distance*, not geodesic distance along the surface. Surface sampling is area-uniform and independent. Edges refer to true maximal edges between noncoplanar adjacent faces: artificial subdivision lines between coplanar faces are excluded. The polyhedron is fixed while \(r\to0\); constants in \(O_P(r^4)\) need not be uniform under degeneration of the shape. No smoothness beyond polygonality or generic-position condition is assumed. The exact polynomial for a box is asserted only for radii strictly below its smallest side length; the endpoint follows by continuity.

## Proof

**1. Same-face contribution.** For a convex polygonal face \(G\), with planar area \(A_G\) and planar perimeter \(L_G\), the ordered pair measure

\[
I_{GG}(r)=\int_G\int_G\mathbf1_{\{\|x-y\|\le r\}}\,dA(y)\,dA(x)
\]

satisfies \(I_{GG}(r)=\pi A_Gr^2-\frac23L_Gr^3+O_G(r^4)\). To verify the coefficient, compare a radius-\(r\) disk centered on a face point against a disk in the whole supporting plane. For a straight boundary segment, the loss per unit segment length is

\[
\int_0^r 2w\sqrt{r^2-w^2}\,dw=\frac23r^3.
\]

Only the \(O(r)\)-neighborhoods of polygon vertices can invalidate this half-plane calculation; each gives an \(O(r^4)\) ordered-pair contribution. Summing over faces, with \(\sum_G L_G=2\sum_e\ell_e\), gives

\[
\sum_G I_{GG}(r)=\pi Sr^2-\frac43r^3\sum_e\ell_e+O_P(r^4).
\]

**2. Adjacent faces.** Near the interior of an edge, put the common edge along a \(z\)-axis and let the two inward transverse rays meet at angle \(\theta\). A point on the first face has transverse distance \(u\ge0\), while one on the second has \(v\ge0\). Their squared Euclidean separation is

\[
u^2+v^2-2uv\cos\theta+(z-z')^2.
\]

For one ordered direction of a face pair, and to third order away from edge endpoints, the pair measure per unit edge length is

\[
J_\theta(r)=\int_{u,v\ge0}\int_{\mathbb R}\mathbf1_{\{u^2+v^2-2uv\cos\theta+w^2\le r^2\}}\,dw\,du\,dv.
\]

The linear map \((u,v)\mapsto u\mathbf e_1-v\mathbf e_2\), with the rays making angle \(\theta\), has absolute Jacobian \(\sin\theta\) and takes the first quadrant to a planar wedge of angle \(\pi-\theta\). The volume of the intersection of a radius-\(r\) ball with this wedge is \((\pi-\theta)/(2\pi)\) times the volume of the ball. Hence

\[
J_\theta(r)=\frac{2(\pi-\theta)}{3\sin\theta}r^3.
\]

There are two orders of adjacent faces per edge. The two endpoint regions contribute \(O_P(r^4)\), so all adjacent-face ordered pairs together contribute

\[
\frac43r^3\sum_e\ell_e\frac{\pi-\theta_e}{\sin\theta_e}+O_P(r^4).
\]

**3. Other face pairs and normalization.** Closures of nonincident faces have positive separation, so make zero contribution for all sufficiently small \(r\). Distinct faces meeting only at a vertex contribute at most \(O_P(r^4)\), since both points lie within \(O(r)\) of that vertex. Adding the same-face and adjacent-face terms and dividing by \(S^2\) proves the expansion. For \(0<\theta<\pi\), the identity \(\sin\theta<\pi-\theta\) follows by putting \(\phi=\pi-\theta\in(0,\pi)\), where \(\sin\phi<\phi\). Every edge summand is therefore positive.

**4. Exact polynomial for a box.** For \(0<r<\min(a,b,c)\), an opposing pair of faces contributes zero. A rectangular face of lengths \(w,h\) contributes exactly

\[
I_{GG}=\int_{u^2+v^2\le r^2}(w-|u|)(h-|v|)\,du\,dv
=\pi whr^2-\frac43(w+h)r^3+\frac12r^4.
\]

For each *single ordered* adjacent-face pair with common edge length \(\ell\), the exact integral is

\[
I_{GH}=\int_{u^2+v^2+z^2\le r^2,\,u,v\ge0}(\ell-|z|)\,du\,dv\,dz
=\frac{\pi\ell}{3}r^3-\frac\pi8r^4.
\]

Summing the six same-face terms, and the two ordered terms for each of twelve edges, gives the *unnormalized* pair measure

\[
\pi Sr^2+\frac83(\pi-2)s_1r^3+3(1-\pi)r^4.
\]

Divide by \(S^2\), obtaining the asserted exact law. Notice that the quartic coefficient is universal once the surface area is fixed, whereas the cubic term measures total box-edge length.

**5. Global second moment and reconstruction.** Center the box at the origin. Symmetry gives \(\mathbb EX=0\), so \(\mathbb E\|X-Y\|^2=2\mathbb E\|X\|^2\). The numerator of \(\mathbb E\|X\|^2\) for the \(x\)-coordinate is \(a^2bc/2+a^3(b+c)/6\); sum cyclically, divide by \(S=2s_2\), and apply the elementary symmetric identities \(\sum a^3(b+c)=s_1^2s_2-2s_2^2-s_1s_3\) and \(\sum a^2bc=s_1s_3\). This yields the stated moment. The formulas for \(s_1,s_2,s_3\) then follow algebraically. Since \(a,b,c\) are the roots of their monic cubic, their multiset is uniquely recovered, even when some sides coincide.

## Verification

Run `python check_boundary_pairs.py` with Python 3, NumPy and SciPy. The checker separately samples two independent area-uniform boundary points by choosing faces with probability proportional to face area; it compares the exact small-radius CDF and second moment on four boxes against 524,288 scrambled Sobol pairs per box. It numerically integrates the wedge-angle kernel at four angles and checks the exact inverse reconstruction for all four boxes. It is a reproducible corroboration, not a proof of a limit or of historical novelty. The analytic steps above prove the full assertion.

## Relationship to prior work

The 1999 work of Mathai, Moschopoulos and Pederzoli studies random distances in and between faces of a cube; cube face-to-face distance formulas are known and the cube special case of the present exact polynomial is not asserted to be historically new. The surface boundary sampling experiment is distinct from uniform-volume pair sampling and from isotropic-uniform-random line chords. Gille's 2005 wedge and rod paper develops those **line-chord** distributions rather than area-uniform pairs on the **surface**. Work on distributions for random points in planar polygons and on geometric chord distributions of polyhedra has related integral kernels but different measures. A published planar polygon pair-distance coefficient is likewise not a three-dimensional polyhedral-surface edge coefficient. The distinctive combined assertion here is a general dihedral-edge fingerprint plus a finite-statistic inverse theorem for all rectangular boxes. This is a best-knowledge comparison, not a certification of historical uniqueness.

## Limitations

This does not reconstruct arbitrary convex polyhedra; for general polyhedra only one weighted edge sum is recovered from the first correction. The box theorem assumes rectangularity in advance, not recovery of that model class from arbitrary unknown surfaces. No explicit uniform error bound is asserted for degenerating families or below poorly separated nonadjacent faces. Full text of the potentially relevant 1999 cube work was not retrievable in this review, and an earlier equivalent inverse formulation may exist. Independent expert or archival novelty review has not been performed.

## References

- W. Gille, *Analysis of the Chord Length Distribution Along an Edge: The Wedge Case and the Quadratic Rod Case*, Journal of Mathematics and Statistics 1 (2005), 106–112, DOI:10.3844/jmssp.2005.106.112, first published 2005-06-30, https://thescipub.com/jmss/jmssp.2005.106.112.pdf.
- A. M. Mathai, P. Moschopoulos, G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81, DOI:10.6092/issn.1973-2201/1104, https://rivista-statistica.unibo.it/article/view/1104.
- E. W. Weisstein, *Cube Line Picking—Face and Face*, MathWorld, https://mathworld.wolfram.com/CubeLinePickingFaceandFace.html (detailed account of known unit-cube adjacent/opposite face formulas).
- F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498 (2013-11-29), https://arxiv.org/abs/1312.2498.
- S. Ciccariello, *The chord-length distribution of a polyhedron*, arXiv:1911.02532 (2019-11-06), https://arxiv.org/abs/1911.02532 (isotropic line-chord rather than boundary-pair measure).
