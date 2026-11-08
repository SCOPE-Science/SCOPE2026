# Self-review

## Correctness — PASS
The domain is positive four-run binary words with an exact partition into identical nonempty subsequences. Divisibility of symbol totals forces the common counts. The first and last positions force every copy to start with zero and end with one, so each common copy has two or four runs. Four-run copies require each original run divisible by the number of copies. Two-run copies require exactly the floor/ceiling threshold, with an explicit constructive allocation proving sufficiency. The disjoint-type union gives the exact composition count by inclusion–exclusion. Riemann-sum counting gives the asymptotic and elementary differentiation gives the sharp minimum. These arguments cover all positive parameters including one-unit edge cases. From the actual `VERIFY.py`, 286 direct state-space partition comparisons and 1,372 exact-composition comparisons passed, along with six large-size density probes. Finite checks are not the proof.

## Originality — PASS, qualified
The closest exact published result is Grytczuk–Pawlik–Ruciński (2025), Proposition 2, which explicitly settles FOUR runs and TWO identical copies. Its criterion is recovered at two copies, and priority for that boundary case is credited. Grytczuk–Pawlik–Pleszczyński (2023), arXiv:2308.13882, investigates shuffle squares and generalized permutations, not the fixed-copy-count, all-integer-q exact four-run composition spectrum. Bulteau–Jugé–Vialette (2023) studies avoiding shuffled squares, and later shuffle-closure discussions are not an exact formula for the selected four-run subclass. Actual semantic record searches for shuffled cubes, q-fold copies, four runs, floor/ceiling conditions and fixed-composition densities returned no governing prior statement. A prior four-run scattered-pattern occurrence result concerns maximizing counts of copies of a specified nonidentical pattern and does not imply partitions into q *identical disjoint* subsequences. Unindexed equivalent results remain possible.

## Value — PASS
The exact class criterion is nontrivial beyond the already known two-copy case: different numbers of copies create arithmetic thresholds, and two-root-type overlap requires explicit subtraction. The fixed-Parikh rational floor-sum counts all four-run candidates without enumerating colorings; the limiting density is a natural global invariant showing an unexpected unique minimum at three copies. This is a complete infinite-parameter classification with direct use as a decision rule and counting benchmark, rather than an arbitrary finite sample.

## Sources and limitations
- Grytczuk–Pawlik–Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (2023), introduction and Section 2.
- Grytczuk–Pawlik–Ruciński, *Shuffle squares and nest-free graphs*, arXiv:2503.22043 (2025), Section 3.1, Proposition 2.
- Bulteau–Jugé–Vialette, *On shuffled-square-free words*, Theoretical Computer Science 941 (2023), 91–103; its accessible abstract concerns avoidability.
- *Subsequence covers of words*, 2025, doi:10.1016/j.tcs.2025.115216; accessible discussion defines arbitrary shuffle closure.
- Relevant semantic-index searches and a comparison with an earlier mathematical result. Residual risk: unindexed shuffled-cube literature or an unexamined full-text theorem might subsume the formula; no external or independent review has been conducted.

Self-review: passed. Independent audit: not yet performed.
