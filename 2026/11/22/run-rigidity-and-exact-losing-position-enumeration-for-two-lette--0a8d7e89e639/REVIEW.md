# Review of the two-letter two-sided subtraction classification

## Correctness — PASS
The proof checks both directions of the P/N criterion. Every candidate P-word has no P-option, and every word outside the proposed regular language has a **specific** deletion into it: first `ba` in the initial `b`-run case, last `ab` entering the terminal `b`-run case, or `ba` at the leftmost singleton `b`-run in the remaining case. These branches exhaust the complement. Positive-run compositions give the binomial formula and the rational generating function; the two-letter deletion minimum plus explicit alternating options prove the sharp lengthwise Grundy maximum. Exhaustive actual-game mex calculations cover all 262143 words of lengths up to 17; separate exact coefficient arithmetic covers 0..200. The proof, not these finite experiments, establishes the infinite claim.

## Originality — PASS against checked evidence
The closest inspected primary text is Inoue and Inazu, *Word Subtraction Games*, arXiv:2611.09157v1, especially the complete two-sided section and its Problem 5.1. The note establishes a Dyck losing language for one-letter Timber moves and non-context-free examples for other regular two-sided moves. It poses the overlapping word-trigger generalization without giving this special two-letter run classification, binomial enumerator, or sharp nimber family. The standard one-sided regular-language theorem does not imply an exact outcome for two-sided moves. Targeted searches for equivalent prefix/suffix-trigger games and published comparable records did not reveal covering claims. Risk: earlier unindexed work or a different terminology may contain an equivalent. This is a *specific-case* result, not a solution to the general problem.

## Value — PASS
The pattern pair `ab`/`ba` is the smallest non-letter case in which the two permitted triggers overlap in both directions. Its complete run-level P/N classification gives an explicit, automata-recognizable solution to a concrete instance of a stated word-trigger generalization question; the rational enumeration quantifies losing positions, and the Grundy upper bound is attained at every length. The contrast with the nonregular Dyck losing language under one-letter triggers is a structural change, not a renamed parameter or a finite table. No general classification of all overlapping triggers is asserted.

## Residual limits
Priority relative to inaccessible or unindexed literature is not guaranteed. The finite checks cannot independently certify every length, and neither a general two-sided regularity principle nor a formula for every individual nimber is claimed.

Self-review: passed. Independent audit: not yet performed.
