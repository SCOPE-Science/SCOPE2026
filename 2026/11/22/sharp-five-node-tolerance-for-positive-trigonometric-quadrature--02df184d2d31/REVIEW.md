# Scientific review: sharp five-node trigonometric quadrature positivity

## Correctness — PASS
The unique Fourier Vandermonde weights are represented by a four-point elementary symmetric polynomial. The central weight sign is exactly the sign of a real cosine expression; the sine product denominator is positive. The four derivative signs reduce its global box minimum to the alternating boundary perturbation, which crosses zero once at the stated closed-form radius. Strict and weak positivity boundaries, and negative-weight witnesses beyond it, follow for all five nodes by cyclic symmetry. The included finite checker passed 1059 reproducible consistency checks, not replacing the general proof.

## Originality — PASS (best-knowledge)
Neumayer–Schäfer–Ullrich (arXiv:2610.32699v1) establish high-probability positive exact quadrature from sufficiently many random nodes. Yu–Townsend (arXiv:2202.04722) treat perturbed trigonometric grids, including negative weights for sufficiently large grids and general stability estimates; their bounds do not give this exact five-node threshold. Peherstorfer (arXiv:1001.2451) supplies general positivity characterization but not the sharp independent-jitter minimax. The nearest queried mathematical records concern three-node degree-one random jitter or special node collisions rather than this finite five-node universal sign problem. Earlier unindexed equivalent results cannot be excluded.

## Mathematical value — PASS
The minimal fully interpolatory five-node degree-two rule is a natural accuracy/robustness benchmark. Its sharp radius is an explicit guarantee under independent node jitter, with an adversarial configuration at the precise positivity failure frontier. This resolves the natural fixed-grid perturbation design problem rather than reporting a numerical sample or a generic sufficient inequality.

## Limits
This does not classify arbitrary larger grids, other exactness degrees, stochastic failure probabilities, floating-point weights, or multidimensional quadrature. Outside the prescribed minimal five-node family the radius need not apply. Independent expert mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
