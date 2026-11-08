# Equivariant collapse of consistently oriented triangular-book multipath complexes

## Finding
For every integer \(m\geq 1\), let \(D_m\) be the directed graph on vertices \(a,b,w_1,\ldots,w_m\) with arrows
\[
c:a\to b,\qquad u_i:b\to w_i,\qquad v_i:w_i\to a\quad (1\leq i\leq m).
\]
Thus each of its \(m\) triangles is a consistently directed cycle, and all triangles share the arrow \(c\). Let \(X_m\) be the simplicial complex whose vertices are the arrows and whose simplices are sets of arrows forming vertex-disjoint directed paths, with isolated vertices permitted.

Let \(S_m\) act by permuting the page indices and fixing \(a,b,c\). There is an **\(S_m\)-equivariant simplicial-collapse sequence**, performed by complete orbits of free face pairs, from \(X_m\) onto the graph \(Y_m\) with vertices \(c,u_i,v_i\) and edges \(\{c,u_i\},\{c,v_i\},\{u_i,v_i\}\) for all \(i\). In particular, \(Y_m\) is a bouquet of \(m\) three-edge cycles with common vertex \(c\), and
\[
|X_m|\simeq_{S_m}|Y_m|\cong\bigvee^m S^1
\]
where the last space carries the natural permutation action on its circle summands. The subscript denotes an equivariant homotopy equivalence of spaces, not merely equality of ordinary homology groups.

More precisely, \(\pi_1(|X_m|,c)\) is the free group \(F_m\) on the loops \(c\to u_i\to v_i\to c\), on which \(S_m\) permutes the chosen generators. Hence
\[
H_1(|X_m|;\mathbb Z)\cong\mathbb Z[\{1,\ldots,m\}]
\]
as an integral \(S_m\)-permutation lattice, and every other positive-degree integral homology group vanishes.

For **every** subgroup \(H\leq S_m\), let \(f_H\) be its number of individually fixed page indices and let \(o_H\) be its number of orbits on the page indices. Then
\[
|X_m|^H\simeq\bigvee^{f_H}S^1,\qquad |X_m|/H\simeq\bigvee^{o_H}S^1,
\]
where a wedge of zero circles means a point. In particular, the full symmetric-group fixed-point space is a point for \(m\geq2\), while its orbit space is a circle.

## Assumptions and scope
The graph is simple and has exactly the \(2m+1\) arrows indicated above. The direction on every triangular page is \(a\to b\to w_i\to a\). No reverse arrows are included. The complex uses the ordinary directed-path convention: at most one chosen incoming and one chosen outgoing arrow at any vertex, and no chosen directed cycle. The statements hold for all finite integers \(m\geq1\) and all subgroups \(H\leq S_m\), including the trivial group. All homotopy and homology claims are integral, without rationalization or a stable-range hypothesis.

## Proof
**1. Complete simplex classification.** Every simplex has at most one \(u_i\), because all \(u_i\) leave \(b\), and at most one \(v_j\), because all \(v_j\) enter \(a\). There is only one arrow \(c\). Every pair \(\{u_i,v_j\}\) is permissible: for \(i=j\) it forms the directed path \(b\to w_i\to a\), and for \(i\ne j\) it forms two vertex-disjoint one-edge paths. The triples \(\{c,u_i,v_j\}\) are permissible exactly when \(i\ne j\): in that case they give the directed path \(w_j\to a\to b\to w_i\), whereas \(i=j\) gives the directed three-cycle through \(w_i\). All \(\{c,u_i\}\) and \(\{c,v_j\}\) are permissible. There are no simplices of dimension above two. Thus the vertices are \(c,u_i,v_i\); the edges are \(\{c,u_i\},\{c,v_i\},\{u_i,v_j\}\) for all \(i,j\); and the only triangles are \(\{c,u_i,v_j\}\) for \(i\ne j\).

**2. Explicit equivariant collapse.** Fix any ordered pair \((i,j)\) with \(i\ne j\). The off-diagonal edge \(e_{ij}=\{u_i,v_j\}\) is contained in precisely one maximal simplex: the triangle \(t_{ij}=\{c,u_i,v_j\}\). Accordingly \((e_{ij},t_{ij})\) is an elementary free-face pair. For distinct ordered pairs these edges and triangles are distinct, so all \(m(m-1)\) pairs can be removed in any order. The remaining simplicial complex consists exactly of the edges \(\{c,u_i\},\{c,v_i\},\{u_i,v_i\}\) and their faces, namely \(Y_m\). The \(S_m\)-action sends the pair indexed by \((i,j)\) to the pair indexed by \((\sigma(i),\sigma(j))\). Elementary triangle collapses can therefore be carried out uniformly on every orbit, fixing the common surviving edges. Their simultaneous deformation retracts agree on intersections (which are surviving edges or vertices), giving an \(S_m\)-equivariant strong deformation retraction from \(|X_m|\) to \(|Y_m|\).

**3. Homotopy and integral action.** For each \(i\), the three retained edges form an unfilled triangular loop based at \(c\). These loops meet only in \(c\), so \(|Y_m|\) is literally a wedge of \(m\) circles. The action of \(S_m\) fixes \(c\) and sends the ordered loop \(c\to u_i\to v_i\to c\) to the same ordered loop with index \(\sigma(i)\); there is no orientation reversal. The fundamental-group and integral homology descriptions follow directly from this graph and the equivariant retraction.

**4. Fixed points and orbit spaces.** Any subgroup \(H\leq S_m\) permutes the loops of \(Y_m\) and fixes their common vertex \(c\). A non-basepoint of a loop can be fixed by all of \(H\) exactly when its page index is fixed by all of \(H\). Therefore \(|Y_m|^H\) is exactly the wedge of the \(f_H\) fixed loops. Likewise \(|Y_m|/H\) identifies precisely the loops in each page orbit, preserving their orientations, giving a wedge of \(o_H\) loops. Restricting and passing to quotients of the constructed equivariant strong deformation retraction proves the two asserted formulae for \(|X_m|\).

The proof also gives the exact face count \(2m^2+3m+2\) when the empty simplex is included, as a direct finite consistency check.

## Verification
The included standard-library program `verify.py` constructs every arrow set for \(1\leq m\leq7\) and independently tests path-forest admissibility. It matches the explicit face classification; checks that every off-diagonal edge has precisely its asserted unique triangle coface; removes all free-face pairs and checks the exact remaining graph; and independently computes reduced mod-two Betti numbers for \(1\leq m\leq5\). It also checks all 30 distinct subgroups of \(S_4\) obtainable from pairs of generators, including their actions, fixed supports, and orbitwise cancellation. The recorded execution output is in `verification_output.txt` and ends in `ALL_VERIFY_OK`. These experiments corroborate the combinatorics; the proof above establishes the statements for all \(m\) and all subgroups without relying on finite extrapolation.

## Relationship to prior work
Deshpande and Sawant (arXiv:2602.14936v1, first submitted 16 February 2026) develop directed linear-forest complexes and conflict graphs and explicitly pose, in Problem 6.3, the determination of homotopy types for multidigraphs with directed cycles. The present calculation answers that question for the explicitly defined shared-arrow triangular-book family and supplies stronger equivariant data. Their general conflict-hypergraph correspondence does not itself give this collapse or subgroup formulas.

Caputi, Collari, Di Trani and Smith (arXiv:2208.04656v1) study multipath homotopy types for directed paths, polygons, grids and transitive tournaments, including a decomposition into dynamical modules. Caputi, Collari and Smith (arXiv:2601.05670v1) study **bidirected** polygons and paths. Neither of these investigated families is the consistently oriented shared-arrow book used here. Previously considered fully bidirected triangular books are also distinct: the additional reverse arcs change the defining simplicial complex, and their homotopy classifications do not imply this theorem merely by restriction.

The collapsing technique is elementary simplicial topology; the mathematical claim is its uniform explicit realization and full symmetric-group, fixed-space and orbit-space classification for this directed graph family, not a new general collapse theorem.

## Limitations
No claim is made for bidirected books, triangles sharing only a vertex, books with nontriangular pages, arbitrary orientations, or the directed-tree complex allowing branching. The source comparisons are not a proof of global novelty; unindexed literature or an unrecognized stronger theorem could exist. The verification is same-model and finite where it uses computation; independent scientific assessment has not occurred.

## References
1. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1, 16 February 2026, https://arxiv.org/abs/2602.14936.
2. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, 9 January 2026, https://arxiv.org/abs/2601.05670.
3. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, 9 August 2022, https://arxiv.org/abs/2208.04656.
