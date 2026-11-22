# Uniform first-order recovery of affine planes from minimum-domination shattering

## Finding
Let \(\Pi\) be any finite affine plane of order \(q\ge2\), not necessarily Desarguesian, and let \(G(\Pi)\) be its bipartite point–line incidence graph. The minimum ordinary vertex-dominating sets are exactly the \(q(q+1)\) sets comprising the \(q\) point vertices of one affine line together with the other \(q-1\) line vertices in its parallel class. In particular, the domination number is \(2q-1\).

Regarding these optimum sets as Boolean concepts queried by vertex membership, their shattered-support polynomial is
\[
\Phi_q(z)=\begin{cases}
1+10z+6z^2,&q=2,\\
1+(2q^2+q)z+\frac{q(q^2-1)(3q+1)}{2}z^2,&q\ge3.
\end{cases}
\]
Both VC and Littlestone dimensions are exactly two. Let \(R(x,y)\) mean that the pair of distinct vertices \(x,y\) is shattered. For every \(q\ge3\), this one-relation graph **uniformly first-order reconstructs** the point sort, the line sort, and the original incidence relation (and hence parallelism), without knowing the order or having the original bipartition marked. Its automorphism group is exactly the collineation group of \(\Pi\). At order two, the shattering graph is \(K_4\sqcup6K_1\), and incidence cannot be recovered invariantly from that graph.

## Assumptions and scope
A finite affine plane of order \(q\) has \(q^2\) points and \(q(q+1)\) lines; each line has \(q\) points, each point lies on \(q+1\) lines, two points lie on a unique common line, and the lines split into \(q+1\) parallel classes containing \(q\) lines each. Ordinary domination uses closed neighborhoods: a selected vertex covers itself and its neighbors. A set \(S\) of query vertices is shattered when every Boolean labeling of \(S\) occurs as the membership trace of some minimum dominating set. The shattering polynomial counts shattered supports by size. Littlestone dimension is the greatest depth of a complete binary decision tree of vertex-membership queries realized at all leaves. The graph with relation \(R\) has no loops. An automorphism of an affine plane means an incidence-preserving permutation of its point and line sorts; no dualities interchanging sorts are permitted. No assertion is made for infinite affine planes or incidence structures not satisfying the affine-plane axioms.

## Proof
**1. All optimum sets.** Write \(p\) for the number of selected point vertices and \(\ell\) for the number of selected line vertices of an arbitrary dominating set. Covering the \(q(q+1)\) line vertices and the \(q^2\) point vertices gives, respectively,
\[
p(q+1)+\ell\ge q(q+1),\qquad p+q\ell\ge q^2.
\]
For any line \(L\), select its \(q\) points and the \(q-1\) *other* lines parallel to \(L\). Every point is either on \(L\) or on one of those selected lines; every line either meets \(L\), and thus a selected point, or is parallel to \(L\), and thus is selected. So \(2q-1\) selected vertices suffice. Conversely, if \(p+\ell\le2q-1\), substituting \(\ell\le2q-1-p\) in the two inequalities yields \(p\ge q\) and \(p\le q\), hence \(p=q\) and \(\ell=q-1\). The second inequality is then an equality. Consequently the chosen \(q-1\) lines must be pairwise disjoint and contain no chosen point, since otherwise the union of them with the \(q\) chosen points has fewer than \(q^2\) points. The chosen lines are parallel; their complement in the plane is the one remaining line of that parallel class, and its points are precisely the chosen \(q\) points. This proves optimality, uniqueness of the displayed form, and the count \(q(q+1)\), for every affine plane.

Call the optimum set indexed by an omitted line \(L\) the concept \(D_L\). Its selected point vertices are the points on \(L\), and its selected line vertices are all other members of the parallel class of \(L\).

**2. Exactly which pairs are shattered.** Two distinct point queries are always shattered: both are positive in the unique concept associated with their joining line; either one alone is positive for any other line through that point; and a line through neither point supplies two negative answers. The latter exists because at least \(q^2-q-1\ge1\) lines avoid both points.

For a point \(p\) and line \(M\), if they are incident, simultaneous positive answers are impossible: a concept selecting \(p\) omits a line through \(p\); if it is parallel to \(M\), that omitted line must be \(M\) itself. If they are nonincident, the traces with both positive, only the point positive, and both negative are always attainable. The remaining trace, only the line positive, requires an omitted line parallel to \(M\) other than \(M\) and the unique line of that class through \(p\). It exists if and only if \(q\ge3\). Thus the nonincident point–line pairs, and only those, are shattered for \(q\ge3\).

For two distinct line queries, nonparallel lines cannot both be positive. For parallel lines, either one alone is positive by omitting the other, and both are negative by omitting a line in another class. Both are positive precisely when a third line exists in their common parallel class, i.e. when \(q\ge3\). Hence parallel pairs are shattered exactly at orders at least three.

No triple is shattered. If three points have a fully positive trace, they lie on a common line; then the trace with exactly two positive is impossible by uniqueness of the line through two points. In a triple of two points and one line, the two positive points uniquely determine the concept, preventing both possible values at the line query. In a triple of one point and two lines, different-direction line queries can never both be positive; for parallel line queries, realizing the two labelings with the point positive and exactly one of the lines positive would require the point to lie on both disjoint omitted lines. For three line queries, any two in different parallel classes cannot both be positive, while in a single parallel class at most one of the three is negative. Thus every triple fails some trace. Heredity excludes all larger supports. The vertex count is \(2q^2+q\). Counting all pairs of points, all nonincident point–line pairs, and all parallel pairs of lines gives for \(q\ge3\)
\[
\binom{q^2}{2}+q^2(q^2-1)+(q+1)\binom q2
=\frac{q(q^2-1)(3q+1)}2.
\]
For \(q=2\), only the six pairs of the four point vertices are shattered. This proves the polynomial and \(\operatorname{VCdim}=2\).

**3. Online dimension.** Restrict the concept class to concepts answering positively at any given *point* vertex \(p\). The concepts are exactly \(D_L\) for the \(q+1\) lines \(L\) through \(p\). At every later query vertex, at most one of these concepts answers positively, unless that query is the already fixed point. Hence every genuine split has a singleton child, so this restriction has Littlestone dimension at most one. If the first positive query is a *line* vertex \(M\), the compatible concepts are the \(q-1\) omitted lines in the parallel class of \(M\) distinct from \(M\). At any further query, either the answer is fixed or one child has at most one concept: a point query has at most one positive candidate; a line query in the same class has at most one negative candidate. Therefore the positive child of *any* informative root query has Littlestone dimension at most one, excluding a depth-three complete tree. Since a shattered pair gives a depth-two complete tree, \(\operatorname{Ldim}=2\) for all orders.

**4. Uniform first-order interpretation and boundary.** For distinct vertices, \(R\) is exactly: point–point always, point–line precisely when nonincident, and line–line precisely when parallel, for \(q\ge3\). In the single-language graph \((V,R)\), define
\[
\operatorname{Point}(x):\quad
\forall y\,\forall z\,\Big(
[y\ne z\land y\ne x\land z\ne x\land\neg R(x,y)\land\neg R(x,z)]
\longrightarrow\neg R(y,z)\Big).
\]
For a point \(x\), the distinct nonneighbors are exactly the \(q+1\) lines through \(x\), lying in different parallel classes, and therefore pairwise nonadjacent in \(R\). For a line \(x\), any two of its \(q\ge2\) point vertices are nonneighbors of \(x\), but adjacent to each other. Thus the formula defines exactly the point sort, uniformly in \(q\); its negation defines the line sort. For \(q\ge3\), the original incidence relation is then
\[
\operatorname{Inc}(p,L):\quad
\operatorname{Point}(p)\land\neg\operatorname{Point}(L)\land\neg R(p,L).
\]
Two reconstructed line vertices are parallel precisely when they coincide or are adjacent in \(R\). Conversely, \(R\) is definable without parameters from the sorted affine-plane incidence relation: its edges are all point pairs, nonincident point–line pairs, and distinct parallel line pairs. Hence the interpretation recovers the affine plane up to a unique sort-preserving isomorphism and \(\operatorname{Aut}(V,R)\cong\operatorname{Aut}(\Pi)\) for \(q\ge3\).

At \(q=2\), the \(R\)-graph has its four point vertices forming \(K_4\) and all six line vertices isolated. The point sort remains definable by the displayed formula, but any permutation of the six line vertices is a graph automorphism, whereas only some preserve incidence. Thus incidence is not parameter-free definable from \(R\) at order two, and \(\operatorname{Aut}(V,R)\cong S_4\times S_6\).

**5. Topology.** Since there are no shattered supports of size three, the shattered-support complex is the one-dimensional complex of the graph \(R\). For \(q\ge3\), the point vertices form a clique and every line vertex is adjacent to at least one point, so it is connected, and its reduced integral homology is concentrated in degree one, freely of rank
\[
\beta_1=|E(R)|-|V(R)|+1=\frac{(q+1)(3q^3-2q^2-5q+2)}2.
\]
It is homotopy equivalent to a wedge of \(\beta_1\) circles. At order two the complex is the disjoint union of a graph \(K_4\) and six isolated vertices, with \(\widetilde H_0\cong\mathbb Z^6\), \(H_1\cong\mathbb Z^3\), and no other reduced homology.

## Verification
Standalone Python (`verify.py`) reconstructs the Desarguesian affine planes of orders \(2,3,4,5\), including the extension-field order four, checks every concept, all supports of sizes zero to three, the defining first-order formula, the incidence reconstruction and Euler homology ranks, and exhaustively enumerates all minimum dominating sets at orders two and three. It runs the exact online-dimension recurrence at orders two and three; higher-order online bounds are proved, not computationally certified. Independently written C++17 (`verify.cpp`) reconstructs prime-field planes of orders \(2,3,5,7\), separately enumerates all supports through size three, verifies point-sort and incidence reconstruction, and exhaustively checks all minimum dominating sets for orders two and three. Both implementations agreed on their overlapping orders. The logs `python.out` and `cpp.out` are reproducible recorded outputs. Experiments on Desarguesian examples do not prove assertions for arbitrary affine planes: the incidence-axiom arguments above do.

## Relationship to prior work
Spiro, Adriaensen and Mattheus (first public 2022-11-25) study *edge* domination of incidence graphs through incidence-free configurations; their edge-covering parameter does not determine ordinary minimum **vertex** dominating sets or the graph of shattered query pairs. Héger and Nagy (2016) study ordinary dominating sets in the *projective*-plane incidence graph and use affine blocking arguments as supporting context; their projective theorem does not entail the present finite-affine-plane interpretation. Earlier analysis of total and paired domination on affine point–hyperplane incidence graphs determines different domination invariants and does not enumerate the ordinary optimum concepts. Work on unions of two nonparallel lines studies their direct point-membership concept class, rather than optimum vertex sets of an incidence graph. The specific contribution here is the uniform first-order reconstruction of arbitrary affine planes from the pair-shattering relation of minimum ordinary dominating sets, together with its precise order-two obstruction and complete learning/topological classification. The comparisons do not prove absolute historical priority.

## Limitations
The theorem assumes a finite affine plane exists and does not posit existence of planes of arbitrary orders. It does not establish an analogous interpretation for projective planes, other finite incidence designs, or ordinary domination in higher-dimensional affine spaces. The exact optimum domination number may be known independently; it is not claimed new in isolation. Full text of every possible older source has not been exhausted, and an unindexed result under equivalent finite-model-theoretic terminology is a historical-priority risk. Mathematical review is not independent. Source programs check finite coordinatized planes only, with the unrestricted assertion proved deductively.

## References
1. S. Spiro, S. Adriaensen, S. Mattheus, “Incidence-free sets and edge domination in incidence graphs,” arXiv:2211.14339 (first public November 25, 2022); *Journal of Combinatorial Designs* 32 (2024), 55–87. https://arxiv.org/abs/2211.14339 ; https://doi.org/10.1002/jcd.21925.
2. T. Héger and Z. L. Nagy, “Dominating sets in projective planes,” arXiv:1603.02933 (2016). https://arxiv.org/abs/1603.02933.
3. “Exact total and paired domination gaps in affine point–hyperplane incidence graphs,” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-total-and-paired-domination-gaps-in-affine-point-hyperplan--19f2e2cbf72d (full result inspected).
4. “Sharp online shattering for unions of two nonparallel lines in finite affine planes,” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-online-shattering-for-unions-of-two-nonparallel-lines-in-f--0156eb59f663 (full result inspected).
