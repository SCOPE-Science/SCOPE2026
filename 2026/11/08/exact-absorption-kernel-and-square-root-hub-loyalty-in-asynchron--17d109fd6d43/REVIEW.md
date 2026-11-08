# Review of exact random-sequential majority absorption on friendship graphs

## Correctness — PASS

The proof treats the full labelled terminal kernel, not just scalar hub-switch probability. A mixed outer pair has one unhappy endpoint while the hub retains its label. Conditional on \(a\) supportive, \(b\) opposing and \(j\) mixed pairs, the hub's rank among \(j+1\) relevant updates is uniform and it switches exactly when that rank is at most \(b-a\). After switching, previously resolved homogeneous pairs remain frozen, and unresolved mixed pairs follow the new hub; another hub switch is impossible. The rank/subset law normalizes exactly. Multinomial averaging and an elementary integral yield the two exact global probabilities; a CLT and uniform integrability give \(\sqrt{\pi k}\,p_k\to1\). Exact rational full-state recursion verified every terminal mass for \(10,920\) labelled states across the first six graph sizes; finite checks are corroborative only.

## Originality — PASS (qualified)

Auletta et al. (arXiv:1402.4050v1) give a sequential majority framework but address existence of successful update sequences, not the probability of each labelled absorbing configuration under random updates. Mossel et al. (arXiv:1207.0893v1) focus on synchronous majority aggregation; Feldman et al. (arXiv:1408.5192v1) use private unannounced signals and different tie conventions. The inspected source statements do not imply the present kernel. Semantic and bibliographic searches also tested zero-temperature alignment, windmill/friendship graphs, and sequence-based aliases; no covering statement was found. Direct sequence-database access was incomplete, and an equivalent theorem in unindexed literature remains possible.

## Mathematical value — PASS

The kernel solves a natural stochastic-selection problem on a complete infinite family of hub networks, for every initial labelled state. It shows quantitatively that local leader reversal occurs at an inverse-square-root rate even though unanimous agreement occurs at an exponential rate. This distinction is not fixed by a general energy-decreasing convergence theorem or by knowing which absorbing states can be reached. Absorption time, different tie rules and unequal selection rates are outside the claim.

## Limitations and sources

Primary comparisons: E. Mossel, J. Neeman and O. Tamuz, arXiv:1207.0893; V. Auletta et al., arXiv:1402.4050; M. Feldman et al., arXiv:1408.5192. Relevant inspected open-access material was confined to the identified sections and targeted full-text searches; priority is qualified. The independent exact computations are available in the accompanying two scripts. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
