# Independent mathematical audit

## correctness

PASS

The actual finite Pappus LCF model [5,7,-7,7,-7,-5]^3 has 18 vertices, 27 edges, bipartition 9+9 and independence number 9. Two exact subset recurrences give all 2^18 independence values, then determine the entire face poset at each threshold. The frozen verify.py explicitly constructs all 9 augmented face sets, performs deterministic toggling, tests every Hasse incidence by complete directed topological sort, and leaves b_k=(1,10,55,202,481,688,460,64,1) critical cells in dimension 18-2k with the augmented empty vertex paired. Removing this pair gives one critical vertex and the higher cells, hence integral sphere wedges by Forman; for k9 gives S0. Independent re-enumeration of ALL 2^18 masks reproduced the 9 face totals (262143,262098,261297,254118,220071,138000,48876,10140,1023) and the signed reduced Euler sequence equal to the stated b_k. These checks support the exact finite claim, with full Hasse sorting inspected as code rather than re-executed here. Purity dimension 17-k and nonzero lower-dimensional homology establish nonshellability for k≥2.

## originality

PASS

New parts are precisely the five interior total-cut homotopy types k=4,5,6,7,8 with ranks 202,481,688,460,64; low levels k1–3 are credited as pre-existing. Bayer et al. and Carnero Bravo treat different graph families, and an indexed connected-bipartite robust-clique result subsumes k3 but not all higher thresholds. Ordinary Pappus five-cut complexes use disconnected induced complements rather than independent-set complements and are not the same complex. No exact Pappus k4–8 full series was identified in semantic searches or examined primary family statements.

## value

PASS

For a canonical 18-vertex symmetric cubic Levi graph, determining every nonvoid level and the previously missing five middle integral homotopy types is a natural complete classification. The non-shellability at all nontrivial levels provides a structural topological property rather than a random isolated numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
