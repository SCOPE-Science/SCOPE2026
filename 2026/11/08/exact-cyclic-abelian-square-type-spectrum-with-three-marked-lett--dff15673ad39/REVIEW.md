# Scientific review: three-marked circular Abelian-square types

## Correctness

**PASS.** The proof explicitly defines cyclic factors of length at most the full word, types as half-length and half-Parikh vectors, and the odd-length three-marker domain. The critical lemma derives all nine integer-start comparisons and reduces them to a necessary-and-sufficient interval for a chosen consecutive zero pair. This yields the complete type set: zero-free types from the longest one-run and exactly-two-zero types from three gap intervals. The containment of the intermediate-gap interval and the full-range property of the largest-gap interval give the exact total formula. The only baseline gap occurs at half-length half the largest gap when that gap is even; an additional small-gap type supplies its missing prefix contribution. Boundary cases with adjacent zeros and length three are included. Direct exhaustive and randomized cross-checks passed; correctness in all lengths rests on the proof, not extrapolation.

## Originality

**PASS, subject to historical-priority risk.** The directly motivating October 2026 Hexagon v2 full text (particularly its Section 5, Proposition on two runs and Conjecture on non-equivalent types) contains neither an exact formula for three scattered minority letters nor a theorem proving every prefix inequality for that family. Its general theorem is about distinct factor strings, not the weaker quantity of equivalence classes, and its two-run formula does not include three isolated zeros. The 1997 circular lower bound is only \(\lfloor(n+1)/4\rfloor\), and the 2026 sparse-letter result treats linear, not circular, factors. A previously reported two-marker circle theorem also covers a different hypothesis. Searches of accessible published records and a comparison with the two-marker statement did not identify an implication-equivalent three-marker classification. The 1997 primary full text and all potentially unindexed literature were not exhaustively available, so independent historical priority remains open.

## Value

**PASS.** This resolves every prefix condition of a recent explicit open conjecture on a natural infinite three-marker class, while determining the individual types and a gap-based closed formula rather than merely a bound. Exact three-gap dependence is a plausible inductive starting point for more markers and separates circular from linear sparse-letter mechanisms. This is not a numerical extension of a table: all odd lengths and all positive three-gap choices are covered by a structural proof.

## Literature and limits

Primary source: D. Bhattacharjee, *The minimum number of distinct abelian squares in a binary circular word*, Hexagon hexagon:2610.00473v2, https://hexagonmath.org/2610.00473v2 ; earliest public version v1 October 22, 2026. Earlier framework: Fraenkel–Simpson–Paterson (1997), Simpson (2018), and Fazekas–Mammoliti–Mercaş–Simpson (2026). The conclusion does not cover four-marker or unrestricted binary circles. The finite verifier provides corroboration, not independent certification of the general theorem.

Self-review: passed. Independent audit: not yet performed.
