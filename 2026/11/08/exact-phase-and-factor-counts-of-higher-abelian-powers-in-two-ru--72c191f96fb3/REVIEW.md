# Review of the Abelian higher-power spectrum

## Correctness

PASS. The equality of Parikh vectors reduces to equality of sliding-window counts modulo the period. An exact cyclic-interval profile shows that a nonextremal Parikh count appears at only two starting phases, hence is impossible for at least three consecutive distinct short-window positions. Extremes give all-monochromatic concatenations, except at the order-two half-period shift, which produces exactly two phases when both runs are even. The word's primitive period resolves the distinction between phase occurrences and distinct factors. The included direct-enumeration program passes 24,464 cases covering 404,329 starting phases. Those computations are diagnostic; the infinite classification is proved by the interval argument.

## Originality

PASS under the accessible-record comparison; not an absolute novelty certificate. The nearest primary work [1] concerns run-length-encoded Abelian-square and regularity algorithms; [2] concentrates on Abelian squares; [3] treats Sturmian Abelian powers; and [4] surveys known variants. The 2026 paper [5] gives results on Abelian squares of circular binary words, including a two-run boundary, but not the higher exponent and arbitrarily long factor count proved here. Searches on equivalent formulations (cyclic Parikh profiles, periodic Abelian repetitions), stronger covering results, exact counting tables, and implication comparisons found no directly subsuming statement. Existing general algorithms may compute individual instances, which is different from the displayed closed formula. Residual risk: an unindexed or differently phrased earlier classification.

## Mathematical value

PASS. Abelian powers are natural repetition statistics; the entire infinite parameter family is characterized by a closed count rather than instance-by-instance enumeration. The theorem distinguishes starting phases from distinct factors, identifies the order-two resonance and parity boundary, and shows exactly why exponents at least three have a different phase spectrum from exponent two. Its geometric obstruction is a reusable structural lemma for run-length encoded periodic words.

## Sources and limits

[1] https://arxiv.org/abs/1701.02836; [2] https://arxiv.org/abs/1701.00948; [3] https://arxiv.org/abs/1506.02797; [4] https://arxiv.org/abs/2207.09937; [5] hexagon:2610.00473v2. The claim excludes Abelian squares and arbitrary cyclic words; no human bibliographic certification is asserted.

Self-review: passed. Independent audit: not yet performed.
