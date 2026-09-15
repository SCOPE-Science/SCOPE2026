# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Threshold localization for the random Turan number of the 3-uniform linear 4-cycle
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20400
- **Disposition:** NO_RESULT
- **Domain:** Probabilistic Combinatorics
- **Method:** hypergraph container-method transfer analysis

## Problem

Let G^3_{n,p} be the random 3-graph and C^3_4 the 3-uniform linear 4-cycle. Prove a.a.s. as n->infinity: ex(G^3_{n,p},C^3_4)=(1+o(1))e(G^3_{n,p}) for n^{-3}<<p<<n^{-5/3}; ex(G^3_{n,p},C^3_4)=Theta(n^{4/3+o(1)}) for n^{-5/3}<<p<<n^{-2/3}; ex(G^3_{n,p},C^3_4)=Theta(pn^2) for p>>n^{-2/3}, up to polylogarithmic factors in the upper bounds at the transition points.

## Attempted claim

Let G^3_{n,p} be the random 3-graph and C^3_4 the 3-uniform linear 4-cycle. Prove a.a.s. as n->infinity: ex(G^3_{n,p},C^3_4)=(1+o(1))e(G^3_{n,p}) for n^{-3}<<p<<n^{-5/3}; ex(G^3_{n,p},C^3_4)=Theta(n^{4/3+o(1)}) for n^{-5/3}<<p<<n^{-2/3}; ex(G^3_{n,p},C^3_4)=Theta(pn^2) for p>>n^{-2/3}, up to polylogarithmic factors in the upper bounds at the transition points.

## Research outcome

Target blocked: the star obstruction defeats the container-transfer upper bounds for ex(G^3_{n,p},C^3_4); only routine lower bounds verified, no independently valuable finding, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Upper bounds via container transfer are blocked by the star obstruction: every vertex-star is C^3_4-free with Theta(n^2) edges, falsifying balanced supersaturation at m ~ n^{4/3}. The dense-regime repair needs stability machinery beyond this pass. Only routine lower bounds were verified.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Upper bounds via container transfer are blocked by the star obstruction: every vertex-star is C^3_4-free with Theta(n^2) edges, falsifying balanced supersaturation at m ~ n^{4/3}. The dense-regime repair needs stability machinery beyond this pass. Only routine lower bounds were verified.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
