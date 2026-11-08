# Scientific review

## Correctness — PASS

The statement concerns a fixed crown graph, not a random input graph. The allowed-edge count \(m^2-t\) and its three transition counts partition all currently feasible edges exactly. Maximality excludes any output with two unmatched vertices on either side; the final \(m=2\) transition identifies failure with a one-third conditional event. The first-moment identity and the ordered-pair survival factor are exact and have been checked symbolically. The convergent product bound gives a uniform, explicit \(O((\log n)/n^2)\) error; independently labeled rational state calculations agree with the compressed recurrence through eight labels. The uniform-maximal comparison counts derangements and uses the standard inclusion–exclusion limit. No finite computation is relied on for the unbounded-size conclusion.

## Originality — PASS, with priority risk

Mészáros, *A BK inequality for random matchings* (arXiv:2006.07234, first public June 12, 2020), concerns a matching chosen uniformly from **all matchings**, or from maximum matchings, and proves negative-dependence properties. It neither samples uniform maximal matchings nor analyzes the process of uniformly choosing an available edge at successive steps. Arnosti, *Greedy Matching in Bipartite Random Graphs* (2021), studies the same RANDOM-EDGE rule but averages algorithmic performance over random input edge sets, rather than evaluating a fixed deleted-diagonal complete bipartite graph. Dyer and Frieze's 1991 paper originally studies greedy matching on fixed graphs; only its abstract and other papers' discussions were accessible, not its complete text, so a previously unlocated specialization is a residual risk. Searches for crown graph, off-diagonal rook board and derangement formulations did not identify the sharp \(2/n\) deficit or the contrasting limiting half-deficit under uniform maximal sampling. A failed search alone is not considered proof of historical novelty.

## Value — PASS

In a graph only one matching away from complete bipartite, every maximal matching is either perfect or short by exactly one edge. Nonetheless two natural measures on those maximal matchings behave radically differently: random-edge greedy is perfect with probability tending to one, and the deficit has a sharp \(2/n\) coefficient, while a uniformly sampled maximal matching remains defective with probability tending to one half. The result therefore diagnoses a genuine distributional bias of a familiar stochastic graph algorithm, not merely a new table entry. The exact finite recurrence permits independent numerical assessment, and the convergent factorial-moment method establishes the full asymptotic.

## Limits and literature

The bound applies only to a fixed, unweighted crown graph and the RANDOM-EDGE sampling rule. It does not extend to weighted edges or RANDOM-VERTEX without a new argument. The uniform-maximal comparison is elementary conditional on the classification of maximal matchings; the sharper greedy probability is the central result. The full 1991 Dyer–Frieze text remains an unresolved historical-priority comparison. Independent specialist verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
