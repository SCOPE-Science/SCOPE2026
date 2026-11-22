# Scientific review

## Correctness — PASS
The theorem specifies the complete one-sided fixed point, coding, and all nonnegative power exponents. The proof establishes every adjacent block pair, derives a weighted maximum recurrence for all real letter weights through a strengthened boundary-placement induction, and applies it to positive and negative indicator weights. The centered incidence identity \((2I+R)^2=3(I+R)+J\), together with \(I+R=-R^2\) on coordinate-sum-zero vectors, proves the exact spread recurrence \(g_{k+2}=3g_k\). The binary sliding-window argument guarantees no missing intermediate frequencies. Summation gives the closed even/odd expressions, including \(k=0\). Both embedded programs were replayed from the included source files; their bounded checks are not substituted for infinite reasoning.

## Originality — PASS against checked material
The 2026 source [1] treats a three-letter morphism with **three** repeats, and the closely related extension [2] claims all repeats at least four; both motivate studying the two-repeat three-letter case, but neither states its exact power-scale complexity. The 2026 binary-alphabet two-repeat result [3] is a different coding and gives logarithmic growth, not the ternary-modulo-three square-root law. A 2024 Parikh-collinear theorem [4] assumes rank-one incidence and cannot apply to the rank-three morphism here. The weighted boundary lemma and generic recurrence have strong antecedents and are not proposed as original. The specific exact resonance formula and growth contrast are the scoped new claim. Searches cannot exclude unpublished or unindexed duplicates, and independent priority examination has not occurred.

## Value — PASS
The fixed point is the digit-two count modulo three in base three, a natural automatic digit statistic; its binary coding asks how many occurrence frequencies are possible in windows. The new result completely determines the Abelian-type count on all geometric scales, giving nontrivial parity oscillation in the scale index and a square-root law. It exposes a sharp contrast with the published binary-parity coding and supplies a computable benchmark for general multi-residue digit-count words. Its validity does not require a downstream theorem or an all-length complexity characterization.

## Sources and risk
Key primary comparison: Allouche–Rampersad–Rigo–Shallit–Stipulanti, arXiv:2610.03837v1; complete checked mathematical statements in two published records listed in RESULT.md, and the Parikh-collinear theorem arXiv:2405.18032. Historical priority and the possibility that a stronger general framework implies the exact small-parameter formula remain residual risks.

Self-review: passed. Independent audit: not yet performed.
