# Sharp orientation extrema for three-triangle translation-feasibility volumes

## Finding

For any three positive scales \(a_0,a_1,a_2\) and any three independently rotated equilateral triangles \(K_i=a_iR_{\theta_i}T\), the four-dimensional volume \(\mathcal V\) of the translation pairs \((x,y)\) giving a nonempty common intersection has the sharp range

\[
A^2\!\left[\sum_{i<j}a_i^2a_j^2+2a_0a_1a_2\left(\sum_i a_i+\min_i a_i\right)\right]
\ \le\ \mathcal V\ \le\
A^2\!\left[\sum_{i<j}a_i^2a_j^2+4a_0a_1a_2\sum_i a_i\right],
\]

where \(A=\operatorname{Area}(T)\). The upper bound is attained exactly when all three directions agree modulo a one-third turn. The lower bound is attained exactly when two triangles have a common direction, the third is rotated by one-sixth turn, and the singleton-direction triangle has a smallest scale (with the expected alternatives under ties). For three equal scales the range is exactly \([11A^2,15A^2]\).

More precisely, let \(\delta_{ij}\in[0,\pi/3]\) be the circular distance between \(\theta_i\) and \(\theta_j\) modulo \(2\pi/3\). The entire orientation-dependent profile is

\[
\boxed{\mathcal V=A^2\sum_{i<j}a_i^2a_j^2+
4A^2a_0a_1a_2\left(a_2\cos\delta_{01}+a_1\cos\delta_{02}+a_0\cos\delta_{12}\right).}
\]

## Assumptions and scope

All triangles are compact, nondegenerate planar equilateral triangles obtained from one fixed triangle \(T\) by positive scaling and rotation; each may first be translated arbitrarily without changing the four-dimensional volume. The feasible-translation body is

\[
\mathcal F(K_0,K_1,K_2)=\{(x,y)\in\mathbb R^2\times\mathbb R^2:
K_0\cap(K_1+x)\cap(K_2+y)\ne\varnothing\}.
\]

Its volume is the ordinary four-dimensional Lebesgue volume, not the maximum two-dimensional area of a triple intersection and not the integral of that overlap area. Every scale is strictly positive. The orientation variables are independent, modulo a symmetry of order three.

For a planar convex body \(K\), write \(|K|=\operatorname{Area}(K)\), and define the symmetric mixed area \(V_2(K,L)\) by \(|K+tL|=|K|+2tV_2(K,L)+t^2|L|\) for \(t\ge0\). This mixed area is continuous, bilinear under Minkowski addition, and translation-invariant.

## Proof

**Step 1 (a mixed-area identity).** We first prove a general identity for any three planar convex bodies with interior:

\[
\boxed{\operatorname{Vol}_4\mathcal F(K_0,K_1,K_2)
=\sum_{i<j}|K_i||K_j|+2\sum_{i<j}|K_k|V_2(K_i,-K_j),}
\]

where \(k\) is the index omitted by each unordered pair \(i,j\).

Fix \(x\in K_0-K_1\), and put \(B_x=K_0\cap(K_1+x)\). For this \(x\), the feasible \(y\)-section is \(B_x-K_2\), of area

\[
|B_x-K_2|=|B_x|+2V_2(B_x,-K_2)+|K_2|.
\]

Fubini gives \(\int_{K_0-K_1}|B_x|\,dx=|K_0||K_1|\) and \(|K_0-K_1|=|K_0|+|K_1|+2V_2(K_0,-K_1)\).

For the remaining term, use the planar boundary formula \(2V_2(B_x,L)=\int_{\partial B_x}h_L(n_z)\,d\mathcal H^1(z)\), where \(n_z\) is the exterior unit normal almost everywhere. The boundary of an intersection of two convex bodies is, up to zero-length exceptions, the disjoint union of those pieces of \(\partial K_0\) contained in \(K_1+x\) and of those pieces of \(\partial(K_1+x)\) contained in \(K_0\). Integrating the first contribution in \(x\), a fixed \(z\in\partial K_0\) is included for exactly a translate-set of area \(|K_1|\); the second contribution similarly has factor \(|K_0|\). Thus

\[
\int_{K_0-K_1}2V_2(B_x,-K_2)\,dx
=2|K_1|V_2(K_0,-K_2)+2|K_0|V_2(K_1,-K_2).
\]

Combining the three terms proves the identity. For polygons all integrals are finite and the ambiguous overlap edges occur only for a null set of translations; the result for arbitrary convex bodies also follows by polygon approximation and continuity.

**Step 2 (the equilateral mixed area).** Let \(T\) have circumradius \(R\) and area \(A=3\sqrt3R^2/4\). Its three sides have length \(\sqrt3R\), with outward normals spaced by \(2\pi/3\). For a second copy rotated through angle \(\phi\), the support function of \(-R_\phi T\) at each such normal is \(R\cos\delta\), where \(\delta\in[0,\pi/3]\) is the least angular distance of \(\phi\) from a multiple of \(2\pi/3\). The boundary formula therefore gives

\[
2V_2(T,-R_\phi T)=3\sqrt3R^2\cos\delta=4A\cos\delta.
\]

By mixed-area homogeneity, \(V_2(K_i,-K_j)=2Aa_ia_j\cos\delta_{ij}\). Substitute this into Step 1 and use \(|K_i|=a_i^2A\) to obtain the displayed orientation profile. As a separate check on dimension and compactness, \(\mathcal F\) is the linear image of \(K_0\times K_1\times K_2\) under \((z,u,v)\mapsto(z-u,z-v)\); it is a full-dimensional compact convex body.

**Step 3 (global extrema and complete equality).** Orientations live on a circle of circumference \(L=2\pi/3\). Order three points on this circle and let their successive gaps be \(g_1,g_2,g_3\ge0\), with sum \(L\). Each pair distance is \(\min(g_i,L-g_i)\) for the gap that separates the other two points; the coefficient of its cosine is the positive scale of the omitted triangle.

If every \(g_i\le L/2\), the weighted sum of cosines is strictly concave on the compact convex triangle \(0\le g_i\le L/2\), \(\sum g_i=L\): every cosine is strictly concave on \([0,\pi/3]\). Its minimum can only be at the triangle's vertices, the permutations of \((0,L/2,L/2)\). If one gap exceeds \(L/2\), write the other two as \(p,q\ge0\), \(p+q\le L/2\). The objective becomes a positive weighted sum of \(\cos p\), \(\cos q\), and \(\cos(p+q)\), strictly concave on this triangle. Its minimum must occur at \((0,0)\), \((L/2,0)\), or \((0,L/2)\). The first configuration is three aligned directions, which has strictly larger value than the other two. Thus every global minimum has two coincident directions and the third at angular distance \(L/2=\pi/3\).

If the singleton triangle has scale \(a_k\), the weighted cosine sum is exactly \((\sum_i a_i+a_k)/2\). Choose any index of minimum scale to obtain the sharp lower bound and its full equality set. Finally each \(\cos\delta_{ij}\le1\), with equality precisely for aligned direction pairs; positive weights enforce the unique upper equality pattern. This proves all assertions.

## Verification

The accompanying `verify.py` independently constructs all twenty-seven vertex images of the linear projection of the product of three triangles, computes their four-dimensional convex hull, and compares the resulting volume against the analytical formula for 250 seeded random scale-and-rotation configurations. It also evaluates the predicted lower and upper extrema for four asymmetric/equal-scale triples, giving eight sharp endpoint checks. The numerical evidence is ancillary: the inequalities for the entire continuous parameter range follow from the preceding proof, not from enumeration.

## Relationship to prior work

Schneider's higher-order difference body measures precisely the common-translation feasibility body for repeated copies of one convex body. The higher-order Rogers–Shephard inequality, as discussed by Haddad, Langharst, Putterman, Roysdon and Ye, already implies the upper value \(15A^2\) when all three triangles coincide; that known endpoint is not presented as new. The present result treats three distinct, independently rotated and independently scaled equilateral templates, computes the full orientation-dependent four-dimensional volume, and classifies the sharp opposite-orientation minimum.

Kweon and Zhu develop algorithms for maximizing the *two-dimensional intersection area* of three translated polygons, a different functional from the measure of all translation pairs that allow any common intersection. Their polygon-translation framework motivates studying the size of the feasible set, but its maximum-overlap results do not directly determine this volume. The explicit weighted angle extremal classification is the contribution asserted here.

## Limitations

Only congruence-type equilateral triangles with arbitrary positive scales and orientation changes are covered; arbitrary triangular shapes, independent shape distortions, and four or more templates are not addressed. This is a self-review, not independent verification. The mixed-area identity is elementary and could occur implicitly in older translative integral-geometry literature; an unindexed formula or equivalent classification remains a historical-priority risk. A bibliographic search is not proof of global novelty.

## References

- H. J. Kweon and H. Zhu, *Maximum overlap area of a convex polyhedron and a convex polygon under translation*, arXiv:2301.02949 (first posted 2023-01-08), especially Section 5, https://arxiv.org/html/2301.02949v2.
- J. Haddad, D. Langharst, E. Putterman, M. Roysdon and D. Ye, *Affine Isoperimetric Inequalities for Higher-Order Projection and Centroid Bodies*, arXiv:2304.07859 (first posted 2023-04-16), particularly the higher-order difference-body definitions and Rogers–Shephard theorem, https://arxiv.org/abs/2304.07859.
- H. J. Kweon and H. Zhu, *Maximum Overlap Area of Several Convex Polygons Under Translations*, arXiv:2307.00409 (first posted 2023-07-01), https://arxiv.org/abs/2307.00409.
- R. Schneider, *Eine Verallgemeinerung des Differenzenkörpers* (1970), foundational higher-order difference-body result, as cited and discussed in arXiv:2304.07859.
