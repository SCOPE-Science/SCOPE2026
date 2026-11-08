# Exact fractional illumination of the regular truncated icosahedron

## Finding
Let \(P\subset\mathbb R^3\) be the regular truncated icosahedron (the Archimedean solid with twelve pentagonal, twenty hexagonal faces and sixty vertices). Its exact fractional directional illumination number is
\[
\boxed{i^*(P)=\frac{20}{7}}.
\]
More precisely, **any direction illuminates at most twenty-one vertices**, and this bound is attained by each of twenty face-center directions of its parent regular icosahedron. Giving each of those twenty directions weight \(1/7\) is a fractional illumination of the whole boundary; each of the sixty vertices receives total weight exactly one. The ordinary directional number is \(i(P)=4\) (already covered by earlier work); hence the exact ordinary-to-fractional ratio is \(7/5\). The new claim is the sharp fractional evaluation and the twenty-one-vertex certificate, not the preexisting ordinary four-direction bound.

## Assumptions and scope
Write \(\varphi=(1+\sqrt5)/2\) and choose the standard regular icosahedron vertex set
\[
A=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
Let \(E\) be its thirty unordered edges, equivalently pairs of points of \(A\) at squared Euclidean distance four. Then
\[
P=\operatorname{conv}\left\{\frac{2u+v}{3}:\{u,v\}\in E,\ (u,v)\text{ ordered}\right\}.
\]
Its sixty points are all vertices. For a convex body \(K\), a direction \(d\ne0\) illuminates \(x\in\partial K\) when \(x+\varepsilon d\in\operatorname{int}K\) for some \(\varepsilon>0\). A fractional illumination is a finite, nonnegative weighted collection of directions such that the weights of the directions illuminating every boundary point sum to at least one; \(i^*(K)\) is the infimum of its total weight. The assertion holds for all congruent, similar and invertible-affine images of \(P\), by affine invariance of directional illumination.

## Proof
### 1. The exact normal-incidence model
The thirty edges of the icosahedron each belong to two of its twenty triangular faces. The truncated solid has outward facet normals
\[
N=A\cup\{u+v+w:\{u,v,w\}\text{ is an icosahedral triangular face}\}.
\]
There are twelve pentagon normals and twenty hexagon normals. At the truncated vertex indexed by the directed original edge \(u\to v\), precisely three facets meet: the pentagon normal \(u\) and the two face normals of the original triangular faces containing \(\{u,v\}\). Consequently a direction \(d\) illuminates that vertex exactly when all three dot products of \(d\) with those outward normals are **strictly negative**. Every direction illuminating a vertex of a face also illuminates all points of the face, so vertex constraints suffice both for ordinary and fractional illumination.

All signs and incidences are certified over the real quadratic field \(\mathbb Q(\sqrt5)\) by the attached standalone `verify.py`. It constructs the twelve original vertices, thirty edges, twenty triangular faces, sixty truncated vertices, and all thirty-two supporting facets without numerical tolerances. The checker verifies that each outward pentagon normal supports exactly five truncated vertices, each hexagon normal supports exactly six, and exactly three supporting facets meet at every truncated vertex.

### 2. Exhaustive upper bound of twenty-one
The thirty-two facet normals form sixteen opposite pairs, so the distinct great-circle boundaries of illumination sign cells are sixteen. Intersect the positive third-coordinate hemisphere with the affine chart \(d=(x,y,1)\). This produces an arrangement of sixteen distinct affine lines. The exact intersections comprise forty-one distinct vertices: twenty-eight lie on two lines and thirteen lie on four. The elementary line-arrangement region formula gives exactly
\[
1+16+28(2-1)+13(4-1)=84
\]
open cells in this chart. The opposite hemisphere has the same count.

For completeness, every region in an arrangement with nonparallel lines has an intersection vertex in its closure. For every one of the forty-one intersection points, the certificate samples rational perturbation rays in the surrounding sectors and assigns the signs of all thirty-two facet normals *exactly* using the first nonzero term at that vertex. It finds eighty-four **distinct feasible sign patterns** in the positive chart, matching the independently computed eighty-four-region upper bound. Their negatives cover the opposite chart. Perturbation of a direction lying on a great circle preserves any strictly illuminated vertices, so this process exhausts the possible maximal illumination patterns, including boundary directions.

There are 152 distinct spherical sign patterns (the hemisphere lists overlap). The exact incidence spectrum is
\[
\begin{array}{c|cc}
\text{illuminated vertices}&20&21\\\hline
\text{number of sign cells}&132&20
\end{array}.
\]
Therefore no direction illuminates more than twenty-one vertices. This is a finite **exhaustive** deduction: the Euler-region count proves that no unexamined line-arrangement cell remains. The checker uses exact rational arithmetic in \(\mathbb Q(\sqrt5)\); its integer perturbation directions are merely witnesses for the certified cell count.

### 3. A matching weighted construction
For each of the twenty original triangular faces with outward normal \(f=u+v+w\), take the illuminating direction \(-f\). Every one of these twenty directions illuminates exactly twenty-one truncated vertices, and every one of the sixty truncated vertices is illuminated by **exactly seven** of them, both statements checked by strict quadratic-field inequalities. Assigning weight \(1/7\) to each of the twenty directions therefore supplies a fractional illumination of total mass \(20/7\).

Conversely, let \(\nu\) be any finite fractional illumination of total mass \(M\). Sum the sixty vertex constraints, then interchange the finite sum over vertices and the sum over weighted directions. Since each direction illuminates at most twenty-one vertices,
\[
60\le\sum_d w_d\#\{v:d\text{ illuminates }v\}\le21M.
\]
Hence \(M\ge60/21=20/7\). This proves the asserted exact fractional number.

For context, `verify.py` also checks that four directions along original icosahedron vertices indexed \(0,1,5,7\) illuminate all sixty truncated vertices. It exhausts the 152 feasible sign-cell illumination subsets and finds no three subsets covering all sixty vertices. This confirms \(i(P)=4\), although the four-direction conclusion is not claimed as new.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. No external packages are required. The script uses pairs of rational numbers to represent \(a+b\varphi\), with \(\varphi^2=\varphi+1\); sign tests compare rational squares exactly. It derives the face structure from the squared-distance graph, validates every facet's vertex incidence, counts all forty-one affine arrangement intersections and eighty-four chart regions, exhausts the resulting 152 feasible direction sign patterns, checks the twenty-one upper bound, verifies the twenty-directions/seven-incidences fractional construction, and checks the ordinary four-cover and three-cover obstruction. Its success marker is `EXACT_OK`.

## Relationship to prior work
Naszódi (2009) introduced fractional illumination, established general bounds and its fractional-transversal interpretation. Gorodzha (first posted 20 September 2026) proved the sharp universal bound \(i^*(K)\le 2^d\) with equality only for parallelotopes; neither paper evaluates this Archimedean solid. The exact vertex-transitive incidence method has been used for the regular icosahedron and regular dodecahedron, whose fractional illumination numbers are both four; those neighboring results do not imply the present **twenty-one-of-sixty** calculation.

Kiss and Oloff de Wet (2012, Theorem 3.4) explicitly give four light sources for the regular truncated icosahedron as part of a study of a *different norm-weighted illumination parameter*. Thus an ordinary illumination upper bound here is established prior work. Their full text does not give a fractional illumination number or the twenty-one-vertex incidence extremum. The present contribution is the exact rational fractional value \(20/7\), the optimal sixty-vertex incidence certificate and the explicit twenty-direction balanced fractional construction.

## Limitations
This result concerns the regular truncated icosahedron (and affine images), not arbitrary combinatorial realizations, arbitrary truncated polyhedra, or the norm-weighted point-source illumination parameter. The exhaustive finite certificate is mathematically complete for the specified coordinates and normal arrangement, not a proof about all polyhedral normal arrangements. Historical priority remains provisional, and no independent mathematical audit has been performed.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022.
2. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex bodies*, Contributions to Discrete Mathematics 7 (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108.
3. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, first posted 2026-09-20.
4. *Exact fractional illumination of the regular dodecahedron and icosahedron*, public mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34.
