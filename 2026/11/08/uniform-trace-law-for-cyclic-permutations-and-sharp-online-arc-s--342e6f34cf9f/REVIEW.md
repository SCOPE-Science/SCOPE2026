# Independent mathematical audit

## correctness

PASS

An all-one witness forces S to be contained in a directed Hamiltonian cycle, so every proper such support is a directed path forest. With n−1 queries, taking all but one positive contracts n−2 arcs to two ordered blocks and forces the supposedly negative arc. The full cycle also fails since n−1 positive arcs force the last one. Conversely any directed path forest with at most n−2 arcs extends to a Hamiltonian cycle by joining tails to successive heads in cyclic block order. For a specified trace, keep the f positive arcs inside their blocks and reverse the cyclic order of the blocks from such a witness. If there is a negative query, there are at least three blocks, so none of the forward quotient arcs is in the reverse quotient cycle. If there is no negative query the original completion suffices. To count, a subset of j forbidden arcs treated as required contracts with the f positives to n−f−j≥2 blocks, giving (n−f−j−1)! directed completions, without a reversal quotient; inclusion–exclusion proves the formula. The path-component count n! binom(n−1,k)/(n−k)! follows by cutting an ordering of all n labels and dividing by the permutations of its n−k nonempty blocks. In an online tree, a depth-(n−1) all-positive branch would have n−2 distinct initial queries and only one consistent hypothesis left; it cannot split again. This proves the upper bound and the shattered support gives the lower bound n−2, including n=3. Independently enumerated exact traces for n=3,4,5 corroborated the formula and support coefficients. The frozen checker was read but not executed; its finite test is no substitute for these arguments.

## originality

PASS

The assessed result is the full directed-cycle arc-trace classification, including strict trace positivity, the support profile and sharp adaptive dimension. Credit cycle contraction and inclusion–exclusion as standard; the factorial count in isolation is a direct application. Earlier undirected tour results have substantial overlap in the learning question, but their statements about unoriented edges do not imply the directed criterion or the unique directed completion used for the online bound. No inspected source covers the complete directed profile or the same online theorem. Priority is assessed only to the extent of available evidence.

## value

PASS

The result classifies every feasible shattered query support in a natural concept class and quantifies exactly how many hypotheses survive each trace. In particular the multiplicity depends only on k and f, not on path layout. The same forced-completion boundary proves that adaptivity cannot raise the optimal depth, rather than just equating two numerically computed dimensions. This combines an explicit structural explanation, sharp boundary and complete support counts; no value is assigned to inclusion–exclusion or a small finite table alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
