# Scientific review — ternary Hamming ordinary four-cut topology

## Correctness (PASS)
The defining predicate is tested on all induced four-vertex subgraphs, not on triples or on independent quadruples. The dual has all 0-, 1- and 2-faces and precisely the cardinality distribution \((27,351,2925,1593,324,54,0)\). A full 5,274-vertex, 17,793-arc Hasse-cycle check validates the 1,877 vertex-toggle pairs. Its only Morse cells are one vertex, 1,398 two-cells and 121 three-cells. The signed integral boundary has rational rank 12 and an explicitly specified rank-12 determinant \(-1\), so its image is a primitive sublattice. This gives \(H_2(D)=\mathbb Z^{1386}\) and \(H_3(D)=\mathbb Z^{109}\), with neither hidden torsion nor other reduced groups. Elementary cell slides and degree-based attaching-map classification establish the dual sphere wedge. Integral Alexander duality reverses degrees to 22 and 21. The separate raw mod-two boundary calculation and Euler characteristic concur; they are corroboration, not the integral proof.

## Originality (PASS against inspected sources)
The originating foundational paper, arXiv:2304.13675, and its sequel, arXiv:2407.08158, do not state this four-cut classification. The closest indexed all-alphabet Hamming result and exact ternary three-cube result are **ordinary three-cut**, not four-cut, and cannot determine the four-subset predicate. Indexed four-cut results for the four-dimensional binary hypercube and the two-dimensional four-by-four rook graph use different graphs. Direct semantic searches for connected quadruples, Hamming four-cut Alexander dual, the exact Betti values, and Cartesian clique-power aliases returned no stronger covering theorem. This is best-knowledge originality, not a guarantee that uncatalogued calculations do not exist.

## Value (PASS)
The ternary three-cube is the smallest fully ternary product with three Cartesian clique factors. Passing from three-cut to four-cut changes the local connectedness condition and produces a topologically nontrivial mixed-dimensional integral dual wedge; the exact 109 lower-degree original homology classes give a concrete nonshellability obstruction. The complete homotopy type of the dual and torsion-free homology of the original supply a motivated standalone invariant of a canonical graph, rather than an arbitrary subset or isolated unverified table entry. No broader theorem is required for this finite classification to be useful.

## Closest literature and limitations
See arXiv:2304.13675 and 2407.08158, as well as published published-finding corpus records `397f4b160890` (all-alphabet three-cut) and `de2f98e55b1f` (four-cut on different strongly regular graphs). A full-text match could remain outside the indexed and inspected publications. The proof and code are finite and specific to \(H(3,3)\); neither the original four-cut homotopy type nor symmetry representations are claimed.

Self-review: passed. Independent audit: not yet performed.
