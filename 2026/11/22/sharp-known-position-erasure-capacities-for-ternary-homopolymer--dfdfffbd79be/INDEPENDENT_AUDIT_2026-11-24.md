# Independent mathematical audit

## correctness

PASS

Known-position erasure recovery means that each coordinate puncturing map is injective on the code. Two distinct source words collide in some coordinate puncturing if and only if their Hamming distance is one. I independently checked the two frozen literal certificates without running either uploaded script: I generated the valid words by recursively extending each prefix with a different final symbol, indexed all puncture fibers by (erased coordinate, remaining word), verified code admissibility and injectivity in each fiber, and used an exact multiset comparison to verify that the listed pieces partition the word set. I checked every cyclic consecutive pair including wraparound and every paired edge for sharing a puncture fiber. The exact output (n, words, fibers, odd cycle length multiplicities, disjoint edges, matched lower/upper bound) was (5,48,156,{15:2},9,23) and (7,192,912,{21:8},12,92). Each odd cycle bounds its contribution by its length rounded down after halving; each edge contributes at most one. Cross-piece edges do not weaken this upper bound, and the separately checked code witnesses meet it.

## originality

PASS

The defensible claim is the pair of exact independence numbers with certified strict deficits from the half-size bound on the labeled graphs. The known-erasure equivalence, the graph model and the half-size bound are not credited as new. The strongest distinct available comparisons use weaker Hamiltonicity-type information, different coding parameters, or a different channel; none established these exact values in the inspected evidence.

## value

PASS

The optimum is the natural maximum number of distinguishable messages with a fixed constrained source and one known erasure. The exact results decide that the simplest universal matching/Hamiltonian upper bound cannot be saturated and quantify the deficits at two small odd lengths. The 192-state case in particular removes four messages from that bound; a researcher benchmarking coding or exact recoloring-graph methods can use the true cutoff and the structural certificates, rather than an unresolved interval or an unaudited solver value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
