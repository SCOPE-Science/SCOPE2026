# Scientific assessment

## Correctness — PASS

The exact state space contains 16,257 values, with the correct bfloat16 subnormal and normal encoding. Explicit rational arithmetic and two independent exact rounding algorithms agree on every successor edge. Orbit-walk and indegree-pruning graph decompositions agree on each vertex's final cycle and tail depth. The separate periodic orbit lists and basin counts together classify every state; a time-limited trajectory sample is not used as proof. Both maps preserve the specified finite state set. The self-contained certificate reproduces all figures from exact integer and rational calculations.

## Originality — PASS within inspected evidence

The 2021 conference paper and the 2023 full journal account describe the self-parameterized logistic design, but report real-map bifurcation/entropy and a different tent-oriented digitization, not the claimed complete bfloat16 logistic graph. The full accessible 2023 low-precision study by Klöwer et al. describes periodic collapse for the ordinary logistic map and generalized Bernoulli map; its exact statements do not determine cycles for the state-dependent gain and specified intermediate rounding. Existing exact classic-logistic binary16 graph reports likewise differ in the transfer map and floating-point format. A related continuous-state attracting cycle near this control does not imply a precise finite-state basin count. Residual priority risk: unindexed hardware notes or published bfloat16 implementations not identified by the searches may contain this exact graph, and a narrow publication-day ambiguity remains for the conference contribution.

## Value — PASS

The bfloat16 attractor basins of a published lightweight chaotic-generator construction are natural, implementation-sensitive invariants. The result supplies the complete graph and quantitative merging of a 2,026-state basin despite 2,205 changed one-step edges. This directly tests the design's advertised broad chaotic behavior under precise low-precision evaluation and is more informative than merely asserting all finite maps are eventually periodic. The state-independent counting measure and exact operator placement are essential limitations.

## Scientific limitations

Only the displayed arithmetic semantics and the full bfloat16 state set are classified. No real-state Lebesgue basin, stochastic-rounding result, field-programmable implementation behavior, or cryptographic certification is asserted. Independent reproduction and publication-priority scrutiny have not occurred.

Self-review: passed. Independent audit: not yet performed.
