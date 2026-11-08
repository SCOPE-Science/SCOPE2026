# Exact ordinary and fractional directional illumination of the regular icosidodecahedron

## Finding
Let \(P\) be the regular icosidodecahedron, namely the convex hull of the thirty midpoints of edges of a regular icosahedron. For ordinary parallel-direction illumination \(I\), and fractional parallel-direction illumination \(I^*\) in the sense of Naszódi, the exact values are
\[
\boxed{I(P)=4,\qquad I^*(P)=3.}
\]
In particular the integrality gap is exactly \(I(P)/I^*(P)=4/3\). A concrete fractional illumination consists of twelve equally weighted directions, of weight \(1/4\) each, opposite the twelve original icosahedron vertices. Each one illuminates exactly ten rectified vertices, and each rectified vertex receives exactly four such directions. The ordinary value four is attained by a four-direction subfamily.

## Assumptions and scope
Set \(\varphi=(1+\sqrt5)/2\) and let \(V\) consist of the twelve vectors
\[
(0,\pm1,\pm\varphi),\quad(\pm\varphi,0,\pm1),\quad(\pm1,\pm\varphi,0).
\]
Let \(E\) consist of the thirty unordered pairs \(\{a,b\}\subset V\) satisfying \(a\cdot b=\varphi\), and put
\[
P=\operatorname{conv}\{(a+b)/2:\{a,b\}\in E\}.
\]
This is the regular icosidodecahedron. A nonzero direction \(u\) illuminates \(x\in\partial P\) when \(x+\varepsilon u\in\operatorname{int}P\) for some \(\varepsilon>0\). The ordinary invariant \(I(P)\) is the smallest number of illuminating directions. The fractional invariant \(I^*(P)\) is the infimum of the sums of nonnegative weights assigned to finitely many directions such that each boundary point receives illuminating weight at least one. They are **not** the norm-weighted quantitative illumination parameter of Kiss and Oloff de Wet.

## Proof
**1. Exact normal-cone reduction.** The original icosahedron has twelve vertices, thirty edges, twenty triangular faces and six antipodal vertex pairs. Its rectification has thirty vertices, twelve pentagonal faces (one for every original vertex) and twenty triangular faces (one for every original face). At a rectified vertex indexed by the original edge \(\{a,b\}\), four outward facet normals are \(a\), \(b\), \(a+b+c\) and \(a+b+d\), where \(\{a,b,c\}\) and \(\{a,b,d\}\) are its two incident original triangles. Therefore \(u\) illuminates that vertex precisely when its scalar product with all four normals is strictly negative.

In particular, if \(u\) illuminates the edge-midpoint vertex for \(\{a,b\}\), then both original endpoints belong to
\[
S(u)=\{a\in V:u\cdot a<0\}.
\]
At most one of each antipodal pair belongs to \(S(u)\), so this set extends to one of the sixty-four six-element antipodal transversals. Thus the number of rectified vertices illuminated by any one direction cannot exceed the number of edges induced by such a transversal.

**2. Ten is the exact single-direction maximum.** Enumerating all \(2^6=64\) antipodal transversals and counting their induced original icosahedral edges gives the **complete** exact table
\[
\begin{array}{c|rrrr}
\text{induced edges}&5&6&9&10\\\hline
\text{number of transversals}&12&20&20&12
\end{array}
\]
The twelve transversals with ten induced edges are precisely the closed vertex neighborhoods \(N[a]\) (the vertex and its five neighbors), as checked by the complete, deterministic integer enumeration in the accompanying verifier. Hence no direction illuminates more than ten rectified vertices.

There is also a nonenumerative bound of ten. Normalize one representative from each antipodal pair to unit length \(w_1,\ldots,w_6\). These are six equiangular vectors with \(|w_i\cdot w_j|=1/\sqrt5\) for distinct indices and \(\sum_i w_iw_i^{\mathsf T}=2I_3\). For any signs \(s_i\in\{-1,1\}\), write \(w_i\cdot w_j=\sigma_{ij}/\sqrt5\). Then \(\|\sum_i s_iw_i\|^2\le12\) implies \(\sum_{i<j}\sigma_{ij}s_is_j\le3\sqrt5<7\). The left side is an odd integer and therefore at most five. Exactly \((15+\sum_{i<j}\sigma_{ij}s_is_j)/2\le10\) pairs in the corresponding transversal are adjacent.

**3. Matching directions and fractional optimum.** For each original vertex \(a\), choose the direction \(-a\). It illuminates the ten rectified vertices corresponding to edges induced by \(N[a]\), and no others. Indeed \(a\cdot b\ge\varphi>0\) for each \(b\in N[a]\); the third vertex of an original triangular face incident to an edge inside \(N[a]\) is never antipodal to \(a\), so the scalar product with its face-sum normal is at least \(\varphi+\varphi-\varphi=\varphi>0\). Conversely, either endpoint outside \(N[a]\) prevents illumination through its pentagonal facet. Each icosahedral edge belongs to exactly four closed neighborhoods: those of its two endpoints and its two common neighbors. Assign weight \(1/4\) to each of the twelve directions. Every rectified vertex receives weight one, and hence so does every other boundary point by the face-inclusion argument below. The total weight is three, giving \(I^*(P)\le3\).

For any fractional illumination, sum the coverage inequalities over all thirty vertices. Since each individual direction illuminates at most ten vertices, the total weight is at least \(30/10=3\). Hence \(I^*(P)=3\).

**4. Ordinary optimum.** If three directions illuminated all thirty vertices, each would have to illuminate exactly ten and the three illuminated ten-sets would be pairwise disjoint. By the complete transversal classification in Step 2, each such ten-set must be the set of original edges induced by some \(N[a]\). Exact graph incidence gives the following intersection rule for two different such edge sets: intersection size five if their centers are adjacent, one if they are distinct and nonadjacent but not antipodal, and zero precisely when the centers are antipodal. Three distinct icosahedral vertices cannot be pairwise antipodal; hence three disjoint ten-sets are impossible. This proves \(I(P)\ge4\).

For the reverse inequality, take four original vertices
\[
 a_1=(0,-1,-\varphi),\quad
 a_2=(0,-1,\varphi),\quad
 a_3=(-\varphi,0,-1),\quad
 a_4=(1,\varphi,0).
\]
The four directions \(-a_1,-a_2,-a_3,-a_4\) illuminate all thirty edge-midpoint vertices: their four induced closed-neighborhood edge sets have union \(E\), certified by exact integer enumeration. Thus \(I(P)=4\).

**5. From vertices to the boundary.** Every boundary point lies in the relative interior of a unique face \(F\). Every direction illuminating any vertex of \(F\) also illuminates that boundary point, because each facet active at the relative interior of \(F\) is also active at that vertex. Therefore the finite vertex inequalities suffice for both ordinary and fractional illumination.

## Verification
Run `python3 verify.py` using Python 3 and the standard library. The verifier constructs coordinates in \(\mathbb Z[\varphi]\), performing integer arithmetic with the exact relation \(\varphi^2=\varphi+1\), and checks all strict normal inequalities without floating-point approximations. It verifies the twelve vertices, thirty edges, twenty original faces, the four facet normals at each rectified vertex, the twelve ten-vertex illumination sets, the fourfold coverage, all sixty-four antipodal transversals and their multiplicities, the maximizer classification, intersection patterns, a four-set cover, and the tight-frame identity. The recorded result is `EXACT_OK`.

The sixty-four-case exhaustion is a valid finite proof because Step 1 reduces **every real direction** to one of those sign transversals. No claim of covering all possible real directions by numerical sampling is made. The separate analytic frame argument checks the extremal count independently. The geometric facet-normal description is the standard rectification of a regular icosahedron and is also checked by the exact incidence reconstruction.

## Relationship to prior work
Naszódi introduced fractional illumination and gave universal bounds, without this exact Archimedean-solid evaluation. Gorodzha proved the universal sharp upper bound \(I^*(K)\le2^d\) and characterized its equality bodies; that result does not determine the specific value three for \(P\). The existing evaluation of \(I^*\) for the regular dodecahedron and icosahedron gives four for each and establishes the vertex-transitivity reduction, but neither evaluation determines the rectified solid. Here the separate ten-edge transversal certificate and fourfold closed-neighborhood covering resolve that case.

Kiss and Oloff de Wet investigated the icosidodecahedron in their full 2012 paper, giving an upper estimate using six finite **point sources** for their distinct norm-weighted illumination parameter. Their Theorem 3.4 expressly provides estimates rather than an exact ordinary or fractional directional value. Their result neither contains nor contradicts the present exact \(I=4\), \(I^*=3\). Their paper's results on the Platonic solids and the different norm-weighted quantity are acknowledged.

## Limitations
The theorem is for the Euclidean regular icosidodecahedron and its affine images, with *parallel-direction* illumination. It is not a result about norm-weighted finite light-source costs, nonregular realizations, other Archimedean solids or higher-dimensional rectifications. Exhaustive finite certificates independently establish the combinatorial classification only after the exact geometric reduction. No independent external mathematical audit has been performed, and historical priority beyond the inspected literature is not guaranteed.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), DOI: 10.55016/ojs/cdm.v4i2.62022.
2. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, Contributions to Discrete Mathematics 7 (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108.
3. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1 (first public 2026-09-20).
4. *Exact fractional illumination of the regular dodecahedron and icosahedron*, 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34.
