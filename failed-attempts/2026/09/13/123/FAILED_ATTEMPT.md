# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Symmetric degree-9 Maynard-Tao ratio at k=50
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1758
- **Disposition:** NO_RESULT
- **Domain:** analytic number theory
- **Method:** symmetric polynomial variational optimization

## Problem

Let k=50 and let R={t in [0,1]^50: sum t_i <= 1}. For symmetric polynomials P of total degree at most 9 define F(t)=P(t) on R and 0 elsewhere, and define I(F)=integral_R F^2 dt and J_m(F)=integral_{R^{(m)}} (integral_0^{1-sum_{i != m} t_i} F dt_m)^2 dt^{(m)} with M(F)=(sum_{m=1}^{50} J_m(F))/I(F) under level of distribution theta=1/2. Is there such a degree<=9 symmetric polynomial with M(F)>4, i.e. sufficient for two primes in a 50-tuple under Bombieri-Vinogradov alone? A complete answer is either explicit coefficients of P plus a rigorous certified numerical quadrature proving M(F)>4, or a rigorous proof that no symmetric degree<=9 polynomial achieves M(F)>4.

## Attempted claim

Let k=50 and let R={t in [0,1]^50: sum t_i <= 1}. For symmetric polynomials P of total degree at most 9 define F(t)=P(t) on R and 0 elsewhere, and define I(F)=integral_R F^2 dt and J_m(F)=integral_{R^{(m)}} (integral_0^{1-sum_{i != m} t_i} F dt_m)^2 dt^{(m)} with M(F)=(sum_{m=1}^{50} J_m(F))/I(F) under level of distribution theta=1/2. Is there such a degree<=9 symmetric polynomial with M(F)>4, i.e. sufficient for two primes in a 50-tuple under Bombieri-Vinogradov alone? A complete answer is either explicit coefficients of P plus a rigorous certified numerical quadrature proving M(F)>4, or a rigorous proof that no symmetric degree<=9 polynomial achieves M(F)>4.

## Research outcome

Target blocked by ill-conditioning: symmetric degree<=9 sieve ratio at k=50 could not be certified above or below 4 within the lane; honest NO_RESULT with validated computational framework preserved as artifacts.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The lane produced a validated exact dynamic-program framework and a consistent but uncertified numerical signal (float maximum sieve ratio 3.33-3.60, below 4); however the Gram matrix is numerically singular (29 of 97 scaled eigenvalues below 1e-12), so no certified existence or nonexistence claim can be made and the 60-digit high-precision eigensolve was not completed before consolidation.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The lane produced a validated exact dynamic-program framework and a consistent but uncertified numerical signal (float maximum sieve ratio 3.33-3.60, below 4); however the Gram matrix is numerically singular (29 of 97 scaled eigenvalues below 1e-12), so no certified existence or nonexistence claim can be made and the 60-digit high-precision eigensolve was not completed before consolidation.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
