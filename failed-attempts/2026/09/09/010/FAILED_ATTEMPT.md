# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Replayable Tutte census and Fano-minor extremals for 3-connected binary matroids on 7-9 elements
- **Round:** 2026-09-07-first-light-01
- **Lane:** 298
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Matroid Theory
- **Method:** basis-exchange enumeration with deletion-contraction Tutte evaluation and explicit minor-sequence testing

## Problem

From committed explicit basis families, enumerate the 3-connected binary matroids on 7, 8, and 9 elements; for each, recompute the full Tutte polynomial by logged deletion-contraction with an independent rank-oracle replay, certify presence/absence of Fano (F7) and dual-Fano (F7*) minors by explicit deletion/contraction sequences, and isolate (a) the matroid with largest maximal Tutte coefficient and (b) the Fano-and-dual-Fano-avoiding matroid with maximal number of bases, each with basis-exchange/sequence certificates.

## Attempted claim

Complete replayable table over the committed 3-connected binary slice on 7-9 elements: every Tutte polynomial with deletion-contraction log plus rank-oracle cross-check, every F7/F7* verdict with explicit minor sequence, and identified extremals: largest maximal Tutte coefficient overall, and most bases among F7- and F7*-free members.

## Research outcome

Dual-recomputed Tutte table with F7/F7* witnesses and two extremals (max coefficient 18: M9_S8e; most bases among Fano-free: M7_MK33 with 81) over 9 committed 3-connected binary matroids; independently replayed VERIFY_OK with stdlib-only scripts.

## Why this attempt failed

Failed axes: originality, value.

originality: Substantive comparison shows no new mathematical content beyond mechanical evaluation of standard definitions on a chosen 9-tuple. Merino et al. 1203.0090 compiles family Tutte formulas/techniques (not a per-matrix census, but shows Tutte computation is standard); Bjorklund-Kaski 2003.03595 gives hardness/algorithms for binary-matroid Tutte (shows computation is standard tool, not a census); Eberhardt 1407.6666 derives Tutte from cyclic flats (alternative standard method); Sage catalog provides Fano/FanoDual/AG32/S8/K33 as individual database entries with on-demand Tutte/minor testing, so Tutte polynomials and minor verdicts for the natural members are mechanically implied by existing tools. Textbook theory mechanically implies several verdicts: F7 self-minor with no F7* (rank 3 vs 4 on 7 elements), dually for F7*, and M(K33) graphic=>regular=>F7/F7*-free by Tutte's excluded-minor characterization. The only technically unlisted numbers (Tutte/minor verdicts for ad-hoc variants M5_X8a/M6_X8b/M8_AG32e/M9_S8e and the two slice extremals) are brute-force outputs over an arbitrary committed list containing a duplicate isomorphism type (auditor proved M3~M5 via explicit perm (2,1,3,4,0,5,6,7)), not a substantive synthesis; dual recomputation (deletion-contraction vs subset expansion) is agreement of two textbook definitions, and explicit (D,C) witnesses are standard search output. A failed-search log or timestamp does not establish priority, and distinctness from SCOPE026 (68-type complete rank-3 census) does not confer novelty on an incomplete arbitrary slice. value: Strongest headline (full Tutte table + F7/F7* witnesses + largest-max-coefficient 18 at M9 and most-bases-among-F-free 81 at M7 over the 9-member slice) is an unexplained enumeration over an arbitrary incomplete scope, not an independently retrievable exact invariant of a natural object. The natural class invoked (3-connected binary 7-9) contains far more than 9 types; delivered slice is admitted committed-not-exhaustive with duplicate M3~M5, and extensions M8/M9 (single added columns [0,1,1,0]^T and [1,1,1,1]^T) and variants M5/M6 lack pre-computation motivation. Famous-member values are known or mechanically implied (Sage on-demand Tutte; M7 F-freeness from regularity; F7 self-verdicts trivial), while ad-hoc-variant values were not motivated before computation and have no shown downstream need as benchmark beyond generic solver testing. Slice extremals are artifacts of the arbitrary 9-set (e.g. max over two F-free members). Certification (dual replay, witnesses, VERIFY_OK) is solid but per instructions does not rescue an arbitrary object or unexplained number. No new general theorem, completed census, or narrow datum satisfying all of motivated-object + unknown non-implied value + reasonably needed precise fact is present.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Committed 9-member slice, not an exhaustive census of all 3-connected binary matroids on 7-9 elements; no isomorphism-completeness claimed. Extremal uniqueness is within the slice only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
