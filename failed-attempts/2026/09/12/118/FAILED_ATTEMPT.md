# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quantitative ASEP Euler hydrodynamic rate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1387
- **Disposition:** NO_RESULT
- **Domain:** interacting particle systems / hydrodynamic limits
- **Method:** relative entropy / block estimates

## Problem

Prove or disprove that for ASEP on Z_N with fixed rates p greater than q, p+q=1, under Euler scaling y=x/N and tau=t/N on the continuum torus T=R/Z, for every C^2 initial density profile rho0 on T with values in [delta,1-delta] whose inviscid Burgers evolution rho(y,tau) stays smooth up to fixed T0 greater than 0, the basic-coupled empirical box-averaged density rho^N(y,tau) with mesoscopic box width N^{-1/2} satisfies sup_{tau in [0,T0]} E[||rho^N(.,tau)-rho(.,tau)||_{L^1(T)}] less than or equal to C N^{-1/4}, where C depends only on p, q, delta, rho0, T0. A complete answer is either a rigorous proof of this rate for all large N, or an explicit smooth rho0, T0 and subsequence of N violating the stated inequality.

## Attempted claim

Prove or disprove that for ASEP on Z_N with fixed rates p greater than q, p+q=1, under Euler scaling y=x/N and tau=t/N on the continuum torus T=R/Z, for every C^2 initial density profile rho0 on T with values in [delta,1-delta] whose inviscid Burgers evolution rho(y,tau) stays smooth up to fixed T0 greater than 0, the basic-coupled empirical box-averaged density rho^N(y,tau) with mesoscopic box width N^{-1/2} satisfies sup_{tau in [0,T0]} E[||rho^N(.,tau)-rho(.,tau)||_{L^1(T)}] less than or equal to C N^{-1/4}, where C depends only on p, q, delta, rho0, T0. A complete answer is either a rigorous proof of this rate for all large N, or an explicit smooth rho0, T0 and subsequence of N violating the stated inequality.

## Research outcome

Target ASEP Euler N^{-1/4} rate could be neither proved nor disproved in-session; entropy-budget costing shows the sharp proof needs beyond-first-order machinery, while TASEP simulations support the rate; clean exit with WORKLOG and scaling artifacts preserved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No rigorous upper or lower bound resolving the target was established; evidence is limited to scaling analysis and small-N TASEP Monte Carlo (N<=1024, tau in {0,0.2}, one sinusoidal profile). The blocking-obstacle costing is an order-of-magnitude estimate, not a no-go theorem, and the artifacts do not constitute proof of the claimed rate.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No rigorous upper or lower bound resolving the target was established; evidence is limited to scaling analysis and small-N TASEP Monte Carlo (N<=1024, tau in {0,0.2}, one sinusoidal profile). The blocking-obstacle costing is an order-of-magnitude estimate, not a no-go theorem, and the artifacts do not constitute proof of the claimed rate.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
