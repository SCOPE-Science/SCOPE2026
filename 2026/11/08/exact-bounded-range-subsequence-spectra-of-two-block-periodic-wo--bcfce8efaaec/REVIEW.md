# Scientific review

## Correctness

**PASS.** The claimed identity is derived from the unique run decomposition of each pattern, rather than extrapolated from computation. The main critical step is the initial-phase optimization and greedy resetting at every letter switch, which is proved for all positive block lengths in RESULT.md. Once the span identity holds, the rational series follows by a disjoint even/odd run-count enumeration. The sharp threshold follows from a nonnegative slack variable; the odd/even parity case and the exceptional one-symbol source block are separately handled. The packaged reference verifier checks all asserted formulas on exhaustive finite families, without claiming these finite checks prove the universal statement.

## Originality

**PASS, conditional on the literature actually accessible.** The closest directly relevant primary article, Kosche–Koß–Manea–Pak (2022, arXiv:2207.09201), defines bounded-range subsequences and studies algorithmic matching, analysis, hardness and circular words. Its material inspected does not give a two-block periodic host's run-decomposed exact span spectrum, its bivariate rational counting series, or the sharp universality threshold. Adamson et al. (arXiv:2407.18599) count absent unrestricted subsequences under a fixed universality index; Menon–Singh (arXiv:2306.07870) count indexed occurrences, not minimum spans of distinct patterns. Research-record and accessible previous-claim comparisons found no implication-equivalent statement. Residual risk: an unindexed exact periodic-source formula or an uninspected stronger theorem might subsume the result.

## Mathematical value

**PASS.** A primary motivation of bounded-range subsequences is that generic analysis is algorithmically difficult. The canonical block-periodic binary family is the smallest natural parameter family beyond the alternating word: it models repeated dwell times for two events. The result classifies, for every pair of dwell times and every target length/window bound, exactly which patterns appear by their minimum span and counts all of them with a rational generating function. The exact sharp window threshold exhibits changes between minimum block lengths one, two and at least three, with explicit extremal witnesses; this is an infinite, structured classification rather than a finite table or a generic algorithm restatement.

## Literature and limitations

First-public source date for the guiding bounded-range model is 2022-07-19 (arXiv:2207.09201v1). Related primary materials include arXiv:2407.18599 and arXiv:2306.07870. All empirical tests are finite; the proof explicitly covers all positive parameters. The novelty assessment is bibliographic, not a guarantee of global priority.

Self-review: passed. Independent audit: not yet performed.
