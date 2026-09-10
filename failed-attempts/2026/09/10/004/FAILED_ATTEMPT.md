# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Deformation census of Csorgo-type loops of order 128 with abelian inner mapping group: closing the minimal-order family or a second non-elementary-abelian witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 500
- **Disposition:** NO_RESULT
- **Domain:** Nonassociative Algebra
- **Method:** group-deformation mu-modification analysis via trilinear alternating forms with inner-mapping commutator replay and central-series certification

## Problem

Decide the order-128 Csorgo deformation family: finite loops Q of order 128 of nilpotency class exactly 3 with abelian (commuting) inner mapping group arising as mu-deformations from the classified |G|=128 nontrivial setups (G,Z,delta). Either certify the exact isomorphism-type count K_C of this family with per-class deformation data, or exhibit a second certified isomorphism type with non-elementary-abelian inner mapping group inequivalent to the published Drapal-Vojtechovsky example. Anchor the attack at the fixed first setup seed (G0,Z0) via exhaustive mu-transversal analysis with full inner-mapping replay.

## Attempted claim

The mu-deformation census over the classified |G|=128 nontrivial setups (G,Z,delta) certifies the exact isomorphism-type count K_C (value determined by the replay) of Csorgo-type loops of order 128 with abelian inner mapping group and nilpotency class exactly 3, delivering per class an explicit deformation datum with trilinear-form log, full inner-mapping commutativity replay, class-3 associator-witness log, and inequivalence data; in the alternative outcome it exhibits at least one certified second isomorphism type with non-elementary-abelian inner mapping group lying outside the published Drapal-Vojtechovsky example, with full replay and inequivalence certificate.

## Research outcome

No auditable TARGET, PRESET_FALLBACK, or EMERGENT claim can be supported. Full K_C census/second-type route not viable in remaining time; fallback exact-N1 binary coverage fails (delta_T/mu-tau transversal unexamined, isomorphism collapse uncomputed). Preserved a verified single-seed Csorgo-type loop fragment (order 128, abelian Inn (Z2)^6, class exactly 3, VERIFY_OK replay) as a reusable construction, documented in DRAFT.md, not claimed as a result.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Fallback coverage: delta free-bit transversal (~2^21 scale) and mu tau params not enumerated; D-uniqueness only sample-screened (1/512 on generator-plus-central screen); N1 isomorphism collapse not computed. Target family (all setup groups/params) untouched. Q0 Inn is the old (Z2)^6 kind, so no new-type value. Evidence: output/artifacts/verify.py replays group/delta/mu/loop/Inn-abelian/class-3 checks with VERIFY_OK (~9s); see output/WORKLOG.md and output/DRAFT.md (fragment only).

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Fallback coverage: delta free-bit transversal (~2^21 scale) and mu tau params not enumerated; D-uniqueness only sample-screened (1/512 on generator-plus-central screen); N1 isomorphism collapse not computed. Target family (all setup groups/params) untouched. Q0 Inn is the old (Z2)^6 kind, so no new-type value. Evidence: output/artifacts/verify.py replays group/delta/mu/loop/Inn-abelian/class-3 checks with VERIFY_OK (~9s); see output/WORKLOG.md and output/DRAFT.md (fragment only).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
