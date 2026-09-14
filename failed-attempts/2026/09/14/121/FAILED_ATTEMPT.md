# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Does finite nuclear dimension plus UCT imply generalized tracial rank one without Q-stabilization?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20124
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Operator Algebras
- **Method:** Elliott invariant and Kirchberg-Phillips classification techniques

## Problem

Let A be a unital, simple, separable, non-elementary, nuclear C*-algebra with finite nuclear dimension satisfying the UCT. It is known that A tensor Q has generalized tracial rank at most one (Gong-Lin-Niu). Does A itself have generalized tracial rank at most one, i.e. can the Q-stabilization be removed without assuming finite decomposition rank, real rank zero, or torsion-free K_0?

## Attempted claim

Let A be a unital, simple, separable, non-elementary, nuclear C*-algebra with finite nuclear dimension satisfying the UCT. It is known that A tensor Q has generalized tracial rank at most one (Gong-Lin-Niu). Does A itself have generalized tracial rank at most one, i.e. can the Q-stabilization be removed without assuming finite decomposition rank, real rank zero, or torsion-free K_0?

## Research outcome

Proved YES: finite nuclear dimension plus UCT implies generalized tracial rank at most one for A itself; Q-stabilization is removable with no extra decomposition-rank, real-rank-zero, or torsion-free hypotheses.

## Why this attempt failed

Failed axes: correctness, value.

correctness: FAIL: DRAFT conflates rational gTR (A tensor Q) with genuine gTR (A). Step 4 claims every stably-finite Z-stable UCT model isomorphic to a C1-limit hence has gTR<=1, but cited range/models prove only rational membership (N1: A tensor U in B1) and Q-stabilized blocks. Unital B1 definition requires a non-zero projection p and implies (SP)/projections. The Jiang-Su algebra Z is unital simple separable non-elementary nuclear finite-nuclear-dimension UCT and projectionless (GLN-I notes Z projectionless; CETWW gives Z Z-stable hence finite nuc dim), so it satisfies hypotheses but cannot have unital gTR<=1. Explicit counterexample disproves headline; purely-infinite branch ok but stably-finite branch invalid. value: FAIL with ADMISSION_DEFECT: no valid retrievable result remains because the headline is false (counterexample Z) and the proof is invalid. The only correct content (rational gTR, Z-stability equivalence, classification conditional on rational hypothesis) is already published. The falsity is exposed by a single well-known object (Z projectionless, finite nuc dim, UCT), i.e. a direct-lookup/cheap-defect negative resolution that Admission should have excluded under STANDARD two-sided value screening. A false strengthening has no independent retrieval value.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: This report proves the assembly of the result but takes four major published theorems as black boxes without re-proof: CETWW 2021 Z-stability from finite nuclear dimension, Rordam Z-stable dichotomy, Kirchberg-Phillips classification with Lin tracial rank zero, and the Elliott-Gong-Lin-Niu classification plus range theorem for Z-stable UCT algebras. Correctness is therefore conditional on those theorems as cited; no independent verification, computation, or literature search beyond the admitted…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
