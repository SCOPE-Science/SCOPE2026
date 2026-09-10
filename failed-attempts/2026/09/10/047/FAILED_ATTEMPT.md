# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Strong-cork witness for the Gompf swallow-follow pair (6_1, m=1) via split-action delta
- **Round:** 2026-09-07-first-light-01
- **Lane:** 616
- **Disposition:** NO_RESULT
- **Domain:** Geometric Topology
- **Method:** involutive/equivariant connected knot Floer complex with split-diffeomorphism action and Stein handle calculus

## Problem

Let K0=6_1 be the stevedore knot (Rolfsen table / KnotInfo diagram source) and J=K0#-K0. Let Y=S^3_{1}(J) with t_lambda the Gompf swallow-follow split diffeomorphism (DMZ Sec 2) and C=C_{6_1,1} the associated compact contractible Stein handle presentation (Gompf 2017 / Tange notes). Decide whether (Y,t_lambda) is a strong cork in the Lin-Ruberman-Saveliev sense by certifying S-nontriviality / delta(K0,t_lambda)>0 from the connected knot Floer complex with split action, with logged Stein handle-slide trace; a positive certificate obstructs extension of t_lambda over any homology ball bounded by Y.

## Attempted claim

The named pair (Y,t_lambda) with Y=S^3_{1}(6_1#-6_1) and t_lambda the swallow-follow involution is a strong cork: t_lambda does not extend over any integral homology ball bounded by Y (in particular over C_{6_1,1}), witnessed by S-nontriviality of (CFK(6_1#-6_1),t_lambda) with delta(6_1,t_lambda)>0 and a logged Stein handle-slide trace of the twist.

## Research outcome

Target (strong-cork witness via S-nontriviality/delta>0 for the (6_1,m=1) swallow-follow pair) is BLOCKED: 6_1 thin slice data (det=9, tau=0, Arf=0) give 2Arf+|tau|=0 mod 4 and 2 even diagonal boxes, so the iota_K-connected complex is a dot with Sarkar s=id (S-trivial) and delta(6_1,t_lambda)=0 (Cyl/A0 triple, DMZ Lemmas 2.13/4.4), replayed in output/artifacts/check_61_gap.py with a 4_1 control. The exact preset fallback requires certifying the positive even D=delta>0 plus S-nontriviality log, i.e. certifying a statement proved false in-budget; hence ATTEMPTED_AND_BLOCKED. No independently valuable original increment (S-triviality is a routine slice + published DMZ Sec-5 corollary). CLEAN_EXIT per output/target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Strong-cork status of (S^3_1(6_1#-6_1),t_lambda) per se remains open: only the DMZ S-nontriviality/delta>0 sufficient route is ruled out (S-trivial, delta=0). A proof via non-DMZ methods or an explicit extension diffeomorphism over a homology ball (actual disproof) was not attempted and is outside the hour budget.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Strong-cork status of (S^3_1(6_1#-6_1),t_lambda) per se remains open: only the DMZ S-nontriviality/delta>0 sufficient route is ruled out (S-trivial, delta=0). A proof via non-DMZ methods or an explicit extension diffeomorphism over a homology ball (actual disproof) was not attempted and is outside the hour budget.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
