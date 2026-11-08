# Scientific review

## Correctness — PASS

The scalar gradient proposal at state \(k\) has neighboring integers \(k-1,k\); adding downward signed-bias probability \(b_k\) produces an exact pure-death chain. Its independent geometric sojourns determine mean and variance without approximation. Strict convexity and box-constrained KKT inequalities prove the unique global water-filling allocation, including finite-budget endpoints. Harmonic-sum and reciprocal-square-tail estimates prove the fixed-budget mean and variance asymptotics. The Lyapunov third-moment ratio is \(O_B(M^{-1/4})\), yielding the Gaussian limit. The companion checker independently passed 422 exact-rational and asymptotic-comparison assertions. The asymptotic argument, not the tests, establishes the infinite claim.

## Originality — PASS, qualified

The 2022 work of Xia, Massei, Hochstenbach and Koren (arXiv:2202.12276) and the 2023 fixed-point follow-up of Xia, Hochstenbach and Massei (arXiv:2301.09511) define signed-biased stochastic rounding and analyze convergence under different conditions. Neither inspected primary source states an optimal **aggregate statewise total-variation bias allocation** or the resulting halved absorption-time logarithm and Gaussian triangular-array fluctuation law. The ordinary coupon-collector decomposition/Gumbel law and the convex KKT water-filling mechanism are acknowledged as classical, not new. Searches for optimal controlled pure-death allocations, rounding bias, stochastic rounding hitting-time laws, and relevant mathematical finding summaries did not identify an equivalent or dominating theorem. Specialist optimal pure-death chain allocation or quantization work could still imply the result; this is a priority risk rather than a claim of exhaustive novelty.

## Value — PASS

Quantized gradient iterates can stall because the probability of escaping a small positive integer state is proportional to that state. A fixed calibration budget presents a nontrivial resource decision: spend bias uniformly or preferentially on the slow states. The exact solution identifies a provably optimal policy for all finite grid sizes and yields a universal leading-runtime reduction and change of fluctuation universality class. This is useful as a controlled small-state benchmark, while not a performance claim for arbitrary floating-point objectives.

## Closest literature and scope limits

Primary sources: https://arxiv.org/abs/2202.12276 and https://arxiv.org/abs/2301.09511 (methods/convergence analysis, not the aggregate budget optimization). The classical coupon-collector law supplies only the unbiased comparison. The theorem assumes monotone one-dimensional state transitions, initial state \(M\), fixed total-variation budget over all possible states, and a fixed \(B\) in the limit. No comparison with an optimal policy under a per-iteration or occupation-weighted budget is claimed.

Self-review: passed. Independent audit: not yet performed.
