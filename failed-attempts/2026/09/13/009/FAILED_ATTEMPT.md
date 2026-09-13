# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Bessel-Legendre ADT improvement-or-barrier on the Yan-Ozbay delay benchmark
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1484
- **Disposition:** NO_RESULT
- **Domain:** switched linear delay systems under average dwell time
- **Method:** augmented multiple Lyapunov-Krasovskii LMI with second-order Bessel-Legendre inequality

## Problem

For the two-mode heterogeneous-delay switched linear benchmark of Yan and Ozbay (SIAM Journal on Control and Optimization 47(2):936-949, 2008, numerical section), considered with its stated delay bounds under interval time-varying delay and its stated exponential decay rate, decide whether an augmented multiple Lyapunov-Krasovskii functional using second-order canonical Bessel-Legendre inequality can certify a common average dwell-time bound strictly smaller than the Razumikhin/Lyapunov-function average dwell-time bound reported for that example. Either exhibit feasible delay-dependent linear matrix inequalities with explicit matrices achieving a strictly smaller certified tau_a, or establish a class-barrier lemma proving via dual linear matrix inequality infeasibility that no functional in that fixed augmented class certifies below the prior bound and exhibit an admissible periodic switching path with average dwell time between the two bounds whose trajectory violates the stated decay bound. Downstream use is certified slow-on-the-average switching for networked delay systems with jitter. A complete answer gives the improved bound with matrices or the infeasibility certificate plus the witness period, order, and initial function.

## Attempted claim

For the two-mode heterogeneous-delay switched linear benchmark of Yan and Ozbay (SIAM Journal on Control and Optimization 47(2):936-949, 2008, numerical section), considered with its stated delay bounds under interval time-varying delay and its stated exponential decay rate, decide whether an augmented multiple Lyapunov-Krasovskii functional using second-order canonical Bessel-Legendre inequality can certify a common average dwell-time bound strictly smaller than the Razumikhin/Lyapunov-function average dwell-time bound reported for that example. Either exhibit feasible delay-dependent linear matrix inequalities with explicit matrices achieving a strictly smaller certified tau_a, or establish a class-barrier lemma proving via dual linear matrix inequality infeasibility that no functional in that fixed augmented class certifies below the prior bound and exhibit an admissible periodic switching path with average dwell time between the two bounds whose trajectory violates the stated decay bound. Downstream use is certified slow-on-the-average switching for networked delay systems with jitter. A complete answer gives the improved bound with matrices or the infeasibility certificate plus the witness period, order, and initial function.

## Research outcome

TARGET blocked short of a complete certificate: recovered the exact Yan-Ozbay benchmark and prior bound 6.5147, derived the second-order Bessel-Legendre LMI class, certified mode 2 rigorously with explicit matrices, but the rigorous heterogeneous-delay mode-1 LMI retains a positive residual (+0.002 best), so no improved average dwell time is claimed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete two-mode LMI certificate was closed: rigorous 10-dimensional mode-1 LMI remains at +4.52 (best triple) / +0.0022 (heterogeneous search), so no certified average dwell time below 6.5147 is claimed. Environment had numpy only (no scipy/cvxpy SDP solver; installs timed out), limiting synthesis to random hill-climbing. The tau-aware nominal tau_a=4.70 is explicitly NOT claimed as a certificate. See DRAFT.md sections 5-6 for the exact qualification.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete two-mode LMI certificate was closed: rigorous 10-dimensional mode-1 LMI remains at +4.52 (best triple) / +0.0022 (heterogeneous search), so no certified average dwell time below 6.5147 is claimed. Environment had numpy only (no scipy/cvxpy SDP solver; installs timed out), limiting synthesis to random hill-climbing. The tau-aware nominal tau_a=4.70 is explicitly NOT claimed as a certificate. See DRAFT.md sections 5-6 for the exact qualification.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
