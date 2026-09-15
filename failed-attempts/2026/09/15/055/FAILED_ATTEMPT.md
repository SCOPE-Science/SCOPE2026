# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform Oh-range bilinear restriction for a fixed elliptic cubic perturbation of the paraboloid in R^3
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20261
- **Disposition:** NO_RESULT
- **Domain:** Harmonic Analysis
- **Method:** time-frequency tile decomposition and wave-packet analysis

## Problem

Let Sigma=[0,1]^2 and for |gamma|<=1/2 let phi_gamma(x,y)=x^2+y^2+gamma y^3/3, E_gamma f(xi)=int_Sigma f(x,y) e^{i(xi_1 x+xi_2 y+xi_3 phi_gamma(x,y))} dx dy. Say f_1,f_2 are c_0-separated for fixed c_0>0 if dist(supp f_1,supp f_2)>=c_0. Prove, via time-frequency tile/wave-packet decomposition and polynomial partitioning induction on scales, that for every (p,q) with q>13/4, 5/q+3/p<3, 5/q+1/p<2, there is C_{p,q,c_0} independent of gamma in [-1/2,1/2] with || |E_gamma f_1 E_gamma f_2|^{1/2} ||_{L^q(R^3)} <= C_{p,q,c_0} ||f_1||_{L^p(Sigma)}^{1/2} ||f_2||_{L^p(Sigma)}^{1/2} for all c_0-separated f_1,f_2.

## Attempted claim

Let Sigma=[0,1]^2 and for |gamma|<=1/2 let phi_gamma(x,y)=x^2+y^2+gamma y^3/3, E_gamma f(xi)=int_Sigma f(x,y) e^{i(xi_1 x+xi_2 y+xi_3 phi_gamma(x,y))} dx dy. Say f_1,f_2 are c_0-separated for fixed c_0>0 if dist(supp f_1,supp f_2)>=c_0. Prove, via time-frequency tile/wave-packet decomposition and polynomial partitioning induction on scales, that for every (p,q) with q>13/4, 5/q+3/p<3, 5/q+1/p<2, there is C_{p,q,c_0} independent of gamma in [-1/2,1/2] with || |E_gamma f_1 E_gamma f_2|^{1/2} ||_{L^q(R^3)} <= C_{p,q,c_0} ||f_1||_{L^p(Sigma)}^{1/2} ||f_2||_{L^p(Sigma)}^{1/2} for all c_0-separated f_1,f_2.

## Research outcome

Target blocked: uniform Oh-range bilinear restriction needs the full gamma-uniform induction core, closable by neither reduction nor compactness in the bounded pass; clean exit with no finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The uniform Oh-range bilinear estimate for the cubic perturbation remains unproved in this pass: the full gamma-uniform wave-packet plus polynomial-partitioning induction could not be closed auditably in the bounded time. Only the elementary geometric inputs (uniform ellipticity eigenvalues in [1,3], uniform normal separation) were verified; the analytic induction core is untouched. No counterexample was found and the target remains plausible.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The uniform Oh-range bilinear estimate for the cubic perturbation remains unproved in this pass: the full gamma-uniform wave-packet plus polynomial-partitioning induction could not be closed auditably in the bounded time. Only the elementary geometric inputs (uniform ellipticity eigenvalues in [1,3], uniform normal separation) were verified; the analytic induction core is untouched. No counterexample was found and the target remains plausible.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
