# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp ordinary-line gap for the 17-point circle-plus-origin Boroczky fragment B17
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1119
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Incidence Geometry
- **Method:** polynomial cell decomposition with Green-Tao transfer

## Problem

Let B17 consist of the 16th roots of unity on the unit circle plus the origin, 17 distinct noncollinear Euclidean points. Determine by an explicit incidence ledger whether B17 spans at least 9 ordinary lines (lines through exactly two points of B17), using a degree-3 polynomial cell decomposition that transfers the Green-Tao near-cubic structure to this finite fragment. Either outcome is a complete resolution with a checkable line list.

## Attempted claim

The named 17-point configuration B17, defined as {(cos(2k*pi/16), sin(2k*pi/16)) : k = 0,...,15} together with (0,0) in the Euclidean plane, spans at least 9 ordinary lines, i.e. at least 9 distinct lines each containing exactly two points of B17, as certifiable by a degree-3 polynomial partitioning incidence ledger.

## Research outcome

Proved the B17 target: exact ledger of 120 spanned lines with 112 ordinary lines, far above the threshold of 9, via exact cyclotomic replay and a line-circle hand proof with degree-3 cell table.

## Why this attempt failed

Failed axes: value.

value: FAIL: ADMISSION_DEFECT. The admitted triviality/value preflight (topic.audit_preflight triviality_preflight PASS, positive-resolution value case as first exact stability data point in 15-19 window with reusable polynomial-cell ledger) is materially false on the proved facts. The exact ledger 112 vs threshold 9 exceeds Dirac-Motzkin by 13x: B17 is highly non-extremal and teaches nothing about few-ordinary-line stability, which concerns sets with ~n/2 ordinary lines, not 112. The count follows in three lines from the textbook fact that a line meets a circle at most twice, i.e. a standard undergraduate exercise applied to n=16, generalizing immediately to C(n,2)-n/2 for any even n-gon plus center with no new idea. The degree-3 polynomial (x^2+y^2-1/4)(x-1/2) plays no logical role in forcing the quota; the hand proof never uses it. No future researcher needs this precise non-extremal count for orchard-planting (which maximizes 3-point lines; B17 has only 8) or Green-Tao casework. Under STANDARD, textbook restatements, mere parameter substitutions, and certification alone without benchmark significance fail value even if correct and new. No bounded addition can repair this intrinsic triviality without changing the problem, so REJECT not REPAIRABLE.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The proved count 112 greatly exceeds threshold 9, so the certificate is stronger than required but specific to the symmetric roots-plus-origin fragment; it does not classify other 17-point sets, prove a general small-n Dirac-Motzkin bound, or extend the Green-Tao threshold, and the Green-Tao transfer here is a cell-avoidance ledger rather than a full structural induction.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
