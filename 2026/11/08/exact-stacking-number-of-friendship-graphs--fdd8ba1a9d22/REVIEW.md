# Self-review

## Correctness (PASS)
For each blade, the local hub-credit function is proved by direct base configurations and an induction reducing blade mass by two. Summing the exact bound against total mass \(4r\) gives positive final center credit and allows a complete constructive sweep. The lower-bound configurations with \(2r+1\) pebbles on one leaf and one pebble on each of the two outer vertices in every other blade are analyzed by exact pebble-flow accounting. Clearing each frozen blade costs at least one net hub pebble and an initial reserve of two; the marked odd pile cannot supply the required resources to end on the hub, a frozen blade, or the marked blade. Every smaller total has an obstruction. The independent finite-state verifier exhaustively checks all configurations at the alleged threshold through \(r=3\) and the obstruction through \(r=7\). Finite verification is not the proof of the universal claim.

## Originality (PASS, provisional priority)
The 2026 introduction by Csernák and Soukup defines stacking and gives exact values for complete/multipartite graphs, paths, and general bounds, but not a full friendship-graph formula (arXiv:2604.22341v1, full HTML inspected). Their October paper discusses the Almost Stacked Hypothesis and clearing on special classes, not this exact infinite-family value (arXiv:2610.09650v1, full HTML inspected). Fairfax-Ball's tree result does not imply the non-tree case (arXiv:2609.31811v1). Multiple named published-finding corpus overlap queries, the closest graph-family results, and 106 accessible preceding claim summaries did not identify equivalent or stronger coverage. Computational tables for up-to-seven-vertex graphs may already include small cases, and unindexed equivalent results cannot be ruled out.

## Mathematical value (PASS)
This supplies the first located exact infinite-family stacking threshold for a natural clique-bouquet cactus class beyond the graph families treated in the defining paper. The optimal linear count \(4r\), the explicit almost-stacked obstruction, and the local energy-accounting proof are structurally informative, with no dependence on a general conjecture. The claim concerns the whole natural family, not an arbitrarily selected graph instance.

## Closest literature and limitations
See the arXiv sources in RESULT.md. The theorem does not concern arbitrary cacti or generalized windmills with larger clique blocks. The connected-graph small-order computer data discussed in the primary literature may imply individual base cases but not the full infinite theorem. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
