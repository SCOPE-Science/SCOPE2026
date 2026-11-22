# Scientific review

## Correctness — PASS

Independence of Poisson counts yields the stated product of taxon detection probabilities and sum of expected detections. The first and second derivatives are written explicitly in RESULT.md; strict concavity gives unique optima and complete boundary handling. Exact rational polynomial factorization and the quadratic root analysis give every listed interval, including the two reversed objective disagreements. A monotone exponential ratio excludes reentry with fewer than three targets. The standalone `verify.py` independently checks exact identities and 64,800 supplementary objective comparisons. Numerical checks do not replace the analytic global proof.

## Originality — PASS on inspected evidence, with residual risk

How et al. (2024) directly motivates heterogeneous primer sensitivity and sampling-effort questions, while Baetscher et al. (2023) choose empirically complementary markers. Fukaya et al. (2022) provide a stronger Bayesian framework for expected-richness design but under different decisions and objective. None of the inspected primary texts gives the exact opposite all-target-versus-richness allocation intervals or sharp three-target reentry theorem. Related mathematical occupancy and budget-allocation work covers other experimental designs and utilities; the general methods of concavity and exponential detection are not asserted as original. Historical priority beyond the material examined remains provisional.

## Value — PASS

Two legitimate objectives, expected biodiversity richness and detecting *every* priority species, lead to incompatible survey choices in both directions at two disjoint budgets. The smallest possible number of taxa for the all-target enter/exit phase is proved. The all-positive assay sensitivities rule out the trivial explanation that one assay cannot detect some targets. The result is a reproducible benchmark for model selection, not a field-calibrated recommendation.

## Limits

The model assumes known-present targets, independent Poisson counts, fixed constant per-effort detection rates, and continuously divisible effort. It excludes false-positive reads, sequencing competition, biological uncertainty, and assay overhead. Some broader historical optimization literature may cover equivalent formulations. Independent external validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
