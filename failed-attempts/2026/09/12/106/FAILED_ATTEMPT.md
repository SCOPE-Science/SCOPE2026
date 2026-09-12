# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Block-doubling ray for escaping (1/2)exp(z): landing vs continuum
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1349
- **Disposition:** NO_RESULT
- **Domain:** transcendental dynamics
- **Method:** exponential dynamic rays / slow-address speed ordering

## Problem

Fix E1(z)=(1/2)*exp(z). Its singular value 0 escapes to infinity along 0, 0.5, 0.824..., 1.14, 1.56, 2.38, 5.44, 116,... so the postsingular set is unbounded and the Julia set is C (escaping regime, not attracting). Let a=(a_n)_{n>=1} over {0,1} be the block-doubling address obtained by concatenating blocks B_k=0^{2^k}1^{2^k} for k>=0 in order, which is bounded, aperiodic and slow in the Schleicher-Zimmer sense. Let g_a:(t_a,infty)->C be its Schleicher-Zimmer dynamic ray. Decide with proof which holds: (i) g_a lands, i.e. lim_{t downarrow t_a} g_a(t) exists and is finite, and state whether the landing point is escaping or non-escaping; or (ii) g_a does not land and its accumulation set in C contains a nondegenerate continuum. A complete answer proves exactly one of (i),(ii) for this fixed escaping map and address, testing lacunary block growth at the speed-ordered bouquet boundary.

## Attempted claim

Fix E1(z)=(1/2)*exp(z). Its singular value 0 escapes to infinity along 0, 0.5, 0.824..., 1.14, 1.56, 2.38, 5.44, 116,... so the postsingular set is unbounded and the Julia set is C (escaping regime, not attracting). Let a=(a_n)_{n>=1} over {0,1} be the block-doubling address obtained by concatenating blocks B_k=0^{2^k}1^{2^k} for k>=0 in order, which is bounded, aperiodic and slow in the Schleicher-Zimmer sense. Let g_a:(t_a,infty)->C be its Schleicher-Zimmer dynamic ray. Decide with proof which holds: (i) g_a lands, i.e. lim_{t downarrow t_a} g_a(t) exists and is finite, and state whether the landing point is escaping or non-escaping; or (ii) g_a does not land and its accumulation set in C contains a nondegenerate continuum. A complete answer proves exactly one of (i),(ii) for this fixed escaping map and address, testing lacunary block growth at the speed-ordered bouquet boundary.

## Research outcome

Target blocked: landing-vs-continuum for the block-doubling ray of (1/2)exp(z) could not be proved within the pass. Extensive numerics (pullback to t=1e-6, N>2M, tail-independence, 47-step itinerary match, escape at step ~50) favor landing at an escaping point, but this remains conjecture without the infinite-block contraction certificate.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof of the t-downarrow-0 limit was obtained: the uniform infinite-block contraction certificate is missing, interval enclosures blow up at depth N=4000, and general escaping-map landing-theorem hypotheses are unverifiable offline. All numerical artifacts are conjectural evidence only, not proof.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof of the t-downarrow-0 limit was obtained: the uniform infinite-block contraction certificate is missing, interval enclosures blow up at depth N=4000, and general escaping-map landing-theorem hypotheses are unverifiable offline. All numerical artifacts are conjectural evidence only, not proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
