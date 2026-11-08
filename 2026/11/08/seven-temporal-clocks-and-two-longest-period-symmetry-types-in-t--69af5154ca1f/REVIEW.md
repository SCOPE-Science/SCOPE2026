# Scientific assessment

## Correctness — PASS

Every one of the \(3^{16}\) labelled configurations is included by an exact finite functional-digraph traversal. Recursive indegree peeling, cycle traversal and reverse topological propagation are sound for a map with one outgoing edge at each state. A second implementation uses an independently coded successor and forward trajectory memoization. Their 55 exact cycle/class rows agree. A separate group-action calculation checks all 1,920 affine automorphisms and exactly traverses the 12,000 representatives of the two longest periods. The source code and outputs are supplied. Integer overflow and excessive-path guards are explicit. The claim does not depend on extrapolation from samples.

## Originality — PASS, with limits

The closest primary finite-graph general theory is Gravner–Lyu–Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, especially Theorem 3 and its proof: it characterizes synchronization and limiting excitation activity, not full labelled temporal-cycle multiplicities or full automorphism orbits on the Clebsch graph. The earlier Fisch–Gravner–Griffeath model paper, arXiv:patt-sol/9303005, studies lattice metastability rather than these finite counts. Standard folded-cube graph properties are prior art. Semantic research-index and literature queries for the Clebsch/folded-cube three-color excitation census did not reveal a covering item. Historical priority cannot be established conclusively by a failed search, and a differently named earlier exact enumeration remains a residual risk.

## Value — PASS

The five-regular Clebsch graph is the unique strongly regular graph with parameters \((16,5,0,2)\), a highly symmetric extremal and Ramsey-related graph. The exact nonlinear recurrent and transient populations supply a finite benchmark for excitation-wave theory; the unexpected periods thirteen and sixteen and the unequal 480/1,920 symmetry splitting of longest cycles are structural invariants not captured by a simple period-bound check. The object and invariants have independent motivation before numerical enumeration. The assertion is deliberately finite: it does not claim an infinite-family extension or a general theorem about all folded cubes.

## Limits and nearest literature

The characterization is limited to the explicitly defined folded five-cube and the synchronous threshold-one, three-color GHM rule. Gravner–Lyu–Sivakoff's general activity theorem is broader qualitatively and remains acknowledged; it does not imply the exact finite census. The source search is not exhaustive proof of priority. The computational evidence has not received external independent audit.

Self-review: passed. Independent audit: not yet performed.
