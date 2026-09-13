# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Async lag enlargement-or-maximality at fixed ADT on the Zhai-Yang delay benchmark
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1488
- **Disposition:** NO_RESULT
- **Domain:** asynchronous switched delay feedback control
- **Method:** matched/mismatched piecewise Lyapunov-Krasovskii LMI at fixed ADT

## Problem

For the documented asynchronous time-delay feedback switched closed loop of Zhai and Yang (Journal of the Franklin Institute 2013, Exponential stability of time-delay feedback switched systems with asynchronous switching, numerical example) and the robust async-delay formulation of Cheng et al. (Journal of Applied Mathematics 2012), with stated plant, delay, controller gains, synchronous stabilizing pairs, and mismatched possibly unstable pairs, fix average dwell time at the value reported there and decide whether a matched/mismatched piecewise Lyapunov-Krasovskii certificate admits a strictly larger maximum detector/controller lag delta_max than reported. Either exhibit feasible matched/mismatched linear matrix inequalities with explicit matrices certifying a strictly larger lag region at that fixed average dwell time, or establish an impossibility lemma via dual infeasibility that the fixed functional class cannot exceed the reported lag and exhibit one admissible asynchronous plant/detector path with lag just beyond the certified region violating the stated decay bound. This single curve point tests the genuine matched-versus-mismatched tradeoff. Downstream use is detector-lag tolerance of asynchronously switched delay feedback. A complete answer gives the enlarged lag with matrices or the maximality certificate plus explicit plant switching times, detector lags, and initial function.

## Attempted claim

For the documented asynchronous time-delay feedback switched closed loop of Zhai and Yang (Journal of the Franklin Institute 2013, Exponential stability of time-delay feedback switched systems with asynchronous switching, numerical example) and the robust async-delay formulation of Cheng et al. (Journal of Applied Mathematics 2012), with stated plant, delay, controller gains, synchronous stabilizing pairs, and mismatched possibly unstable pairs, fix average dwell time at the value reported there and decide whether a matched/mismatched piecewise Lyapunov-Krasovskii certificate admits a strictly larger maximum detector/controller lag delta_max than reported. Either exhibit feasible matched/mismatched linear matrix inequalities with explicit matrices certifying a strictly larger lag region at that fixed average dwell time, or establish an impossibility lemma via dual infeasibility that the fixed functional class cannot exceed the reported lag and exhibit one admissible asynchronous plant/detector path with lag just beyond the certified region violating the stated decay bound. This single curve point tests the genuine matched-versus-mismatched tradeoff. Downstream use is detector-lag tolerance of asynchronously switched delay feedback. A complete answer gives the enlarged lag with matrices or the maximality certificate plus explicit plant switching times, detector lags, and initial function.

## Research outcome

Target blocked and cleanly exited: after twelve distinct retrieval routes and a 40+ minute solver-install attempt, the verbatim Zhai-Yang/Cheng benchmark data and the verified SDP computation needed for the lag enlargement-or-maximality decision remained unavailable, so no auditable target claim could be closed; see output/target_exit.json (CLEAN_EXIT) and output/WORKLOG.md.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation was limited by two structural barriers documented in output/target_exit.json: the verbatim Zhai-Yang benchmark numbers were unrecoverable because the paper is closed-access with no open copy on any reachable index or mirror, and the Cheng open-access full text was hard-blocked on every mirror from this network; additionally the SDP solver stack (cvxpy/clarabel/scipy) never became importable within the pass, so no LMI feasibility or violation-path computation could be executed and verified. No claim about the reported lag region is made.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation was limited by two structural barriers documented in output/target_exit.json: the verbatim Zhai-Yang benchmark numbers were unrecoverable because the paper is closed-access with no open copy on any reachable index or mirror, and the Cheng open-access full text was hard-blocked on every mirror from this network; additionally the SDP solver stack (cvxpy/clarabel/scipy) never became importable within the pass, so no LMI feasibility or violation-path computation could be executed…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
