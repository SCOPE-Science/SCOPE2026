# Four disconnected circles of largest four-simplices in the orthogonal square–pentagon free sum

## Finding

Let \(A_i=(\cos(i\pi/2),\sin(i\pi/2),0,0)\), \(i=0,1,2,3\), and \(B_j=(0,0,\cos(2\pi j/5),\sin(2\pi j/5))\), \(j=0,1,2,3,4\), and put \(P=\operatorname{conv}\{A_i,B_j\}\subset\mathbb R^4\). Every largest-volume four-simplex contained in \(P\), **with its vertices allowed anywhere in \(P\)**, is exactly of the following form:

Choose one of the four adjacent square-vertex pairs \(\{A_i,A_{i+1}\}\) (indices modulo four). Choose a cyclically maximal-area triangle of the pentagon \(\operatorname{conv}\{B_j\}\). The latter is either one of the five triangles with vertex sets \(\{B_j,B_{j+1},B_{j+3}\}\) (indices modulo five), or a triangle obtained by holding two of these pentagon vertices fixed and sliding the third along a single pentagon edge joining two such maximal triples. Take the convex hull of these two square vertices and the three pentagon points. **There are no other maximizing four-simplices**.

For each fixed square pair, the five vertex triangles and the five one-parameter sliding families form a topological circle, combinatorially a five-cycle. The full space of *unordered* maximizing four-simplices (with the Hausdorff topology on their vertex sets) is the **disjoint union of four circles**, with 20 vertex-supported points and 20 open one-dimensional sliding strata. No maximizing simplex has two independently moving vertices, and no optimizing square vertex can move. The sharp maximum volume, already known in the vertex-supported case, is

\[
M=\frac{\sin(2\pi/5)+2\sin(\pi/5)}{24}=\frac{\sqrt5}{20}\operatorname{vol}_4(P).
\]

The **new assertion is the complete all-points equality classification and topology**; neither the sharp numerical maximum nor the 20 vertex-supported cases is asserted as new.

## Assumptions and scope

The Euclidean coordinates above specify the unique unit-sphere nine-vertex maximum-volume four-polytope up to isometry, established by Medgyes (2026). A contained four-simplex means the convex hull of five affinely independent points of \(P\), not necessarily vertices of \(P\). Equality configurations are compared as *unordered sets* of five simplex vertices, with no artificial labels or vertex ordering. The five-cycle is topological, not an embedded round circle. The statement is confined to this particular polytope.

Write \(s=\sin(2\pi/5)\) and \(t=\sin(\pi/5)\), so that \(t/s=(\sqrt5-1)/2\); note \(s+2t>2s>2s-t>2t>0\).

## Proof

**1. Determinant maximum and strict vertex pattern.** For square-plane points \(a_1,a_2\) and pentagon-plane points \(b_1,b_2,b_3\), the four-dimensional simplex volume is exactly
\[
\frac{1}{24}|\det_2(a_1,a_2)|\,|\det_2(b_2-b_1,b_3-b_1)|.
\]
This follows by subtracting one vertex in the standard augmented affine determinant and expanding by the two orthogonal coordinate blocks. For three square and two pentagon vertices the analogous determinant is the double area of the square triangle times the determinant of the two pentagon vectors. The four square triangles have double area \(2\), square-pair determinants have magnitude \(1\) precisely for adjacent pairs and \(0\) for opposite pairs. The ten pentagon vertex triangles have two possible double areas: \(s+2t\) for the five cyclic \((1,2,2)\) triples and \(2s-t\) for the five cyclic \((1,1,3)\) triples. Every pentagon pair has absolute determinant \(s\) or \(t\). Other distributions of five original vertices span dimension at most three. Because \(s+2t>2s\), the unique maximum determinant magnitude \(s+2t\) among all vertex quintuples comes from **exactly two adjacent square vertices and one of the five specified pentagon triples**. Its volume is \(M=(s+2t)/24\), agreeing with the previously established maximum and 20 vertex-supported equality configurations.

**2. Equality-support principle for arbitrary points.** Let \(x_1,\ldots,x_5\in P\) be arbitrary and write each as a convex combination of the nine original polytope vertices, using only strictly positive coefficients on its chosen support. The oriented augmented determinant \(D(x_1,\ldots,x_5)\) is affine in each argument. Expanding all five convex combinations therefore expresses it as a convex average of oriented determinants of vertex quintuples. Every such determinant lies in \([-24M,24M]\). Equality \(|D|=24M\) holds **only if every combination of vertices in the Cartesian product of the five supports has determinant equal to the same endpoint \(+24M\) or \(-24M\)**: an average of bounded reals can attain an extreme only when every positive-weight summand does. In particular, all combinations have two square vertices and three pentagon vertices. If any one support contained both a square vertex and a pentagon vertex, fixing arbitrary members of the other four supports would give two combinations with different square-vertex counts, a contradiction. Thus (after relabeling) precisely two of the points lie in the square plane and three in the pentagon plane. The strict pattern in Step 1 makes this conclusion invariant under all choices of representations.

**3. Square rigidity.** For \(a,a'\) in the filled unit square \(Q=\operatorname{conv}\{(1,0),(0,1),(-1,0),(0,-1)\}\),
\[
|\det_2(a,a')|\le\|a\|_2\|a'\|_2\le1.
\]
Every nonvertex point of \(Q\) has Euclidean norm strictly less than one, because its four extreme points lie on the strictly convex Euclidean unit circle. Equality therefore forces both points to be vertices of the square, and their perpendicularity forces an adjacent pair. Since the pentagon triangle double area is at most \(s+2t\), saturation of the four-dimensional product in Step 1 forces saturation in both factors; the square pair is fixed at an adjacent vertex pair.

**4. Exact equality classification in the pentagon.** Label the five pentagon vertices cyclically by \(0,1,2,3,4\). Every maximal oriented *vertex* triangle has underlying unordered triple
\[
T_j=\{j,j+1,j+3\},\qquad j\in\mathbb Z/5\mathbb Z,
\]
by the strict two-level triangle-area comparison in Step 1. Each \(T_j\) intersects exactly two other \(T_k\) in two vertices; the two respective third vertices are consecutive on the pentagon. The resulting five-vertex incidence graph is \(C_5\). Conversely, when two maximal vertex triples share two vertices, moving the third along the edge joining their distinct third vertices preserves oriented area by affine dependence and equal signed endpoint area. These five edge segments are therefore all families of maximum-area pentagon triangles.

To prove *exhaustiveness*, write each point of an arbitrary maximum-area pentagon triangle as a convex combination of pentagon vertices with positive support. Its oriented area is again the convex average of the corresponding ordered vertex triangle areas, so every triple in the Cartesian product of the three supports must have maximal **same-signed** area. If two points had supports containing two or more vertices, then fixing the third support choice would produce at least four distinct maximum-area vertex triangles containing the fixed third pentagon vertex. But the list \(T_j\) shows each pentagon vertex belongs to only three maximum-area vertex triples. This is impossible. Hence at most one point has non-singleton support. With the other two fixed vertices, at most two pentagon vertices can be maximal third vertices; if there are two, they are adjacent in the original pentagon. Accordingly the moving point lies on exactly that edge. This proves that the five line segments described above, including their endpoints, are the complete maximum-triangle family.

**5. Moduli topology.** There are precisely four square choices. For each, Step 4 gives exactly five isolated endpoint triples joined by five nondegenerate line segments in a pentagonal cycle. Their interiors are disjoint because only one point can be mobile, and families have distinct fixed vertex pairs; different square choices cannot meet by Step 3. Therefore the unordered maximizer space is homeomorphic to the disjoint union \(S^1\sqcup S^1\sqcup S^1\sqcup S^1\), with four five-cycle components and 20 one-dimensional open strata. The unlabelled formulation also shows there are no further permutation multiplicities.

## Verification

Run `python3 verify.py` alongside this document (Python standard library only). The checker works in the exact algebraic field \(\mathbb Q(\sqrt5)\), using oriented trigonometric determinant coefficients and a rational square comparison; no floating-point approximations are used. It checks all \(\binom95=126\) vertex simplices and their determinant spectrum, the five maximum pentagon triangles, and **all \(31^3\) nonempty triples of vertex-support subsets**, proving that only singleton supports or one two-vertex edge support yield the maximal oriented triangle. It independently checks that the equality graph is a connected five-cycle for each square choice, hence four cycles in all. The infinite classification rests on the affine-support and strict-convexity proof above; the finite checker verifies its exhaustive combinatorial premise.

## Relationship to prior work

Medgyes (arXiv:2611.10078v1, 6 November 2026) establishes the extremal nine-vertex polytope and its volume, **not** the maximizing contained-simplex locus. A previously published complete five-level spectrum of the 126 vertex-supported four-simplices gives the sharp maximum and its twenty vertex realizations; its text **explicitly declines to classify non-vertex-supported maximizers**. Those numerical and vertex-classification statements are treated as prior results, rather than reintroduced as novelty. The 2017 solution of Arhimede Mathematical Journal, Problem E–45 (pp. 136–137), notes the nonunique maximal-area inscribed triangle of a regular pentagon and exhibits moving vertices along pentagon edges; this planar phenomenon is also treated as prior. The new claim is the full arbitrary-point equality *rigidity, exclusion of mixed and simultaneous motions, and four-component moduli topology* for the four-dimensional square–pentagon free sum, which is not stated or implied by any of the inspected sources alone. A related already recorded ten-vertex orthogonal double-pentagon simplex classification has a different, connected trivalent equality structure; it does not imply this nine-vertex four-component classification.

## Limitations

This is an equality-case classification for the unique extremal nine-vertex polytope, not for all nine-vertex polytopes or all orthogonal polygonal sums. The numerical maximum, maximal-area pentagon triangle family, and twenty vertex-supported maximizers predate this work. Prior literature could contain an unindexed or implicit classification of the entire four-dimensional equality locus; historical priority is provisional. The proof is elementary and does not yield a quantitative near-optimal stability theorem or a general formula for other polygon orders.

## References

- C. Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1, first submitted 2026-11-06. https://arxiv.org/html/2611.10078v1
- *The five-level four-simplex spectrum of the extremal nine-vertex four-polytope*, published mathematical record, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-five-level-four-simplex-spectrum-of-the-extremal-nine-vertex--8fd04d9c4b23
- A. Espuny Díaz, solution to Problem E–45, *Arhimede Mathematical Journal* 4 (2017), no. 2, pp. 136–137. https://amj-math.com/wp-content/uploads/2018/02/AMJ2017-vol4iss2.pdf
