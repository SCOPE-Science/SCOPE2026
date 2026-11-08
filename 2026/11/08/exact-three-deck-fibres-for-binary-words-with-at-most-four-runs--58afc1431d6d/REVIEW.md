# Scientific assessment

## Correctness — PASS

The proof first separates words with fewer than four runs by subsequence count signatures. It reconstructs a four-run source uniquely from its two length-three mixed triples when its starting bit is fixed. Comparing opposite-start sources produces \(ad\,t(t-1)=0\), so they can collide only as fair reversal pairs. Four double-counting identities establish sufficiency. The unequal patterns \(0010\) and \(0100\) separate every remaining pair at deck order four. A bounded factor-pair census counts each doubleton once. The independent dynamic-programming verifier checks all claimed restricted classes through length 28, four-deck injectivity through 24, and exact arithmetic tests through 300. Its finite scope is stated.

## Originality — PASS (with bibliographic limitations)

The 2026 paper *Deck Reconstruction for Restricted Word Classes* already proves a stronger four-deck *upper bound* for the larger class with at most two runs of ones. That component is explicitly credited, not represented as novel. Earlier fair-word literature recognizes the fairness equation and nonpalindromic length-seven examples. The proposed original statement is instead the exact three-deck doubleton-or-singleton classification for at most four total runs, its necessary-and-sufficient four-positive-run equation, and the all-length divisor census for the restricted code size. The inspected sources do not state or imply this complete fibre result, though an unindexed equivalent cannot be ruled out.

## Value — PASS

The claim resolves every ambiguity class, not merely a reconstruction upper bound, for a natural finite-run source family at every length. Such exact fibres directly yield optimal in-class zero-error reconstruction code sizes and expose how reversal symmetry creates the unique possible failure mode of the three-deck, while the fourth deck removes it. The restricted-source qualification is essential: no unrestricted code claim is made.

## Relevant literature and remaining risks

Angal et al. (2026), arXiv:2610.41110, Theorem 1.3; Richomme (2025), arXiv:2510.07159, fair words section; Chrisnata et al. (2019/2021), distinct deck enumeration; Golm et al. (2022), gapped decks. Possible equivalent restricted three-deck classifications outside the indexed material remain a research risk. Independent scientific validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
