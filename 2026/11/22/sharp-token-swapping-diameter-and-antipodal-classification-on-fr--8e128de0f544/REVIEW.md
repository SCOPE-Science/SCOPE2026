# Mathematical research review

## Correctness — PASS
For every integer \(t\ge2\), decompose an arbitrary token permutation into the cycle containing the hub and disjoint cycles on leaves. The known star-only construction gives a legal path of at most \(h+s+q\le3t\) swaps; equality is possible only for hub-fixed perfect matchings. Within-petal pairs are resolved in one edge swap instead of three, ruling those out. For all remaining cross-petal perfect matchings, used swap edges are necessarily connected through the hub. The connected-factorization lemma (proved directly in RESULT.md by tracking cycles and newly connected components) gives \(m\ge N+c-2=3t\), proving exactly the stated antipodal class. Inclusion--exclusion over the \(t\) forbidden local pairs then yields its count. The checker exhaustively enumerates all \(6,120,5040,362880\) states for \(t=1,2,3,4\), including the exact farthest-state class for each eligible case. No assumption about large instances depends on enumeration.

## Originality — PASS, with residual uncertainty
Aichholzer et al.'s tree-swap analysis (arXiv:2103.06707, earliest version March 11 2021) concerns trees, including the star baseline; Bonnet et al. (doi:10.1007/s00453-017-0387-0) analyze complexity and swapping on stars. Neither cited work states the sharp friendship-graph diameter together with its if-and-only-if antipodal classification. Ganesan (arXiv:1111.3114) studies transposition-tree-generated Cayley graphs. Gijswijt--de Meijer (doi:10.37236/12771) treats symmetry rather than shortest-swap antipodes; its full article text was not available to verify any possible incidental metric claim. Kiya et al. (arXiv:2210.02835) study a different consecutive-edge-walk swapping rule. Comparisons against indexed exact swapping results on Petersen and other base graphs concern different metrics. No relevant indexed statement implied the theorem, but no finite bibliography can exclude an unindexed equivalent.

## Value — PASS
The friendship graph is a canonical infinite family of one-articulation block graphs and is the first non-tree extension of a star by the most local possible edges (disjoint peripheral pairs). The exact all-order worst-case cost, unique structural characterization of all extremal token placements and closed antipode count quantify precisely why a fifty-percent increase in legal moves fails to reduce worst-case routing complexity. These conclusions are stronger than another one-instance graph census and provide a natural graph-swap benchmark.

## Scientific limitations
No exact metric is claimed for all pairs of permutations, nor an all-block-graph extension. The included computational tests check only \(t\le4\). Independent checking and historical-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
