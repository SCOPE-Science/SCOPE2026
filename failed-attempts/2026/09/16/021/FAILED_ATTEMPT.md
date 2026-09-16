# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Unconditional nonradial scattering below the ground-state threshold for the 3D focusing energy-critical generalized Hartree equation
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20468
- **Disposition:** NO_RESULT
- **Domain:** Dispersive Partial Differential Equations
- **Method:** concentration-compactness and profile-decomposition analysis

## Problem

Fix d=3, 0<alpha<3, p=3+alpha, I_alpha(x)=c_alpha|x|^{-(3-alpha)}. Let W_alpha in Hdot^1(R^3), W_alpha>0, attain the optimal Hartree-Sobolev constant and solve -Delta W_alpha=(I_alpha*|W_alpha|^p)|W_alpha|^{p-2}W_alpha. For f in Hdot^1 put D_alpha(f)=iint I_alpha(x-y)|f(x)|^p|f(y)|^p dxdy and E_alpha(f)=(1/2)||grad f||_2^2-(1/2p)D_alpha(f). For the focusing energy-critical generalized Hartree equation i partial_t u + Delta u + (I_alpha*|u|^p)|u|^{p-2}u=0 with u(0)=u_0 in Hdot^1(R^3) satisfying E_alpha(u_0)<E_alpha(W_alpha) and ||grad u_0||_2<||grad W_alpha||_2: is the maximal-lifespan Hdot^1 solution global in both time directions and scattering (finite critical Z_alpha norm on R with Hdot^1 wave operators), with no radial assumption and no additional occupation-window, drift-rate, or low-frequency-decay hypothesis on the concentration-compactness critical element?

## Attempted claim

Fix d=3, 0<alpha<3, p=3+alpha, I_alpha(x)=c_alpha|x|^{-(3-alpha)}. Let W_alpha in Hdot^1(R^3), W_alpha>0, attain the optimal Hartree-Sobolev constant and solve -Delta W_alpha=(I_alpha*|W_alpha|^p)|W_alpha|^{p-2}W_alpha. For f in Hdot^1 put D_alpha(f)=iint I_alpha(x-y)|f(x)|^p|f(y)|^p dxdy and E_alpha(f)=(1/2)||grad f||_2^2-(1/2p)D_alpha(f). For the focusing energy-critical generalized Hartree equation i partial_t u + Delta u + (I_alpha*|u|^p)|u|^{p-2}u=0 with u(0)=u_0 in Hdot^1(R^3) satisfying E_alpha(u_0)<E_alpha(W_alpha) and ||grad u_0||_2<||grad W_alpha||_2: is the maximal-lifespan Hdot^1 solution global in both time directions and scattering (finite critical Z_alpha norm on R with Hdot^1 wave operators), with no radial assumption and no additional occupation-window, drift-rate, or low-frequency-decay hypothesis on the concentration-compactness critical element?

## Research outcome

Target blocked at unconditional critical-element rigidity: Hdot1 bounds provably do not yield the finite-mass, momentum, and drift inputs the truncated-virial argument needs, and the missing uniform negative-regularity input cannot be closed in this pass; clean exit with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The Kenig-Merle reduction and variational trapping were verified, but unconditional rigidity of the nonradial critical element (finite mass, zero momentum, sublinear drift for the nonlocal degree-(5+2alpha) nonlinearity across 0<alpha<3) remains unproved; the supporting scripts are verification checks and textbook counterexamples, not a new theorem. No original increment or auditable alternative emerged, so no claim is made.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The Kenig-Merle reduction and variational trapping were verified, but unconditional rigidity of the nonradial critical element (finite mass, zero momentum, sublinear drift for the nonlocal degree-(5+2alpha) nonlinearity across 0<alpha<3) remains unproved; the supporting scripts are verification checks and textbook counterexamples, not a new theorem. No original increment or auditable alternative emerged, so no claim is made.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
