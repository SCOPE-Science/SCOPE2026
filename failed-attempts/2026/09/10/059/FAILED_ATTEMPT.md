# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Primarity versus complemented splitting in the Schlumprecht cell: block-factorization or distortion-separated RIS witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 631
- **Disposition:** NO_RESULT
- **Domain:** Banach Space Geometry
- **Method:** Ramsey-theoretic block-basis combinatorics with distortion estimation and Bourgain-Delbaen comparison

## Problem

Decide the primarity versus complemented-splitting dichotomy for the named Schlumprecht cell S: either prove S is primary via a new uniform block-diagonal factorization lemma, or exhibit a certified pair of complemented disjoint RIS block subspaces of S with incomparable distortion witnesses and computed projection norms.

## Attempted claim

The Schlumprecht space S (with f(t)=log2(t+1)) is primary: whenever S is isomorphic to E (+) F for closed subspaces E,F (equivalently, via a bounded projection on S), either E or F is isomorphic to S. Proof via a uniform block-diagonal factorization lemma: there exists K such that every bounded operator on a tail of S K-factors the identity on some block subspace, forcing one summand to contain a complemented copy of S isomorphic to S.

## Research outcome

NO_RESULT. Target blocked with exact refutation of literal lemma (rank-one obstruction) and circularity of repaired route. Preset fallback attempted and blocked: finite-vector ratio arithmetic certifies >2 on finite vectors but the exact (supports, projection<=6 x2, ratio>=2 at logged L*) certificate is not jointly established. Honest CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Literal uniform K-factorization lemma for all bounded operators is false (rank-one/compact obstruction, replayed via output/artifacts/verify_target_block.py); repaired projection dichotomy is circular without a new uniform estimate. Fallback exact criterion unmet: finite-vector ratio >2 replays (18/log2(442)>2, output/artifacts/ratio_finite_cert.py) but infinite disjoint normalized RIS pair with logged growth integers and both canonical projection bounds <=6 not established. No original independently valuable increment; finite computations are standard identities. Gate record: output/target_exit.json (CLEAN_EXIT / ATTEMPTED_AND_BLOCKED).

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Literal uniform K-factorization lemma for all bounded operators is false (rank-one/compact obstruction, replayed via output/artifacts/verify_target_block.py); repaired projection dichotomy is circular without a new uniform estimate. Fallback exact criterion unmet: finite-vector ratio >2 replays (18/log2(442)>2, output/artifacts/ratio_finite_cert.py) but infinite disjoint normalized RIS pair with logged growth integers and both canonical projection bounds <=6 not established. No original indepen…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
