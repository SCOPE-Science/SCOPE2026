# Review of exact bounded-run palindromic defect

## Correctness — PASS

The proof exhaustively classifies palindromic factors by their one-, three-, or five-run form; its two possible five-run centers are distinguished. The inclusion–exclusion terms account exactly for repeated three-run strings. A three-variable minimum/maximum identity then produces the defect formula for all positive integer run lengths. The six-run additive decomposition follows algebraically; the minimal-word characterization follows by deleting the two endpoint letters and using factoriality of rich words. The bivariate run lengths and ordered unequal middle-run lengths yield the stated generating function. The seven-run boundary word's palindrome set is explicitly listed. Independent direct enumeration checks, detailed in VERIFICATION.md, passed, but finite tests are not an infinite proof.

## Originality — PASS, with residual risk

Pelantová–Starosta (2017, https://arxiv.org/abs/1708.06911) ask for minimal non-rich word characterization; their exhibited length-eight example is not claimed here as new. Guo–Shallit–Shur's full 2015 manuscript (https://arxiv.org/abs/1503.09112), linked to their 2016 run-length article, establishes sufficient conditions for richness and growth lower bounds, not the numeric six-run defect, exact local additivity, or bounded-run forbidden-word enumerator. The journal abstract suggests additional qualitative characterization; its final text was unavailable for comparison. Currie–Mol–Rampersad (https://arxiv.org/abs/1908.03169) address repetition thresholds of infinite rich words, not these finite-run defect formulas. Searches of relevant indexed literature and mathematical findings identified no precise equivalent; lack of search hits does not certify global novelty. A stronger uninspected final journal version or unindexed independent classification remains possible.

## Mathematical value — PASS

This gives a complete exact infinite-parameter quantitative invariant for a natural finite-complexity class, an additive local decomposition with a sharp first failure, and the entire bounded-run family of minimal obstructions with a rational length generating function. These connect directly to the established question of identifying minimal non-rich words, while not purporting to solve it in all lengths or for arbitrary run counts. The quantitative information is not obtained solely by quoting the known existence of rich-word families.

## Scientific limitations

Only binary words with at most six runs are covered. Seven-run data is a single sharp boundary example, not a census. The distinct-palindrome enumeration is independent of computed tests. Potential related unpublished or unindexed prior work and differences between available preprint and final journal article remain originality risks.

Self-review: passed. Independent audit: not yet performed.
