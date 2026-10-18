# The ordinary \(3\)-cut complex of the Heawood graph is a wedge of \(36\) ten-spheres
## Finding
Let \(H\) be the Heawood graph, realized as the incidence graph of the Fano plane with point vertices \(p_i\) and line vertices \(\ell_j\), where \(i,j\in\mathbb Z/7\mathbb Z\) and \(p_i\) is adjacent to \(\ell_j\) exactly when \(i-j\in\{0,1,3\}\). Let \(\Delta_3(H)\) be the ordinary \(3\)-cut complex: its facets are the complements of three-vertex sets that induce disconnected subgraphs of \(H\). Then
\[
\Delta_3(H)\simeq \bigvee^{36} S^{10}.
\]

## Assumptions and scope
The graph is finite, simple, and is defined by the incidence rule above; no graph-library naming convention is used in the proof. The cut complex is the ordinary cut complex, not the total cut complex: a three-set contributes a facet whenever its induced subgraph is disconnected, whether or not the set is independent. The claim is only about this single finite graph and this value of \(k=3\).

## Proof
The Heawood graph has \(14\) vertices and \(21\) edges and is cubic and triangle-free. Hence every connected induced three-vertex subgraph is an induced path of length two. Choosing the middle vertex and two of its three neighbours gives exactly
\[
14\binom{3}{2}=42
\]
connected triples. Therefore the remaining \(\binom{14}{3}-42=322\) triples are disconnected, so \(\Delta_3(H)\) has exactly \(322\) facets, all of cardinality \(11\), and is pure of dimension \(10\).

Enumerate every nonempty face from the defining criterion that a face belongs to \(\Delta_3(H)\) exactly when its complement contains at least one disconnected triple. This gives \(16{,}235\) nonempty faces and the face vector
\[
(14,91,364,1001,2002,3003,3432,3003,2002,1001,322).
\]

On this face poset, process the vertices in the order \(0,1,\ldots,13\). At vertex \(v\), match every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unmatched. The resulting matching has exactly \(8{,}099\) matched pairs and leaves exactly \(37\) critical faces: one critical vertex and \(36\) critical faces of dimension \(10\). An exhaustive orientation of all \(112{,}924\) cover relations in the Hasse diagram, with matched covers directed upward and all other covers downward, is acyclic. Thus this is an acyclic discrete-Morse matching.

Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(\Delta_3(H)\) with one \(0\)-cell and exactly \(36\) cells of dimension \(10\), and no cells in intermediate dimensions. Every attaching map of a \(10\)-cell has target the single \(0\)-cell, so this CW complex is a wedge of \(36\) copies of \(S^{10}\).

## Verification
The bundled `verify.py` uses only the Python standard library. It reconstructs the graph directly from the displayed incidence rule, enumerates all connected and disconnected triples, enumerates the full cut complex, reconstructs the sequential element matching, checks every matched pair, and performs a topological sort of the fully oriented Hasse diagram to certify acyclicity. It then independently forms all simplicial boundary matrices over \(\mathbb F_2\) and computes their exact ranks. The resulting reduced mod-\(2\) Betti vector is zero in dimensions \(0\) through \(9\) and equals \(36\) in dimension \(10\), independently agreeing with the Morse conclusion. The recorded verifier output ends with `VERIFY_OK`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue define the ordinary cut complex and prove general structural results. Their Theorem 6.1 shows that when a cut complex contains the full codimension-one skeleton, its homology is torsion-free and can occur only in the top two dimensions; Proposition 6.2 supplies that skeleton under a girth condition. Since the Heawood graph has girth \(6\), those results apply for \(k=3\). They also force the reduced Euler characteristic here: there are \(42\) connected triples, so the absolute Euler-characteristic contribution is \(\binom{13}{2}-42=36\). They do not determine whether the degree-\(9\) homology vanishes, do not give the Heawood homotopy type, and the paper's listed exact families do not include the Heawood graph. The acyclic matching above supplies precisely that missing information.

The companion total-cut construction is different: the total \(3\)-cut complex uses only complements of independent triples. The total-cut paper explicitly distinguishes the two notions and states that the total complex is a subcomplex of the ordinary cut complex. Thus results for a total cut complex do not imply the present ordinary-cut homotopy type.

## Limitations
This is an exact finite result for one graph. It does not classify ordinary \(3\)-cut complexes of all cubic bipartite graphs, does not assert shellability, and does not provide a graph-family formula. The literature comparison cannot exclude an unindexed or unpublished duplicate. The proof's nontrivial finite step is the acyclicity of the specified matching; it is checked exhaustively by the bundled verifier rather than replaced by an unproved general matching lemma.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26; SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675, doi:10.1137/23M1569034.
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27.
