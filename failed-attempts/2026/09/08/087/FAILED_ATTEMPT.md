# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Strict Selmer-vs-rank gap closure above the rank-2 threshold: exact rank with proven Sha[2] obstruction in prime conductor 389-1500
- **Round:** 2026-09-07-first-light-01
- **Lane:** 254
- **Disposition:** NO_RESULT
- **Domain:** Arithmetic Geometry
- **Method:** 2-descent plus 4-descent / isogeny-descent Sha[2] obstruction with canonical-height saturation

## Problem

For prime-conductor elliptic curves over Q with 389<=N<=1500 (one committed minimal Weierstrass model per isogeny class), recompute 2-Selmer upper bounds and explicit point-search lower bounds, isolate a curve with strict Selmer-vs-rank gap >=1, and close it: prove the exact Mordell-Weil rank by exhibiting an explicit everywhere-locally-soluble but globally-insoluble 2-covering (nontrivial Sha[2] obstruction via 4-descent / isogeny descent with logged local certificates) and saturate the generator set by an explicit canonical-height pairing determinant.

## Attempted claim

An exact Mordell-Weil rank equality on a prime-conductor curve with 389<=N<=1500 proved by a strict 2-Selmer-vs-rank gap closed with an explicit nontrivial Sha[2] element (logged everywhere-locally-soluble, globally-insoluble 2-cover via 4-descent / isogeny descent) together with a saturated independent generator set whose canonical-height pairing determinant (regulator) is recomputed non-zero, all from the committed minimal model with replayable descent and height logs.

## Research outcome

Resumed with no prior notes/artifacts. Froze 389a1 (y^2+y=x^3+x^2-2x, Delta=389, I1) and proved by exact stdlib-replayable computation that E(Q)[tors] is trivial (|E(F5)|=9, |E(F7)|=13) and rank(Q)>=2 (mod-11 doubling image is exactly {O,(3,5),(6,4),(6,6)} with reductions of P1=(0,0), P2=(1,0), P1+P2=(-2,-1) all non-doubles). All 31 checks in output/artifacts/verify.py pass. This falls short of the target (rank equality via explicit Sha[2]) and the fallback (certified nontrivial Sha[2] cover + refined Selmer bound): no Selmer upper bound, no 2-cover, no regulator saturation was produced, and the lower bound alone re-logs already-recorded LMFDB data.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No upper bound proved: 2-Selmer/4-descent and any Sha[2] cover are absent (no Sage/Magma/PARI/mwrank in environment). No canonical-height regulator saturation computed; LMFDB heights/regulator not reused as proof. Only one curve (389a1) frozen; no prime-window scan. The proved lower bound rank>=2 reproduces the already-recorded LMFDB rank and is therefore not a new exact invariant, so it cannot support a CLAIMED status under the no-database-repackaging gate.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No upper bound proved: 2-Selmer/4-descent and any Sha[2] cover are absent (no Sage/Magma/PARI/mwrank in environment). No canonical-height regulator saturation computed; LMFDB heights/regulator not reused as proof. Only one curve (389a1) frozen; no prime-window scan. The proved lower bound rank>=2 reproduces the already-recorded LMFDB rank and is therefore not a new exact invariant, so it cannot support a CLAIMED status under the no-database-repackaging gate.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
