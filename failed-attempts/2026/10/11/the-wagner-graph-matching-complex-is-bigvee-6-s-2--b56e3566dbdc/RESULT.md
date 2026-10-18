# The Wagner-graph matching complex is \(\bigvee^{6}S^2\)
## Finding
Let \(M_8\) be the Wagner graph, with vertex set \(\mathbb Z/8\mathbb Z\), cycle edges \(\{i,i+1\}\), and antipodal edges \(\{i,i+4\}\). Let \(\operatorname{Match}(M_8)\) be the ordinary matching complex whose faces are matchings of \(M_8\). Then \[\operatorname{Match}(M_8)\simeq \bigvee^{6}S^2.\]

The result is an exact homotopy statement, not only a homology computation. The Wagner graph is the eight-vertex Möbius ladder: an eight-cycle together with the four antipodal chords.

## Assumptions and scope
Graphs are finite and simple. The ordinary matching complex \(\operatorname{Match}(G)\) has one vertex for each edge of \(G\), and a set of such vertices is a face exactly when the corresponding graph edges are pairwise vertex-disjoint. Here \(M_8\) has twelve edges. No statement is made for larger Möbius ladders.

## Proof
Order the twelve edges of \(M_8\) as the eight cycle edges
\[
01,12,23,34,45,56,67,70
\]
followed by the four antipodal edges
\[
04,15,26,37.
\]
The matching complex has \(105\) nonempty faces, with face vector
\[
(f_0,f_1,f_2,f_3)=(12,42,44,7).
\]

Apply sequential element matching on the face poset. At stage \(j\), for every still-unmatched face \(F\) not containing the \(j\)-th graph edge, pair \(F\) with \(F\cup\{e_j\}\) whenever the latter is also a face and still unmatched. The complete construction gives \(49\) matched pairs. Direct orientation of all \(244\) Hasse covers—matched covers upward and all others downward—is acyclic. Exactly seven critical cells remain: one critical \(0\)-cell and six critical \(2\)-cells.

Forman's discrete Morse theorem therefore reduces \(\operatorname{Match}(M_8)\) to a CW complex with one \(0\)-cell, six \(2\)-cells, and no cells in any other positive dimension. Every \(2\)-cell is attached along a map \(S^1	o *\), so the resulting CW complex is \(igvee^6 S^2\).

## Verification
The accompanying `verify_wagner_matching.py` reconstructs \(M_8\), enumerates every matching face, reconstructs all Hasse covers, replays the sequential matching, and verifies acyclicity by topological sorting of the complete directed Hasse graph. It also independently computes simplicial homology over \(\mathbb F_2\). The boundary ranks are
\[
\operatorname{rank}\partial_1=11,\qquad
\operatorname{rank}\partial_2=31,\qquad
\operatorname{rank}\partial_3=7,
\]
so the reduced mod-two Betti vector is
\[
(0,0,6,0).
\]
The saved verifier output ends with status `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville develop discrete-Morse and star-cluster methods for ordinary matching complexes, including exact homotopy types for paths, cycles, and Dutch windmill graphs. Their full text does not treat the Wagner graph or Möbius ladders. A later paper of Agarwal and Basak studies Möbius ladders themselves, but its stated objects are the independence complex and the **perfect matching complex**, not the ordinary matching complex used here. Thus those results do not imply the claim above.

The ordinary matching complex is equivalently the independence complex of the line graph \(L(M_8)\); searches using both formulations were included in the comparison check.

## Limitations
This is a single finite case and does not establish a formula for \(\operatorname{Match}(M_{2n})\). The full text of the 2026 Möbius-ladder paper was not accessible in the available lawful routes during this check; its title and abstract explicitly concern independence and perfect matching complexes, so it is scientifically distinct, but this access limitation remains a literature-comparison risk. Unindexed theses or private computations could also contain the same finite homotopy type.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first public 2022-07-27; published in New York Journal of Mathematics 29 (2023), 1393–1412. Primary MSC 57Q70.
2. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public 2026-08-31.
