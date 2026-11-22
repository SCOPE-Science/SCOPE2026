# Scientific review

## Correctness — PASS

The candidate is a uniform-in-size theorem for all finite cycles \(n\ge3\) with two strictly positive rates \(p>q\) and a positive Poisson reset rate. The master equation gives a two-root recurrence, periodic matching gives a positive normalized law, and the ratio of the negative and positive contributions to each local hopping flux has an explicit closed form. Strict inequalities in derivatives with respect to the bias and root parameter establish a permanently positive half of the edges and unique transverse zero on each remaining edge. Their strict order follows from \(R_{j+1}/R_j=h/x^2>1\). The weak-bias expansion is supported by finite-state analytic perturbation and implicit differentiation. A separately implemented rational stationary solver independently checks the signs and finite numerical examples. Residual scientific risk: only homogeneous rings and hopping-only currents are covered; model changes may invalidate the result.

## Originality — PASS, qualified

The closest exact primary source is Rose et al. (2018), arXiv:1806.01298, whose spectral reset-state and current decomposition covers general chains and whose worked finite-cycle calculation assumes one-way hopping. Its formulas do not state or automatically supply the needed strict all-parameter sign inequalities in the two-way biased cycle. Riascos et al. (2019) work with undirected graphs; Tucci et al. (2020) distinguish gauge-dependent total reset currents from physical local diffusive flux; Sarkar and Gupta (2022) reset comb branches to the backbone. Li and Sun (2025) study biased networks but the accessible article summary concerns stationary measures and hitting efficiency, not this exact cascade. Semantic database searches for edge-current sign reversals, biased ring resetting, and threshold order found only different ratchet, membrane and exclusion-current settings. An implicit derivation from general finite Markov resolvents, and the uninspected full text of Li–Sun, remain priority risks rather than novelty certificates.

## Mathematical value — PASS

The result gives a complete finite-size and rate-parametric classification of which microscopic hopping edges oppose imposed clockwise bias under global resetting. All \(n\) edges are classified, and the exact count, crossing simplicity, ordering, and small-bias law make testable transport predictions not captured by routine stationary-density formulas alone. It clarifies an important observable distinction: a reset-induced counterflow along hopping edges is not a gauge-independent reversal of the overall transported current. This is a structural transport result, not an arbitrary small-parameter census.

## Independent validation and limits

The independent audit has not been performed. Finite exact and numerical checks corroborate but cannot establish a theorem for infinitely many system sizes or rates. Publication priority is provisional pending specialist examination of broader prior literature.

Self-review: passed. Independent audit: not yet performed.
