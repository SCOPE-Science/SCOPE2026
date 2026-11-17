# Largest tetrahedra and sixteen movable-apex families in the rhombicuboctahedron

## Finding

Let \(L=1+\sqrt2\), and let \(P\subset\mathbb R^3\) be the standard **small rhombicuboctahedron** with edge length \(2\):
\[
P=\operatorname{conv}\{\text{all independently signed coordinate permutations of }(L,1,1)\}.
\]
Among **all** tetrahedra contained in \(P\), including those with arbitrary nonvertex points, the largest Euclidean volume is
\[
\boxed{M(P)=\frac{16+10\sqrt2}{3}.}
\]
Exactly **48 unordered four-vertex subsets** attain this volume; the determinant magnitudes of all \(\binom{24}{4}=10626\) vertex quadruples take exactly **23 distinct values**, including zero. The complete exact spectrum is supplied in `SPECTRUM.csv`.

There are **16 distinct two-dimensional movable-apex families** of maximizing tetrahedra: for each of the eight triangular faces of \(P\), exactly two particular base triples produce a maximizing tetrahedron when the fourth vertex is chosen **anywhere** in that face. These families cover all 48 vertex-supported maximizing tetrahedra, with three vertex-supported members per family. This statement does **not** assert that these are all arbitrary-point maximizers.

The containing polyhedron has volume \(\frac{96+80\sqrt2}{3}\), so the sharp maximal tetrahedral occupancy fraction is
\[
\boxed{\frac{M(P)}{\operatorname{Vol}_3(P)}=\frac{1+5\sqrt2}{56}.}
\]

## Assumptions and scope

All distances, determinants and volumes use the ordinary Euclidean metric in \(\mathbb R^3\). The shape is the *small* 24-vertex rhombicuboctahedron, **not** the 48-vertex truncated cuboctahedron, sometimes called the great rhombicuboctahedron. The exact source coordinate model has edge length \(2\), and changing the edge length by a positive factor multiplies the maximal tetrahedral volume by its cube without changing the volume fraction.

A maximizing tetrahedron is the convex hull of any four points in the solid; it need not have its corners at original solid vertices. Counts referring to vertex-supported cases treat unordered four-element vertex sets, and the movable-apex families allow every point of a two-dimensional triangular face.

## Proof

**1. Reduction to finitely many determinants.** Fix any three vertices of a contained tetrahedron. Its signed sixfold volume is affine in the remaining vertex, hence the absolute determinant is a convex function of that vertex. Every point of a convex polytope is a convex combination of its vertices; replacing the free point by a polytope vertex cannot decrease the maximum. Applying this sequentially to the four corners shows
\[
6M(P)=\max_{0\le i<j<k<l<24}\left|\det(v_j-v_i,v_k-v_i,v_l-v_i)\right|,
\]
where the \(v_i\) enumerate the 24 signed coordinate permutations of \((L,1,1)\). This is an *exhaustive* finite reduction for the unrestricted problem, not an inference from sampling.

**2. An exact determinant certificate.** All coordinates lie in \(\mathbb Z[\sqrt2]\); the ring operation
\[
(a+b\sqrt2)(c+d\sqrt2)=(ac+2bd)+(ad+bc)\sqrt2
\]
keeps every triple product exact. The standalone `CHECK.py` provides an exhaustive proof certificate with integer-pair arithmetic and exact comparison in this quadratic ring. It forms the vertices in the fixed order: first the coordinate occupied by \(L\) (positions \(1,2,3\)), then the eight independent sign triples in lexicographic order. It computes all 10,626 determinants, canonicalizes each absolute magnitude, and counts every level. The resulting 23 exact determinant levels with their 10,626 total multiplicities appear in `SPECTRUM.csv`. Its largest magnitude is
\[
D_*=32+20\sqrt2=12+20L
\]
with multiplicity exactly 48. As a separate symmetry consistency check, fixing one vertex gives \(\binom{23}{3}=1771\) quadruples and, for each determinant level, the full count is exactly six times this anchored count. This follows because the solid's 24 vertices are transitively permuted by isometries and every unordered quadruple has four members. Consequently \(M(P)=D_*/6=(16+10\sqrt2)/3\).

The explicit certificate is reproducible with `python3 CHECK.py` and uses neither external modules nor floating-point tolerance. Its `expected_L` table is a fixed, individually checkable algebraic tally, **not** numerical evidence extrapolated to an infinite claim.

**3. Construction and count of the movable-apex families.** Each signed normal \((s_1,s_2,s_3)\), with each sign equal to \(\pm1\), supports one triangular face on the plane
\[
s_1x_1+s_2x_2+s_3x_3=L+2.
\]
There are exactly eight such faces, each with three vertices. For each triangular face the same exhaustive determinant certificate finds precisely two fixed unordered base triples whose signed determinant with each of its three apex vertices is the same, with magnitude \(D_*\). Therefore affineness of the signed determinant shows that **every** apex point in the whole triangle gives maximum volume. The 16 face/base combinations are distinct; they account for exactly the 48 maximizing vertex quadruples, each exactly once.

For a concrete example, take the triangular face
\[
F=\operatorname{conv}\{(L,-1,1),(1,-L,1),(1,-1,L)\}
\]
and the two base triples
\[
\begin{aligned}
B_1&=\{(-L,-1,-1),(-1,L,1),(1,1,-L)\},\\
B_2&=\{(-L,1,1),(1,L,-1),(-1,-1,-L)\}.
\end{aligned}
\]
For either base \(B_j\) and **every** \(z\in F\), the tetrahedron \(\operatorname{conv}(B_j\cup\{z\})\) has volume \(D_*/6\). The remaining 14 families are obtained from the other seven triangular faces by signed coordinate symmetry. The checker also verifies the signed determinant agreement individually across all 16 cases, not merely equality of absolute values.

**4. Occupancy.** The solid has 18 square faces of side length \(2\), all at distance \(L\) from its center (six coordinate squares and twelve diagonal squares), and eight equilateral triangular faces of side length \(2\), at center-distance \((L+2)/\sqrt3\). Splitting into center-based pyramids gives
\[
\operatorname{Vol}_3(P)=\frac13\left[18\cdot4L+8\sqrt3\frac{L+2}{\sqrt3}\right]
=\frac{16+80L}{3}=\frac{96+80\sqrt2}{3}.
\]
Dividing by the sharp tetrahedral volume yields \((1+5\sqrt2)/56\), as claimed.

## Verification

Run `python3 CHECK.py` from the directory containing this result. The program constructs the vertices, compares algebraic numbers by exact integer-square tests, enumerates all 10,626 vertex quadruples, checks the 23-valued determinant spectrum and 48 maximal quadruples, independently verifies a fixed-vertex 1,771-case symmetry table, and checks the eight triangular faces, the two base triples per face, and equal **signed** determinants over all three apex vertices. It prints `RHOMBICUBOCTAHEDRON_TETRA_PASS` upon success. `SPECTRUM.csv` gives each nonnegative determinant value in the basis \(1,L\), together with its exact multiplicity.

The exact finite certificate is part of the proof for this fixed algebraic polyhedron. Its finite nature does not claim an infinite-dimensional generalization, and numerical sampling is not used to certify the maximum.

## Relationship to prior work

Steininger and Yurkevich's 2021 paper supplies the explicit coordinates for the rhombicuboctahedron in its appendix, while its main investigation concerns Rupert's problem and projection-containment constants, not the maximum volume of a tetrahedron contained inside this solid. Standard sources provide the 24-vertex and 26-facet combinatorics and ordinary volume; these facts do not determine the largest inscribed tetrahedral fraction or its movable-apex equality cases.

Published results on maximal tetrahedra in the **48-vertex great rhombicuboctahedron** (truncated cuboctahedron), the **24-vertex snub cube**, and cube–octahedron intersections concern geometrically distinct solids, neither equivalent to nor including this 24-vertex model. In particular, the apparent similarity of the phrase *rhombicuboctahedron* does not imply the same body; the number of vertices and face types separate the cases. Circumscription of Archimedean solids *by regular tetrahedra* is a reversed containment problem with a regularity constraint, and likewise does not give this maximum.

## Limitations

The statement is confined to one regular 24-vertex polyhedron, rather than an all-polyhedra classification. Exactly 48 maximizing *vertex-supported* tetrahedra are proved, and 16 complete two-dimensional families of arbitrary-point maxima are exhibited; no assertion is made that all nonvertex equality cases belong to those families. The all-quadruple algebraic enumeration is fully reproducible but remains a finite computation, and its independent implementation deserves external review. An equivalent result in a historical table or otherwise unindexed source cannot be ruled out by search alone. Independent mathematical audit has not been performed.

## References

1. Jakob Steininger and Sergey Yurkevich, *An algorithmic approach to Rupert's problem*, arXiv:2112.13754, first public preprint 2021-12-27, Appendix (rhombicuboctahedron coordinates); https://arxiv.org/abs/2112.13754 and https://ar5iv.labs.arxiv.org/html/2112.13754 .
2. Paul Bourke, *Uniform Polyhedra (80)*, identifying the small rhombicuboctahedron with 24 vertices, 48 edges, and 26 faces, https://paulbourke.net/geometry/polyhedra/ .
3. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496, 2014-02-26, general geometric background, https://arxiv.org/abs/1402.6496 .
4. M. Firsching, *Computing maximal copies of polyhedra contained in a polyhedron*, *Experimental Mathematics* **24** (2015), 98–105, general computational context, DOI:10.1080/10586458.2014.956374.
5. Thomas Murphy and David Weed, *Circumscribing Archimedean Solids With A Regular Tetrahedron*, public presentation (related reversed containment problem); https://www.fullerton.edu/math/faculty/tmurphy/undergrad-research/Archimedean_Solids_23.pdf (original PDF currently not retrievable from that address).
