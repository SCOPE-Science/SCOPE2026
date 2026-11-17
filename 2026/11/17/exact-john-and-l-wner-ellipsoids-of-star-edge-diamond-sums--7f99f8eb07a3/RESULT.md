# Exact John and Löwner ellipsoids of star edge-diamond sums

## Finding
For every integer \(m\ge 2\), take the standard orthonormal basis \(e_0,e_1,\ldots,e_m\) of \(\mathbb R^{m+1}\), and define the full-dimensional, centrally symmetric polytope
\[
P_m=\sum_{j=1}^{m}\operatorname{conv}\{e_0,-e_0,e_j,-e_j\}.
\]
Its unique maximum-volume contained ellipsoid (John ellipsoid) and unique minimum-volume containing ellipsoid (Löwner ellipsoid), in these **fixed Euclidean coordinates**, are respectively
\[
J_m=\left\{(z,x):\frac{z^2}{m(m-1)}+\sum_{j=1}^{m}x_j^2\le1\right\},
\qquad
L_m=\left\{(z,x):\frac{z^2}{m^2}+\frac1m\sum_{j=1}^{m}x_j^2\le1\right\}.
\]
Every one of the \(2m+2^{m+1}\) facets is tangent to \(J_m\). The complete set of tangencies consists of the \(2m\) points \(\pm e_j\), \(1\le j\le m\), and the \(2^{m+1}\) points
\[
\left((m-1)\sigma_0,\frac{\sigma_1}{m},\ldots,\frac{\sigma_m}{m}\right),\qquad \sigma_i\in\{-1,1\}.
\]
The polytope has exactly \(2\cdot3^m-2^m\) vertices. Of these, only \(2+2^m\) touch \(L_m\): the two poles \(\pm m e_0\) and the \(2^m\) leaf-sign corners \((0,\sigma_1,\ldots,\sigma_m)\). Their proportion tends to zero exponentially. The sharp ratio of the two ellipsoid volumes is
\[
\frac{\operatorname{vol}(L_m)}{\operatorname{vol}(J_m)}
=\frac{m^{(m+1)/2}}{\sqrt{m-1}}.
\]

## Assumptions and scope
All sums are Minkowski sums and all distances/ellipsoids use the ordinary Euclidean structure, not a lattice-normalized metric. The coordinates are \((z,x_1,\ldots,x_m)\). John and Löwner refer to **unrestricted** ellipsoids, including possible translations and tilted axes, rather than just ellipsoids constrained to the coordinate axes. The theorem covers every integer \(m\ge2\). At \(m=1\), the body is a two-dimensional diamond, with John disk of radius \(1/\sqrt2\), Löwner disk of radius \(1\), and four contact points for each.

## Proof
**1. Exact halfspace description.** A vector from the \(j\)-th summand has form \(a_j e_0+b_j e_j\) with \(|a_j|+|b_j|\le1\). Hence \(|x_j|\le1\) and \(|z|\le\sum_j(1-|x_j|)=m-\sum_j|x_j|\). Conversely, when \(|x_j|\le1\) and \(|z|\le m-\sum_j|x_j|\), choose \(b_j=x_j\) and numbers \(a_j\in[-(1-|x_j|),1-|x_j|]\) with \(\sum a_j=z\), possible because their sum interval is exactly \([-(m-\sum|x_j|),m-\sum|x_j|]\). Thus
\[
P_m=\{(z,x):|x_j|\le1\ (1\le j\le m),\quad |z|+\sum_j|x_j|\le m\}.
\]
In particular, the facet inequalities are \(\pm x_j\le1\) and \(\sum_{i=0}^m\sigma_i x_i\le m\) for \(\sigma\in\{-1,1\}^{m+1}\), taking \(x_0=z\). All are genuine, distinct facets for \(m\ge2\): each coordinate slab has points of relative interior where the sum inequality is strict, and each signed sum hyperplane has a relatively open positive-orthant patch with all \(|x_j|<1\). Hence the count is \(2m+2^{m+1}\).

**2. Reduction to diagonal centered ellipsoids.** The body is invariant under independent sign reversals of every coordinate and under all permutations of the leaf coordinates. Existence and uniqueness of unrestricted John and Löwner ellipsoids of a full-dimensional convex body imply that each optimal ellipsoid has the same symmetries; its center is zero and its squared semiaxes are \(a^2\) on \(z\) and \(b^2\) on each leaf coordinate. Their volume is \(\kappa_{m+1}ab^m\), where \(\kappa_{m+1}\) is the unit-ball volume.

**3. John ellipsoid.** For a centered axis-symmetric ellipsoid, containment in each leaf slab is exactly \(b\le1\). Containment in every signed-sum halfspace is exactly \(a^2+mb^2\le m^2\), by the Euclidean support function of an ellipsoid. Thus maximizing its volume reduces to maximizing
\[
f(b)=b^m\sqrt{m^2-mb^2},\qquad0<b\le1.
\]
Its logarithmic derivative has the sign of \(m^2-(m+1)b^2\). For every integer \(m\ge2\) this is strictly positive on \((0,1]\), because \(m^2>m+1\). Therefore \(b=1\) and \(a^2=m(m-1)\). Equality of the corresponding support functions at each facet gives the listed tangencies: \(\pm e_j\) at slab facets, and, at each signed-sum facet, the unique point \((a^2\sigma_0/m,b^2\sigma_1/m,\ldots,b^2\sigma_m/m)\). No other facets exist, so this list is complete. Each tangent point is distinct.

**4. Vertex census.** Fix the signs of all coordinates. In the corresponding closed orthant, \(P_m\) is the region \(0\le y_j\le1\), \(0\le w\le m-\sum_j y_j\), where \(w=|z|\), \(y_j=|x_j|\). This is the convex hull of points with all \(y_j\in\{0,1\}\) and \(w\in\{0,m-\sum y_j\}\). Those with \(w=0\) and fewer than \(m\) unit leaves lie on the segment joining the corresponding two opposite-pole points. Thus every vertex must be of the form
\[
(z,x)=\bigl(\pm(m-k),\text{exactly }k\text{ leaf coordinates }\pm1,\text{ others }0\bigr),
\quad 0\le k<m,
\]
or \(z=0\) and all \(m\) leaf coordinates independently equal \(\pm1\). Every listed point is indeed exposed: choose a linear functional with leaf coefficients of magnitude strictly greater than the central coefficient on the selected leaves and strictly smaller on the unselected leaves, with independently chosen signs. This yields the exact count \(2\sum_{k=0}^{m-1}\binom mk2^k+2^m=2\cdot3^m-2^m\).

**5. Löwner ellipsoid.** Any centered invariant enclosing ellipsoid with semiaxes \(A,B\) must contain the poles \(\pm m e_0\) and all leaf-sign corners; hence \(A\ge m\) and \(B\ge\sqrt m\). The candidate \(A=m\), \(B=\sqrt m\) contains every listed vertex: on the orbit with \(k\) unit leaves its squared ellipsoid gauge is
\[
\frac{(m-k)^2}{m^2}+\frac{k}{m}
=1-\frac{k(m-k)}{m^2}\le1.
\]
It therefore contains the entire polytope and has the least permitted volume. Equality occurs exactly for \(k=0\) and \(k=m\), establishing the listed contact vertices and screening of all intermediate orbits. Uniqueness of the unrestricted Löwner ellipsoid completes the proof. The stated ratio and exponential sparsity follow by direct division of the semiaxis products and the vertex counts.

## Verification
The standalone file `star_edge_diamond_verify.py` (standard Python 3 only) checks, using exact rational arithmetic, the full proposed vertex lists, their facet constraints, all outer ellipsoid gauges and equality conditions, all inner supporting hyperplanes, and contact counts for \(1\le m\le8\). Run `python star_edge_diamond_verify.py`. These are independently replayable finite checks, not a substitute for the preceding arbitrary-dimensional proof.

## Relationship to prior work
Wang, Hou, Thawinrak, Liu and Dai (2026), arXiv:2608.16037, introduce and investigate Minkowski sums of coordinate cross-polytopes, including the general graph-indexed construction and halfspace descriptions. Their Proposition 3.5 already supplies general inequality representations; its specialization here is not claimed as novel. Their results concern Ehrhart enumeration, lattice volumes, support-enumerators and related questions, rather than the two unrestricted extremal ellipsoids or their entire contact sets. The classical uniqueness and optimality principles for John and Löwner ellipsoids are also prior mathematical tools.

Related published work on **cycle-indexed** edge-diamond sums treats a different graph geometry and obtains round extremal ellipsoids; it does not specialize to the star-indexed anisotropic result. A result on minimum enclosing **Euclidean balls** of complete-multipartite edge-diamond sums includes the star as a graph instance, but a minimum sphere does not determine the minimum-volume ellipsoid or its contact set; the outer sphere itself is not claimed new. Star PQ-adjacency polytopes are different polytopes. No equivalent complete star ellipsoid statement was located in the checked mathematical records, but that absence does not prove absolute historical priority.

## Limitations
The formula applies to unweighted unit coordinate diamonds sharing one axis and does not assert a classification for arbitrary graphs or unequal weights. The results are exact in the specified Euclidean embedding; arbitrary affine changes alter the displayed semiaxes. The claim has not received independent external audit. A differently named earlier theorem on diagonally clipped cross-polytopes could cover this same body; this remains a historical priority risk.

## References
1. H. Wang, Q. Hou, W. Thawinrak, Z. Liu and Z. Dai, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037, first posted 2026-08-17, https://arxiv.org/abs/2608.16037.
2. F. John, *Extremum problems with inequalities as subsidiary conditions*, in Studies and Essays Presented to R. Courant on his 60th Birthday (1948), 187–204; classical existence, uniqueness and contact conditions for extremal ellipsoids.
