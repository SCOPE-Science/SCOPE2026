# Scientific review

## Correctness — PASS

The conditional Poisson-arrival argument gives the exact path-integral regression. Lloyd nearest-center reassignment is legitimate for arbitrary binary count partitions. The exact threshold score follows from a Poisson shift identity. Uniform tail control proves finite-rate attainment, while the standard-normal bound is certified globally by an explicit positive double integral with strict equality only at a zero threshold. Wasserstein-two quantizer stability, uniform integrability of squared standardized counts, and compactness establish all high-rate limit and optimizer quantifiers. The standalone implementation passed 1,182 independent finite-law and grid checks. Those finite tests do not prove the asymptotics; the proof does.

## Originality — PASS, provisional priority

Closest published problems concern queue-delayed Poisson path reconstruction using full-count packets and area-error loss (Wang–Chen–Ephremides 2019), image inference from many binary Poisson pixels (Chan–Elgendy–Wang 2016), and rate-constrained Gauss–Markov sampling with quantized measurements (Arafa et al. 2020). None of the inspected pertinent source statements implies the all-encoder one-bit Poisson path-area Bayes optimum or its globally optimal sampling time. Standard Gaussian scalar quantization and the factor \(2/\pi\) are explicitly prior art, not the novelty. Other source families, especially older continuous-time estimator quantization, leave an acknowledged historical-priority risk; the available broad paper abstract concerns a noisy signal-plus-white-noise observation model rather than the present exact count process.

## Value — PASS

A strict one-bit measurement budget is a natural sensing and quadrature constraint for cumulative arrival streams, including photon-count systems. The exact formula permits finite-rate joint site/cutoff optimization. The theorem quantifies an unexpected high-rate gap: carefully centered one-bit thresholds retain more than half the integration variance while a fixed nonzero-presence indicator loses asymptotically all such information, and the optimal time nevertheless converges to the full-count optimum. No application-performance guarantee beyond the model is asserted.

## Limits

Only one predetermined noiseless sample, known rate, deterministic binary encoding, and squared Bayes loss are covered. The finite-rate maximizing integer cutoff is characterized algorithmically, not in closed form. The literature search cannot prove absolute novelty; independent validation and priority assessment have not been performed.

Self-review: passed. Independent audit: not yet performed.
