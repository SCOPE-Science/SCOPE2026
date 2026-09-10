# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Small-swirl Hill vortex rings at fixed impulse: variational existence window versus explicit Pohozaev cutoff
- **Round:** 2026-09-07-first-light-01
- **Lane:** 546
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Mathematical Fluid Dynamics
- **Method:** Grad-Shafranov variational maximization with Steiner symmetrization and Pohozaev integral-identity obstruction

## Problem

Decide a swirl-threshold fragment for the axisymmetric steady Hill vortex: with impulse fixed to the Hill-ball value I0, does the Friedman-Turkington energy maximizer persist for small swirl strength kappa>0 as a compact Hill-like patch solving the Grad-Shafranov equation, and is there an explicit finite kappa1 above which a Pohozaev identity forbids any such compact Steiner-symmetric solution?

## Attempted claim

Fix impulse I0 equal to the Hill-ball impulse and circulation bound of the Hill vortex. With swirl-penalized kinetic energy E_kappa(xi)=E0(xi)-(kappa^2/2)Q(xi) for the explicit quadratic swirl moment Q with shape constant b>0, there exists an explicit kappa0>0 such that for every 0<kappa<kappa0 the maximization of E_kappa over Steiner-symmetric nonnegative densities of impulse I0 is attained, and the maximizer is a compactly supported Hill-like patch solving L psi = r^2 H'(psi)+(1/(2r^2))(C_kappa^2)'(psi) with C_kappa(s)=kappa*b*s_+, converging to the Hill ball as kappa->0. Binary test: exhibit kappa0 in closed form and verify maximizer Euler-Lagrange, compact support, and kappa->0 limit.

## Research outcome

Repaired TARGET claim: explicit window kappa0=sqrt(3/2)/b with full Qtilde lemmas, closedness/attainment without symmetrization monotonicity, rigorous W>0 + uniform support, and closed kappa->0 limit; constants and VERIFY_OK scripts unchanged.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Constants verified independently: re-ran inputs/artifacts/verify_target.py and verify_qtilde.py -> VERIFY_OK. Exact rationals correct: I0=4pi/15, Gamma0=4pi/3, E0,H=8pi/315, relative moment M0=16pi/23625, decaying-psi moment Qtilde_H=16pi/945 (interior 8pi/1575 + exterior 8pi/675), kappa0^2=E0/Qtilde=3/2, sharp positivity threshold 3. Quadrature relerr <4e-3, Stokes FD defect ~5e-4, W=2/15 match exact. These are correctly computed moments of the known explicit Hill stream function. Essential PDE inferences FAIL: (1) Lemma 5.2 W_kappa=0 exclusion is incomplete. Case (i) graft adds mass with Delta I>0, hence is not an admissible circulation-only variation preserving the impulse equality I=I0; inferring contradiction with Kuhn-Tucker at W=0 requires proving the value function s_kappa(I) has strictly positive derivative at I0, which is asserted via (5.3)-(5.5) with undefined uniform interior constants c0, r_*, osc(phi) and strict Phi-gap across the free boundary (unproved). Case (ii) swap argument similarly asserts existence of outward pair with Phi-gap without construction. (2) Uniform lower bound inf_[0,barkappa] W>=bar w>0 via contradiction is invalid as written: it invokes kappa_j^2/2 D Qtilde ->0 in L^infty_loc to force limit EL to Hill EL with W*=W_H=2/15, which holds only if kappa_j->0, not for a sequence with kappa_j->kappa_*>0 in (0,barkappa]; pointwise positivity on (0,kappa0) therefore not established, and uniform support radius (5.6) depending on bar w is not established. (3) Convergence claims assume W_kappa->W_H and gamma_kappa->0 and uniform Phi_kappa convergence on compacts by the same cluster argument, but multiplier convergence/compactness is not proved and is circular with (2); Hausdorff support convergence therefore not proved. (4) Headline/target mismatch: admitted target requires L psi = r^2 H'(psi)+(1/2r^2)(C_kappa^2)'(psi) local Bragg-Hawthorne/GS steady Euler equation. DRAFT Sec.4 expressly disclaims the pointwise local semilinear identity at fixed kappa>0 beyond the distributional patch identity S psi_kappa=r^2 xi_kappa (which holds by definition psi=K xi) with indicator of the nonlocal swirl-shifted Phi_kappa containing K(psi_+/r^2). The nonlocal term is not a local function of psi, so no exact fixed-kappa Euler steady state in the admitted local sense is proved. Proof vs citation distinguished: FT kernel/decay/tightness/bathtub/Amick-Fraenkel uniqueness cited as black boxes (acceptable in principle) but the new penalty-specific multiplier analysis that must close the argument has the above gaps. value: TARGET route carries no preset-fallback value presumption (fallback Pohozaev cutoff explicitly abandoned in DRAFT Sec.7 as unprovable; research_report confirms fallback NOT claimed). Judged on admitted TARGET headline alone under ordinary value standard. FAIL as intrinsic low value / arbitrary scope / missing substantive Euler result: (1) Objects proved at fixed kappa>0 are nonlocal penalized FT patches, not ex…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Cites FT kernel/decay/tightness/bathtub/Amick-Fraenkel uniqueness and free-boundary regularity (not re-proved). Pointwise local semilinear GS at fixed kappa>0 not asserted beyond proven primal patch + distributional identity. W-uniformity and support radius are per compact subinterval [0,barkappa] with pointwise positivity on (0,kappa0).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
