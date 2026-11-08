# Generic central sections of type-D root polytopes have a universal face type and two exact face counts

## Finding
For an integer \(d\ge4\) let
\[
P_d=\operatorname{conv}\{\pm e_i\pm e_j:1\le i<j\le d\}\subset\mathbb R^d,
\qquad S_u=P_d\cap\{x:u\cdot x=0\}.
\]
If the absolute values \(|u_1|,\ldots,|u_d|\) are pairwise distinct, then **the entire face lattice of** \(S_u\) is independent of \(u\) up to isomorphism. Its extreme face numbers are
\[
\boxed{f_0(S_u)=\frac{4d(d-1)(d-2)}3,\qquad f_{d-2}(S_u)=2^d+2d-6.}
\]
For \(d=4\), every such three-dimensional section has face vector \((32,48,18)\), with six quadrilateral and twelve hexagonal facets, and has the combinatorial type of a **chamfered cube**. The six quadrilaterals are pairwise nonadjacent; each of the twelve hexagons meets precisely two quadrilaterals along edges, and these twelve pairs constitute the edges of the octahedral graph on the six quadrilaterals. Thus the statement is stronger than a numerical face-vector coincidence. A Haar-distributed normal satisfies the hypothesis almost surely.

## Assumptions and scope
The root vectors are the \(2d(d-1)\) distinct signed two-coordinate vectors. The hyperplane passes through the origin; an affine translated hyperplane has different section behavior. The normal may be any nonzero real vector with pairwise distinct coordinate magnitudes (a zero coordinate is permitted, provided no two magnitudes coincide). Facets of \(S_u\) have dimension \(d-2\); the term *face lattice* includes all incidences. The claim is combinatorial, not an assertion of metric or affine equivalence. At exceptional normals with \(u_i=\pm u_j\), root vertices may lie on the hyperplane and the section type may change.

## Proof
**1. Parent polytope and its edge graph.** As in Proposition 18 of Ardila--Beck--Hoşten--Pfeifle--Seashore [1], the complete irredundant list of facets of \(P_d\) is
\[
\sigma_i x_i\le1\quad(1\le i\le d,\ \sigma_i\in\{\pm1\}),\qquad
\sum_{i=1}^d\sigma_i x_i\le2\quad(\sigma\in\{\pm1\}^d).
\]
The first \(2d\) facets are cross-polytopes, and the other \(2^d\) are signed hypersimplices. The vertex list follows directly from its defining convex hull.

Two distinct root vertices \(v,w\) are joined by an edge of \(P_d\) **if and only if** \(v\cdot w=1\). For sufficiency, after sign and coordinate symmetries write \(v=e_1+e_2\), \(w=e_1+e_3\). The linear functional \(2x_1+x_2+x_3\) takes its maximum over the root vertices precisely at these two vertices, exposing an edge. For necessity, if the two roots have disjoint supports, their midpoint is also the midpoint of a different pair of roots; if they have the same support but opposite signs in one coordinate, the same is true after choosing any third coordinate. If they share just one coordinate with opposite signs, use any fourth coordinate to construct an alternative root pair with the same midpoint. Antipodal roots have midpoint zero, which is interior to \(P_d\). None of these segments is an exposed edge. This exhausts the possible scalar products of distinct roots. The argument uses \(d\ge4\) precisely for the fourth-coordinate alternative.

**2. All generic normal directions have the same combinatorics.** The group of arbitrary signed coordinate permutations preserves \(P_d\). It sends every normal with pairwise distinct absolute coordinates into a normal with
\[
u_1>u_2>\cdots>u_d\ge0.
\]
At each root vertex \(v=\pm e_i\pm e_j\), the sign of \(u\cdot v\) is determined by the sign of its coefficient at the index having the larger absolute normal coordinate. Therefore the sign assignment to all original vertices is identical throughout this normalized chamber, including the case \(u_d=0\). No original vertex lies on the cutting hyperplane. Every nonempty proper face of the section is the intersection with an original face whose vertices have both signs, and its dimension decreases by one. Its incidences are inherited from inclusions among original faces. Thus identical sign assignments give isomorphic complete section face lattices.

**3. Count section vertices.** Because the hyperplane misses all vertices, every new vertex cuts exactly one original edge transversely. In the normalized chamber, positive original vertices are
\(q_{ij}^{+}=e_i+e_j\) and \(q_{ij}^{-}=e_i-e_j\), for \(1\le i<j\le d\). Counting the neighbors with negative scalar product using the edge criterion in step 1 gives respectively
\[
N_{ij}^{+}=i+j-3,\qquad N_{ij}^{-}=i+2d-j-3.
\]
Each crossing edge has exactly one positive endpoint, so it is counted once, and hence
\[
\begin{aligned}
f_0(S_u)
&=\sum_{1\le i<j\le d}(N_{ij}^{+}+N_{ij}^{-})
=2\sum_{i=1}^{d-1}(d-i)(i+d-3)\\
&=\frac{4d(d-1)(d-2)}3.
\end{aligned}
\]
All terms and boundaries are integer-valued, and the double sum is exact.

**4. Count section facets.** An original facet contributes a facet to \(S_u\) exactly when it has vertices on both sides of the cutting hyperplane. For \(x_i=\pm1\), the facet vertices are \(\pm e_i\pm e_j\) with the sign at position \(i\) fixed. The only uncut coordinate facets are the two with \(i=1\). Thus \(2d-2\) coordinate facets survive.

For a signed hypersimplex facet with sign vector \(\sigma\), its vertices are \(\sigma_i e_i+\sigma_j e_j\) for \(i<j\). The scalar-product sign of this vertex is \(\sigma_i\), because \(u_i>u_j\ge0\). All these signs coincide exactly when \(\sigma_1=\sigma_2=\cdots=\sigma_{d-1}\); \(\sigma_d\) is unrestricted. This excludes precisely four of the \(2^d\) signed facets, leaving \(2^d-4\). The total is therefore
\[
f_{d-2}(S_u)=(2d-2)+(2^d-4)=2^d+2d-6.
\]

**5. The three-dimensional specialization.** For \(d=4\), one may take \(u=(8,4,2,1)\) without changing the combinatorial type. The crossed original coordinate facets comprise the two facets with \(i=2\), which give quadrilaterals, and the four with \(i\in\{3,4\}\), which give hexagons. Among the signed facets, four with \(\sigma_1=\sigma_2=\sigma_3\) are uncut; four with \(\sigma_1=\sigma_2\ne\sigma_3\) cut in quadrilaterals; the remaining eight with \(\sigma_1\ne\sigma_2\) cut in hexagons. This follows by applying the dot-product edge test to the six vertices of each octahedral original facet. There are six quadrilaterals and twelve hexagons.

Each cut edge of the original regular \(24\)-cell belongs to exactly three original octahedral facets, so the section is simple: every section vertex has degree three. Consequently \(f_1=3f_0/2=48\). Applying the same facet--edge incidence rule to the six quadrilaterals shows that no two share an edge, every hexagon is adjacent along edges to exactly two quadrilaterals, and among the fifteen unordered quadrilateral pairs, precisely the three antipodal pairs are absent. The remaining twelve pairs form the octahedral graph \(K_{2,2,2}\). This square--hexagon pattern is the face-incidence structure of the chamfered cube; explicit exact incidence enumeration in the accompanying checker independently gives the full identification. \(\square\)

## Verification
The included standalone Python 3 checker uses only the standard library. It enumerates all root vertices and exposed edges using the proved dot-product criterion; constructs every original coordinate and signed facet by its exact equality; counts original edges intersecting the section; and counts the vertices of each surviving section facet. For dimensions \(d=4,5,6,7\), it obtains respectively \(32,80,160,280\) section vertices and \(18,36,70,136\) facets, exactly the formulas above. For \(d=4\), it verifies the \(6\)-quadrilateral/\(12\)-hexagon profile, the \(48\) edges, trivalence of all \(32\) vertices and the \(12\)-edge octahedral quad-hex adjacency pattern. It repeats the enumeration with a different strictly decreasing normal to corroborate chamber stability. These are finite tests; the proof above establishes every dimension and every generic normal.

Run with `python3 geometry_droot_checker.py`; success ends with `D_ROOT_GENERIC_SECTION_EXACT_COUNTS_OK`.

## Relationship to prior work
Ardila et al. [1] give the root-system vertex and complete facet descriptions and study **triangulations of the original root-polytope boundaries**. Proposition 18 is used explicitly above; its stated face enumerations concern boundary triangulations, not hyperplane sections. Cellini and Marietti [2] study a different central hyperplane arrangement passing through codimension-two faces of root polytopes, and their paper identifies special relations between this arrangement and root facets. The present statement instead concerns sections by hyperplanes through the *origin* with arbitrary generic normal.

The well-known chamfered cube face profile [4] is not claimed as a new polyhedron, and geometric accounts of special noncentral slices of the 24-cell [3] display the same \(6+12\) face profile. The proposed contribution is the all-dimensional generic-section rigidity together with exact universal vertex and facet counts and the identification of the central, generic four-dimensional case. Priority remains provisional: the cited descriptions of root polytopes and classical oriented-matroid section theory provide tools from which parts might be derivable, and an unlocated equivalent section enumeration cannot be excluded.

## Limitations
The theorem makes no assertion for all exceptional directions or for translated hyperplanes. It supplies the two extreme face numbers in every dimension, not the complete numerical \(f\)-vector for \(d>4\). Different normal vectors generally give sections that are not congruent or affinely equivalent. No computer enumeration or numerical evidence is used in place of the infinite-dimensional proof. Historical priority and independent verification remain open.

## References
[1] F. Ardila, M. Beck, S. Hoşten, J. Pfeifle, and K. Seashore, “Root polytopes and growth series of root lattices,” arXiv:0809.5123, version 1 publicly posted 2008-09-30, Section 5, Proposition 18. https://arxiv.org/html/0809.5123v1

[2] P. Cellini and M. Marietti, “Root polytopes and abelian ideals,” arXiv:1207.3429 (2012), Introduction and Section 4. https://arxiv.org/abs/1207.3429

[3] “Cross-sections: a 4D body passing through our world,” The Fourth Dimension, section on 24-cell special-direction slices. https://legost.in/en/utilities/4d/slices

[4] “Chamfer (geometry),” chamfered-cube combinatorial description. https://handwiki.org/wiki/Chamfer_%28geometry%29
