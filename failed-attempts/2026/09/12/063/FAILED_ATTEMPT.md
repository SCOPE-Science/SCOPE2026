# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform power convergence rate of entropic interpolation to geodesics
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1222
- **Disposition:** NO_RESULT
- **Domain:** metric geometry / optimal transport
- **Method:** zero-noise Schrodinger-to-Wasserstein geodesic selection estimates

## Problem

Let (X,d,m) be a compact RCD(K,infinity) space and let mu0,mu1 in P_2(X) have finite entropy, finite Fisher information, and densities bounded above and below on their supports. Let mu_t, t in [0,1], be any W_2-geodesic joining mu0 to mu1 and mu^epsilon_t the Schrodinger entropic interpolation with parameter epsilon>0 and the same endpoints. Prove or disprove: there exist exponents alpha>0 and constant C depending only on K, diam(X), and the endpoint density/Fisher bounds such that sup_{t in [0,1]} W_2(mu^epsilon_t,mu_t) <= C*epsilon^{alpha} for all small epsilon>0 (after suitable choice of geodesic when non-unique). A complete answer is either a proof of such a uniform quantitative zero-noise convergence rate with explicit alpha and C, or a proof that no uniform power rate holds by exhibiting an RCD base (e.g. with branching geodesics or a conical singularity) and endpoints where limsup_{epsilon->0} epsilon^{-alpha} sup_t W_2(mu^epsilon_t,mu_t)=infinity for every alpha>0.

## Attempted claim

Let (X,d,m) be a compact RCD(K,infinity) space and let mu0,mu1 in P_2(X) have finite entropy, finite Fisher information, and densities bounded above and below on their supports. Let mu_t, t in [0,1], be any W_2-geodesic joining mu0 to mu1 and mu^epsilon_t the Schrodinger entropic interpolation with parameter epsilon>0 and the same endpoints. Prove or disprove: there exist exponents alpha>0 and constant C depending only on K, diam(X), and the endpoint density/Fisher bounds such that sup_{t in [0,1]} W_2(mu^epsilon_t,mu_t) <= C*epsilon^{alpha} for all small epsilon>0 (after suitable choice of geodesic when non-unique). A complete answer is either a proof of such a uniform quantitative zero-noise convergence rate with explicit alpha and C, or a proof that no uniform power rate holds by exhibiting an RCD base (e.g. with branching geodesics or a conical singularity) and endpoints where limsup_{epsilon->0} epsilon^{-alpha} sup_t W_2(mu^epsilon_t,mu_t)=infinity for every alpha>0.

## Research outcome

Target blocked on both horns: no uniform action-excess-to-distance modulus follows from the coarse bounds, and no explicit slower-than-every-power singular example was found; bounded 1D Sinkhorn checks confirm only the easy smooth-case power rate, so a clean exit with no claim is returned.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The session established neither a uniform power-rate proof nor a rigorous slower-than-every-power counterexample: the proof route lacks the uniform stability modulus and the disproof route lacks an explicit construction, while the 1D Sinkhorn proxy numerics cover only smooth and mildly rough densities and cannot address uniformity over the infinite-dimensional RCD(K,infinity) class.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The session established neither a uniform power-rate proof nor a rigorous slower-than-every-power counterexample: the proof route lacks the uniform stability modulus and the disproof route lacks an explicit construction, while the 1D Sinkhorn proxy numerics cover only smooth and mildly rough densities and cannot address uniformity over the infinite-dimensional RCD(K,infinity) class.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
