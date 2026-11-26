# Independent mathematical audit

## correctness

PASS

Lexicographic bits give exactly one encoding per labeled loopless tournament, and the transition table includes all 2^n Boolean states using precisely incoming counts 2,3,5. Indegree-zero peeling removes exactly noncycle states; reverse peel order computes exact first entry depths since each removed state points either to a later removal or a cycle. An independently authored and completed enumeration gave spectra {1} for n=1–5, {1,3} for n=6, and {1,…,9} for n=7; depths were (1,1,2,2,4,9,23). The order-seven maximum-period histogram matched (1633632,30240,329840,25200,30240,21840,11040,5040,10080). Explicit relabeling of the whole extrema sets produced two size-5040 graph orbits for period nine, represented by 9393 and 9514, and one size-5040 graph–state orbit for depth 23, represented by (1721,86). Label and state transformations preserve the update by equivariance. These outputs distinguish a tournament’s maximum period from all periods coexisting in it, and distinguish graph counts from graph–state counts.

## originality

PASS

The map itself and small unrestricted-digraph maxima are prior. The exact spectrum, sharp depth, and two types of extremal orbit count for strict tournaments were not covered by the inspected prime-rule paper or a distinct exact catalogue record. In particular, the complete-directed-graph result uses arcs in both directions and cannot be specialized to one arc per pair.

## value

PASS

Tournaments isolate asymmetry while fixing a single direction per pair, a natural graph restriction for the prime activation rule. The exhaustive spectra locate the first failure of fixed-point-only behavior and show that at the next order all periods up to the maximum appear. Observed sharp slowdown and the orbit counts distinguish genuinely different extremal examples from many label copies. They are useful exact benchmarks for a broader theory of attractors and transients, even without its general solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
