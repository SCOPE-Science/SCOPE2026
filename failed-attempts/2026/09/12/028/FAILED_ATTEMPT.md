# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified Dual-Density Barrier for ML-DSA-44 Below BKZ Blocksize 70
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1106
- **Disposition:** NO_RESULT
- **Domain:** Cryptography
- **Method:** Banaszczyk transference with BKZ-profile upper envelope

## Problem

Prove or refute that for ML-DSA-44 Module-LWE (ring Z_8380417[x]/(x^256+1), ranks k=4 and l=4), no dual-lattice vector obtainable by BKZ reduction with blocksize at most 70 can make the standard Fourier distinguisher achieve advantage 0.25 or more, establishing a certified dual-density barrier at that blocksize.

## Attempted claim

For Decision-MLWE at ML-DSA-44 parameters (n=256, k=4, l=4, q=8380417 with Dilithium bounded-uniform error), every dual vector achievable by BKZ with blocksize beta<=70 has Euclidean length exceeding the threshold needed for Fourier distinguishing advantage 0.25, so no such BKZ effort reaches advantage 0.25.

## Research outcome

Target blocked on both proof and refutation sides: geometry bounds the wrong side (Minkowski witness below threshold) and the BKZ-70 envelope is vacuous (211993x above threshold); no independently valuable finding emerged, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The attempted barrier instantiation used exact ML-DSA-44 parameters with scripted threshold, Minkowski, and BKZ-envelope arithmetic, but all available bounds constrain the wrong side of the per-instance algorithmic claim: existence bounds guarantee short advantage-capable vectors non-constructively while the BKZ-70 envelope is vacuous, and empirical BKZ-70 runs at dimension ~2048 plus any structural shortcut were out of reach in the pass.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The attempted barrier instantiation used exact ML-DSA-44 parameters with scripted threshold, Minkowski, and BKZ-envelope arithmetic, but all available bounds constrain the wrong side of the per-instance algorithmic claim: existence bounds guarantee short advantage-capable vectors non-constructively while the BKZ-70 envelope is vacuous, and empirical BKZ-70 runs at dimension ~2048 plus any structural shortcut were out of reach in the pass.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
