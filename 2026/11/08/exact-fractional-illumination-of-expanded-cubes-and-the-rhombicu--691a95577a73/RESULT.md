# Exact fractional illumination of expanded cubes and the rhombicuboctahedron

## Finding
For every real \(a>1\), let
\[
P_a=\operatorname{conv}\left\{(\varepsilon_1 x_{\pi(1)},\varepsilon_2 x_{\pi(2)},\varepsilon_3 x_{\pi(3)}):\;\varepsilon_j\in\{-1,1\},\ \pi\in\mathfrak S_3,\ (x_1,x_2,x_3)=(a,1,1)\right\}\subset\mathbb R^3.
\]
Then the ordinary directional illumination number and its fractional version are exactly
\[
\boxed{I(P_a)=4,\qquad I^*(P_a)=\frac{24}{7}}.
\]
The largest number of its 24 vertices illuminated by a single direction is exactly seven. The resulting ordinary-to-fractional gap is \(I(P_a)/I^*(P_a)=7/6\). The standard regular rhombicuboctahedron occurs at \(a=1+\sqrt2\).

At the endpoint \(a=1\), the body becomes the cube \(P_1=[-1,1]^3\) and \(I(P_1)=I^*(P_1)=8\). Thus the fractional invariant drops discontinuously from eight to \(24/7\) under an arbitrarily small positive expansion of the cubic vertices into the 24-vertex family. All these statements are preserved under invertible affine transformations.

## Assumptions and scope
A nonzero vector \(d\in\mathbb R^3\) illuminates a boundary point \(x\) of a convex body \(P\) if \(x+\varepsilon d\in\operatorname{int}P\) for some \(\varepsilon>0\). The ordinary invariant \(I(P)\) minimizes the number of illuminating directions. The fractional invariant \(I^*(P)\) minimizes the total nonnegative weight of a finite family of directions such that each boundary point receives illuminating weight at least one; repeated directions may be combined. Normalizing directions to unit length does not change illumination.

For a polytope, it suffices to illuminate its vertices, both ordinarily and fractionally. If \(x\) is any boundary point in a face \(F\), a direction illuminating any vertex \(v\in F\) also illuminates \(x\): write \(x=\lambda v+(1-\lambda)y\) for some \(y\in F\) and \(\lambda>0\); then \(x+\lambda\varepsilon d\) is in the interior whenever \(v+\varepsilon d\) is. The same implication transfers weighted coverage.

## Proof
**1. Exact halfspace model.** For \(a>1\), \(P_a\) is precisely the intersection of the 26 halfspaces
\[
|x_i|\le a\quad(1\le i\le3),\qquad
|x_i|+|x_j|\le a+1\quad(1\le i<j\le3),\qquad
|x_1|+|x_2|+|x_3|\le a+2.
\]
Each indicated inequality involving absolute values represents all its sign choices. Every signed permutation of \((a,1,1)\) satisfies them. Conversely, to compute the support function of their intersection, take an arbitrary linear objective, reorder the absolute coefficients as \(c_1\ge c_2\ge c_3\ge0\), and reorder the absolute coordinates correspondingly as \(z_1,z_2,z_3\). Telescoping the subset-sum constraints gives
\[
c_1z_1+c_2z_2+c_3z_3
=(c_1-c_2)z_1+(c_2-c_3)(z_1+z_2)+c_3(z_1+z_2+z_3)
\le ac_1+c_2+c_3,
\]
with equality at an appropriate signed permutation of \((a,1,1)\). Equality of support functions establishes the halfspace description.

At a vertex \(v=(s_1a,s_2,s_3)\), where the sign coordinates are \(s_j\in\{-1,1\}\), exactly four facets are active: the one with outward normal \(s_1e_1\), the two with normals \(s_1e_1+s_2e_2\) and \(s_1e_1+s_3e_3\), and the one with normal \(s_1e_1+s_2e_2+s_3e_3\). All other vertices follow by signed coordinate permutations. The strict inequality \(a>1\) guarantees no additional facets become active. Thus \(d\) illuminates \(v\) if and only if its dot product with all four displayed normals is negative.

**2. Sharp seven-vertex bound.** First take a generic direction whose three absolute coordinates \(A_i=|d_i|\) are nonzero, pairwise distinct, and satisfy no equality \(A_i=A_j+A_k\). To illuminate a vertex with large coordinate in position \(i\), the sign of that coordinate must oppose \(d_i\). The other two signs give exactly four choices. Both signs opposed to the corresponding direction always work; just the sign at \(j\) aligned works exactly when \(A_i>A_j\); just the sign at \(k\) aligned works exactly when \(A_i>A_k\); both aligned work exactly when \(A_i>A_j+A_k\). Hence the number of illuminated vertices is
\[
N(d)=\sum_{i=1}^3\left(1+\mathbf1_{A_i>A_j}+\mathbf1_{A_i>A_k}+\mathbf1_{A_i>A_j+A_k}\right),
\]
where in the \(i\)-th summand \(\{i,j,k\}=\{1,2,3\}\). Each pair of distinct absolute coordinates contributes exactly one to the middle terms, and at most one coordinate can exceed the sum of the other two. Therefore \(N(d)\) equals six if the strict triangle inequalities hold, and seven if one coordinate strictly dominates the sum of the other two. For a nongeneric direction, every illuminated vertex continues to be illuminated after a sufficiently small generic perturbation because all required inequalities are strict. Consequently \(N(d)\le7\) for every direction. Equality occurs, for example, at \(d=(4,2,1)\).

**3. Exact fractional value.** Summing the vertex constraints of an arbitrary fractional illumination, and using the bound \(N(d)\le7\), yields \(24\le7\sum w_j\). Thus \(I^*(P_a)\ge24/7\). Conversely, take all 48 signed permutations of \((4,2,1)\). Every such direction illuminates seven vertices. Signed permutations act transitively on the 24 vertices, so double-counting the \(48\cdot7\) incidence pairs shows that each vertex is illuminated by exactly 14 of the directions. Giving each direction weight \(1/14\) covers every vertex with total weight one and has total mass \(48/14=24/7\). This proves \(I^*(P_a)=24/7\).

**4. Exact ordinary value.** Since \(I(P_a)\ge\lceil I^*(P_a)\rceil=4\), it remains to show four directions suffice. Use
\[
d_1=(-4,-2,1),\quad d_2=(-1,4,2),\quad d_3=(2,1,-4),\quad d_4=(4,-2,1).
\]
The following table gives, for each sign triple \((s_1,s_2,s_3)\), one illuminating direction index for the three possible positions of the coordinate of magnitude \(a\). Every entry is certified by the four strict facet-normal inequalities from step 1.

| Signs | Magnitude \(a\) in position 1 | Position 2 | Position 3 |
| --- | --- | --- | --- |
| \((-,-,-)\) | 4 | 2 | 2 |
| \((-,-,+)\) | 3 | 2 | 3 |
| \((-,+,-)\) | 4 | 4 | 4 |
| \((-,+,+)\) | 3 | 4 | 3 |
| \((+,-,-)\) | 1 | 2 | 2 |
| \((+,-,+)\) | 1 | 2 | 3 |
| \((+,+,-)\) | 1 | 1 | 1 |
| \((+,+,+)\) | 1 | 1 | 3 |

All 24 vertices are covered, proving \(I(P_a)=4\).

**5. Cube endpoint.** At \(a=1\) the body is the cube. To illuminate a cube vertex \(s\in\{-1,1\}^3\), a direction must have \(s_id_i<0\) for each coordinate. Thus one direction illuminates at most one cube vertex, so both ordinary and fractional illumination require total cost at least eight. The eight directions opposite the eight cube vertices give equality.

## Verification
The accompanying standalone `verify.py` is pure Python and uses only exact integer arithmetic. At the representative value \(a=2\), it checks that all 24 vertices have exactly the four claimed active normals among the 26 facet inequalities. It constructs all 48 distinct signed permutations of \((4,2,1)\), verifies that every one illuminates exactly seven vertices and that every vertex is hit exactly 14 times, and checks the explicit four-direction cover. It also compares the analytic generic-direction count with direct strict-normal tests for 288 integer directions. The script prints `EXACT_OK` on success. The continuum statement for every \(a>1\) follows from the halfspace and normal-cone proof, not from testing one parameter.

## Relationship to prior work
Naszódi (2009) introduced fractional illumination and its weighted-direction definition. Gorodzha (2026) proved the sharp universal inequality \(I^*(K)\le2^d\) with equality precisely for parallelotopes; that bound does not determine the value for this non-parallelotopal family. Kiss and Oloff de Wet (2012, Theorem 3.4 and its proof) already exhibited four ordinary light sources for the regular rhombicuboctahedron and provided estimates for a different norm-weighted illumination parameter. The four-direction claim for that regular solid is therefore not claimed as new.

A published symmetry lemma states that fractional illumination of a vertex-transitive polytope equals its number of vertices divided by the maximum number illuminated by one direction; its specific evaluations cover the regular dodecahedron and icosahedron, not the rhombicuboctahedron. The present contribution is the sharp seven-vertex incidence bound and the resulting exact \(24/7\) value throughout the full expanded-cube family, with the cube-endpoint discontinuity. A separate published study of the cube–octahedron intersection family establishes a four-direction ordinary illumination profile, but its polytopes have a different normal-fan and face structure; its result does not imply this fractional value.

## Limitations
The result concerns the stated expanded-cube family and its invertible affine images, not every realization of the rhombicuboctahedral combinatorial type. Ordinary illumination of the regular member has prior coverage. The exact fractional value has not received independent mathematical validation, and literature searches cannot establish absolute historical priority. The scaled limit as \(a\to\infty\) is an octahedron, but no claim of continuity at that limit is made.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1 (first posted 2026-09-20), https://arxiv.org/abs/2609.23913.
3. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, Contributions to Discrete Mathematics 7 (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108, https://cdm.ucalgary.ca/article/download/62108/46729/177610.
4. *Exact fractional illumination of the regular dodecahedron and icosahedron*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34.
5. *Exact illumination phase profile of the cube–octahedron intersection family*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-illumination-phase-profile-of-the-cube-octahedron-intersec--20022a556c31.
6. P. Bourke, *Small Rhombicuboctahedron* (2021), https://paulbourke.net/geometry/Rhombicuboctahedron/ (standard coordinates and face structure).
