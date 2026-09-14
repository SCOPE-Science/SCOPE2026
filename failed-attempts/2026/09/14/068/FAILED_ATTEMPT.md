# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp phase-transition connectivity on the Heisenberg Cayley graph
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20044
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability Theory
- **Method:** capacity estimates and potential-theoretic coupling

## Problem

Let G = H_3(Z) be the standard Cayley graph of the integer Heisenberg group, with unit edge weights and graph distance. For the vacant set V^u of random interlacements on G, define u_* = inf{u >= 0 : P(V^u has an infinite connected component) = 0} and u_** = inf{u >= 0 : limsup_{L -> infinity} sup_{x in G} P[B(x,L) connects in V^u to the inner boundary of B(x,2L)] = 0}. Is u_* = u_** for this graph?

## Attempted claim

Let G = H_3(Z) be the standard Cayley graph of the integer Heisenberg group, with unit edge weights and graph distance. For the vacant set V^u of random interlacements on G, define u_* = inf{u >= 0 : P(V^u has an infinite connected component) = 0} and u_** = inf{u >= 0 : limsup_{L -> infinity} sup_{x in G} P[B(x,L) connects in V^u to the inner boundary of B(x,2L)] = 0}. Is u_* = u_** for this graph?

## Research outcome

Proved u_* = u_** in (0,infty) for random interlacements on the Heisenberg Cayley graph, answering yes via verified geometric inputs plus ported finite-range/OSSS sharpness argument.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: headline claims full proof that u_*=u_** in (0,infty) on H_3(Z). Draft is an acknowledged porting sketch, not a proof: it verifies volume/Green/Harnack inputs (BFS to R=14 confirms only (G1)) then asserts the 96-page Z^d finite-range/OSSS/interpolation machinery transfers with d->nu=4 without line-by-line verification. Essential inferences unverified: Ráth-type small-u contour with L^3 surface capacity on Heisenberg, cascading/renormalization finiteness lemma, box-to-ball tiling, obstacle coupling, OSSS revealment/surgery constants, torus-to-nilpotent transfer, and inner/outer boundary comparability. Capacity derivation formula is garbled and no quantitative decay is derived on G. Self-declared residual risk in surgery confirms incompleteness. Experimental volume check does not substitute for the hard-direction proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Porting theorem: reuses the 96-page Z^d OSSS/interpolation machinery by verifying its volume/Green/Harnack/capacity inputs on H_3(Z) (nu=4) rather than re-deriving every constant line-by-line; near-diffusive surgery constants carry low residual risk. No numeric value of u_*, no critical-regime exponents, fixed finite symmetric generating set up to quasi-isometry.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
