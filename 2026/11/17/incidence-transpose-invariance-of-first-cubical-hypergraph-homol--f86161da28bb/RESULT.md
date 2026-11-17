# Incidence-transpose invariance of first cubical hypergraph homology

## Finding
Let \(H=(V,\mathcal E)\) be a finite hypergraph with nonempty hyperedges and with every vertex in at least one hyperedge. Let \(H^*\) have one vertex for each member of \(\mathcal E\), with one hyperedge \(\{e\in\mathcal E:v\in e\}\) for each \(v\in V\), with duplicate dual hyperedges permitted to coalesce. For the normalized \(\Box\)-cubical homology introduced by Zaidi and Jamil, incidence transposition gives an integral isomorphism
\[
H^{\Box}_1(H;\mathbb Z)\ \cong\ H^{\Box}_1(H^*;\mathbb Z).
\]
The isomorphism is independent of all incidence-witness choices and respects relabeling of the incidence relation. It includes free and torsion summands, if present. No assertion is made about higher-degree cubical homology or homotopy equivalence of the hypergraphs.

## Assumptions and scope
A hypergraph is a finite incidence relation with distinct nonempty edge sets and no unsupported vertices. For any finite graph \(G\), form its *triangle-square complex* \(T(G)\) by attaching one \(2\)-cell along each simple \(3\)-cycle and simple \(4\)-cycle (additional attaching maps along nonsimple short loops are unnecessary). Define \(P(H)\) as the graph on \(V\) joining distinct vertices that lie together in a hyperedge. Define \(L(H)\) as the graph on \(\mathcal E\) joining distinct hyperedges that intersect. These satisfy \(P(H^*)=L(H)\). All homology groups use integer coefficients unless explicitly stated otherwise.

## Proof
**1. Reduction to an ordinary graph.** Every hyperedge of the domain \(\Box\)-hypercube has exactly two vertices. Thus a map from that hypercube to \(H\) is a hypergraph morphism precisely when the endpoints of each cube edge are equal or adjacent in \(P(H)\). In every dimension, singular cubes, coordinate degeneracies, and face operators coincide with those for the discrete cubical chain complex of \(P(H)\). Therefore
\[
C^{\Box}_\bullet(H;\mathbb Z)\cong C^{\mathrm{cube}}_\bullet(P(H);\mathbb Z)
\]
canonically as chain complexes. The same holds for \(H^*\) and \(L(H)\).

**2. Low-dimensional cubical presentation.** For a graph \(G\), the normalized cubical \(1\)-chains have one generator for each orientation of every edge. The boundary of the nondegenerate square with successive vertex values \((u,v,u,u)\) at \((00,10,01,11)\) is the sum of the two oppositely oriented traversals of \(uv\). Thus a backtrack is a boundary. The nondegenerate square \((a,b,c,c)\), where \(a,b,c\) form a triangle, gives its oriented triangular boundary. An injectively labeled square gives the boundary of its four-cycle. Conversely, the boundary of any nondegenerate square is a closed walk of at most four graph edges; after cancellation of backtracks, it is zero or a triangle or quadrilateral. It follows over \(\mathbb Z\), not merely over a field, that
\[
H^{\mathrm{cube}}_1(G;\mathbb Z)\cong H_1(T(G);\mathbb Z).
\]
In particular the presentation includes all relations and has no unaccounted extra relations from higher-dimensional cubes, since \(H_1\) involves only the maps in dimensions \(1\) and \(2\).

**3. Incidence-witness map on closed walks.** Work on one connected incidence component. Choose a vertex \(v_*\) and an incident hyperedge \(e_*\). For an oriented closed graph walk \(v_0=v_*,v_1,\ldots,v_k=v_*\) in \(P(H)\), select \(e_i\in\mathcal E\) containing \(v_i,v_{i+1}\). Send it to the closed walk
\[
e_*,e_0,e_1,\ldots,e_{k-1},e_*
\]
in \(L(H)\), suppressing repeated consecutive vertices. Each required step is legal: \(e_{i-1}\) and \(e_i\) both contain \(v_i\), and the initial and terminal steps share \(v_*\). If the witness on one edge is changed from \(e_i\) to \(e'_i\), the resulting difference is a sum of two triangular boundaries in \(L(H)\): the triangles with vertex sets \(\{e_{i-1},e_i,e'_i\}\) and \(\{e_i,e'_i,e_{i+1}\}\). Degenerate triangles give zero. A deleted or inserted backtrack changes the image by loops within a clique of hyperedges sharing one original vertex, hence by triangular boundaries. A triangle or square in \(P(H)\) maps to a closed walk of at most three or four edges in \(L(H)\), respectively, modulo a conjugating path to the basepoint. These walks bound cells in \(T(L(H))\). The construction therefore induces a homomorphism of abelianized based loop groups, equivalently
\[
\Phi:H_1(T(P(H));\mathbb Z)\longrightarrow H_1(T(L(H));\mathbb Z).
\]
Witness independence also removes dependence on the auxiliary choices after abelianization; changing the base incidence merely changes the based description by conjugation.

**4. Inverse and integral conclusion.** Repeat the same construction for the transposed incidence relation, replacing each transition between intersecting hyperedges by a common original vertex. For a walk from Step 3, choose \(v_i\) at the transition \(e_{i-1}\to e_i\). The resulting twice-transferred walk is the original walk up to cyclic rotation and deletion of passages through vertices of a single original hyperedge. Such deletions change the class only by triangular boundaries because all vertices of a hyperedge form a clique in \(P(H)\). Similarly, the opposite composite is the identity. Therefore \(\Phi\) and the transposed map are mutual inverses on integral first homology. Components correspond through the same incidence bipartite graph, so taking direct sums over components proves the theorem.

## Verification
The standalone script `verify_dual_box_h1.py` enumerates **all** nondegenerate \(\Box\)-cubes through dimension \(2\) for each of six finite incidence examples, forms the signed integral boundary relations, and applies integer Smith normal form. It checks both the original and transposed hypergraphs. The cases include a loose five-cycle of triples (where each side has \(H_1\cong\mathbb Z\)), a loose four-cycle of triples (where each side has \(H_1=0\)), a five-cycle graph, the Fano triple system, a mixed-size asymmetric example, and a single hyperedge. Every comparison passes. These are finite corroborations, not an infinite proof; the unrestricted argument is in Steps 1–4.

## Relationship to prior work
Zaidi and Jamil, *A cubical approach to homology theories for hypergraphs* (arXiv:2610.08196v1, October 6, 2026), define the \(\Box\)-theory and formulate in Conjecture 4.4 the stronger assertion that each hypergraph is homotopy equivalent to its incidence dual. Their homotopy-invariance theorem supplies a necessary consequence of that conjecture, not its proof. The present theorem establishes this degree-one necessary consequence without assuming homotopy equivalence. Barcelo–Greene–Jarrah–Welker (arXiv:1803.07497) treat cubical homology of ordinary graphs; they do not establish hypergraph incidence-transpose invariance. Classical Dowker duality relates the homotopy types of two unflagified Dowker nerves; it does not directly identify the extra triangle and square relations introduced by the graph-based \(\Box\)-chain theory. The explicit witness comparison is required for the stated invariant.

## Limitations
The theorem is strictly a first-homology result, not a proof of the homotopy-duality conjecture. It does not assert equality of \(\Gamma\)- or \(\times\)-homology or any higher-degree \(\Box\)-group. Empty hyperedges and unsupported vertices are excluded to avoid disappearing vertices under incidence dualization; the supported core can be treated separately. The source novelty comparison does not exclude unindexed earlier formulations of the same low-dimensional incidence symmetry.

## References
1. S. H. A. Zaidi and S. S. Jamil, *A cubical approach to homology theories for hypergraphs*, arXiv:2610.08196v1 (first posted October 6, 2026), https://arxiv.org/abs/2610.08196.
2. H. Barcelo, C. Greene, A. S. Jarrah, and V. Welker, *Discrete Cubical and Path Homologies of Graphs*, arXiv:1803.07497 (2018), https://arxiv.org/abs/1803.07497.
3. C. H. Dowker, *Homology groups of relations*, Ann. of Math. 56 (1952), 84–95; see also the discussion in *Dowker's theorem for higher-order relations*, https://doi.org/10.1007/s41468-026-00239-x.
