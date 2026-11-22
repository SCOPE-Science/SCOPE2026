# Self-review

## Correctness (PASS)

The chromatic–Tutte identity, finite-difference inversion, and Bencs–Csikvári large-girth evaluation theorem give the exact exponential coefficient-curvature limit. The monotone growth of the Tutte exponential base makes the leading finite-difference term dominate at each fixed index. An explicit derivative identity at the sole piecewise transition and strict concavity past it establish the sharp signs, including both boundary cases. The supplemented verifier checks exact rational squares over 7,301 index–degree pairs; finite computations are corroboration, not an infinite proof.

## Originality (PASS, with historical-priority risk)

Zhang–Dong [2] prove the \(j=2\), \(d\ge4\) failure. Their result does not assert a full fixed-index phase transition or the reversal to positive curvature at \(j=d-1\), nor a cubic conclusion. The older Bencs–Csikvári theorem [1] provides the necessary asymptotic evaluations, not the curvature classification. Searches of published mathematical records and other related polynomial work revealed no exact equivalent; unindexed earlier discoveries remain possible. This is a specific new implication of the cited results, not an independent strengthening of their underlying Tutte-growth theorem.

## Value (PASS)

The theorem identifies where the low-index obstruction ends and strict local log-concavity returns across every high-girth regular degree, a structural distinction that is not visible from a single failure at degree two. It also settles every fixed-index asymptotic curvature for cubic regular graphs. The exact frontier is a natural next question for the same chromatic expansion, and gives useful boundaries for investigations of global shape without falsely claiming global unimodality.

## Limits and verification

The proof is asymptotic with fixed indices, provides no numerical girth thresholds, and uses [1] as an external theorem. Positive curvature at all fixed indices is weaker than global log-concavity. See the standalone verifier and `VERIFICATION.md`. Historical priority is provisional and no external mathematical review is claimed.

Self-review: passed. Independent audit: not yet performed.
