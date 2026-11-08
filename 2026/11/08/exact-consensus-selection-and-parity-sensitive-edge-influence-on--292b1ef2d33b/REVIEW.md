# Scientific review: exact triangular-book consensus selection

## Correctness — PASS

The theorem specifies all parameters, tie conventions and initial-state conditions. Every strict-majority flip decreases the number of bichromatic edges, so convergence to some fixed state is almost sure; the only fixed states are the two consensuses. The entire probability kernel follows from three disjoint hub-configuration cases. With agreeing one-hubs, the initially unstable hubs compete against the zero-valued leaves, and the probability of the necessary consecutive effective leaf changes is an exact finite product; with agreeing zero-hubs, color complementation applies; with opposite hubs, both leaves' tie retention and the hub inequalities give an exact three-way choice. Removing the hub edge changes precisely the activation threshold in the polarized state; its parity difference and the positive quarter limit follow algebraically. Independent exact-count-state and labelled-graph Markov calculations corroborate every asserted boundary and the edge comparison; they are not the infinite-size proof.

## Originality — PASS, with stated priority risk

The closely matching 2014 work of Auletta et al. studies the same local update and asks about existence of update sequences capable of overturning an initial majority. Its analysis is adversarial and does not give this precise uniform-update selection distribution on triangular books. Feldman et al. study a different asynchronous learning model with private-signal tie breaking and not-yet-reported opinions; its star/expander claims do not imply this kernel. Nearby prior results on synchronous split-graph majority, asynchronous minority dynamics, and asynchronous strict majority on complete bipartite graphs do not cover the **added hub edge** in the present random-sequential majority model. The absence of a high-ranking indexed research-literature match is not treated as proof of uniqueness. The remaining risk is a little-indexed equivalent calculation or general stochastic influence model with the book as an unstated corollary.

## Mathematical value — PASS

The probability of the eventually selected unanimous opinion under random update order is a natural invariant, not merely an enumeration of stable states. This theorem computes it for **all** initial configurations on an infinite family of graphs, including ties, and quantifies a meaningful structural intervention: one added hub-hub edge affects the polarized outcome **only** at odd leaf counts, by an exact size-dependent amount. Two initially aligned hubs can still persuade an asymptotically overwhelming opposing population with limiting probability one quarter. Such order-selection probabilities are not determined by deterministic reachability or by the identity of absorbing configurations. The theorem does not claim the more difficult fixation-time law or larger hub cliques.

## Sources and residual risks

- V. Auletta et al., *Minority Becomes Majority in Social Networks*, arXiv:1402.4050 (first public version 2014-02-17): same local majority/retention rule, but worst-case and existential outcome questions.
- M. Feldman et al., *Reaching Consensus via non-Bayesian Asynchronous Learning in Social Networks*, arXiv:1408.5192 (first public version 2014-08-22): related stochastic opinion aggregation under a different initial-information model and tie rule.
- Relevant published dynamical and database records were compared by mathematical implication, not titles alone. No independent external scientific review has been made, and unindexed rediscovery is possible.

Self-review: passed. Independent audit: not yet performed.
