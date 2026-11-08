# Self-review: distinct-square diversity in three-one words

## Correctness — PASS

All four gap variables are nonnegative integers, and the statistic counts distinct literal squares, not their occurrences. A square has an even number of ones, hence here zero or two. The former give the floor-of-maximum term; the latter have unique rooted form \(0^x1 0^y\), mapped to the two adjacent one-pairs. The only shared shapes arise when the internal gaps coincide. This establishes the wordwise formula for every gap quadruple. Generating functions follow by independent nonnegative-variable decompositions for each of these terms, not by extrapolating enumeration. The order-five pole gives the mean slope and the weak-composition simplex limit gives the distribution.

The accompanying checker independently counted literal square strings in all 31,465 words through length 30, plus 240 deterministic longer samples. It also compared exact rational-series coefficients through zero-count 50. These finite checks do not certify infinitely many cases; the general proof does.

## Originality — PASS (historical-priority qualification)

Materially inspected original work of Fraenkel–Simpson (1995), Kucherov–Ochem–Rao (2003), Deza–Franek–Thierry (2013), and Brlek–Li (2022) concerns unavoidable/extremal square counts, occurrences, double-square structure, and unrestricted bounds. None of the observed principal statements provides the complete three-one exact square-set count or its aggregate law. OEIS A229617 counts strings with at most three squares, a different aggregate. Existing general inequalities do not entail the exact results. The 1998 Fraenkel–Simpson paper was available only as abstract/bibliographic material; no whole-document exclusion is asserted. A historically unindexed equivalent is possible.

## Value — PASS

Fixed-composition square diversity is a natural structural problem. The three-one family admits interactions between two adjacent one-pairs while remaining exactly solvable. The joint wordwise formula, rational aggregate generating function, and nondegenerate conditional Dirichlet limit give complete and interpretable information beyond a routine finite enumeration or generic upper bound.

## Limitations and validation

Exactly three ones, indexed linear binary words, literal contiguous distinct squares only. The limiting law is specified as a pushforward without a closed density. Full primary-source access was incomplete for the 1998 article. External mathematical validation was not performed.

Self-review: passed. Independent audit: not yet performed.
