# Scientific assessment

## Correctness — PASS

For the exactly specified stationary-heading planar active Brownian model, the angular Markov generator gives stationary first and second harmonics and a common exponential angular covariance rate. Integrating their covariances yields the forward drift and both displacement variances, matching the independently published formulas (Baouche et al., 2024, Eqs. 17–18). A monotone-likelihood-ratio comparison between the two lag kernels proves that their ratio strictly decreases across the exact admissible interval. A second strictly decreasing rational function identifies the reset-to-rotation ratio, establishing a complete bijection. Finally the longitudinal/transverse excess ratio has two exact distinct roots, and each branch supports a positive relaxation rate reproducing the same full one-lag covariance. `CHECK.py` passed 1,063 finite diagnostics. The proof, not the sampled checks, establishes the universal statements.

## Originality — PASS, with publication-priority uncertainty

The closest forward paper is Baouche et al. (2024), arXiv:2405.06769, especially its equations (17)–(18) and Appendix C. These **explicitly imply the forward moment formulas and are credited**, but do not assert the two-lag inverse bijection, exact compatibility range, or one-lag full-covariance ambiguity. Kumar, Sadekar and Basu (2020), arXiv:2008.03294, discuss the same physical resetting protocol and forward crossover behavior under a different initial-heading preparation. No covering inverse theorem was identified in the inspected material or targeted literature comparisons. An unindexed inference theorem or a treatment of these deductions as immediate corollaries of published forward formulas is a residual priority risk; absence from search results is not a proof of worldwide novelty.

## Mathematical value — PASS

The observable selection is physically motivated: tracking of a microswimmer's position may be easier than directly measuring its heading. A single finite lag of even the complete position covariance is insufficient in general, whereas the drift plus just two transverse variances gives globally unique physical parameters, exact consistency inequalities, and a constructive inversion with only two scalar root solves. This is a minimal observational design within the specified first/second-moment measurement family, not an arbitrary parameter slice. It does not claim finite-sample statistical stability.

Self-review: passed. Independent audit: not yet performed.
