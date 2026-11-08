# Self-review

**Claim considered:** Exact noise-stability law for minimum spanning tree edge sets of cacti under independent edge refreshing, with strict log-convexity in cycle length, sharp cycle-profile extremizers and many-cycle Poisson transition.

## Correctness — PASS

Conditioning on the number of refreshed edges proves the one-cycle same-maximum probability. Cactus cycles have disjoint edge sets, so their change events are independent. The key nonstandard shape lemma is proved by computing the pushforward density of the diagonal-plus-independent copula and showing it is strictly decreasing; integration by parts gives an explicitly positive moment representation and strict log-convexity. Pair-balancing establishes extremizers, and binomial size biasing proves uniform small-noise control. The enclosed exact checker confirms the relevant low-order cases and finite inequalities (554 assertions); it does not establish the infinite result.

## Originality — PASS (qualified)

The closest directly inspected publications are Israeli and Peled (arXiv:2306.07357, K_n MST metric noise), Mathwieser and Çela (arXiv:2211.15611, query optimization over cactus MSTs), and Dombry, Ribatet and Stoev (arXiv:1503.05748, generic concurrence of maxima). The general facts that cactus MSTs remove each cycle's largest edge, and that concurrence is a known probabilistic concept, are prior results. Inspected material and targeted mathematical database searches did not establish the specific partial-refresh shape inequality, associated cycle-length optimizers or Poisson edge-change law. A historically equivalent result under different terminology remains possible.

## Value — PASS

The finding gives the full distribution of the number of cycles whose deleted MST edge changes under random weight refreshing, for every finite cactus. It identifies how cycle-length balance shapes exact stability across all positive noise rates and proves a size-dependent sharp transition in an expanding graph family. The invariant is natural for perturbation robustness, not an arbitrary graph-table entry.

## Limits and inspection

Weights must be iid atomless with independent refreshes; conclusions are not asserted for arbitrary graphs or correlated weights. Earlier general concurrence results, MST noise results and cactus decomposition are credited. An independent mathematical audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
