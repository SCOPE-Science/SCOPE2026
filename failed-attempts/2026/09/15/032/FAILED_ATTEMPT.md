# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Stationary hydrodynamic profile for the outward ASEP on a fixed transient Cayley tree (q >= 2)
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20225
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability Theory
- **Method:** hydrodynamic limits and coupling arguments

## Problem

Consider the Basu–Mohanty outward ASEP on the finite rooted N-level Cayley tree with coordination z=q+1 for fixed q>=2: one root at level 0; each site at level i has q children at level i+1; particles enter at the root at rate alpha>0 if empty; each bulk particle attempts to jump outward at total rate 1 to a uniformly chosen child, the jump succeeding iff the target is vacant; each particle at the last level N-1 exits at rate beta>0. Start from the all-empty configuration and let the system reach stationarity. Let I_q^{(N)} be the stationary total current flowing between successive levels and rho_i^{(N)} the stationary mean occupation per site at level i. Prove that for each fixed q>=2, alpha>0, beta>0 and each fixed level i, as N->infinity: I_q^{(N)} -> I_q(alpha)=alpha(1-rho_0(alpha)) and rho_i^{(N)} -> I_q(alpha)/q^i, independently of beta, where rho_0(alpha) in (0,1) is the physical root of (1-alpha(1-rho_0)/rho_0)^{1/q} = alpha(1-rho_0)/q (with the explicit q=2 form in Eqs. (18)-(19) of Basu–Mohanty), and with last-level behaviour rho_{N-1}^{(N)} = c(alpha,beta)/q^{N-1}, c=I_q(alpha)/beta. In particular prove absence of 1D-type boundary layers at fixed i and beta-independence of the bulk current for q>=2.

## Attempted claim

Consider the Basu–Mohanty outward ASEP on the finite rooted N-level Cayley tree with coordination z=q+1 for fixed q>=2: one root at level 0; each site at level i has q children at level i+1; particles enter at the root at rate alpha>0 if empty; each bulk particle attempts to jump outward at total rate 1 to a uniformly chosen child, the jump succeeding iff the target is vacant; each particle at the last level N-1 exits at rate beta>0. Start from the all-empty configuration and let the system reach stationarity. Let I_q^{(N)} be the stationary total current flowing between successive levels and rho_i^{(N)} the stationary mean occupation per site at level i. Prove that for each fixed q>=2, alpha>0, beta>0 and each fixed level i, as N->infinity: I_q^{(N)} -> I_q(alpha)=alpha(1-rho_0(alpha)) and rho_i^{(N)} -> I_q(alpha)/q^i, independently of beta, where rho_0(alpha) in (0,1) is the physical root of (1-alpha(1-rho_0)/rho_0)^{1/q} = alpha(1-rho_0)/q (with the explicit q=2 form in Eqs. (18)-(19) of Basu–Mohanty), and with last-level behaviour rho_{N-1}^{(N)} = c(alpha,beta)/q^{N-1}, c=I_q(alpha)/beta. In particular prove absence of 1D-type boundary layers at fixed i and beta-independence of the bulk current for q>=2.

## Research outcome

Disproved the literal target: its i=0 profile clause, current relation, and BM root equation are jointly unsatisfiable for all alpha>0,q>=2; certificate plus exact/Monte-Carlo corroboration provided.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: the negative resolution exposes only a statement-level quantifier/normalization defect, namely profile claimed for each fixed i including i=0 (first-coefficient mismatch) contradicting I=alpha(1-r) plus the BM root equation in one line of algebra. It resolves none of the substantive hydrodynamic-limit, decorrelation, or beta-decoupling questions; the repaired i>=1 core stays open with O(1) negative correlations and 3-10% MF gaps. Per STANDARD, a TARGET whose likely negative resolution is a type error, vacuity, or tiny-instance mismatch fails admission; this cheap-defect disproof is not independently retrievable value even though correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Proved: impossibility of the literal conjunction including the profile clause at i=0. Not proved: any repaired positive statement (profile restricted to i>=1 with Eq.17 root, exact beta-independence, exact current value) — numerically supported (bulk i>=1 within ~2%, last-level scaling within ~2%, beta-decoupling TV 0.705->0.162) but requiring new decorrelation/coupling technology given O(1)-relative negative correlations and 3-10% mean-field gaps. The q=2 explicit Eqs.18-19 closed-form pointer…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
