# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Involutory identical-twin STS(21) decision
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1574
- **Disposition:** NO_RESULT
- **Domain:** combinatorial design theory
- **Method:** symmetry-broken backtracking with Pasch-switch isomorphism test

## Problem

Let an STS(21) be 70 triples on 21 points with Pasch defined as the (6,4) quadrilateral; a single-Pasch system has exactly one Pasch, and its Pasch-switch mate replaces that quadrilateral by the opposite trade on the same six points. An identical twin is a single-Pasch STS(21) whose mate is isomorphic to it. Decide by isomorph-free SAT backtracking with involution symmetry breaking whether there exists an identical-twin STS(21) admitting an involutory automorphism fixing exactly three points and preserving its unique Pasch 6-set setwise. Either exhibit explicit canonical block lists for the system and an isomorphism to its switched mate plus the involution, or certify unsatisfiability under that symmetry with a machine-checkable proof.

## Attempted claim

Let an STS(21) be 70 triples on 21 points with Pasch defined as the (6,4) quadrilateral; a single-Pasch system has exactly one Pasch, and its Pasch-switch mate replaces that quadrilateral by the opposite trade on the same six points. An identical twin is a single-Pasch STS(21) whose mate is isomorphic to it. Decide by isomorph-free SAT backtracking with involution symmetry breaking whether there exists an identical-twin STS(21) admitting an involutory automorphism fixing exactly three points and preserving its unique Pasch 6-set setwise. Either exhibit explicit canonical block lists for the system and an isomorphism to its switched mate plus the involution, or certify unsatisfiability under that symmetry with a machine-checkable proof.

## Research outcome

Target blocked: 450-system sweep over all three canonical FIX classes found Pasch counts of 8+ and zero single-Pasch systems, yielding no twin witness, while the search space (~1.1e10 stage-1 nodes) is far from exhausted so no UNSAT certificate is possible; honest NO_RESULT with CLEAN_EXIT and preserved verification artifacts.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No identical-twin witness was found and no unsatisfiability certificate was produced: only 450 sigma-invariant systems were sampled from a space exceeding 1e10 stage-1 nodes, so neither existence nor nonexistence is decided. The isomorphism backtracker is custom code, not a verified solver; Pasch-switch and twin tests were applied only to the lowest-Pasch samples. All claims are bounded accordingly.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No identical-twin witness was found and no unsatisfiability certificate was produced: only 450 sigma-invariant systems were sampled from a space exceeding 1e10 stage-1 nodes, so neither existence nor nonexistence is decided. The isomorphism backtracker is custom code, not a verified solver; Pasch-switch and twin tests were applied only to the lowest-Pasch samples. All claims are bounded accordingly.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
