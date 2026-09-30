# Independent Audit — 2026/09/14/028

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `392dcf40984a8996d977b2b485fb10ed10d404e6`  
**Audited current source tree:** `392dcf40984a8996d977b2b485fb10ed10d404e6`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — FAIL

FAIL. The program does not implement Dawson's Kayles (octal 0.07). In Dawson's Kayles a move removes exactly two adjacent pins; from a row of n, striking positions k,k+1 leaves rows of lengths k and n−k−2. The record instead removes the struck pair together with their immediate neighbours and uses lengths max(k−1,0) and max(n−k−3,0), which is a different game. The mismatch is already decisive at n=4: under actual misère Dawson's Kayles, an end-pair move leaves a row of length 2, which is P, so n=4 is N; the submitted census labels n=4 P. An independent recursion for the actual 0.07 rule gives single-row P values through 36 of {2,3,7,8,12,16,17,21,22,26,30,31,35,36}, not the submitted list.

## Originality — FAIL

FAIL. The claimed object/result pairing is invalid because the computation concerns a different deletion rule. The exhaustive ledger may be original data for that altered game, but it is not an original result about Dawson's Kayles and cannot inherit the 0.07 literature framing.

## Scientific value — FAIL

FAIL AS SUBMITTED. A complete exact enumeration for a precisely named game could be useful, but a mislabeled ruleset defeats reproducibility and comparison with the misère-quotient literature. The package would require a new record with corrected game definition and motivation, or a complete recomputation for the actual 0.07 rules.

## Independent checks

- compared the encoded split formula with the standard 0.07 move rule
- verified the n=4 contradiction by hand
- independently memoized the actual misère 0.07 game through n=36 and obtained a different P-set
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The independent P-list is included only as a diagnostic of the rules mismatch; this audit does not claim a literature-priority result for that list.
- The submitted recursion appears internally consistent for its altered pair-plus-neighbours rule, but that does not validate the Dawson's Kayles headline.
- Open-access sources were sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/14/028
- https://www.cut-the-knot.org/Curriculum/Games/DawsonKayles.shtml
- https://theory.stanford.edu/~blynn/play/summer.html
- https://arxiv.org/abs/math/0609825

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
