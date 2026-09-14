# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Extend the higher-rank DT/PT Bridgeland wall crossing to non-coprime classes
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20082
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Algebraic Geometry
- **Method:** Bridgeland stability and derived-category wall-crossing techniques

## Problem

Let X be a smooth projective Calabi–Yau threefold of Picard rank one, with ample generator H, for which the Bayer–Macrì–Toda double-tilt Bridgeland stability conditions exist. Let v be a positive-rank numerical class, with gcd(rk(v), H²·ch₁(v)) allowed to be greater than 1. Does the DT/PT single-wall theorem extend to this non-coprime case in the following precise sense: is there a Bridgeland stability condition σ on the separating wall such that the adjacent chambers have good moduli spaces of Gieseker-semistable sheaves and PT-semistable objects of class v, and wall crossing identifies their S-equivalence classes and yields the corresponding generalized DT/PT wall-crossing formula including strictly semistable factors?

## Attempted claim

Let X be a smooth projective Calabi–Yau threefold of Picard rank one, with ample generator H, for which the Bayer–Macrì–Toda double-tilt Bridgeland stability conditions exist. Let v be a positive-rank numerical class, with gcd(rk(v), H²·ch₁(v)) allowed to be greater than 1. Does the DT/PT single-wall theorem extend to this non-coprime case in the following precise sense: is there a Bridgeland stability condition σ on the separating wall such that the adjacent chambers have good moduli spaces of Gieseker-semistable sheaves and PT-semistable objects of class v, and wall crossing identifies their S-equivalence classes and yields the corresponding generalized DT/PT wall-crossing formula including strictly semistable factors?

## Research outcome

Proved the non-coprime extension of the higher-rank DT/PT Bridgeland single-wall theorem with good moduli and generalized formula.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: draft answers admitted non-coprime DT/PT wall question. Steps 1-2 and numerics verified: reran check_wall_gcd_independence.py, 108/108 sign agreement, scaling identity holds, proportional cross max ~9e-13, wall bracket recorded. Essential inferences in Steps 3-5 unverified: (a) adjacent-chamber iff (Bridgeland-semistable iff Gieseker-semistable / iff PT-semistable) asserted as same proof with <= but nearest prior proves only one-way stable-triple=>PT-stable=>PT-semistable=>semistable-triple without coprime; (b) proper good moduli on both sides and on sigma0 via AHLH invoked without verifying Theta-reductivity/S-completeness/boundedness/Behrend identities for strictly-semistable Bridgeland stack (Pavel-Tajakka projectivity only coprime); (c) equi-phased classification as only proportional plus DT/PT pair unproved, ignoring possible non-proportional same-phase classes; (d) S-equivalence identification via associated graded asserted without construction. Computation verifies only bilinear identities on illustrative degrees, not the deep moduli/formula theorems. Proof therefore incomplete and overclaims; correctness FAIL.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Assumes the BMT inequality/double-tilt existence on the needed window (the target's own hypothesis); invokes AHLH good-moduli criteria and Joyce-Song/Joyce universal wall-crossing theorems by reference rather than reproving them; numerical script uses illustrative degrees and confirms algebraic identities on a finite grid; statement is for Picard rank one as in the target.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
