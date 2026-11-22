# Scientific review

## Correctness

**PASS.** The two protocols differ by the single rank-one transition change out of the outward-facing left-wall state. Resolvent subtraction and two boundary equations give an exact identity for the generating function of *cumulative*, rather than instantaneous, first-passage differences. All factors after removal of \(f-b\) have nonnegative Taylor coefficients, yielding the all-time order. Reachability proves strictness for every starting state when the corridor has at least three sites. The two-site inward-start exception is incorporated explicitly. Positive rates ensure almost-sure absorption. The packaged `check.py` independently reconstructs both Markov kernels and verifies 17,760 exact rational coefficient identities and sign assertions across 40 instances, not an infinite proof.

## Originality

**PASS, qualified.** Marris and Giuggioli, arXiv:2404.13360, Sections II and VII, formulate both boundary protocols and numerically compare first-hit probability peaks; Section VI gives mean first-passage calculations. Their broad first-passage machinery is the closest prior coverage, but the assessed *uniform stochastic-order sign theorem* and its nonnegative rank-one CDF-factorization are not asserted in the inspected text, figures or conclusions. The continuous-time first-passage literature and related searches do not establish the same assertion under the same lattice boundary conditions. There remains a specific risk of an unindexed equivalent theorem or derivation that may imply the sign claim.

## Mathematical value

**PASS.** The known protocol comparison distinguishes intermediate-time probability peaks, but that by itself cannot decide the optimal reflection rule for all possible deadlines. A full first-order stochastic dominance statement is a stronger, decision-relevant transport theorem: it supplies one protocol choice simultaneously for every deadline and every increasing cost of hitting time, across persistent and antipersistent regimes, with an exact parameter-independent threshold. The anti-persistent reversal and full state-uniformity are not routine single-parameter numerical refinements.

## Sources and limits

Primary: Marris–Giuggioli (2024), arXiv:2404.13360, original submitted 20 April 2024, especially equations (1), (34), Figure 9, Sections VI-VII and Appendix A. Contextual: Malakar et al. (2018), arXiv:1711.08474, on continuous-time run-and-tumble first passage. The complete-stochastic-order theorem is restricted to a fully absorbing endpoint and the two specified left-wall protocols; partial target reactivity or two-sided reflection are not covered. No independent scientific audit was conducted.

Self-review: passed. Independent audit: not yet performed.
