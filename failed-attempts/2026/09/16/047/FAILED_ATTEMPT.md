# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharpness of the (2n−1) interleaving–bottleneck bound for rectangle-decomposable R^n-modules, n ≥ 3
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20489
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Topology
- **Method:** interleaving-distance and stability analysis

## Problem

Let M,N be pointwise finite-dimensional rectangle-decomposable R^n-modules with interleaving distance d_I and bottleneck distance d_B. It is known that d_B(M,N) ≤ (2n−1)·d_I(M,N). For each fixed n ≥ 3, determine the optimal constant C_opt(n) = sup d_B(M,N)/d_I(M,N) over such pairs (with 0<d_I<∞): is C_opt(n) = 2n−1, and if not what is its exact value? In particular, does there exist for some n ≥ 3 a rectangle-decomposable pair with d_B/d_I > 3?

## Attempted claim

Let M,N be pointwise finite-dimensional rectangle-decomposable R^n-modules with interleaving distance d_I and bottleneck distance d_B. It is known that d_B(M,N) ≤ (2n−1)·d_I(M,N). For each fixed n ≥ 3, determine the optimal constant C_opt(n) = sup d_B(M,N)/d_I(M,N) over such pairs (with 0<d_I<∞): is C_opt(n) = 2n−1, and if not what is its exact value? In particular, does there exist for some n ≥ 3 a rectangle-decomposable pair with d_B/d_I > 3?

## Research outcome

Target C_opt(n) sharpness for n>=3 remains unresolved: no verified rectangle pair with dB/dI>3 and no improved upper bound; heuristic hits were diagnosed as false positives and the obstruction is preserved in target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Distance oracles (exact rectangle dI and bottleneck dB) and a validated bilinear interleaving-feasibility solver were built, but no certified ratio->3 example and no improved upper bound were established. Heuristic search flags were all refuted as false positives, and the known n=2 ratio-3 calibration was not re-derived with the exact solver before the budget expired.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Distance oracles (exact rectangle dI and bottleneck dB) and a validated bilinear interleaving-feasibility solver were built, but no certified ratio->3 example and no improved upper bound were established. Heuristic search flags were all refuted as false positives, and the known n=2 ratio-3 calibration was not re-derived with the exact solver before the budget expired.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
