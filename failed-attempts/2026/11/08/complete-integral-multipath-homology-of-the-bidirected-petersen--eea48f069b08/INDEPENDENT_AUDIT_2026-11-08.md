# Independent mathematical audit

## correctness

PASS

The frozen Petersen KG(5,2) model has 10 vertices and 15 undirected edges, bidirected to 30 arcs. A face is a directed path forest (in/out degree ≤1, no cycles). Frozen verify_petersen_multipath.py contains two complete arc-set enumerators, full Hasse incidence acyclicity tests for ascending/descending toggle matchings, exact signed Morse boundary recursions, unit-pivot integral reductions with zero residual, and an unreduced mod-2 cross-check. It asserts Smith unit-only reductions giving tilde-H ranks (12,1,44,94) in degrees 4–7. Independent fresh exhaustive direct enumeration of all 59203 faces reproduced f_{-1..8}=(1,30,360,2240,7860,15912,18280,11160,3120,240), Euler −39=12−1+44−94. Integer Smith boundaries were examined but not fully re-executed. C is not affected by the decisive prior coverage.

## originality

FAIL

Prior original publication on 2026-10-18 already states the exact SAME fully bidirected Petersen multipath complex, with reduced integral homology Z^12, Z, Z^44, Z^94 in dimensions 4–7 and zero elsewhere, explicitly torsion-free. Its full proof and Result were read, and the underlying GP(5,2) edge presentation is graph-isomorphic to the present KG(5,2); both constructions use vertex-disjoint directed simple paths, including the exclusion of directed two-cycles. Earlier result additionally gives three-connectivity and π4=Z^12. No novel remaining final mathematical conclusion survives, so current claim is covered regardless of new verifier or packaging.

## value

PASS

The complete torsion-free integral homology of a natural ten-vertex cubic graph’s bidirected multipath complex is mathematically useful and nontrivial, especially its four adjacent nonzero degrees. That independently worthwhile invariant is nevertheless ALREADY KNOWN, so scientific originality fails and overall acceptance is rejected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
