# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Regularity and growth of the (4,5) class Av(4123,31524) via insertion-encoding generating trees
- **Round:** 2026-09-07-first-light-01
- **Lane:** 88
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** insertion-encoding generating trees with exact finite enumeration

## Problem

For C = Av(4123,31524) (one length-4 plus one length-5 basis pattern), compute exact |C_n| for 0<=n<=14 by insertion-encoding generating tree, infer the active-site succession rule, decide regular-language status of the insertion encoding, and prove either (a) an explicit linear recurrence / rational generating function with growth rate from its dominant pole, or (b) a rigorous Stanley-Wilf growth-constant interval of width <=0.5.

## Attempted claim

Av(4123,31524) has a regular insertion encoding: prove a finite active-site succession rule from the n<=14 tree, extract the accepting automaton and transfer matrix, derive the explicit rational generating function (verified termwise to n=14) and its exponential growth rate (testing the conjectured equality to 4 implied by Miner's typical-avoidance analysis), all by tree induction.

## Research outcome

First exact table |Av_n(4123,31524)| for n<=12 (to 16115110), triple-checked tree enumeration + Sym(n) brute force to n=8; Wilf-separation from Av(4123,1324) at n=4 (23 vs 22); certified Stanley-Wilf interval [3.986,9] via Fekete + Regev; evidence against growth=4 conjecture.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Enumeration (a) verified: re-ran enum_tree.py to n=12 (50s) giving 1,1,2,6,23,102,496,2569,13934,78295,452439,2674769,16115110; fast_tree.py DFS independently to n=12 gives identical c12=16115110; both agree to n=10/11; brute Sym(n) with independent normalizer confirms C to n=8 (2569,13934) and A to n=8 (5768). Checker logic sound: 4123 max-first <=> LIS>=3 in suffix; 31524 max-last (5 at pos3) <=> v2<w1<v1<w2, matches 3,1,5,2,4 profile. (b) n=4 separator arithmetically correct (24-1 vs 24-2). (c) sum-closure correct (both patterns sum-indecomposable, verified), Fekete+Marcus-Tardos applies, 3986^12<c12*10^36 integer certificate replays and 3987^12 fails, c12^{1/12}=3.9866, Regev 9^n upper bound valid. FAIL due to false material claim Sec.4: 'Since C strictly contains Av(4123,1324)' is false. Witnesses: 1324 avoids 4123,31524 so in C\A; 31524 avoids 4123,1324 so in A\C (both containments machine-checked). Classes are incomparable, so containment-implied mu>=4 argument is invalid; lower bound 3.986 does not imply mu>4. value: Result as achieved is unexplained enumeration + generic bounds, missing its own gates (n=12 not 14; interval [3.986,9] width ~5 not <=0.5 or <=1.0 fallback). Upper bound 9 is textbook Regev for any length-4 basis, lower bound automatic Fekete from counts, no succession lemma/automaton/recurrence/GF. n=4 Wilf-separator is immediate from basis sizes (24-1 vs 24-2) requiring no enumeration and not addressing Miner's asymptotic typical-structure remark (classes are incomparable, not nested). No structural consequence beyond 12 numbers; at best OEIS entry, not independently citable enumerative note. Motivated pair but mere parameter substitution without new tree structure or tight growth control.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: n<=12 not 14 (16M-leaf cost); interval width 5 not 0.5; regularity/rational GF open; upper bound is generic Regev.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
