# Scientific review of exact Gini contraction for an ordered path gossip sweep

## Correctness
**PASS.** The statement defines one specific linear map and one quotient seminorm, avoiding any assumption about other edge schedules. The layer-cake cut decomposition gives an exact binary reduction. The triangle inequality quantifies every pairwise update's Gini dissipation; geometric decay of the carried value bounds all binary inputs. Contiguous trailing one-block inputs make every triangle inequality an equality. An explicit successive-ratio inequality proves the exceptional small-size minima and unique balanced optimum from nine agents onward. The asymptotic coefficient follows from the closed formula. The embedded exact-arithmetic checker independently exhausts all binary cuts through 12 agents and reproduces the optimizers, but unrestricted correctness relies on the proof.

## Originality
**PASS, with historical priority risk.** The nearest full-text deterministic gossip treatment by Liu et al. (2011, DOI 10.1109/JPROC.2011.2159689) evaluates eigenvalue/singular-value or induced matrix seminorms, not the sum of all coordinate-pair absolute differences for a fixed ordered path sweep. Their 2010 complete-gossip coefficient uses a Euclidean matrix seminorm, not this Gini functional. Charron-Bost et al. (arXiv:1408.0620, inspected primary text) address general dynamic approximate consensus and time bounds, while Boyd et al. (2006) analyze randomized gossip. Cao (arXiv:2108.07904) gives Gini decay in a stochastic mean-field model rather than the sharp deterministic finite-dimensional coefficient. No equivalent all-dimensional formula was found in the inspected sources or the relevant research index, but absence of an indexed match alone cannot establish global novelty. The 2010 Springer full text could not be inspected in its entirety; its identified statements concern different seminorms.

## Mathematical value
**PASS.** The exact best one-sweep rate measures total pairwise disagreement under a canonical deterministic spanning-path sweep. The dimensional law \(1-\gamma_n\sim8/n^2\), explicit worst-case binary shapes, and transition to balanced extremizers resolve an intrinsic quantitative stability question not settled by qualitative convergence or spectral contraction results. These results identify the sharp finite-stage stability cost of this information-propagation order and support precise comparisons with alternative gossip schedules; no downstream theorem is presumed.

## Limits
No assertion is made for all possible gossip edge orders, weighted means, arbitrary interaction graphs, or powers of the sweep. Further independent literature review is appropriate before asserting publication priority.

Self-review: passed. Independent audit: not yet performed.
