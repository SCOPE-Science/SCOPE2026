# Scientific review

## Correctness: PASS

The unnormalized grounded inverse-trace objective is explicitly defined for every graph and budget in the claim. The arbitrary-profile Schur complement has positive denominator because the leader set is nonempty. Both fixed-hub and free-hub profile optimizations are strict away from matching profiles, and the two rational comparisons identify the exact equality boundary. All leader-set counts use explicit petal orbits. Independent exact-arithmetic matrix construction confirms the derived objective in 2,712 small cases; additional profile tests do not replace the infinite proof.

## Originality: PASS (qualified)

Primary source comparison: Fardad, Lin and Jovanović (2011) establishes the trace-inverse model and develops relaxation algorithms; Fitch and Leonard (arXiv:1407.1569) derives a general joint-centrality equivalent and solves paths and cycles; Patterson, McGlohon and Dyagilev (arXiv:1412.6595) treats paths and rings. Their inspected results do not imply the stated friendship-graph minimizer without the new petal-profile optimization. Existing research records on friendship-graph zero forcing and on windmill graph spectral updates concern other invariants. A potentially relevant 2020 windmill-coherence article was accessible as an abstract but not in full text; its possible relationship to arbitrary leader placement remains a serious publication-priority uncertainty. The absence of a matching search result is not a proof of global novelty.

## Value: PASS

The result is a natural complete classification for a standard stochastic leader-selection objective on a family of clustered networks. The exact threshold identifies when a structurally central hub should be excluded despite its high connectivity; counts and a strict nonnested budget transition give usable design information beyond simply computing one example or repeating a generic relaxation.

## Scope and residual risk

Only simple unweighted friendship graphs, noise-free leaders, and unnormalized grounded inverse trace are covered. The 2020 windmill-coherence full-text access gap and unindexed equivalent results remain originality risks. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
