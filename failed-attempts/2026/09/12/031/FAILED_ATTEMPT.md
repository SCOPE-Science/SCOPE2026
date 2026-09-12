# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-term divergence expansion of the fractional KPZ Wick constant
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1104
- **Disposition:** NO_RESULT
- **Domain:** Stochastic Analysis
- **Method:** Wiener-chaos covariance lattice-sum and zeta analysis

## Problem

With Fourier basis e_k(x)=exp(2 pi i k.x) on T^2, eigenvalues (4 pi^2|k|^2)^{5/4} for (-Delta)^{5/4}, stationary variances E|Psihat_k|^2 = 1/(2(4 pi^2|k|^2)^{5/4}), and Fourier cutoff |k|<=N, define C_N = sum_{0<|k|<=N} (4 pi^2|k|^2) E|Psihat_k|^2. The target is the two-term expansion C_N = a_star N^{3/2} + a_0 + o(1) with explicit a_star>0 from the continuum integral and explicit finite part a_0 from Epstein-zeta continuation, both tied to the stated normalization.

## Attempted claim

Under the stated Fourier normalization and cutoff, the fractional KPZ Wick constant satisfies C_N = a_star N^{3/2} + a_0 + o(1) with the explicit continuum coefficient a_star and Epstein-zeta finite part a_0 derived from the lattice sum; any deviation beyond o(1), including a different coefficient or an extra logarithmic term, falsifies the claim.

## Research outcome

Target C_N = a_star N^{3/2} + a_0 + o(1) blocked: exact reduction and constants pinned, dense scan to N=3000 and eight rigorous finite-N jump certificates (VERIFY_OK) show persistent sharp-cutoff fluctuations, but no uniform o(1) bound or infinite-family anomaly was closable; clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No limit statement was proved in either direction: the o(1) remainder needs uniform circle-remainder control and disproof needs an infinite Omega-family bound, both beyond the clock. Finite-N jump certificates are rigorous but decide no asymptotic limit. Constants a_star and a_0 are numerically pinned (50-digit mpmath) but lack certified remainder bounds.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No limit statement was proved in either direction: the o(1) remainder needs uniform circle-remainder control and disproof needs an infinite Omega-family bound, both beyond the clock. Finite-N jump certificates are rigorous but decide no asymptotic limit. Constants a_star and a_0 are numerically pinned (50-digit mpmath) but lack certified remainder bounds.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
