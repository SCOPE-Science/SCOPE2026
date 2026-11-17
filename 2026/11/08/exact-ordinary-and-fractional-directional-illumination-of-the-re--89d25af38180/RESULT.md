# Exact ordinary directional illumination of the regular icosidodecahedron and its fractional integrality gap

## Finding and provenance
Let \(P\) be the convex hull of the thirty edge midpoints of a regular icosahedron. For illumination by parallel directions, the **ordinary illumination number** is
\[
\boxed{I(P)=4.}
\]
The fractional illumination number \(I^*(P)=3\) was already established in *The icosidodecahedron has fractional illumination number three* (public research record, 25 October 2026). Combining the new ordinary determination with that earlier fractional determination gives the exact ordinary/fractional gap \(I(P)/I^*(P)=4/3\). We do **not** claim the already-published fractional value, the maximal ten-vertex directional coverage, or the 64-transversal induced-edge count as new. The new contribution is the obstruction to ordinary three-direction coverage, the explicit ordinary four-direction cover, and the resulting integrality gap.

## Hypotheses and definitions
Let \(\varphi=(1+\sqrt5)/2\) and let the icosahedral vertices be
\[
V=\{(0,\pm1,\pm\varphi),(\pm\varphi,0,\pm1),(\pm1,\pm\varphi,0)\}.
\]
An icosahedral edge is a pair \(\{a,b\}\subset V\) with \(a\cdot b=\varphi\); the rectified polytope is \(P=\operatorname{conv}\{(a+b)/2\}\) over these thirty edges. A direction \(u\ne0\) illuminates a boundary point \(x\) when \(x+\varepsilon u\in\operatorname{int}P\) for some \(\varepsilon>0\). \(I(P)\) is the minimum number of such directions covering the boundary. \(I^*(P)\) minimizes total nonnegative weight of a finite family of such directions covering each boundary point to weight at least one. These are directional invariants, not the norm-weighted exterior-light-source cost of Kiss and Oloff de Wet.

## Proof of the ordinary determination
At the rectified vertex corresponding to the icosahedral edge \(ab\), the four incident facet normals are the two pentagonal normals \(a,b\) and two triangular normals \(a+b+c,a+b+d\), where \(abc,abd\) are the two incident original faces. Thus \(u\) illuminates this rectified vertex exactly when it pairs strictly negatively with all four normals. In particular both \(a\) and \(b\) must have negative pairing with \(u\).

The twelve original vertices form six antipodal pairs, so the strictly negative original vertices for any \(u\) extend to an antipodal transversal containing one vertex from each pair. The complete 64-transversal induced-edge census, already established in the October 25 fractional-illumination result and independently reconstructed here, has induced-edge cardinalities \(5,6,9,10\) with multiplicities \(12,20,20,12\). Its twelve ten-edge maximizers are exactly the closed icosahedral neighborhoods
\[
N[a]=\{a\}\cup\{b\in V:\{a,b\}\text{ is an icosahedral edge}\},\qquad a\in V.
\]
Hence every direction illuminates at most ten of the thirty rectified vertices, and if it illuminates ten then its illuminated vertex set must be the edge set induced by some \(N[a]\). The latter bound and fractional value are prior work, rather than novel steps.

For each original vertex \(a\), the direction \(-a\) illuminates exactly the ten rectified vertices indexed by edges induced by \(N[a]\). This follows by the four-normal test: the original neighbors and \(a\) pair positively with \(a\), and both original triangular-face normals pair positively as well. Explicit incidence counting gives, for distinct centers \(a,b\), the intersection size of the two ten-edge sets:
\[
|E(N[a])\cap E(N[b])|=\begin{cases}
5,&a,b\text{ adjacent},\\
1,&a,b\text{ neither adjacent nor antipodal},\\
0,&b=-a.
\end{cases}
\]
The identity is a finite, exact icosahedral incidence statement; it is independently verified by enumerating the six antipodal pairs and thirty original edges.

Suppose three directions illuminated all thirty rectified vertices. Since each covers at most ten, they would each have to cover exactly ten, and their three ten-sets would have to be pairwise disjoint. Every maximizing ten-set equals some \(E(N[a])\); the displayed intersection rule makes pairwise disjointness possible only for antipodal centers. Three distinct centers cannot be pairwise antipodal. Therefore \(I(P)\ge4\).

For the matching upper bound use four directions opposite to
\[
(0,-1,-\varphi),\quad(0,-1,\varphi),\quad(-\varphi,0,-1),\quad(1,\varphi,0).
\]
Their closed-neighborhood edge sets have union all thirty original edges. The accompanying exact-arithmetic `verify.py` checks this covering directly against all thirty edges and each of the four active rectified facet normals. Thus four directions illuminate every rectified vertex. Every boundary point belongs to the relative interior of a face containing a vertex; any direction illuminating that vertex also strictly decreases the active facet inequalities at the face point. Therefore vertex illumination extends to the entire boundary. Hence \(I(P)\le4\), proving the asserted ordinary value.

## Fractional context and verification
The earlier October 25 theorem proves \(I^*(P)=3\) from the ten-vertex bound and icosahedral symmetry averaging. Equivalently, the twelve directions \(-a\), each with weight \(1/4\), illuminate every rectified vertex with total weight exactly one; summing the thirty vertex constraints, with at most ten illuminated vertices per direction, gives the matching lower bound three. These statements are reproduced solely to make the joint integrality gap self-contained and are **not** new originality claims.

Run `python3 verify.py` with the standard library. It represents the original coordinates in \(\mathbb Z[\varphi]\) using \(\varphi^2=\varphi+1\), reconstructs 12 vertices, 30 edges, 20 original triangular faces and 32 rectified facets, exhausts all 64 antipodal transversals, checks the unique maximum neighborhoods, all ten-set intersections, the four strict-normal inequalities and the explicit four-direction cover. It prints `EXACT_OK`. The finite enumeration is exhaustive after the proved reduction from all real illuminating directions to antipodal sign transversals; it is not numerical sampling of real directions. A separate combinatorial reconstruction likewise confirms 64 counts, 0 three-set covers and a four-set cover.

## Relationship to earlier work and limitations
The published October 25 result, *The icosidodecahedron has fractional illumination number three*, proves precisely the same fractional \(3\) and the ten-edge transversal bound, including the induced-edge distribution. Its full theorem and proof were read. It does not assert the ordinary \(I(P)=4\), classify intersections of maximizing illumination sets or exhibit the necessary four-set cover. Those further facts do not follow merely from \(\alpha(P)=10\): a three-direction cover could have been possible if three maximum sets were disjoint. The intersection obstruction is the substantive distinguishing step.

Naszódi introduced the fractional invariant. The exact fractional values four for the regular dodecahedron and icosahedron are also earlier results. Kiss and Oloff de Wet considered a different norm-weighted exterior-source parameter for the icosidodecahedron, and Gorodzha proved general fractional upper bounds. None of these gives the ordinary four-direction obstruction. The claim applies to the regular polytope and its affine images only; it does not classify every optimal four-cover, other Archimedean solids or the norm-weighted exterior-source invariant. Historical priority beyond the inspected full texts remains best-of-knowledge rather than exhaustive.

## References
1. *The icosidodecahedron has fractional illumination number three*, published 2026-10-25, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-the-icosidodecahedron-has-fractional-illumination-number-three--2e50febb140e/RESULT.md .
2. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), DOI: 10.55016/ojs/cdm.v4i2.62022.
3. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, Contributions to Discrete Mathematics 7 (2012), DOI: 10.55016/ojs/cdm.v7i1.62108.
4. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913.
5. *Exact fractional illumination of the regular dodecahedron and icosahedron*, published 2026-10-11, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34/RESULT.md .
