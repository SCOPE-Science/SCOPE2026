# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Is delta*d_0 > 4/3 sufficient for linear-time Omega(n) decoding of general Tanner expander codes?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20501
- **Disposition:** NO_RESULT
- **Domain:** Coding Theory
- **Method:** expander-graph and message-passing analysis

## Problem

Let c,d be fixed integers, 0<alpha,delta<=1 fixed, n->infinity. Let G be a (c,d,alpha,delta)-bipartite vertex expander with bipartition L union R, |L|=n, and let C_0 subset of F_2^d be a binary linear [d,k_0,d_0] inner code. Let T(G,C_0) subset of F_2^n be the Tanner code. If delta*d_0 > 4/3, does there exist a deterministic decoder running in time O_{c,d,alpha,delta}(n) that corrects Omega_{c,d,alpha,delta}(n) adversarial errors for every such G and every such C_0?

## Attempted claim

Let c,d be fixed integers, 0<alpha,delta<=1 fixed, n->infinity. Let G be a (c,d,alpha,delta)-bipartite vertex expander with bipartition L union R, |L|=n, and let C_0 subset of F_2^d be a binary linear [d,k_0,d_0] inner code. Let T(G,C_0) subset of F_2^n be the Tanner code. If delta*d_0 > 4/3, does there exist a deterministic decoder running in time O_{c,d,alpha,delta}(n) that corrects Omega_{c,d,alpha,delta}(n) adversarial errors for every such G and every such C_0?

## Research outcome

Target blocked: delta*d0 > 4/3 sits in the acknowledged open gap (necessary > 1, best proven sufficiency > 2) with every known decoder family provably stopping above 4/3 and no refutation route available; clean exit with no alternative worth pursuing.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof or disproof of the delta*d0 > 4/3 claim was obtained: sufficiency analyses for all known decoder families provably stop above 4/3, distance bounds exclude a planting refutation throughout (4/3,2], and an all-algorithms lower bound is beyond current techniques. Literature search was used only to locate the blocking thresholds, capped at two calls, and all threshold computations were reproduced locally.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof or disproof of the delta*d0 > 4/3 claim was obtained: sufficiency analyses for all known decoder families provably stop above 4/3, distance bounds exclude a planting refutation throughout (4/3,2], and an all-algorithms lower bound is beyond current techniques. Literature search was used only to locate the blocking thresholds, capped at two calls, and all threshold computations were reproduced locally.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
