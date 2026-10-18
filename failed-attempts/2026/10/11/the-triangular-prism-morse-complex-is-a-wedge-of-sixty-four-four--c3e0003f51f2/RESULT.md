# The triangular-prism Morse complex is a wedge of sixty-four four-spheres
## Finding
For the triangular prism graph \(P=C_{3}\mathbin{\square}K_{2}\), the Morse complex of acyclic discrete vector fields satisfies
\[
\mathcal{M}(P)\simeq\bigvee^{64}S^{4}.
\]

## Assumptions and scope
The graph \(P\) has vertex set \(\{0,1,2,3,4,5\}\), with two triangles \(012\) and \(345\), together with the three matching edges \(03,14,25\). A vertex of \(\mathcal{M}(P)\) is a primitive discrete vector field \((v,e)\), where \(v\) is an endpoint of edge \(e\). A simplex is a collection of such pairs in which no graph vertex or graph edge appears twice and the induced edge orientations contain no directed cycle. This is exactly the ordinary Morse complex for the one-dimensional simplicial complex \(P\).

## Proof
There are \(18\) primitive vector fields. The verifier enumerates every nonempty subset of these \(18\) candidates and tests the two defining conditions above. Exactly \(1727\) simplices survive, with face vector
\[
(18,126,428,705,450).
\]

On this complete face poset, the verifier performs a fixed sequence of vertex toggles. It obtains \(831\) disjoint matched cover relations and leaves exactly one critical \(0\)-simplex and \(64\) critical \(4\)-simplices. To verify that this is an acyclic matching rather than merely a pairing, the program reconstructs all \(6606\) Hasse covers, reverses precisely the matched covers, and topologically sorts the resulting directed Hasse graph. All \(1727\) faces occur in the topological order, so the matching is acyclic.

Forman's discrete Morse theorem therefore gives a CW model with one \(0\)-cell, no cells in dimensions \(1,2,3\), and \(64\) cells in dimension \(4\). Every attaching map of a \(4\)-cell has target the single \(0\)-cell, hence the CW model is a wedge of \(64\) four-spheres.

## Verification
Run `python verify.py` from the directory containing the supplied files. The script exhaustively reconstructs the Morse complex, replays the fixed matching, checks every directed Hasse cover for acyclicity, and then independently computes the reduced mod-\(2\) homology from boundary matrices. It prints `VERIFY_OK` only after all assertions pass.

The independent chain calculation has boundary ranks
\[
(17,109,319,386)
\]
in dimensions \(1\) through \(4\), giving reduced mod-\(2\) Betti vector
\[
(0,0,0,0,64).
\]
The Euler characteristic is \(65\), consistent with the claimed wedge.

## Relationship to prior work
Donovan, Lin, and Scoville define the Morse complex and emphasize that precise homotopy types are known only for a small collection of complexes; their paper computes several families but does not treat the triangular prism. Scoville and Zaremsky subsequently give general connectivity bounds for graph Morse complexes. For a \(3\)-regular graph on six vertices their bound gives simple connectivity, but it does not determine the exact homotopy type.

A database search under the equivalent descriptions “triangular prism Morse complex,” “rooted forest complex triangular prism,” and “directed forest complex triangular prism” located a prior exact computation of reduced mod-\(2\) homology, concentrated in degree \(4\) with rank \(64\), but not an exact homotopy equivalence. Homology concentration alone does not imply a wedge-of-spheres homotopy type; the acyclic matching above supplies the missing implication.

## Limitations
The result concerns the ordinary Morse complex of this single graph, not the pure Morse complex, not Morse complexes of all prism graphs, and not all cubic graphs. The originality search found no exact triangular-prism homotopy computation, but terminology for graph Morse complexes overlaps with directed-tree and rooted-forest complexes, so an older equivalent formulation under those terms remains a residual literature risk.

## References
1. C. Donovan, M. Lin, N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, first public 2019-09-25. Primary MSC 57Q70.
2. N. A. Scoville, M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first public 2020-04-22.
3. D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122. This older work is cited by the two papers above for complete graphs and cycles and supplies terminology relevant to equivalence searches.
