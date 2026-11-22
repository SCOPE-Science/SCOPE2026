# Scientific review

## Correctness — PASS

The claim is an all-finite-horizon stochastic-order statement, not a numerical guess. The exact rational identity for \(T\circ U-U\circ T\) shows the commutator is nonnegative at every positive covariance exactly under \(g+\lambda q\ge1\). The four packet-arrival cases yield the adjacent-swap identity. Monotonicity of every subsequent Kalman map transfers the comparison through arbitrary random suffixes, while conditioning handles arbitrary prefixes. Repeated adjacent swaps prove optimal sorting. Outside the frontier with positive process noise, one positive zero of a concave quadratic gives the unique order reversal. The accompanying verifier replayed 14884 exact-rational assertions, including full enumeration of representative five-observation schedules, without purporting to replace the universal proof. No unproved lemma is used for an essential step.

## Originality — PASS, with residual historical risk

Actual literature comparisons include primary full-text sections of Wu–Ding–Cheng–Shi (2018), Marelli–Sui–Rohr–Fu (2018), Leong–Dey–Quevedo (2015/2016 preprint), and the available Singh–Kamath–Kumar (2019) full text. The former address different combinations of multiple processes, long-run policy monotonicity, stochastic-filter stability, state-adaptive communication and time-stamped fixed-gain packet priority. Closest published related results on deterministic two-sensor **precision** order and infinite-horizon **precision** allocation have different control variables and cannot imply the stochastic dominance of permuted **packet-receipt probabilities**. No previously inspected claim states the general finite-horizon Bernoulli-reliability rearrangement and sharp local frontier. Missing older equivalent rearrangements in the substantial filtering and stochastic-order literature remain possible; two particularly relevant published related full texts could not be fetched, so this is not a priority certification.

## Value — PASS

The result replaces factorial enumeration of fixed sensor assignments with a single sorting operation for all finite horizons, all inhomogeneous noncontractive/enough-noise prediction schedules, and all increasing terminal-risk criteria. The sharp inequality separates a uniform reliability-order policy from a regime with a provable prior-dependent order reversal, providing design guidance about how process innovation and attenuation affect channel sequencing. Equal-precision lossy sensing is a natural communications-limited Kalman problem; the theorem is not a mere relabeling of a deterministic precision-scheduling result.

## Scientific limits

No claims for adaptive policies, correlated channels, unequal precisions, vector filters, or time-average covariance. Historical priority is provisional; separate expert appraisal could discover an earlier equivalent theorem.

Self-review: passed. Independent audit: not yet performed.
