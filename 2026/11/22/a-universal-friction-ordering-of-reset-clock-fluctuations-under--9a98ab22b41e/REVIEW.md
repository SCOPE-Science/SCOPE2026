# Scientific review: friction ordering of velocity-reset clock noise

## Correctness — PASS

The claim specifies positive forcing, reset prefactor and damping; zero thermal noise; the full exponent range \(\alpha>-1\); and iid reset cycles. Integration of the exact deterministic trajectory gives the stated event hazard, including its integrable singularity for negative exponents. The decisive lemma is not numerical: strict monotonicity of \(z/(e^z-1)\) determines the hazard-elasticity direction, then the quantile ratios have a strict rank monotonicity. Equal-mean normalized quantiles cross exactly once, proving strict convex order. Renewal variance asymptotics give the count-Fano interpretation. The Weibull and exponential endpoint limits and the explicit strong-damping coefficient follow from justified survival-integral limits, with finite moments. The standalone numerical tests passed but are supporting checks only.

## Originality — PASS, with residual priority risk

The closest source, Takeishi–Akimoto, arXiv:2603.14164, constructs precisely the velocity-resetting dynamics, obtains general frictionless interval densities, and solves the damped deterministic one-power stationary velocity profile. Those established facts are credited. Its inspected waiting-time and damped sections, and conclusion, do not report monotone *normalized convex order across damping for all power exponents* or the sharp count-noise endpoints and coefficient. Eule–Metzger, arXiv:1510.07876, provides generic arbitrary-wait renewal resetting theory, not the special friction-parameter ordering. The 2025 stochastic-order paper of Arab et al. supplies generic ordering terminology in a distinct transformed-distribution family, without the present friction-controlled survival family. Indexed related results on velocity-only Poisson resetting and active velocity forcing have different dynamics and observables; none supplies a stronger covering statement. Standard star-order and renewal tools are not claimed as invented. Priority beyond checked indexes, especially alternate reliability terminology or unpublished computations, remains a real risk.

## Value — PASS

The result is motivated by a non-Poisson event clock in a model introduced to explain nonlinear transport. Its single global statement controls **all** normalized convex costs of inter-reset timing, not just one selected variance, and distinguishes the two physically opposite classes \(\alpha>0\) and \(-1<\alpha<0\) without adjusting other parameters. It gives a sharp Weibull-to-Poisson noise range and explicit damping convergence scale. This determines how viscous dissipation changes the predictability of collision/reset events despite altering their absolute frequency, and provides exact benchmarks for physical count measurements and simulation. It is not a routine recomputation of the known stationary velocity density.

## Limits and closest comparisons

No conclusion extends to nonzero acceleration noise, non-iid intervals, correlated reset memories, finite-time count noise, or variable damping in one cycle. Numerical checks are finite. The general stochastic-order literature could contain an unindexed equivalent specialization; a publication-priority search is not a proof of uniqueness.

Self-review: passed. Independent audit: not yet performed.
