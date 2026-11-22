# Scientific review

## Correctness — PASS

The proof reconstructs the two-state post-transcriptional burst kernel from [1], verifies that every matrix is nonnegative and uniformly substochastic, and uses an invariant sign cone to compare every nonzero tail for all initial protein counts. A telescoping matrix-product bound and the exact first tail give respectively the explicit total-variation upper bound and optimal-order lower bound. Independent exact-rational tests for 6,000 finite comparisons and symbolic algebra checks passed; these tests corroborate, rather than substitute for, the analytic proof.

## Originality — PASS (literature-bounded)

Jia [1] already derives the burst matrix product and unregulated geometric law and qualitatively observes a large-protein geometric shape; the new claim is only the strict all-tail comparison and sharp-order total-variation convergence bound. Bokes–Singh [2] studies continuous-concentration feedback, and Bokes [3] treats a jump-drift model and steady-state WKB asymptotics. Searches found no directly dominating two-state kernel theorem. The full text of [3] was restricted and could not be assessed, and independent priority assessment remains outstanding.

## Value — PASS

The global stochastic order turns a state-dependent molecular burst mechanism into an interpretable direction-of-effect guarantee for all increasing burst statistics, while the sharp inverse-count rate gives a mathematically justified accuracy scale for the geometric approximation. Both address natural questions raised by the explicit but opaque burst matrices; neither claims finite-timescale validation of the molecular reduction.

## Sources and boundaries

[1] Jia, arXiv:2611.18062v1 (2026), Eq. (5). [2] Bokes and Singh, Journal of Mathematical Biology 74 (2017), 1483–1509, https://arxiv.org/abs/1602.08568. [3] Bokes, DCDS-B 27 (2022), 2129–2145, https://doi.org/10.3934/dcdsb.2021126. See RESULT.md for the complete proof and CHECK.py for reproducibility.

Self-review: passed. Independent audit: not yet performed.
