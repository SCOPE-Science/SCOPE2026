# Universal-apex transfer for geodesic general-position complexes

## Finding
For each integer \(m\ge2\), let \(H_1,\ldots,H_m\) be nonempty connected finite simple triangle-free graphs on disjoint vertex sets. Add one vertex adjacent to every vertex of their disjoint union and denote the resulting graph by \(G=K_1\vee(H_1\sqcup\cdots\sqcup H_m)\). Define the **geodesic general-position complex** \(\operatorname{GP}(G)\) to have as faces exactly the vertex subsets containing no three distinct vertices on one shortest path of \(G\).

Define \(D_2(H)\) as the simplicial complex of subsets \(U\subseteq V(H)\) for which the induced subgraph \(H[U]\) has maximum degree at most one. Let \(b_i=|E(H_i)|-|V(H_i)|+1\), the ordinary cycle rank of the connected graph \(H_i\). Then there is an integral homotopy equivalence
\[
|\operatorname{GP}(G)|\simeq
|D_2(H_1)*\cdots*D_2(H_m)|\vee
\bigvee^{m-1}S^1\vee\bigvee^{\sum_{i=1}^m b_i}S^2.
\]
No torsion-freeness is asserted for the arbitrary join factor. In particular, taking all \(H_i=C_4\) gives the complete integral classification
\[
|\operatorname{GP}(K_1\vee(mC_4))|\simeq
\bigvee^{m-1}S^1\vee\bigvee^m S^2\vee\bigvee^{3^m}S^{2m-1},\qquad m\ge2.
\]
For two squares this is \(S^1\vee2S^2\vee9S^3\), and for three it is \(2S^1\vee3S^2\vee27S^5\). Here all wedge multiplicities refer to geometric CW homotopy, not just dimensions over a field.

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted. The parts \(H_i\) must be connected, triangle-free and nonempty; parts need not be pairwise isomorphic and may contain cycles. The number of parts \(m\) is at least two. The expression \(mC_4\) means a disjoint union of \(m\) four-cycles, before adding one common adjacent apex. In particular this construction is **not** the bouquet of cycles obtained by identifying a rim vertex, and it is not an independence, clique-free, robust-clique, multipath or matching complex.

For a connected graph \(H\), \(D_2(H)\) permits the empty set and all two-vertex sets and forbids any subset containing a vertex with at least two neighbors in the selected induced subgraph. The join \(*\) is the simplicial join on disjoint vertex sets. An empty or zero wedge of spheres is interpreted as a point summand and does not contribute reduced homology.

## Proof
**Step 1: classify faces without the apex.** Let \(z\) denote the apex. Every pair of distinct rim vertices has distance one if adjacent in its source graph, and distance two otherwise. A rim-only triple lies on a geodesic exactly when two selected edges of length one share a vertex and their other endpoints are nonadjacent. Because each \(H_i\) is triangle-free, this is exactly an induced three-vertex path inside some \(H_i\). No path of length two in \(G\) with a rim middle vertex can have endpoints in different parts: the middle vertex has no rim adjacency outside its part. Consequently a rim-only selected set is in general position if and only if its intersection with every \(H_i\) has induced maximum degree at most one. Hence the apex-deleted subcomplex is precisely
\[
A=D_2(H_1)*\cdots*D_2(H_m).
\]

**Step 2: describe the apex star.** A face containing \(z\) cannot contain two rim vertices from different parts, since \(z\) lies on their unique length-two shortest path. Two rim vertices from one part may occur with \(z\) exactly when they are adjacent; otherwise \(z\) is their geodesic midpoint. Triangle-freeness excludes three mutually adjacent rim vertices. Thus all such faces are the cone \(z*B\), where
\[
B=H_1\sqcup\cdots\sqcup H_m
\]
is viewed as a one-dimensional simplicial complex. Each edge of \(B\) belongs to \(A\), so as an exact simplicial union
\[
\operatorname{GP}(G)=A\cup_B(z*B).
\]
In particular its realization is the mapping cone of the inclusion \(|B|\hookrightarrow |A|\).

**Step 3: prove the attaching map nullhomotopic.** For every nonempty graph \(H_i\), all vertex pairs are faces of \(D_2(H_i)\); hence its realization is path-connected, including the one-vertex case. The join of two nonempty connected CW complexes is simply connected (indeed two-connected). Since \(m\ge2\), \(|A|\) is simply connected. The domain \(|B|\) is a disjoint union of connected finite graphs. The restriction of the inclusion to each connected graph is nullhomotopic: any map from a connected graph into a simply connected space contracts because a graph is a one-dimensional CW complex. The contractions of its \(m\) components may be chosen to reach one common target point since \(|A|\) is path-connected. Thus the whole inclusion \(|B|\to|A|\) is nullhomotopic.

**Step 4: split the mapping cone.** A simplicial inclusion is a cofibration, so its mapping cone is homotopy invariant under replacement of the attaching map by a constant map. It follows that
\[
|\operatorname{GP}(G)|\simeq |A|\vee \Sigma|B|,
\]
where \(\Sigma\) denotes the *unreduced* suspension of the possibly disconnected space \(|B|\). As \(|B|\) has exactly \(m\) connected components and each component is a finite graph of cycle rank \(b_i\), its suspension splits as
\[
\Sigma|B|\simeq \bigvee^{m-1}S^1\vee\bigvee^{\sum_i b_i}S^2.
\]
One way to see the latter is to contract a spanning tree in each component, obtaining a disjoint union of pointed circles bouquets; suspending their disjoint union adds one independent one-circle for every component beyond the first, and suspends each original one-circle to a two-sphere. This proves the general equivalence with integral coefficients and the actual homotopy type.

**Step 5: evaluate the square family.** A selected triple of vertices in \(C_4\) always contains an induced path of length two; every selected pair is allowed. Therefore \(D_2(C_4)\) is exactly the one-dimensional complete graph on four vertices, which is homotopy equivalent to a wedge of three circles. The join of \(m\) such connected circle bouquets is a wedge of \(3^m\) spheres of dimension \(2m-1\): using the standard equivalence \(X*Y\simeq\Sigma(X\wedge Y)\) for connected based CW complexes and distributing smash products over finite wedges yields the multiplicity and dimension. Each square has cycle rank one, so Step 4 adds \(m\) two-spheres and \(m-1\) circles. The square-family formula follows for every \(m\ge2\).

## Verification
Run `python3 verify_wheel_bouquets.py` from the directory containing the standalone file. It exhaustively enumerates every subset of each finite test graph, independently checks all three-point geodesic equalities using graph shortest-path BFS and the local per-petal face rule, constructs the mod-two simplicial boundary matrices, and compares reduced Betti ranks with the factor-join prediction. Tested petal lengths are \([4]\), \([4,4]\), \([4,5]\), \([5,5]\), \([4,6]\), \([4,4,4]\) and \([4,4,4,4]\); all seven comparisons passed. The largest test has seventeen vertices and \(14673\) nonempty simplicial faces. Additional hand-coded, separately executed exact boundary tests checked connected non-cycle factors (three- and four-vertex paths and stars) against the general formula. These finite checks support error detection only; the infinite theorem rests on the preceding topological proof.

## Relationship to prior work
Iršič, Klavžar, Rus and Tuite (2024), Proposition 3.3, already describe general-position subsets under graph joins via clique and disjoint-union-of-cliques conditions and derive the corresponding *counting polynomial*. The face-set characterization used in Steps 1 and 2 is therefore not claimed as novel by itself. Rather (2026, first public 6 March 2026) develops general-position enumerators and unimodality for multipartite graphs and coronas. Neither full text supplies the mapping-cone splitting, the general transfer through the dissociation complexes, or the all-multiplicity integral homotopy classification of the multi-square-apex family. Other published calculations for unrelated clique avoidance, multipath, and bouquet geometries do not imply the statement without changing their defining complexes. Classical join-connectivity and mapping-cone splitting are used as standard topology, not claimed as new.

## Limitations
The splitting requires at least two connected triangle-free components after deleting the universal apex. It need not hold for arbitrary graph joins, triangles inside components, or for a single component. The general factor \(D_2(H_i)\) is not explicitly classified and may retain interesting higher homology or torsion; this finding makes no universal sphere-wedge assertion for that factor. The result is nonequivariant; no automorphism representation or explicit simple-homotopy collapse is asserted. Full historical priority cannot be proved by indexed searches, and no independent mathematical audit has been performed.

## References
1. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, Results in Mathematics **79**, 110 (2024), DOI: 10.1007/s00025-024-02133-3, especially Proposition 3.3. https://link.springer.com/article/10.1007/s00025-024-02133-3
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (first posted 2026-03-06), https://arxiv.org/abs/2603.06930 and https://arxiv.org/html/2603.06930v3
3. Standard topological facts: connectivity of joins of connected CW complexes, nullhomotopy of graph maps to simply connected targets, and homotopy invariance of mapping cones.
