# The Coxeter double cover as the optimum three-path-cover slide graph of the Heawood graph

## Finding
Let \(H\) be the Heawood graph, namely the point-line incidence graph of the seven-point Fano plane. Consider its minimum three-vertex-path covers, with two covers adjacent when one selected vertex is exchanged for an unselected neighbor in \(H\). The exact reconfiguration graph is
\[
\mathcal R_{\mathrm{slide}}(H)\cong 2K_1\sqcup (\operatorname{Cox}\times K_2),
\]
where \(\operatorname{Cox}\) is the twenty-eight-vertex Coxeter graph and \(\times\) denotes the categorical (Kronecker), *not* Cartesian, graph product. In fact the same graph is obtained when the replacement vertex may be anywhere in \(H\), not merely adjacent.

The minimum cover cardinality is seven. There are exactly fifty-eight optimum covers: two isolated configurations and a connected, cubic, fifty-six-vertex component with eighty-four edges. Every vertex in the mobile component has distance-shell vector
\[
(1,3,6,12,18,12,3,1),
\]
so its radius and diameter are both seven. The two isolated configurations have eccentricity zero in their singleton components; the whole disconnected reconfiguration graph has no finite global diameter under the usual convention.

## Assumptions and scope
The Fano plane has points \(P=\{0,1,\dots,6\}\) and lines \(\ell_i=\{i,i+1,i+3\}\) with all indices modulo seven, for \(0\le i\le6\). The graph \(H\) has fourteen vertices, comprising the seven points and seven lines; a point and line are adjacent exactly when incident. A three-path means three distinct consecutive vertices of a simple path, so a set \(C\subseteq V(H)\) is a three-path vertex cover if every such path meets \(C\). A legal move preserves both the cover property and cardinality seven. Vertex labels are fixed; graph products and components are interpreted as ordinary simple undirected graphs.

Define \(\mathcal T\) as the family of twenty-eight three-point subsets of \(P\) that are *not* Fano lines. For \(T\in\mathcal T\), let \(S(T)\) be its three side lines, each joining one of its three pairs. Define the two seven-vertex sets
\[
A_T=T\cup(\mathcal L\setminus S(T)),\qquad B_T=V(H)\setminus A_T=(P\setminus T)\cup S(T),
\]
where \(\mathcal L\) is the set of seven line-vertices. Also write \(P_*\) and \(\mathcal L_*\) for the pure point-side and pure line-side seven-vertex sets.

## Proof
**1. Covers are complements of dissociation sets.** The complement \(U=V(H)\setminus C\) contains no three-vertex path precisely when the induced graph \(H[U]\) has maximum degree at most one. Thus a minimum three-path cover is the complement of a maximum dissociation set.

**2. Maximum dissociation cardinality is seven.** Each bipartition class is a dissociation set of cardinality seven. If a dissociation set of size eight existed, Fano point-line duality lets us assume it selected at least four point-vertices. For five selected points only the unique line through their two omitted points has at most one selected incident point, so three further selected line-vertices are impossible. For six or seven selected points no line has at most one selected incident point. For four selected points, the point-set is either a quadrangle (complement of a Fano line), in which case only its complementary line has at most one selected point, or a line together with a fourth point, in which case precisely three lines have at most one selected point. Neither permits four selected line-vertices. Hence no eight-element dissociation set exists, and any larger one would contain one, establishing the maximum seven.

**3. Complete classification of optimum covers.** For a seven-element dissociation set, the possibilities of zero or seven selected points give \(\mathcal L_*\) and \(P_*\). With one selected point at most five lines can be selected; with two points at most four lines can be selected, because their common line is forbidden and at least one of the two other lines through each point must also be omitted. Fano duality excludes the mirrored counts. For three selected points and four lines, the points cannot lie on a Fano line: every other Fano line then meets their line in precisely one of its three points, and four selected such lines would repeat a point. If the three points form a noncollinear triangle \(T\), exactly its three side lines are forbidden, and the remaining four lines each meet \(T\) in at most one point; the four are therefore forced. This gives \(A_T\). The four-point/three-line case is the point-line dual and is exactly \(B_T\): the four points form a Fano line plus one external point, with three uniquely admissible selected line-vertices. Therefore the complete collection of maximum dissociation sets, and by complementation the complete collection of minimum covers, is
\[
\{P_*,\mathcal L_*\}\ \cup\ \{A_T,B_T:T\in\mathcal T\}.
\]
There are \(2+2\cdot28=58\) distinct sets. As complementation preserves the one-for-one replacement relation, the same enumeration describes the optimum covers without relabelling their configuration graph.

**4. One-replacement adjacency.** No one-vertex replacement connects two distinct sets of type \(A\): the four chosen lines uniquely determine the three excluded side lines, hence the original triangle. The same applies to type \(B\), and neither pure bipartition class has a legal replacement among the fifty-eight optima. To replace one vertex of \(A_T\) to obtain \(B_U\), one must add exactly one point. Since the point-sets are respectively \(T\) and \(P\setminus U\), this is possible only when \(T\cap U=\varnothing\). Conversely suppose \(T\cap U=\varnothing\). The three side lines of \(T\) and the three side lines of \(U\) are disjoint sets of lines: a three-point line cannot include two points from each disjoint triangle. Of the seven Fano lines, let \(q\) be the unique line belonging to neither side-line set. Then \(q\) meets each triangle in at most one point, so it contains the unique point \(x\in P\setminus(T\cup U)\). One has \(B_U=(A_T\setminus\{q\})\cup\{x\}\), and \(x\) and \(q\) are incident in \(H\). Thus every allowed one-vertex jump is already a one-edge slide, and
\[
A_T\sim B_U\quad\Longleftrightarrow\quad T\cap U=\varnothing.
\]
The standard Fano-triangle realization of the Coxeter graph has vertex-set \(\mathcal T\), with edges joining disjoint triangles. Duplicating each triangle into the \(A\)- and \(B\)-types and connecting only across types gives precisely \(\operatorname{Cox}\times K_2\). The pure states are two isolates, proving the asserted graph isomorphism and the equality of jump/slide graphs.

**5. Component metric.** The finite, fully specified graph on \(\mathcal T\times\{0,1\}\) was traversed exhaustively by breadth-first search. For each of its fifty-six roots the resulting ordered layer sizes are exactly \((1,3,6,12,18,12,3,1)\). The attached `verify_structure.py` constructs this graph from the stated Fano lines and checks all roots; `verify_independent.py` reconstructs the result independently using dot products of nonzero vectors in \(\mathbb F_2^3\), directly tests the three-path-cover condition, and checks all pairwise reconfiguration distances. Both terminate without third-party libraries. Since all fifty-six mobile vertices are visited from any root and layer seven is nonempty, the component is connected and self-centered with diameter seven. The degree count is three throughout, giving exactly \(56\cdot3/2=84\) edges.

## Verification
Run `python3 verify_structure.py` and `python3 verify_independent.py` beside this document. The first checks the twenty-eight noncollinear triples, all \(\binom{14}{8}=3003\) forbidden size-eight dissociation sets, all \(\binom{14}{7}=3432\) size-seven candidates, exact slide/jump adjacency and all fifty-six breadth-first-search layer vectors. The second uses a different point-line model and tests all sizes for the minimum three-path-cover cardinality, enumerates every optimum and reconstructs both move graphs directly. Both report fifty-eight optimum configurations, two isolates, one fifty-six-state cubic component, eighty-four edges and sharp mobile diameter seven. No probabilistic search, cutoff extrapolation or external graph database is used.

## Relationship to prior work
Hoang, Suzuki and Yagita introduced and analyzed three-path-cover reconfiguration in the broader framework of \(k\)-path vertex covers, including complexity classifications and constructive methods for paths and cycles [1]. Hoang subsequently studied token slides for such covers on caterpillars [2]. These results motivate the optimization-constrained question but do not state the Heawood configuration graph. The Fano-triangle presentation of the Coxeter graph and the existence of its canonical bipartite double graph are classical [3,4], and neither their vertex/edge counts nor the already known abstract Coxeter graph are claimed to be new. The subject of the present result is the specific realization of that double graph as the exact optimum-cover reconfiguration graph, including the two frozen covers and equality of sliding and jumping.

## Limitations
This is an exact classification for the single fourteen-vertex Heawood graph, not an all-cubic-graph theorem. The mobile-component diameter is distinct from any global diameter convention for a disconnected graph. The two verification scripts provide complete finite checks, while the preceding incidence argument supplies the structural proof. Although comparisons to the accessible literature did not uncover an equivalent optimum-cover realization, a previously unindexed formulation through dissociation sets, Fano antiflags, or cubic symmetric graph lifts remains possible.

## References
[1] D. A. Hoang, A. Suzuki, T. Yagita, *Reconfiguring k-Path Vertex Covers*, first public preprint 2019-11-08, https://arxiv.org/abs/1911.03026 (subsequent journal version 2022).

[2] D. A. Hoang, *TS-Reconfiguration of k-Path Vertex Covers in Caterpillars for k ≥ 4*, first public preprint 2022-03-22, https://arxiv.org/abs/2203.11667.

[3] *Coxeter graph*, construction as the disjointness graph of non-line Fano triples, https://mathworld.wolfram.com/CoxeterGraph.html and https://en.wikipedia.org/wiki/Coxeter_graph (background identification only).

[4] *Bipartite Double Graph*, https://mathworld.wolfram.com/BipartiteDoubleGraph.html (background graph-product definition only).
