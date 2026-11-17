# Scientific review: Heawood joint-period classification

## Correctness

PASS. Both explicitly defined deterministic maps on the Fano incidence graph were completely enumerated over all \(3^{14}=4{,}782{,}969\) labelled colorings. Two algorithmically different exact C++17 programs agree on all ten pairs of eventual least periods, the 512,736 total discrepant states, and the two disjoint period-halving populations. Indegree elimination and path recursion have separately justified finite-functional-graph correctness. A third presentation checks the two witness trajectories and verifies incidence isomorphism when converting their encodings. `verification/replay.py` compiled and replayed both complete programs against the captured output; no random sampling is substituted for exhaustive coverage.

## Originality

PASS, qualified. The published GHM-only Heawood classification establishes the GHM marginal, but cannot assign a CCA period to each original coloring. General finite-graph CCA/GHM theory gives synchronization/activity statements rather than this exact labelled pair census. The biclique pointwise-equality theorem is inapplicable because the Heawood graph is not complete bipartite. The earlier joint Petersen and Frucht comparisons concern different graphs and document only the eight-to-four discrepancy. Searches using Heawood, Fano, cyclic contact, refractory dynamics, both model names, period-halving aliases and all three numeric totals identified no statement covering this Heawood joint table. Exact priority cannot be proved by search, and the complete 1993 source text was unavailable.

## Mathematical value

PASS. The smallest cubic graph of girth six is a natural geometric incidence network for testing how two canonical three-state excitable dynamics disagree from the **same** initial state. The exact joint distribution is a canonical complete finite classification, not an arbitrary subset: it determines all period-agreement basins and shows the second, ten-to-five collapse absent from the earlier ten-vertex Petersen and twelve-vertex Frucht comparisons. It distinguishes qualitative activity or individual period marginals from a much finer cross-model invariant that may guide similar graph comparisons. No unproved universal generalization is inferred.

## Closest references and limits

The exact Heawood GHM census, the biclique CCA/GHM comparison, and the arbitrary-graph excitation-activity theorem are the nearest mathematical results. The finite computation is reproducible, but historical priority and external mathematical validation remain open. All claims are confined to the explicitly specified fourteen-vertex Heawood graph, three colors, threshold one, synchronous updates and eventual least temporal periods.

Self-review: passed. Independent audit: not yet performed.
