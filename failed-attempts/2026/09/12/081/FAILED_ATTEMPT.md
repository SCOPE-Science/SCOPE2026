# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hyperbolic fixed-window vertex fluctuation law and CLT
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1265
- **Disposition:** AUDIT_1_REJECT
- **Domain:** hyperbolic stochastic geometry
- **Method:** stabilization plus Malliavin-Stein with hyperbolic-to-Euclidean localization

## Problem

Let H^2 be the hyperbolic plane of curvature -1 with stationary Poisson-Voronoi tessellation of intensity lambda>0. Fix the geodesic ball B_1 of radius 1 about a fixed origin and let N_lambda be the number of Voronoi vertices in B_1. Determine the fixed-window high-intensity fluctuation law: prove E[N_lambda]/lambda converges to an explicit constant mu*>0 given by a stated integral with curvature error control, prove liminf_{lambda->infinity} Var(N_lambda)/lambda >= v* for an explicit v*>0, and prove (N_lambda-E[N_lambda])/sqrt(Var(N_lambda)) => N(0,1) as lambda->infinity. A complete answer states mu* and v*, gives the mean asymptotics, the variance lower bound, and Gaussian convergence for this fixed window with hyperbolic-to-Euclidean localization control.

## Attempted claim

Let H^2 be the hyperbolic plane of curvature -1 with stationary Poisson-Voronoi tessellation of intensity lambda>0. Fix the geodesic ball B_1 of radius 1 about a fixed origin and let N_lambda be the number of Voronoi vertices in B_1. Determine the fixed-window high-intensity fluctuation law: prove E[N_lambda]/lambda converges to an explicit constant mu*>0 given by a stated integral with curvature error control, prove liminf_{lambda->infinity} Var(N_lambda)/lambda >= v* for an explicit v*>0, and prove (N_lambda-E[N_lambda])/sqrt(Var(N_lambda)) => N(0,1) as lambda->infinity. A complete answer states mu* and v*, gives the mean asymptotics, the variance lower bound, and Gaussian convergence for this fixed window with hyperbolic-to-Euclidean localization control.

## Research outcome

Proved the hyperbolic fixed-window vertex fluctuation law: mean ratio -> mu*=4pi(cosh1-1), variance-per-intensity liminf >= v*=3, and Gaussian CLT via localization plus Malliavin-Stein.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL. ADMISSION_DEFECT: the admitted radius-1 fixed-window high-intensity target is mechanically implied by nearest prior substantive work and should not have passed admission originality. Mean: Calka-Chapron-Enriquez arXiv:1807.09043 proves high-intensity mean asymptotics on Riemannian manifolds with first term equal to Euclidean (e2=6 per typical cell, i.e. vertex density 2 per area) plus curvature second term, and Isokawa plus D'Achille-Thale arXiv:2606.26049 Thm 1.1 give exact hyperbolic D_{d,k}(lambda) face-volume densities whose large-lambda expansion yields E[N]/lambda->2vol(B1); multiplying textbook Miles intensity 2 by textbook vol(B1)=2pi(cosh1-1) is parameter substitution. Variance/CLT: Penrose-Yukich 2013 limit theory on manifolds and Lachieze-Rey-Schulte-Yukich 2019 normal approximation for exponentially stabilizing functionals explicitly covering m-dimensional Riemannian manifolds, plus Herold-Hug-Thale PTRF 2021 fixed-window growing-intensity CLT in hyperbolic space via Malliavin-Stein/U-statistics, substantively imply linear variance nondegeneracy and Gaussian limit for this strict special case (d=2, H^2, fixed B1). Hyperbolic-to-Euclidean normal-chart localization at scale lambda^-1/2 is the standard step already in those manifold papers, not a new idea. A timestamp or literal-title search miss does not establish priority. value: FAIL. ADMISSION_DEFECT: target fixes arbitrary radius 1 and asks for Euclidean-inherited first order plus a crude rounded variance bound, which the STANDARD rules out as arbitrary parameter fact and mere parameter substitution. mu*=2vol(B1) combines two textbook facts (Euclidean Poisson-Voronoi vertex intensity 2 and hyperbolic disk area 2pi(coshR-1)) with no curvature phenomenon in the limit; v*=3 is a non-sharp rounding of 3.2076 obtained from an arbitrary inner radius 1/2, with no exact limit, no demonstrated downstream need, and no benchmark significance. The CLT is the expected Euclidean inheritance in the fixed-window high-intensity regime, unlike the genuinely new hyperbolic growing-window CLT failure for d>=4 discovered by Herold-Hug-Thale; no new boundary, classification, counterexample, or exact natural invariant motivated before computation is contributed. Correct and even if deemed new, this is textbook restatement plus arbitrary slice, not independently worth retrieving later.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The CLT rate O(lambda^{-1/4} log^K lambda) is not optimized and K is not made explicit; only convergence is asserted. Existence or exact value of lim Var(N_lambda)/lambda is not claimed, only the lower bound v*=3. The mean remainder O(lambda^{1/2} log^4 lambda) is crude but explicit. General-position, moment bounds, and standard Malliavin-Stein/stabilization ingredients are cited from the Poisson-Voronoi literature rather than re-proved; the simulations corroborate the transferred Euclidean ing…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
