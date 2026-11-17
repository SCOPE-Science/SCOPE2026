# Independent mathematical audit

## correctness

PASS

The 14-vertex Heawood incidence graph (points P_i, lines L_j with P_{j,j+1,j+3}) has exactly 3^14=4,782,969 labelled states. Deterministic rule 1->2,2->0,0->1 iff adjacent excited yields one successor per state. The original package includes census_indegree.cpp and paths-based alternative. Independently implemented a new C++ 4,782,969-state enumeration: construct all successor indices, peel indegree-zero vertices, traverse precisely surviving cycles for true least periods, then reverse peel order for exact preperiod T and eventual period P. Obtained 55 positive (T,P) classes, 21,099 periodic states, primitive orbit counts {1:1,3:5334,4:224,5:84,6:42,8:168,10:84,14:96}, entry populations T0..10 (21099,305203,1303711,1272154,1100708,526918,168336,42840,17136,12768,12096), no T>10 and all T10 in P4. Exhaustiveness follows from explicit iteration over every integer 0..3^14-1 and correct functional-graph peeling; the calculation is a finite proof, not extrapolation. lcm of periods is 840 so F^850=F^10 and 840 minimal.

## originality

PASS

Best of knowledge: Doba 2018 and Gravner–Lyu–Sivakoff 2018 establish qualitative synchrony/periodic-state and excitation-rate results for general graph Greenberg–Hastings dynamics. Their primary mathematical theorems and searchable full texts do not enumerate the Heawood 55-class entry-time/period table, its eight primitive orbit counts, or sharp ten-update entry bound. Resultary exact-dynamics records concern other specific graphs; no earlier Heawood numerical census identified. A preexisting unindexed exact computation remains possible.

## value

PASS

The Heawood graph is the unique smallest cubic girth-six cage and a canonical finite incidence graph. A complete labelled-state 4.8-million-state functional-graph census yields the exact rare-period spectrum, basin-entry distribution and sharp global transient; these are nontrivial natural benchmark invariants for excitable network dynamics. Finite size does not diminish value because the entire natural model is classified, with exhaustive reproducible evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
