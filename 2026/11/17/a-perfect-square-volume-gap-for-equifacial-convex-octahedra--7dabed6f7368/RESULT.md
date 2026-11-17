# A perfect-square volume gap for equifacial convex octahedra

## Finding
Fix a Euclidean triangle \(T\) with **distinct** side lengths \(0<a<b<c\) and all three angles acute. Let \(\mathcal O(T)\) denote the convex three-polytopes combinatorially equivalent to the octahedron whose eight genuine triangular facets are congruent to \(T\), including reflected copies. Congruence of polyhedra is ordinary Euclidean congruence.

**Theorem.** Among \(\mathcal O(T)\), the centrally symmetric (coordinate) realization has the **smallest volume**. Every realization has a unique inscribed ball tangent to all eight faces, and the coordinate realization also has the **smallest inradius**. There is exactly one minimizing congruence class except for the following sharp exceptional family, in which there are exactly two:
\[
(a,b,c)=\lambda\bigl(\sqrt{1+2t},\sqrt{t^2+2t},1+t\bigr),
\qquad \lambda>0,\quad t>1.
\]
The second minimizer in this exceptional case is the noncentrally symmetric *twisted* octahedron whose four equatorial edges have length \(c\). The twisted realizations with equatorial edges of length \(a\) or \(b\) always have strictly larger volume and inradius than the coordinate realization.

More precisely, consider any twisted realization, and label its equal equatorial edges by \(s\in\{a,b,c\}\), the two other face-edge lengths by \(p,q\). Its positive coordinate parameters \(r,d,e\), uniquely determined up to exchanging \(d,e\), satisfy
\[
 p^2=r^2+d^2,\qquad q^2=r^2+e^2,\qquad
 s^2=2r^2+(e-d)^2.
\]
Write \(V_{\rm tw}(s)\) for its volume and \(V_{\rm co}\) for that of the coordinate realization. The exact algebraic identity is
\[
\boxed{V_{\rm tw}(s)^2-V_{\rm co}^2
=\frac49(e-d)^2(r^2-2de)^2\ge0.}
\]
If \(\Delta\) is the area of \(T\), their inradii satisfy the second exact identity
\[
 \rho_{\rm tw}(s)^2-\rho_{\rm co}^2
 =\frac{(e-d)^2(r^2-2de)^2}{16\Delta^2}.
\]

An explicit exceptional example is the scalene acute triangle with sides \((\sqrt5,2\sqrt2,3)\): its coordinate and longest-equator twisted octahedra are noncongruent, but each has surface area \(24\), volume \(8\), and inradius \(1\).

## Assumptions and scope
The term *convex octahedron* means a full-dimensional convex three-polytope with six vertices and the standard octahedral graph; all eight facets must be nondegenerate triangles, not a triangulation of larger facets. The face triangle is **acute and scalene**; this ensures existence of the coordinate realization and all three twisted realizations. Reflected face copies are permitted. The result does not compare non-octahedral eight-facet polytopes or triangles with coinciding side lengths. All volumes and radii use the usual Euclidean metric.

The four-class classification used in the theorem is established in [2]. It follows from the three-edge-colorings of the dual cube: precisely four unordered partitions of its twelve edges into three perfect matchings exist. One is the three-coordinate-matching type; each of the other three selects one matching as the straight coordinate matching, corresponding to the chosen equatorial edge length. [2] proves each feasible class is geometrically rigid and that all four exist for an acute scalene triangle. A finite exact matching enumeration corroborating this exhaustiveness is embedded with this result.

## Proof
**1. Explicit volume formulas.** In the coordinate type, the six vertices are the three antipodal pairs on mutually perpendicular axes of half-lengths \(x,y,z>0\). Every face has lengths \(a,b,c\), so the three squared half-lengths are the quantities
\[
 \frac{a^2+b^2-c^2}{2},\qquad
 \frac{a^2+c^2-b^2}{2},\qquad
 \frac{b^2+c^2-a^2}{2}
\]
in some order. They are positive by acuteness, and the eight tetrahedra from the origin to the facets give \(V_{\rm co}=4xyz/3\).

For a twisted class, take
\[
 U=(0,0,h),\quad V=(0,0,-h),\quad
 A=(r,0,\tau),\quad B=(0,r,-\tau),\quad
 C=(-r,0,\tau),\quad D=(0,-r,-\tau),
\]
where \(h=(d+e)/2\) and \(\tau=(e-d)/2\). Since \(r,d,e>0\), the eight triangles \(UAB,UBC,UCD,UDA,VAB,VBC,VCD,VDA\) are genuine facets [1,2], and the distances of their edges are precisely \(p,q,s\) above. Each triangular facet together with the origin bounds a tetrahedron of absolute determinant \(hr^2\). Therefore
\[
 V_{\rm tw}(s)=\frac{8hr^2}{6}=\frac23 r^2(d+e).
\]

**2. Exact square certificate.** Set \(R=r^2\). When the same three face lengths are used in the coordinate realization, its squared orthogonal half-lengths may be labelled as
\[
 X=de,\qquad Y=R+e(e-d),\qquad Z=R+d(d-e).
\]
This follows by substituting the expressions for \(p^2,q^2,s^2\) into the coordinate half-length formulas. All three are positive by acuteness. Hence
\[
 V_{\rm co}^2=\frac{16}{9}de\,[R+e(e-d)]\,[R+d(d-e)],\quad
 V_{\rm tw}(s)^2=\frac49 R^2(d+e)^2.
\]
Since
\[
 [R+e(e-d)]\,[R+d(d-e)]
 =R^2+(R-de)(e-d)^2,
\]
subtracting and using \((d+e)^2=4de+(e-d)^2\) yields
\[
 \frac94(V_{\rm tw}(s)^2-V_{\rm co}^2)
 =R^2(d+e)^2-4de\,[R^2+(R-de)(e-d)^2]
 =(e-d)^2(R-2de)^2.
\]
This is a universal exact identity, not a numerical or perturbative bound.

**3. Sharp equality classification.** The face triangle is scalene, so \(p\ne q\) and therefore \(d\ne e\). Equality holds precisely when \(R=2de\). Under this equation
\[
 s^2=(d+e)^2,\qquad p^2=d^2+2de,\qquad q^2=e^2+2de.
\]
Consequently \(s^2-p^2=e^2>0\) and \(s^2-q^2=d^2>0\): the equatorial edge length must be the **longest** side \(c\). Conversely, after exchanging \(d,e\) take \(e/d=t>1\), scale \(d=\lambda>0\), and put \(R=2\lambda^2t\). The three lengths are exactly the exceptional family displayed in the Finding section. They are scalene and acute: \(s^2<p^2+q^2\) because \(p^2+q^2-s^2=2de>0\). By [2] these parameters give a genuine twisted octahedron, and the certificate vanishes. The two arrangements are not congruent, because one polyhedron is centrally symmetric and the other has a non-coordinate edge-coloring [2]. No other twisted class can tie. All assertions about numbers of minimizing classes follow from the four-class exhaustion.

**4. The inball conclusion.** All eight facets in each realization are congruent, of area \(\Delta>0\). In the coordinate type, the origin is fixed by a face-transitive symmetry group. In the twisted type, the isometries described in [1, Section 2] form a face-transitive group fixing the origin. In both cases the origin is interior, so it has the same positive perpendicular distance \(\rho\) from all eight supporting planes. The sphere of radius \(\rho\) therefore touches all eight facets. To prove maximality and uniqueness, let \(n_i\) be the eight outward unit facet normals. The elementary polyhedral balance identity gives \(\sum_i\Delta n_i=0\), hence \(\sum_i n_i=0\). For an arbitrary enclosed sphere with center \(x\) and radius \(s_0\), each supporting inequality is \(n_i\cdot x+s_0\le\rho\). Summing gives \(s_0\le\rho\). Equality forces \(n_i\cdot x=0\) for every facet, and the normals span \(\mathbb R^3\) since the body is bounded, so \(x=0\). The inball is unique. Decomposing the volume into the eight equal-height pyramids gives \(V=8\Delta\rho/3\), so comparing squared volumes is exactly equivalent to comparing squared inradii and yields the stated identity.

**5. Explicit exceptional witness.** Take \(d=1,e=2,r^2=4\). The three face-edge squares are \(5,8,9\), with triangular area \(\Delta=3\). The twisted volume is \(\tfrac23\cdot4\cdot3=8\). The coordinate half-axis squares are \(2,6,3\), giving \(V_{\rm co}=\tfrac43\sqrt{36}=8\). Their common inradius is \(3\cdot8/(8\cdot3)=1\), but the prescribed edge-length arrangements differ.

## Verification
The standalone file `check_volume_gap.py` uses exact rational arithmetic, not floating-point approximations, to replay the perfect-square identity and compare volumes for 728 feasible rational coordinate instances, including equality cases. It also exhaustively enumerates all nine perfect matchings of the cube and their four three-matching partitions, with straight-matching count distribution \([1,1,1,3]\). These computations check algebra and the finite combinatorial premise; the proof above establishes the universal geometric inequalities and the equality locus independently of sampled instances.

## Relationship to prior work
Georgiou [1] first proved that every triangle has an eight-face equifacial convex octahedral realization and gave the alternating-height twisted construction. The subsequent published classification [2] proved that an acute scalene triangle has exactly four rigid octahedral realization classes (one coordinate, three twisted), and that a right or obtuse scalene triangle has two twisted classes. Those results establish *which* polyhedra are possible but do not compare their Euclidean volumes or inradii. The present contribution is the exact nonnegative square identity, the unconditional minimum-volume and minimum-inradius determination throughout the acute scalene domain, and the complete one-parameter exceptional family of distinct minimizers. A routine face-volume calculation alone would not determine this global inequality or its equality locus. For a prescribed obtuse triangle the coordinate type does not exist, so the minimization claim is intentionally not made in that domain.

## Limitations
The theorem requires acute **scalene** faces and the combinatorial octahedron; it does not prove a global minimum among all eight-facet convex polyhedra with the same faces, classify isosceles cases, or rank the three twisted volumes against each other. The published existence and four-class classification are cited as prior work, not claimed as original. The perfect-square equality follows from analytic coordinate identities; finite checks are only corroboration. Historical priority of the volume comparison cannot be established conclusively from searchable records, and no independent mathematical audit has been performed.

## References
[1] George M. Georgiou, *Congruent Triangular Faces, Reflections Allowed: Universal Realization and the Minimum Face Count in Problem B22*, arXiv:2608.01109v1, first public 2026-08-02, Sections 2–4. https://arxiv.org/abs/2608.01109

[2] *All edge-length arrangements of scalene-faced convex octahedra*, published mathematical record, 2026-10-25, identifier `72d76a5b-3c3a-43f5-90f4-71e0fa2cce71`, repository https://github.com/published-finding corpus/2026 .
