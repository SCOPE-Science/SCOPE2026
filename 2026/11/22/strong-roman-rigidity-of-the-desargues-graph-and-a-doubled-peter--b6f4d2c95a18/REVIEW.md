# Self-review

## Correctness — PASS

The graph is explicitly defined by inclusion between two- and three-element subsets of a five-element set. The analytic bound \(3w\ge2n\) follows by assigning each zero vertex to a valid two- or three-labeled defender: such defenders can support at most two or three zeros, respectively. This yields \(w\ge14\). At weight fourteen the bound forces exactly four label-multiplicity cases. All \(7{,}441{,}920\) labeled assignments in those cases are enumerated by the delivered self-contained C++17 checker, which verifies the original strong Roman condition, not an approximate relaxation. Exactly 40 survive, split 10+30 by whether the one-labeled vertices are complementary or incident. A separate Python permutation-orbit implementation independently reconstructs all 40 and validates their defender conditions. The complete 780-pair Hamming histogram and direct adjacency checks prove that the first nonempty exchange edges occur at distance six, where the graph is a doubled Petersen subdivision with radius five and diameter six.

## Originality — PASS with priority risk

The 2015 original preprint introduces the invariant and establishes general theoretical results, but does not state an exact minimum-labeling census or an optimal-Hamming-exchange graph on \(H(5,2)\). The 2026 exact-value paper considers different graph families. The closest technical record on ordinary Roman functions of the Desargues graph uses a distinct domination constraint, so its 340 minimizers and reconfiguration theorem do not determine the present 40 minimum strong Roman functions. No indexed result found implies the doubled Petersen subdivision. Index coverage is incomplete, and the complete text of one relevant technical record could not be retrieved; neither absence from search nor graph partition alone proves publication priority.

## Value — PASS

The 20-vertex Desargues graph is an especially natural cubic incidence graph, with vertex classes indexed by subsets of five points. The result adds more than an isolated small minimum: it completely characterizes the optimal allocations, establishes a sharp local-mobility threshold, and exhibits a canonical reconstruction of the Petersen graph from the optimum configurations. The precise doubled subdivision connects a defensive graph-labeling invariant with a classical Kneser geometry. Finite scope and unresolved historical priority remain limitations.

Self-review: passed. Independent audit: not yet performed.
