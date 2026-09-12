# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform Lyapunov bound and time-average tightness for fractional Burgers
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1103
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Stochastic Analysis
- **Method:** Ito energy estimate with Krylov-Bogoliubov tightness via compact embedding

## Problem

Let u_N be the Galerkin-truncated renormalized fractional stochastic Burgers system on zero-mean fields over T^2 with dissipation -(-Delta)^{5/4}, divergence-form quadratic transport Wick-ordered by C_N, and Fourier-truncated white forcing at |k|<=N. With Lyapunov function V(u)=||u||_{L^2(T^2)}^2, the target is an N-independent K<infinity such that sup_{N>=1} sup_{t>=0} E V(u_N(t)) <= K(1+V(u_0)), proved by a direct Ito energy estimate using only dissipation-versus-transport cancellation, together with tightness in C^{-kappa}(T^2), kappa>0 small, of the time-averaged laws Q^T_N = T^{-1}int_0^T Law(u_N(t)) dt uniformly in N and T>=1, yielding tight limit points as candidate invariant measures with no gap asserted and no use of candidate 1.

## Attempted claim

The renormalized fractional Burgers Galerkin dynamics at sigma=5/2 on T^2 satisfy sup_N sup_{t>=0} E||u_N(t)||_{L^2}^2 <= K(1+||u_0||_{L^2}^2) by direct Ito energy cancellation, and their time-averaged laws are tight in C^{-kappa} uniformly in N and T>=1; certified super-uniform moment growth or explicit mass escape falsifies the claim, and no part of the certificate consumes candidate 1.

## Research outcome

Proved the full target: exact transport cancellation yields an N-uniform Ito Lyapunov bound with explicit K and uniform tightness of time averages in C^{-kappa}.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: Headline is textbook Galerkin energy ledger mechanically implied by standard skew-symmetric SPDE theory, not new. Exact cancellation <v,partial_x(v^2/2)>=0 is undergraduate integration-by-parts underlying all Burgers/Navier-Stokes energy estimates (Da Prato-Debussche-Temam 1994 stochastic Burgers; E-Khanin-Mazel-Sinai 2000 1D Burgers invariant measures; Goldys-Maslowski 2005 1D Burgers/2D Navier-Stokes ergodicity; Brzezniak-Debbi-Goldys 2011 FSBE Lemmas 3-4 prove harder 1D white-noise L2 bounds with interpolation). With trace-class noise and any coercive A the Ito bound d/dt E||u||^2<=-2gamma E||u||^2+tau and Krylov-Bogoliubov tightness via compact Sobolev-Besov embedding are routine exercises; sigma=5/2, e=(1,0), K=max(1,tau/2gamma) are mere parameter substitutions. Wick ordering is vacuous here since gradient kills constant, so no renormalization content. No source needs to state sigma=5/2 verbatim: broader textbook theorem substantively implies it. ADMISSION_DEFECT: Admission originality preflight claimed no broader theorem implies 2D tightness lemma, missing that generic dissipative skew-symmetric Galerkin theory does. value: FAIL: Correct but textbook restatement plus arbitrary parameter slice with no independent retrieval value. Bound holds for any sigma>0 and any divergence-form skew-symmetric Galerkin truncation with additive trace-class noise; sigma=5/2, unit torus, e=(1,0) add no boundary. Trace-class noise makes system classical function-valued, so 2D singular-transport/Wick narrative is vacuous (renormalization does nothing, nonlinearity cancels entirely, linear OU gives same bound). Explicit K is Poincare ratio tau/2gamma, mechanically computable, not a needed exact invariant; tightness is standard Krylov-Bogoliubov input with no limit passage, uniqueness, mixing or sampling benchmark demonstrated. Certification via 16^2-grid Euler-Maruyama does not create value per STANDARD. ADMISSION_DEFECT: Admission triviality/value preflight passed non-vacuity and two-sided value, but positive resolution is 3-line exercise and negative resolution (growth/mass escape) was impossible given exact cancellation, so TARGET two-sided value premise was materially false; audit plan itself expected interpolation but none was needed.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The lemma gives uniform boundedness and tightness of Cesaro families only; it does not construct an invariant measure (no Krylov-Bogoliubov limit passage is taken), nor uniqueness, mixing, or any spectral gap. The proof is for the scalar divergence-form gradient-transport Galerkin model with trace-class noise; space-time white noise in 2D and non-gradient or vector-valued variants are not covered. The numerical replay is a finite-resolution consistency check, not part of the analytic proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
