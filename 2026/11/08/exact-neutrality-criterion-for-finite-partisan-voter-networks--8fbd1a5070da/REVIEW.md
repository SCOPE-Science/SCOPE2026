# Scientific review

## Correctness — PASS

The statement specifies a finite connected simple undirected graph, a fixed binary preference at every vertex, and a strict homogeneous partisan bias. The proof reconstructs the exact continuous-time transition rates from the microscopic copying rule. An active edge contributes \(\varepsilon(p_i+p_j)/(4m)\) to the generator of degree-weighted positive mass. Dynkin stopping at the almost-surely finite consensus time proves the exact occupation correction. Evaluating the generator at singleton-positive states proves that universal neutral exit probabilities force cross-preference edges. Testing a general linear martingale on singleton-positive and singleton-negative states forces its coefficients to be proportional to vertex degree, and then forces the same colouring. The star exit probability and first-change waiting time follow exactly. The checker uses exact rational arithmetic, but the finite tests are not substituted for the all-graph proof.

## Originality — PASS (qualified)

Llabrés–San Miguel–Toral (arXiv:2606.05062, 2026) defines the microscopic process and separates active edges by preference; its pair-approximation Eq. (20a) already displays a difference of same-preference active-link densities, so the basic *form* of bias-induced drift is not claimed as novel. Its analysis, including appendices and discussion, concerns network pair approximations, stationary local ordering and simulations, not the exact every-initial-state finite-graph exit law or equivalence with the existence and uniqueness of linear martingales. The paper's balanced-preference convention is not needed for the present finite-graph theorem. Llabrés et al. (arXiv:2301.09563) derives approximate stochastic exit probabilities on complete networks. Masuda–Redner (2011) examines preference-biased mean-field evolution; Sood–Antal–Redner (2008) and Suchecki et al. (2004) give degree-weighted conservation for the unbiased network voter process. The new assertion is the *sharp topology–preference if-and-only-if and uniqueness* result with a finite-population exact fixation interpretation.

Targeted searches for equivalent formulations, broader network-voter results, exact fixation tables and same-source reductions did not uncover a covering statement. These searches do not establish global uniqueness. Remaining originality risk: the conclusion could be implicit in an unindexed general theory of weighted voter dualities or in a source not retrieved; the 2026 edge-type equation supplies a short route to one direction of the new equivalence.

## Value — PASS

The theorem identifies a nontrivial structural boundary at which a system with arbitrarily strong (but non-frozen) heterogeneous partisan preferences nevertheless preserves an exact neutral fixation law. The complete characterization, uniqueness of the conserved linear statistic, and occupation formula distinguish this family from arbitrary strongly biased networks. The star consequence shows that a single high-degree initially positive agent can have the same fixation odds as all initially negative leaves together while the decision delay becomes unbounded near complete reluctance; it separates consensus odds from consensus speed. These are natural finite-population questions in network social dynamics, not arbitrary parameter substitutions.

## Limitations and closest literature

The result is restricted to the microscopic homogeneous-bias, static undirected model, excludes the unbiased and frozen endpoints from the equivalence, and does not estimate generic graph consensus times. The most relevant antecedent is Llabrés–San Miguel–Toral (2026), especially its active-edge decomposition; classical unbiased degree conservation is also strongly related. Neither numerical checks nor record searches prove novelty. The title and results do not assert empirical social effects or independent validation.

Self-review: passed. Independent audit: not yet performed.
