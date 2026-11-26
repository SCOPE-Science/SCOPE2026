# Independent mathematical audit

## correctness

PASS

Rook distance is Hamming distance, so the only forbidden triples are 144 three-corner L shapes (72 nonadjacent pairs, two middle vertices each). Independently recognized the same rule by requiring every selected square to be alone in at least one of its selected row or column: a violation supplies an L, and conversely. Enumerated the f-vector (16,120,416,632,240,16), so the maximum facet dimension is five. Reconstructed the 670 disjoint pairs on the nonempty face poset and topologically sorted all 5312 oriented covers. The critical cells are one vertex, 98 three-cells and one four-cell; discrete Morse theory gives a homotopy-equivalent CW model, not a claim of elementary simplicial collapse to an abstract wedge. Independently reduced the signed boundary of the critical 4-cell in DAG order using 191 nonzero unit-pivot updates. Each update subtracts the boundary of the matching upper cell, with its orientation determined by the position of the deleted vertex. The zero residual in the full 3-chain group leaves zero Morse boundary; neither torsion nor nullhomotopy is inferred from finite-field Betti numbers. Below the sole 4-cell the CW model is a wedge of 98 three-spheres; Hurewicz identifies π₃ with H₃ there, so zero integral attaching degrees prove nullhomotopy and the claimed wedge.

## originality

PASS

The star-forest description, all face counts, maximum facet dimension, and even the set of maximal dimensions of the same board are covered by prior enumerators. The integral wedge type, specifically the 98 three-spheres and one four-sphere with null integral attachment, is not explicitly or mechanically obtained from those counts. The closest inspected integral homotopy theorem has three rows, not four. Pass applies to the homotopy classification, not to the classical or enumerative inputs.

## value

PASS

Determines the complete wedge type and the two nonzero reduced integral homology groups of a natural board complex, despite maximal simplices in dimension five. This is genuinely different data from face enumeration: identifying the wedge requires verifying a null attachment. The balanced board is a useful exact reference for the broader problem of topologizing graph general-position sets or bipartite star forests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
