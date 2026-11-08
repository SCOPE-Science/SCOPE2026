# Scientific assessment

## Correctness

**PASS.** A fourteen-vertex ternary configuration has a unique base-three integer encoding from zero through \(3^{14}-1\), and each update is computed from the explicitly specified cubic incidence graph. The indegree-peeling theorem for finite functional graphs proves that the surviving vertices are exactly periodic states and that reverse peeling supplies exact entry times. Source `verification/census_indegree.cpp` implements this argument without heuristic stopping. An independently structured memoized-trajectory program based on an alternative Fano-plane line listing agrees on all fifty-five nonzero classes. The counts cover all \(4782969\) states. Periodic-cycle and maximal-transient witnesses have been checked directly. Arithmetic is exact and finite.

## Originality

**PASS with historical-priority qualification.** The 2016 preprint by Gravner--Lyu--Sivakoff, inspected in its later full journal text, supplies global circulation criteria and asymptotic activity, not a Heawood-specific labelled-state census. Doba's full 2018 study similarly proves equilibrium-versus-periodic dichotomy and a maximum-cycle-density law, but no Heawood census or exact transient distribution. Searches for Heawood/Fano incidence excitation, alternative cellular-automaton terminology, complete functional-graph orbit counts, and the exact numerical signatures identified no covering statement. Earlier exact computations outside indexed sources remain possible, and the original 1978 model article was not inspected in full. Binary majority rules on the same graph and three-state excitation rules on other graphs are mathematically different maps and do not imply these counts.

## Mathematical value

**PASS.** The Heawood graph is the canonical smallest cubic graph of girth six, simultaneously bipartite, symmetric and the incidence graph of the Fano plane. Its full Greenberg--Hastings functional-graph census is a natural finite benchmark that the general asymptotic circulation criteria do not determine. The eight-period spectrum includes the unusual coexistence of temporal period five and period fourteen, while all states at the sharp ten-step delay feed exclusively four-cycles. These exact quantitative phenomena are not recoverable from the graph's girth or diameter alone. The result is intentionally finite and does not claim a general graph-family law.

## Limitations and comparison

The work is an exhaustive computer-assisted finite proof, not an infinite theorem or a hand enumeration of every state. The full transition map is generated reproducibly from source, and the embedded table is checked against two implementations. The exact-census novelty assessment remains conditional on the accessible literature search. The current result does not classify orbit equivalence under the graph automorphism group and does not provide periods for other thresholds.

Self-review: passed. Independent audit: not yet performed.
