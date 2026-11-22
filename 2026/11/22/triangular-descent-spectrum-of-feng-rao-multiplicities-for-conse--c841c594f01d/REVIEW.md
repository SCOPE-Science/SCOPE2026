# Mathematical review

## Correctness
**PASS.** The normal form \(tn+r=(t-r)n+r(n+1)\) is unique for \(0\le r<n\) and \(t\ge r\). The proof counts all ordered summand pairs in both the no-carry and one-carry cases and thereby obtains a closed formula for every \(\nu_n\) value. Its finite-difference analysis separately handles interior and end-of-block transitions, proving no unexamined decreases remain. The independent reachability/convolution checker passes for \(2\le n\le48\), but no finite test is used as a substitute for the universal proof.

## Originality
**PASS on inspected evidence.** The most relevant primary source, Bras-Amorós (arXiv:2307.16448, Sections V–VII), determines the terminal descent of the sequence, not its full location-and-magnitude distribution. Delgado et al. (arXiv:1306.2862, Sections 2–3 and Theorem 43) determine generalized Feng–Rao numbers of two-generator semigroups rather than this complete adjacent-step spectrum. The earlier manuscript on Feng–Rao numbers treats stable higher-weight quantities. Published mathematical-record searches for the full triangular descent spectrum and its equivalent ordered-pair formulation did not return a stronger covering statement. The main residual risk is that an older Hermitian-code formula or unindexed finite-difference calculation may imply the histogram without using the same terminology. This search result is not proof of priority.

## Mathematical value
**PASS.** The descending transitions of the Feng–Rao multiplicity sequence are the precise obstruction to its local monotonicity and determine where termwise shortcuts may fail. The literature has studied the final such transition; a complete exact list of all earlier transitions and their sizes is a natural, structurally informative refinement. The result covers an infinite arithmetic family, gives a sharp triangular multiplicity law, and identifies the aggregate total decrease, not an arbitrary finite calculation.

## Scope and risk
No claim about concrete code minimum distances, all two-generator semigroups, or external independent validation is made. The proof and checker are supplied; only self-review was completed.

Self-review: passed. Independent audit: not yet performed.
