# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified Guy-Smith non-periodicity lower bound for the open octal game 0.007 (Treblecross) through heap 200
- **Round:** 2026-09-07-first-light-01
- **Lane:** 207
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Game Theory
- **Method:** Sprague-Grundy DP with Guy-Smith non-closure scan and per-period failing witnesses

## Problem

For the open octal game 0.007 (Treblecross) on heap sizes 0<=n<=200: compute Sprague-Grundy values by DP from the octal code, then prove a certified Guy-Smith non-periodicity lower bound — i.e., exhibit, for every candidate pair (preperiod q<=Qmax, period p<=Pmax) in a stated box, one explicit failing index where the required window equality breaks — establishing that eventual periodicity, if it holds, must have preperiod exceeding Qmax or period exceeding Pmax.

## Attempted claim

Certified Guy-Smith exclusion bound for octal game 0.007 (Treblecross) through N=200: exact logged Grundy table G(n), n<=200, plus for each candidate (preperiod q<=Qmax, period p<=Pmax) in the stated box one explicit failing index refuting window equality, proving that any eventual period satisfies q>Qmax or p>Pmax (stated Qmax/Pmax fixed by the scan, e.g. all p<=34 and q<=52-classical-scale box at minimum).

## Research outcome

Certified Guy-Smith exclusion bound for open octal game 0.007 through heap 200: exact logged Grundy table plus per-pair failing witnesses excluding all (preperiod<=100, period<=100), exceeding the topic minimum box (52,34). Fully machine-checked via independent replay.

## Why this attempt failed

Failed axes: value.

value: The headline exclusion (Q*>100 or P*>100, certified on [0,200]) is a tiny arbitrary-box observation that adds no independently retrievable knowledge. (a) Mechanically implied by long-published data: G(0..200) is a prefix of values published in OEIS A071426 (b-file to 10000, covering .007 by offset) and of Flammenkamp tables computed past 1e9; given those values the 10100-pair scan is a seconds-long trivial check, and no closed-form-free status changes that since the data itself is public. (b) Strictly dominated by existing public computation: Flammenkamp's non-closure through 2^30 with rare values to index ~5M already tells experts far more than a 100-box falsification on 200 heaps; no future periodicity proof, which must operate at the scale of the last rare index plus depth, could cite a 100-box exclusion on N=200 as a lemma. (c) Arbitrary scope: the (100,100) box is set by the N=200 compute budget (q+p<=200) rather than by a literature conjecture -- no source conjectures .007 has a Dawson-34- or Kayles-12-scale period, those being other games' periods, so the 'classical-scale exclusion' motivation is post hoc. This is exactly the 'correct and new but unexplained enumeration / tiny unmotivated gain' case the standard says to reject even when certified: VERIFY_OK certification does not rescue an arbitrary box, per the explicit rule that certification alone does not rescue an unexplained number. No bounded addition (more motivation text, more witnesses at the same scale) can make a 100-box bound on N=200 substantive; reaching a competitive scale would be a new research direction, not a repair. Hence intrinsic low value.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Finite-box falsification on [0,200] only; proves no general periodicity/non-periodicity result and nothing outside the (100,100) box. Corner pair (100,100) rests on the single test index n=100. Witness-leastness is a scan artifact, not claimed. Flammenkamp/OEIS used only as consistency check, never as proof source.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
