# The Heawood ordinary five-cut complex is a wedge of 491 eight-spheres

## Finding
Let \(H\) be the 14-vertex Heawood graph, the point-line incidence graph of the Fano projective plane. Its ordinary five-cut complex \(\Delta_5(H)\) has a facet \(V(H)\setminus U\) for every five-vertex subset \(U\subseteq V(H)\) that induces a disconnected graph. Then there is an **integral homotopy equivalence**
\[
\Delta_5(H)\simeq\bigvee^{491}S^8.
\]
In particular its only nonzero reduced integral homology group is \(\widetilde H_8(\Delta_5(H);\mathbb Z)\cong\mathbb Z^{491}\). The complex has dimension eight and is pure, with 1,750 facets. It has the full six-skeleton of the thirteen-simplex but precisely 28 missing seven-dimensional faces, corresponding under complementation to the 28 induced six-cycles of \(H\). These missing faces account for a correction of 28 spheres relative to the topological count that would arise if a higher-girth hypothesis held: \(491=\binom{13}{4}-252+28\).

## Assumptions and scope
Vertices are labeled \(0,\ldots,13\). Labels \(0,\ldots,6\) denote points and \(7+j\) denotes the line through points \(j,j-1,j-3\), where arithmetic is modulo seven. This is the Fano incidence graph: there are 14 vertices, 21 edges, degree three at every vertex and girth six. All complexes are ordinary abstract simplicial complexes; the empty face is included. A subset is a face of \(\Delta_5(H)\) if and only if its complement contains an induced disconnected five-vertex subset. This convention is distinct from the total cut complex, where the complementary set must be independent.

The classification is of this particular finite graph, not of all cubic bipartite graphs or all girth-six graphs. Coefficients in the homology conclusion are \(\mathbb Z\), and the homotopy equivalence is nonequivariant.

## Proof
**1. Classify induced five-vertex graphs.** The graph has girth six. Every induced subgraph on five vertices is therefore a forest and is connected exactly when it has four edges. Its connected five-vertex subgraphs must be either a path with five vertices or a tree with degree sequence \((3,2,1,1,1)\). For the paths, choose their unique middle vertex (14 options), choose two of its three neighbors (3 options), and choose an outer neighbor of each (2 options each); this gives \(14\cdot3\cdot4=168\) paths. For the branched trees, choose their unique degree-three vertex (14 options), choose which of its three arms is extended (3 options), and choose the extension (2 options); this gives \(14\cdot3\cdot2=84\). Girth six ensures that no counted choice identifies vertices or supplies a forbidden chord. Consequently, precisely \(168+84=252\) five-vertex subsets are connected. There are \(\binom{14}{5}-252=1750\) disconnected five-subsets and exactly that many distinct facets.

**2. Locate the only missing subtop faces.** Every induced six-vertex subset \(W\) whose five-vertex deletions are all connected must be an induced six-cycle. Indeed, if \(H[W]\) is a forest, one can delete a suitable vertex to leave it disconnected; if \(H[W]\) has a cycle, girth six forces all six vertices onto a chordless six-cycle. Conversely, deleting any vertex from such a cycle leaves a connected path. Thus the nonfaces of cardinality eight are exactly the complements of induced six-cycles. Each six-cycle corresponds to a triple of noncollinear Fano points, with their three pairwise joining lines. There are \(\binom73-7=28\) noncollinear point triples, hence exactly 28 missing eight-element faces. Every seven-vertex subset contains a disconnected five-subset: if it has no six-cycle, take a six-subset and delete a suitable vertex; if it contains a six-cycle, its seventh vertex meets at most one cycle vertex (two would create a cycle shorter than six), so combine that seventh vertex with four cycle vertices avoiding its neighbor. Thus every face of cardinality at most seven occurs: the six-skeleton is complete.

**3. Build the full face poset twice.** Let \(F\) be the 1,750 facets, i.e. complements of disconnected five-subsets. Define \(\mathcal F=\{S:S\subseteq f\text{ for some }f\in F\}\). An independent membership test checks whether \(V(H)\setminus S\) contains a disconnected five-subset. The supplied `verify.py` checks the two definitions on every one of the \(2^{14}\) vertex subsets, obtaining the same 14,633 faces (including the empty face). In degrees \(-1\) through eight the numbers are
\[
(1,14,91,364,1001,2002,3003,3432,2975,1750).
\]
In particular there are 14,632 nonempty faces. This independently corroborates the count of 28 missing seven-faces and the connected-five-set count.

**4. An explicit complete acyclic discrete-Morse matching.** Work on the nonempty face poset, initially containing all 14,632 faces. In order \(v=0,1,\ldots,13\), simultaneously pair each remaining face \(S\) not containing \(v\) with \(S\cup\{v\}\), provided both faces remain; then remove all these disjoint pairs before advancing. This completely deterministic prescription yields, by stage, the numbers of pairs
\[
(6920,53,32,20,17,14,14,0,0,0,0,0,0,0).
\]
These sum to 7,070 matched pairs. Exactly 492 nonempty faces remain: the singleton \(\{0\}\) and 491 faces of size nine (dimension eight). There are no other critical faces. For an independent acyclicity check, orient every unpaired Hasse cover from its upper face to its lower face and reverse every paired cover. `verify.py` constructs all 96,880 cover incidences among all 14,632 nonempty faces, then exhaustively performs a topological sort, eliminating all 14,632 nodes. This proves the oriented Hasse graph has **no directed cycles**, not merely that a bounded search failed to find one. The pair list is characterized deterministically; its canonical little-endian 16-bit pair digest is recorded below for an exact replay comparison.

**5. Deduce the homotopy equivalence.** Forman's discrete Morse theorem gives a CW complex with one zero-cell and 491 eight-cells, and no other positive-dimensional cells. Because every attaching map for an eight-cell lands in the single zero-cell, the CW complex is a wedge of 491 copies of \(S^8\). This is an integral homotopy equivalence, so torsion is excluded without appealing to finite-field ranks. As a numerical cross-check, the reduced Euler characteristic from the face vector is exactly 491, also equal to \(\binom{13}{4}-252+28\).

## Verification
Run `python3 verify.py` in the directory containing the standalone file. It requires only the Python 3 standard library and no downloaded data. The program constructs the labeled incidence graph, verifies degrees and all connected five-set counts, independently tests all faces, identifies 28 induced six-cycles and the complementary missing seven-faces, executes the fully specified matching, checks every Hasse incidence, proves acyclicity by a complete topological traversal, and checks Euler characteristic. Its successful output is in `verification_output.txt` and ends with `VERIFY_OK HEAWOOD_FIVE_CUT_TOP_SPHERE_WEDGE`.

The 7,070 pairs in generation order, serialized as pairs of unsigned little-endian 16-bit face masks, have SHA-256 digest:
`72e2fe9bfdd9509f5054b3b4ee42ec66068b47683a83f64266110dc3b4710314`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675), study cut complexes and give a lower-skeleton criterion and homological formulas in Section 6. Here that complete-next-to-top-skeleton criterion fails: there are exactly 28 missing seven-faces. Their theorem therefore does not imply this five-cut homotopy type. *Topology of Cut Complexes II* (arXiv:2407.08158) develops different graph-family and symmetry results and does not supply this Fano incidence example.

The published result *High-girth cut complexes are wedges of top-dimensional spheres* (published-finding corpus record `2026/10/11/SCOPE-high-girth-cut-complexes-are-wedges-of-top-dimensional-spheres--ec8bbe3d352b`) proves a uniform formula when a graph has girth at least \(k+2\). It genuinely covers the Heawood four-cut case, but for five-cuts it requires girth seven; \(H\) has girth six. Applying its formula beyond the hypotheses would give 463 instead of 491. The explicit 28-cycle correction explains the boundary. A separate published record, *The total 3-cut complex of the Heawood graph is a wedge of 36 eight-spheres* (`2026/10/4/SCOPE-the-total-3-cut-complex-of-the-heawood-graph-is-a-wedge-of-36-ei--0c003a069433`), concerns a different complex and does not imply this result.

The count of 28 Heawood six-cycles, and a homological classification of these hexagons in a torus embedding, were already established in the published record *Seven facial and twenty-one essential hexagons in the Heawood dual of Möbius' torus* (`2026/10/11/SCOPE-seven-facial-and-twenty-one-essential-hexagons-in-the-heawood-du--41e8f1c94420`). That result does **not** concern ordinary five-cut complexes, so its known cycle count does not imply the 491-sphere homotopy classification. The present claim does not present the standalone six-cycle count as new.

## Limitations
The proof is exhaustive and exact for the specified graph. It does not classify ordinary five-cut complexes of all girth-six graphs, prove a general 28-cycle correction principle, or determine the integral equivariant homotopy type under the Heawood automorphism group. The statement is not a shellability claim. Mathematical novelty was assessed against accessible primary literature and related published statements; a logically equivalent unindexed or inaccessible publication remains a residual bibliographic risk. No independent external audit has been performed.

## References
1. M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public April 26, 2023), especially Section 6. https://arxiv.org/abs/2304.13675
2. M. Bayer et al., *Topology of Cut Complexes II*, arXiv:2407.08158 (first public July 11, 2024). https://arxiv.org/abs/2407.08158
3. *High-girth cut complexes are wedges of top-dimensional spheres*, public research record `2026/10/11/SCOPE-high-girth-cut-complexes-are-wedges-of-top-dimensional-spheres--ec8bbe3d352b`, with its full theorem and proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-high-girth-cut-complexes-are-wedges-of-top-dimensional-spheres--ec8bbe3d352b
4. *The total 3-cut complex of the Heawood graph is a wedge of 36 eight-spheres*, public record `2026/10/4/SCOPE-the-total-3-cut-complex-of-the-heawood-graph-is-a-wedge-of-36-ei--0c003a069433`.
5. *Seven facial and twenty-one essential hexagons in the Heawood dual of Möbius' torus*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-seven-facial-and-twenty-one-essential-hexagons-in-the-heawood-du--41e8f1c94420
6. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145, for the discrete Morse CW homotopy theorem.
