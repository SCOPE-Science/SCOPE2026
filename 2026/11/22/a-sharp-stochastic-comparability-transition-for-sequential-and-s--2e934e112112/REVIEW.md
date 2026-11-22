# Review of a sharp wheel-parking stochastic-comparability theorem

## Correctness — PASS
The stated domain is every finite wheel \(K_1\vee C_n\) with integer \(n\ge3\). The exact first-priority mixture gives the greedy law; the hub-plus-rim maximal-independent-set decomposition gives the static law. The cyclic \(2\)-or-\(3\)-gap count proves the Perrin recurrence and the strict singleton CDF witness at \(n\ge8\). A first-choice recursion gives the exact path-mean generating function. Its factorial remainder is bounded for every \(n\ge20\). The cubic spectral representation of the static cycle polynomial provides a uniform upper bound \(\mathbb ET_n<0.42n\). Combining these proves a strict wheel mean advantage for \(n\ge44\). A reproducible Fraction-arithmetic checker covers every integer \(8\le n\le43\), and independently enumerates all vertex orders and maximal independent sets for small wheels. The exceptional finite cases were checked explicitly. The integer-indexed infinite conclusion is analytic, not extrapolation from experiments. Re-execution of `verify.py` yielded 455 passing exact assertions.

## Originality — PASS under inspected evidence
The closest 2026 primary study establishes first-order sequential domination on paths and cycles, counterexamples on other connected graphs, and a subcubic conjecture; it does not state a complete wheel-family comparison. The publicly indexed wheel result *Rare-hub variance inflation in random greedy adsorption on clique-joined cycles* already gives the exact greedy wheel mixture and its mean scaling; those ingredients are credited, and neither supplies the **static** wheel distribution or the all-integer strict mean comparison. The published indexed cycle results derive individual greedy-output probabilities and uniformity exceptions; they do not compare the wheel's two occupancy cardinality laws. Classical Perrin enumeration explains the static count, not the whole sharp comparison. A related prior local-graph parking family in an accessible research ledger uses clique bouquets, not wheel rims, and has a different stochastic-comparability phase diagram. Search results and these implication comparisons support novelty at the stated narrow scope, but cannot certify exhaustive historical uniqueness.

## Value — PASS
The new comparison addresses the natural finite-size problem posed by the two standard jamming ensembles on a simple connected graph family. It identifies **exactly** where stochastic comparability changes, at eight rim vertices, and proves that every larger wheel has an unexpected two-sided risk profile: more catastrophic hub-only outcomes yet larger mean occupancy under sequential dynamics. The joint tail-versus-mean mechanism is useful whenever stochastic dominance is proposed as a measure of sequential adsorption performance, not merely as a numerical anomaly for one small graph.

## Closest literature and limitations
- Higuita-Diaz, López and Roldán-Correa, *Stochastic Dominance in Discrete Parking Processes on Graphs*, arXiv:2611.14718v1, 10 November 2026, especially the model definitions, cycles, counterexamples and conjecture.
- *Rare-hub variance inflation in random greedy adsorption on clique-joined cycles*, public research record dated 8 November 2026, with an exact greedy wheel mixture and fluctuation analysis.
- *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles*, public research record dated 18 October 2026, which proves a pointwise cycle-output phenomenon, not this wheel stochastic comparison.
- Bisdorff and Marichal (2008) for cycle MIS/Perrin enumeration, and Krapivsky (2020) for the one-dimensional adsorption law.

Only uniform priorities and simple unweighted wheels are covered. A hidden or unindexed equivalent result remains a historical-priority risk. No independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
