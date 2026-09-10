# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Turan density of linear 3-uniform Berge-K_{3,3}-free hypergraphs via certified flag-algebra SDP and extremal construction
- **Round:** 2026-09-07-first-light-01
- **Lane:** 507
- **Disposition:** NO_RESULT
- **Domain:** Extremal Combinatorics
- **Method:** flag-algebra semidefinite programming with symmetrization-stability analysis and explicit blow-up construction matching

## Problem

Determine the exact Turan edge-density of 3-uniform linear Berge-K_{3,3}-free hypergraphs by producing a rationally rounded flag-algebra SDP upper bound (flags of order at most 7) matched by an explicit linear Berge-K_{3,3}-free blow-up/Steiner-type construction, or otherwise certify an explicit stability-gap interval between the best SDP upper bound and the best construction lower bound.

## Attempted claim

The Turan edge-density of 3-uniform linear Berge-K_{3,3}-free hypergraphs equals the density of the explicit balanced blow-up/Steiner-type construction identified in the record, certified by a rationally rounded flag-algebra SDP upper bound (flags of order at most 7) whose value coincides with the construction density, closing the cell.

## Research outcome

Target (exact linear 3-uniform Berge-K_{3,3} Turan density via coincident rounded flag-SDP upper bound and blow-up/Steiner construction) not closed: no SDP upper bound U was produced and no matching construction density identified. Preset fallback (rounded SDP U0 + exact 15-vertex witness L0 with U0-L0<=0.05) not met: only the L-leg exists — a verified 15-vertex/20-edge linear Berge-K_{3,3}-free witness (pair-density 4/7, rate 4/45, exhaustive recheck) — while the required SDP dual rounding file is absent. Target-directed work yielded verified partial evidence (checker, witness, obstruction certificate, host-restricted census) but no independently valuable auditable theorem; honest NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

["No order<=7 flag-algebra SDP dual with rational rounding was produced: environment is stdlib-only (no SDP solver), so the fallback's upper-bound leg and the target's U=L closure are both absent.", 'Lower-bound leg alone is insufficient: verified 15-vertex/20-edge linear Berge-K_{3,3}-free witness gives pair-density 4/7 and rate 4/45, but trivial linearity upper bound U0=1 leaves gap 3/7>0.05, failing the binary fallback criterion.', 'Naive KST shadow-graph reduction was invalidated (linearity does not force 9 distinct covering edges; certificate obstruction9.json), removing the only non-SDP upper-bound shortcut.', 'Optimality not established anywhere: n=9 full extremal number not closed (exact BB seeded at m=10 did not converge); 15-vertex m=20 witness is heuristic (m=21-22 seen transiently, edge lists not stabilized); STS(9) m=10 maximality is host-restricted to AG(2,3), not a general ex_lin(9) theorem.', 'Emergent candidates (linearity-vs-distinctness obstruction, STS(9)-host census, STS(15)-Bose copy census with weak m<=32 host bound) are routine small-census/obstruction notes and do not meet the SCOPE independent originality/value bar; per instructions they are logged in WORKLOG.md, not claimed.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ["No order<=7 flag-algebra SDP dual with rational rounding was produced: environment is stdlib-only (no SDP solver), so the fallback's upper-bound leg and the target's U=L closure are both absent.", 'Lower-bound leg alone is insufficient: verified 15-vertex/20-edge linear Berge-K_{3,3}-free witness gives pair-density 4/7 and rate 4/45, but trivial linearity upper bound U0=1 leaves gap 3/7>0.05, failing the binary fallback criterion.', 'Naive KST shadow-graph reduction was invalidated (linearity…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
