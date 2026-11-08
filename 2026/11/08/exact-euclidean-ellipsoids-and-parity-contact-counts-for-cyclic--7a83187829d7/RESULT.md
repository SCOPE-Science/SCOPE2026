# Exact Euclidean ellipsoids and parity contact counts for cyclic edge-diamond sums

## Finding
For each integer \(n\ge3\), let \(e_1,\ldots,e_n\) be the standard Euclidean basis, let \(C_n\) have edges \(\{i,i+1\}\) with indices modulo \(n\), and put
\[
D_{ij}=\operatorname{conv}\{e_i,-e_i,e_j,-e_j\},\qquad
K_n=\sum_{\{i,j\}\in E(C_n)}D_{ij}\subset\mathbb R^n.
\]
The unique maximum-volume inscribed ellipsoid (John ellipsoid) of \(K_n\) is the ball \(r_n B_2^n\); the unique minimum-volume containing ellipsoid (Löwner ellipsoid) is \(R_nB_2^n\), where
\[
\boxed{r_n^2=\min\{n,4\},\qquad R_n^2=n+2\lfloor n/2\rfloor.}
\]
Both centers are the origin. Exactly \(T_n\) supporting facets touch the John ball, and exactly \(F_n\) vertices touch the Löwner ball, where
\[
\boxed{T_n=\begin{cases}2^n,&n=3,\\2n+2^n,&n=4,\\2n,&n\ge5,\end{cases}\qquad
F_n=\begin{cases}2^{n/2+1},&n\text{ even},\\n\,2^{(n+3)/2},&n\text{ odd}.\end{cases}}
\]
For \(n=3\), the John contacts have unit normals \((\pm1,\ldots,\pm1)/\sqrt n\); for \(n=4\), both these normals and the signed coordinate directions occur; for \(n\ge5\), precisely the \(2n\) signed coordinate directions occur. For even \(n\), Löwner contacts are vectors with \(n/2\) alternating entries equal to arbitrary \(\pm2\) and all other entries zero. For odd \(n\), they have \((n-1)/2\) pairwise nonadjacent positions with entries \(\pm2\), one additional entry \(\pm1\) at an endpoint of the sole edge uncovered by those positions, and all other entries zero.

## Assumptions and scope
All Minkowski sums use their indicated Euclidean coordinate realization, not an intrinsic metric on a different affine embedding. The cycle is simple, with \(n\ge3\); every edge diamond has weight exactly one. Balls and ellipsoids are measured in the ambient \(n\)-dimensional Euclidean metric. The words *touching facet* and *touching vertex* mean a facet or vertex that intersects the boundary of the corresponding extremal ball. All counts refer to geometrically distinct faces or points.

A more general exact structural reduction, used below, holds for arbitrary nonempty hyperedges \(I_\alpha\subset[n]\) covering all coordinates and positive real weights \(w_\alpha\). For \(K=\sum_\alpha w_\alpha\operatorname{conv}\{\pm e_i:i\in I_\alpha\}\), write \(W(S)=\sum_{\alpha:I_\alpha\cap S\ne\varnothing}w_\alpha\). Its centered inradius and circumradius satisfy
\[
 r(K)=\min_{\varnothing\ne S\subset[n]}\frac{W(S)}{\sqrt{|S|}},\qquad
 R(K)^2=\max_{\pi\in\mathfrak S_n}\sum_{i=1}^n\left(\sum_{\alpha:\,i\text{ last in }I_\alpha\text{ under }\pi}w_\alpha\right)^2.
\]
The first formula follows directly from the published subset inequalities (and is not advanced as a separate historical novelty claim); the second is an orientation/load reduction. Every support-minimizing unit direction has coordinates \(\sigma_i/\sqrt{|S|}\) on one minimizing subset \(S\), zero elsewhere, with arbitrary independent signs \(\sigma_i\in\{-1,1\}\).

## Proof
**1. Support and optimal interior directions.** For a unit vector \(u\), support additivity yields
\[
h_K(u)=\sum_\alpha w_\alpha\max_{i\in I_\alpha}|u_i|.
\]
Let \(a_i=|u_i|\). Order its distinct positive levels and express \(a\) as a positive linear combination \(a=\sum_j\delta_j\mathbf1_{S_j}\) of nested, nonempty superlevel indicators. The same layer-cake decomposition gives
\[
h_K(u)=\sum_j\delta_jW(S_j)\ \ge\ r_*\sum_j\delta_j\sqrt{|S_j|}\ \ge\ r_*\|a\|_2,
\quad r_*:=\min_{S\ne\varnothing}W(S)/\sqrt{|S|}.
\]
The last inequality is the Euclidean triangle inequality. Equality at a minimizing indicator \(a=\mathbf1_S/\sqrt{|S|}\) proves \(\min_{\|u\|_2=1}h_K(u)=r_*\). Because positive weights and coordinate coverage make \(r_*>0\), equality in the Euclidean triangle inequality forces all nonzero level indicators to be parallel. Nested distinct indicator vectors cannot be parallel; hence every minimizer has exactly one positive magnitude and a minimizing support \(S\). Coordinate signs do not affect the support. Central symmetry implies that the origin-centered ball of this radius is largest among all balls: any ball \(B(c,s)\subset K\) has its reflection \(B(-c,s)\subset K\), and averaging gives \(B(0,s)\subset K\).

For the cycle, a nonempty proper vertex subset \(S\) containing \(k\) vertices in \(c(S)\) consecutive cyclic components meets exactly \(k+c(S)\) edges. Thus
\[
\frac{W(S)}{\sqrt{|S|}}=\frac{k+c(S)}{\sqrt k}\ge\frac{k+1}{\sqrt k}\ge2,
\]
where the second equality case is only \(k=1\). The full set meets \(n\) edges and has ratio \(\sqrt n\). Hence the squared inradius and the exact minimizing normal orbits are those stated. Every corresponding support face is a facet: for a singleton its free summands are diamonds along a spanning path on the remaining vertices, giving affine dimension \(n-1\); for the full-set normals each edge contributes a signed segment, whose differences span the \((n-1)\)-space perpendicular to that normal because the cycle is connected. No other facets can touch the centered ball, since all minimizing normals have been classified.

**2. Circumradius via a maximum-load orientation.** Every vertex of a Minkowski sum comes from choices of summand vertices. For a hyperedge \(I_\alpha\), choose \(\sigma_\alpha w_\alpha e_{i_\alpha}\). Let \(d_i=\sum_{\alpha:i_\alpha=i}w_\alpha\), the *unsigned load* at \(i\). Then \(\|\sum_\alpha\sigma_\alpha w_\alpha e_{i_\alpha}\|_2^2\le\sum_i d_i^2\), with equality precisely when all summands assigned to each active coordinate have the same sign. Taking signs consistently shows that the maximum squared norm is the maximum of \(\sum_i d_i^2\) over assignments of each hyperedge to one of its coordinates.

If an optimal assignment gives hyperedge \(I_\alpha\) of weight \(w>0\) to \(i\) while \(j\in I_\alpha\setminus\{i\}\), moving it from \(i\) to \(j\) would change the sum of squared loads by \(2w(d_j-d_i+w)\). Maximality therefore gives \(d_i\ge d_j+w>d_j\). Sorting coordinates in increasing load produces a total order in which each hyperedge is assigned to its latest coordinate. Conversely each total order yields such an assignment. This proves the claimed general permutation formula.

For an unweighted simple cycle, each vertex receives \(0\), \(1\), or \(2\) assigned edges. Write \(t\) for the number of load-two vertices. No two such vertices can be adjacent, and \(\sum_i d_i=n\); therefore
\[
\sum_i d_i^2=n+2t\le n+2\lfloor n/2\rfloor.
\]
Alternating independent sets of size \(\lfloor n/2\rfloor\) attain equality. For even \(n\) there are exactly two such sets, all remaining loads are zero, and the independent signs on the \(n/2\) nonzero coordinates yield \(2\cdot2^{n/2}\) points. For odd \(n\) there are exactly \(n\) maximum independent sets, and each leaves a unique edge outside the set of load-two vertices. This edge has two possible assignments, producing one load-one coordinate. The \((n+1)/2\) nonzero coordinates have independent signs, giving \(n\cdot2\cdot2^{(n+1)/2}\) distinct points. Every such point is a vertex because the squared Euclidean norm is strictly convex, so a norm-maximizer cannot be a nontrivial convex combination of distinct points of \(K_n\). These constructions also prove all listed farthest-point patterns and counts. The origin is the unique circumcenter: for any fixed farthest point \(v\), the opposite pair \(v,-v\in K_n\) makes at least one squared distance from any nonzero center \(c\) no smaller than \(\|v\|_2^2+\|c\|_2^2\).

**3. Extremal ellipsoids.** Each summand and hence \(K_n\) is invariant under arbitrary independent coordinate sign changes, and the cycle is invariant under cyclic permutation of coordinates. A full-dimensional convex body has a unique maximum-volume inscribed ellipsoid and unique minimum-volume containing ellipsoid. Their centers and shape matrices must be invariant under this symmetry group. Invariance under every coordinate sign change forces the matrices to be diagonal; cyclic permutation forces all diagonal entries equal. Thus both ellipsoids are centered Euclidean balls. Their radii equal the inradius and circumradius already computed; the preceding support and vertex classifications give their exact facet and vertex contact numbers.

## Verification
The accompanying standalone `verify.py` uses integer and rational arithmetic only. It independently (i) enumerates the subset-coverage squared minima for cycles of orders \(3\) through \(12\); (ii) enumerates all signed edge-to-endpoint selections for orders \(3\) through \(8\), checking both farthest radii and numbers of distinct farthest vertices; (iii) enumerates edge endpoint loads for additional orders; (iv) checks the exact support inequality against a finite integer-normal grid; (v) checks many small weighted graphs and independent weighted-hyperedge examples. Running `python verify.py` prints `PASS total 288399 assertions including weighted hypergraph outer-radii`. These finite tests are corroboration; the exact theorem for every \(n\ge3\) is proved above.

## Relationship to prior work
Wang, Hou, Thawinrak, Liu and Dai (arXiv:2608.16037v1, first posted 2026-08-17) introduce these Minkowski sums of coordinate cross polytopes and prove a general subset-inequality description (their Proposition 3.5), as well as lattice-point and volume results. Their subset inequalities directly supply the first general inradius formula after applying Cauchy–Schwarz; that elementary implication is explicitly acknowledged rather than claimed as new. The new result here is the *complete Euclidean extremal-ellipsoid and contact classification* for the edge-diamond cyclic specialization, together with the maximum-load orientation analysis and exact parity-dependent farthest-vertex counts. The source's Sections 3–5 do not state these latter results.

Eur, Fink, Larson and Spink (arXiv:2209.06752; published 2024) and Thawinrak (arXiv:2512.01332) study volumes and lattice enumeration of more general type-B generalized permutohedra. Related Euclidean results for symmetric-edge graph polytopes concern different bodies, built as a convex hull of edge roots rather than a Minkowski sum of coordinate diamonds; their radii and contact counts do not imply those above. Results for graphical zonotopes likewise use sums of segments in zero-sum root directions, not edge-supported cross polytopes.

## Limitations
The theorem concerns the canonical Euclidean embedding and unit edge weights of a single cycle. The general hypergraph formulas reduce radius questions to finite subset and ordering optimization but do not give closed numerical evaluations for every hypergraph, nor classify all their ellipsoids. Historical completeness cannot be guaranteed from targeted literature searches. The result is mathematically proved and computationally corroborated but has not received independent expert audit.

## References
- H. Wang, Q. Hou, W. Thawinrak, Z. Liu, and Z. Dai, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037v1 (2026-08-17), https://arxiv.org/abs/2608.16037 .
- C. Eur, A. Fink, M. Larson, and H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752; Proc. London Math. Soc. 128 (2024), https://arxiv.org/abs/2209.06752 .
- W. Thawinrak, *Counting Lattice Points in Generalized Permutohedra From A to B*, arXiv:2512.01332 (2025-12-01), https://arxiv.org/abs/2512.01332 .
