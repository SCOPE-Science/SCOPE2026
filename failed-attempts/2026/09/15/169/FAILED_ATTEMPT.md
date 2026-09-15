# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified 2-primary Adams computation of the 18-stem
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20423
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Topology
- **Method:** certified Adams spectral-sequence computation and differential verification

## Problem

Construct a proof-assistant-checked (Lean or Coq) derivation that the 2-completed stable homotopy group pi_18(S^0) is isomorphic to Z/8 (+) Z/2 — hence the integral stable stem pi_18^S ≅ Z/8 (+) Z/2, since the odd-primary components vanish in this stem — by certifying the mod-2 Steenrod algebra presentation, the Adams E_2 page in stems ≤ 18, all Adams differentials affecting stems ≤ 18, and the hidden 2-extension resolving E_infinity to Z/8 (+) Z/2, with every step checked in the proof assistant.

## Attempted claim

Construct a proof-assistant-checked (Lean or Coq) derivation that the 2-completed stable homotopy group pi_18(S^0) is isomorphic to Z/8 (+) Z/2 — hence the integral stable stem pi_18^S ≅ Z/8 (+) Z/2, since the odd-primary components vanish in this stem — by certifying the mod-2 Steenrod algebra presentation, the Adams E_2 page in stems ≤ 18, all Adams differentials affecting stems ≤ 18, and the hidden 2-extension resolving E_infinity to Z/8 (+) Z/2, with every step checked in the proof assistant.

## Research outcome

Target blocked: the from-scratch Adams engine yields a non-minimal (wrong) E_2 above stem 1, the oracle is incomplete, and the bare Lean install lacks the entire formalized stack, so no certified 18-stem derivation was achievable; clean exit with no finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The lane produced an uncertified, provably non-minimal E_2 prototype whose values above stem 1 disagree with the classical Adams table, an incomplete independent oracle script, and a bare Lean 4.9.0 install with no formalized Steenrod, Ext, spectral-sequence, differential, or extension libraries; no differential, hidden-extension, or proof-assistant-checked step was completed, so the 18-stem identification remains entirely unestablished here.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The lane produced an uncertified, provably non-minimal E_2 prototype whose values above stem 1 disagree with the classical Adams table, an incomplete independent oracle script, and a bare Lean 4.9.0 install with no formalized Steenrod, Ext, spectral-sequence, differential, or extension libraries; no differential, hidden-extension, or proof-assistant-checked step was completed, so the 18-stem identification remains entirely unestablished here.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
