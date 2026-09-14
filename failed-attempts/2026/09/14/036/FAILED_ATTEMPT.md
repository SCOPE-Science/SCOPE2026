# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Dyadic 4-arm quasi-multiplicativity at 1-2-4 with 2^-10
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1908
- **Disposition:** AUDIT_1_REJECT
- **Domain:** critical planar percolation arm events
- **Method:** RSW separation and FKG gluing

## Problem

Consider critical Bernoulli bond percolation on Z^2 at p=1/2. For 0<r<R let Ann(r,R)=[-R,R]^2 minus the interior of [-r,r]^2, and let A(r,R) be the alternating 4-arm event with four disjoint paths across Ann(r,R) in cyclic order open, closed-dual, open, closed-dual. Prove or disprove the explicit dyadic quasi-multiplicativity lower bound P(A(1,4)) >= 2^{-10} * P(A(1,2)) * P(A(2,4)). A complete resolution is either a rigorous proof of this inequality with the stated constant 2^{-10} via RSW separation and FKG gluing, or a rigorous disproof exhibiting a certified violation of the inequality.

## Attempted claim

Consider critical Bernoulli bond percolation on Z^2 at p=1/2. For 0<r<R let Ann(r,R)=[-R,R]^2 minus the interior of [-r,r]^2, and let A(r,R) be the alternating 4-arm event with four disjoint paths across Ann(r,R) in cyclic order open, closed-dual, open, closed-dual. Prove or disprove the explicit dyadic quasi-multiplicativity lower bound P(A(1,4)) >= 2^{-10} * P(A(1,2)) * P(A(2,4)). A complete resolution is either a rigorous proof of this inequality with the stated constant 2^{-10} via RSW separation and FKG gluing, or a rigorous disproof exhibiting a certified violation of the inequality.

## Research outcome

Proved the dyadic 4-arm quasi-multiplicativity lower bound at 1-2-4 with constant 2^{-10} via an explicit machine-checked 10-bond forcing construction with FKG gluing.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: admitted TARGET is a vacuous arbitrary-parameter fact. The proof uses no RSW input beyond p=1/2 symmetry: any fixed 10-bond pattern has probability 2^-10, and the relative inequality follows solely from product factors <=1, so the stronger absolute bound P(A(1,4))>=2^-10 makes the quasi-multiplicativity form vacuous. Exhibiting straight corridors at fixed scale 1-2-4 is a textbook positivity exercise, teaches nothing about separation/gluing across scales, and has no demonstrated downstream need. Certification does not create value. Intrinsic low value requires REJECT.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof establishes the stated dyadic instance at scales 1-2-4 with constant 2^{-10} only; it does not prove general-scale quasi-multiplicativity, sharp arm exponents, or optimality of the constant. The Monte Carlo gauge is diagnostic, not part of the proof. The argument uses only straight corridors and p=1/2 symmetry, not full RSW inputs.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
