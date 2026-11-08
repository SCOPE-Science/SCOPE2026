# Scientific review

## Correctness

PASS. The proof supplies exact hypotheses and normalization: synchronous one-step motion, fixed independent with-replacement offers, positive geometric waits and a starting vertex already counted. The optimality argument uses count-chain monotonicity and deterministic alternation, so the greedy policy is simultaneously all-deadline optimal. The likelihood-ratio comparison is reconstructed through strictly ordered geometric factors and log-concave convolution; summing the cross-product inequalities gives the exact strict-even parity statement. The expectation identity follows from maxima of coupled independent collector times. A standalone labeled-state checker independently confirms hundreds of finite exact CDF identities. Finite checks are not used to prove the infinite theorem.

## Originality

PASS with historical-priority qualification. Georgakopoulos–Haslegrave–Sauerwald–Sylvester (arXiv:1911.05170) introduce the limited-offer random walk, but their paper's relevant statements concern general graph cover/hitting bounds, complete-graph asymptotics and computational complexity, rather than this exact all-size bipartite stochastic order. O'Neill (2023) proves monotonicity for a distinct linear-rate occupancy model, not for the nonlinear discovery probability induced by multiple simultaneous offers. The classical log-concave likelihood-ratio convolution lemma is explicitly attributed and not claimed as new. An older greedy edge-exploration walk is a materially different sampling rule. Remaining risk: a differently titled specialized coupon-collection theorem might imply the new inequalities.

## Value

PASS. The cover-time decision problem for controlled random walks is generally hard. Here an infinite family has a single policy minimizing the entire cover-time law, with an exact start-side stochastic ranking, parity equality at every odd deadline and a sharp universal one-step upper bound for its expectation gap. The nontrivial structural step is a likelihood-ratio comparison across changing geometric-stage arrays; neither optimality alone nor an ordinary expected-time calculation implies that order. This goes beyond an isolated example or a routine finite census.

## Closest literature and scope

The closest source is *The Power of Two Choices for Random Walks* (2019 preprint, 2022 journal), whose inspected introduction, table of known cases, strategy-complexity section and conclusion do not assert this theorem. The complete 2023 open-access occupancy article supplies the strongest available related parameter-stochastic-order result but uses linear birth rates. The theorem applies only to independent uniform offers with replacement on complete bipartite graphs; no extension to arbitrary graphs or weighted choices is claimed. Independent historical verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
