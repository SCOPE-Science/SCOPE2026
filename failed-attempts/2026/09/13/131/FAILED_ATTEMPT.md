# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit spectral gap for named nonlinear Anosov f_star on T^3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1774
- **Disposition:** NO_RESULT
- **Domain:** hyperbolic dynamics
- **Method:** anisotropic Banach spaces, cone and Lasota-Yorke plus Ulam/determinant

## Problem

Let A_star be the toral automorphism of T^3 induced by [[2,1,0],[1,2,1],[0,1,1]] (determinant 1, eigenvalue moduli approximately 3.247, 1.555, 0.198) and S_star(x1,x2,x3) = (x1 + 0.03*sin(2*pi*x2), x2 + 0.02*sin(2*pi*x3), x3) mod 1. Let f_star = A_star o S_star, a real-analytic volume-preserving diffeomorphism, C^1-close to A_star hence Anosov with dim E^s = 1 and dim E^u = 2, nonlinear and non-algebraic. Let m be Lebesgue measure and (P g)(x) = g(f_star^{-1}(x)). Prove or disprove that P on a suitable anisotropic Banach space has spectral radius 1, essential spectral radius at most 0.7, eigenvalue 1 simple, no other spectrum in {|lambda| >= 0.9}, implying |int phi*(psi o f_star^n) dm - int phi dm int psi dm| <= 100*(0.9)^n*||phi||_{C^1}*||psi||_{C^1} for all C^1 phi,psi and n >= 0. A complete answer certifies the explicit strip and rate with cone, Lasota-Yorke, aperiodicity and finite-rank Ulam/determinant data, or rigorously exhibits a resonance lambda != 1 with |lambda| >= 0.9 or C^1 observables violating the stated correlation bound.

## Attempted claim

Let A_star be the toral automorphism of T^3 induced by [[2,1,0],[1,2,1],[0,1,1]] (determinant 1, eigenvalue moduli approximately 3.247, 1.555, 0.198) and S_star(x1,x2,x3) = (x1 + 0.03*sin(2*pi*x2), x2 + 0.02*sin(2*pi*x3), x3) mod 1. Let f_star = A_star o S_star, a real-analytic volume-preserving diffeomorphism, C^1-close to A_star hence Anosov with dim E^s = 1 and dim E^u = 2, nonlinear and non-algebraic. Let m be Lebesgue measure and (P g)(x) = g(f_star^{-1}(x)). Prove or disprove that P on a suitable anisotropic Banach space has spectral radius 1, essential spectral radius at most 0.7, eigenvalue 1 simple, no other spectrum in {|lambda| >= 0.9}, implying |int phi*(psi o f_star^n) dm - int phi dm int psi dm| <= 100*(0.9)^n*||phi||_{C^1}*||psi||_{C^1} for all C^1 phi,psi and n >= 0. A complete answer certifies the explicit strip and rate with cone, Lasota-Yorke, aperiodicity and finite-rank Ulam/determinant data, or rigorously exhibits a resonance lambda != 1 with |lambda| >= 0.9 or C^1 observables violating the stated correlation bound.

## Research outcome

Target blocked and exited clean: certified-modulo-rounding cone and bunching data plus stable Galerkin spectra were obtained, but the validated resonance-exclusion gap (tail 3.9e4 vs margin 0.0116) proved structurally unclosable within the pass, with no audit-grade emergent increment.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No TARGET resolution was achieved: no validated essential-radius bound, no resonance exclusion on {|lambda| >= 0.9}, and no correlation estimate were proved. Supporting numerics are double-precision with ad-hoc padding rather than full interval arithmetic, the 13 low-period orbits are unvalidated Newton outputs, and the near-resonance diagnosis is a routine consequence of the integer linear part, so no emergent claim is submitted.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No TARGET resolution was achieved: no validated essential-radius bound, no resonance exclusion on {|lambda| >= 0.9}, and no correlation estimate were proved. Supporting numerics are double-precision with ad-hoc padding rather than full interval arithmetic, the 13 low-period orbits are unvalidated Newton outputs, and the near-resonance diagnosis is a routine consequence of the integer linear part, so no emergent claim is submitted.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
