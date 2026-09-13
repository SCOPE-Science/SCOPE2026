# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Threshold-window width exponent for FK q=3 across growing boxes
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1777
- **Disposition:** NO_RESULT
- **Domain:** planar random-cluster / near-critical FK percolation
- **Method:** random-cluster differential/influence inequality in p plus mixing/one-arm bound

## Problem

Prove or disprove the following threshold-window width exponent for FK q=3 across growing boxes: for each integer n>=8 let B_n=[0,n]x[0,n] intersected with Z^2 with nearest-neighbour edges and wired boundary condition, and for p in [0,1] let f_n(p)=P^{wired}_{B_n,p,q=3}(Cross_n) be the wired crossing probability with q=3 fixed and p varying, where Cross_n is left-right open crossing and p_c(3)=sqrt(3)/(1+sqrt(3)). Define p_n(a)=inf{p: f_n(p)>=a} for a in {1/4,3/4} and width w_n=p_n(3/4)-p_n(1/4). Then w_n <= min(1,4*n^{-0.20}) for every n>=8. A complete answer is a rigorous proof of this polynomial window-decay bound across all stated box sizes using a correct random-cluster differential/influence inequality in p, or a rigorous disproof by exhibiting an explicit n>=8 with a certified proof that w_n > min(1,4*n^{-0.20}), establishing a correlation-length-tied lower bound on the threshold window. Scope: q=3, growing wired-box family, p-window defined by the 1/4-3/4 crossing levels. Any rigorous argument is allowed.

## Attempted claim

Prove or disprove the following threshold-window width exponent for FK q=3 across growing boxes: for each integer n>=8 let B_n=[0,n]x[0,n] intersected with Z^2 with nearest-neighbour edges and wired boundary condition, and for p in [0,1] let f_n(p)=P^{wired}_{B_n,p,q=3}(Cross_n) be the wired crossing probability with q=3 fixed and p varying, where Cross_n is left-right open crossing and p_c(3)=sqrt(3)/(1+sqrt(3)). Define p_n(a)=inf{p: f_n(p)>=a} for a in {1/4,3/4} and width w_n=p_n(3/4)-p_n(1/4). Then w_n <= min(1,4*n^{-0.20}) for every n>=8. A complete answer is a rigorous proof of this polynomial window-decay bound across all stated box sizes using a correct random-cluster differential/influence inequality in p, or a rigorous disproof by exhibiting an explicit n>=8 with a certified proof that w_n > min(1,4*n^{-0.20}), establishing a correlation-length-tied lower bound on the threshold window. Scope: q=3, growing wired-box family, p-window defined by the 1/4-3/4 crossing levels. Any rigorous argument is allowed.

## Research outcome

Target blocked: polynomial window w_n<=4n^{-0.2} for wired-box FK q=3 needs unavailable q=3 arm estimates; generic bounds give only O(1/log n); disproof infeasible. Clean exit with no finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No unconditional proof or disproof of the polynomial window was obtained. Generic influence methods cap at logarithmic width; quantitative routes need unavailable q=3 arm/mixing estimates; disproof needs an infeasible large-box certificate. Only the trivial n<=1024 regime and standard reductions were established.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No unconditional proof or disproof of the polynomial window was obtained. Generic influence methods cap at logarithmic width; quantitative routes need unavailable q=3 arm/mixing estimates; disproof needs an infeasible large-box certificate. Only the trivial n<=1024 regime and standard reductions were established.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
