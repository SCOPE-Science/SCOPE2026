# Sharp integral second-homology onset for general-position complexes of cycle graphs

## Finding
For every integer \(n\ge 3\), let \(C_n\) be the unweighted cycle with vertices \(\mathbb Z/n\mathbb Z\), with its intrinsic shortest-path distance. Define \(\operatorname{GP}(C_n)\) as the abstract simplicial complex consisting of subsets \(S\) such that **no three distinct members of \(S\) lie on a single shortest path** between two cycle vertices. Then
\[
H_2(\operatorname{GP}(C_n);\mathbb Z)\ne0
\quad\Longleftrightarrow\quad
\bigl(n\text{ is odd and }n\ge9\bigr)
\ \text{or}\ \bigl(n\text{ is even and }n\ge12\bigr).
\]
Moreover, for every order in the nonvanishing range, a six-vertex octahedral-boundary subcomplex (not an induced subcomplex) supplies an explicitly oriented **primitive** integral second-homology class. This is a sharp existence classification, not a formula for the full Betti number or a homotopy equivalence.

## Assumptions and scope
All paths and distances are those of the original cycle. In particular, both shortest paths are considered in the even antipodal case. All homology is unreduced integral simplicial homology, and \(H_2\) is unchanged by reduction. For oriented simplices, \([a,b,c]\) has boundary \([b,c]-[a,c]+[a,b]\). The complex includes all pairs of distinct vertices and the empty simplex.

## Proof
**Step 1: Characterize the triangles and bound the dimension.** Let three cycle vertices be ordered around the circle, with positive integral cyclic gaps \((a,b,c)\) satisfying \(a+b+c=n\). The three vertices are in geodesic general position if and only if
\[
2a<n,\qquad2b<n,\qquad2c<n.
\]
Indeed, if \(a\ge n/2\), the complementary arc, of length \(b+c\le n/2\), is a shortest path between the endpoints of that gap and passes through the third selected vertex. Conversely, if each gap is strictly shorter than half the perimeter, then each circular arc containing all three selected vertices has length greater than half the perimeter; no shortest path can contain all three. Equality at a half-perimeter is forbidden because a tied geodesic exists.

No four distinct vertices form a face. To see this, write their four positive cyclic gaps as \((a,b,c,d)\). One of the complementary two-step arcs of lengths \(a+b\) and \(c+d\) has length at most \(n/2\), and contains three of the chosen vertices. That arc is geodesic. Hence \(\dim\operatorname{GP}(C_n)\le2\), and in particular the group of simplicial 2-boundaries is zero:
\[
B_2=\operatorname{im}(\partial_3)=0.
\]

**Step 2: Explicitly exhibit primitive spherical cycles in all claimed positive cases.** Assume \(n\) is odd with \(n\ge9\), or even with \(n\ge12\). Choose positive integers \((g_0,g_1,g_2)\) summing to \(n\) and differing by at most one (thus each is either \(\lfloor n/3\rfloor\) or \(\lceil n/3\rceil\)). In these ranges
\[
2\le g_i\qquad\text{and}\qquad g_i+1<n/2
\]
for all three indices (check the two smallest allowed orders directly; the inequality then grows monotonically within each parity). Put \(s_0=0\), \(s_1=g_0\), \(s_2=g_0+g_1\) modulo \(n\), and take three pairwise disjoint two-vertex blocks
\[
A_i=\{s_i,s_i+1\}\quad(i=0,1,2).
\]
For any binary choices \(e_i\in\{0,1\}\), the cyclic gaps among \(s_0+e_0,s_1+e_1,s_2+e_2\) are
\[
g_i+e_{i+1}-e_i\quad(i\bmod3),
\]
which lie between \(g_i-1\) and \(g_i+1\), and are strictly between zero and \(n/2\). Thus every one of the eight transversals \(A_0\times A_1\times A_2\) is a two-simplex. These are the facets of the octahedral sphere \(S^0*S^0*S^0\), realized as a subcomplex, with oriented fundamental cycle
\[
z_n=\sum_{(e_0,e_1,e_2)\in\{0,1\}^3}
(-1)^{e_0+e_1+e_2}
[s_0+e_0,s_1+e_1,s_2+e_2].
\]
Every edge occurs in exactly two terms with opposite boundary coefficients. Hence \(\partial_2 z_n=0\). There are no 3-simplices, so \([z_n]\ne0\) in integral \(H_2\). Since \(z_n\) has coefficient \(1\) on one triangle and \(B_2=0\), it is indivisible in \(H_2\), i.e. primitive. This proves the positive implication in all infinitely many claimed orders.

**Step 3: Vanishing at every excluded order.** The triangle-gap criterion reduces the remaining orders to the finite set \(n\in\{3,4,5,6,7,8,10\}\). Each permitted triangle has one of the following cyclic gap types (the order of gaps is irrelevant here):

| \(n\) | Allowed triangle gap types | Free-edge elimination |
|---|---|---|
| 3 | \((1,1,1)\) | Its three edges each occur once |
| 4 | None | No triangles |
| 5 | \((1,2,2)\) | Every length-one edge occurs in exactly one triangle |
| 6 | \((2,2,2)\) | Each length-two edge occurs in exactly one triangle |
| 7 | \((1,3,3),(2,2,3)\) | First remove \((1,3,3)\) triangles using unique length-one edges; then remove \((2,2,3)\) triangles using unique length-three edges |
| 8 | \((2,3,3)\) | Every length-two edge occurs in exactly one triangle |
| 10 | \((2,4,4),(3,3,4)\) | First remove \((2,4,4)\) triangles using unique length-two edges; then remove \((3,3,4)\) triangles using unique length-four edges |

For each row, these assertions follow directly by fixing the endpoints of the indicated edge in the cyclic gap characterization: there is exactly one compatible remaining vertex of the currently considered triangle type. Each listed operation is a genuine elementary simplicial collapse of one triangle along an edge contained in no other surviving triangle. In the two-phase cases, the second-phase unique edges have no cofaces after the first-phase removals. The resulting complex has dimension at most one. Such collapses preserve homology and a one-dimensional complex has \(H_2=0\). This exhausts every other order and finishes the proof.

## Verification
The independent standalone script `verify.py` builds triangles in two separate ways: it tests the geodesic betweenness equality directly using the cycle metric, and it applies the strictly-less-than-half cyclic-gap criterion. The two enumerations agree for all \(3\le n\le40\); no four-vertex face survives in these cases. A deterministic free-edge deletion replays all triangles at \(n=3,4,5,6,7,8,10\), and explicit balanced-gap octahedral cycles are tested for all admissible \(9\le n\le100\). Every directed boundary of each eight-triangle cycle vanishes over the integers. The self-contained proof, not those finite checks, supplies the universal quantifiers.

To reproduce: run `python3 verify.py` using only the standard library and compare the output byte-for-byte with `verification_expected.txt`.

## Relationship to prior work
Cody and Detore introduced a geodesic hypergraph framework and derived \(k,d\)-chromatic and perfection formulas for cycles (first public January 7, 2026). Their work gives the combinatorial context for general-position constraints but not this topological threshold or explicit integral octahedral classes. Chandran, Klavžar, and Tuite survey the general-position problem and its counting, graph-operation and coloring variants (first public January 31, 2025); the present question concerns homology of the simplicial complex of *all* admissible sets rather than the usual maximum-set cardinality. Related computations of general-position complexes of ladder graphs concern a distinct metric graph family. A published study of geodesic shattering on cycles concerns shattered supports, which are not the general-position face sets defined here.

## Limitations
No formula for the full rank of \(H_2\), for integral \(H_1\), for full homotopy type, or for symmetry representations is asserted. The octahedral boundary is a subcomplex, not an induced subcomplex, because all pairs of vertices are allowed as edges. An oriented octahedral cycle provides one primitive class, not necessarily an integral basis. The finite replay does not independently certify all orders; the infinite-range conclusion uses the symbolic argument. Exhaustive bibliographic priority, especially against unindexed formulations, cannot be guaranteed. Independent mathematical review remains outstanding.

## References
- Brent Cody and Rose Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351, first posted 2026-01-07, https://arxiv.org/abs/2601.04351 .
- Ullas Chandran S.V., Sandi Klavžar and James Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385, first posted 2025-01-31, https://arxiv.org/abs/2501.19385 .
- American Mathematical Society, MSC2020 `55U10`, simplicial sets and complexes in algebraic topology, https://mathscinet.ams.org/msc/msc2020.html?t=55U10 .
