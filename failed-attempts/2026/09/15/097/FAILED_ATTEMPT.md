# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Infinite non-bipartite 7-regular Ramanujan families
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20324
- **Disposition:** NO_RESULT
- **Domain:** Graph Theory
- **Method:** spectral graph theory and interlacing polynomials

## Problem

Does there exist an infinite sequence of connected non-bipartite 7-regular graphs G_n with |V(G_n)| -> infinity such that every nontrivial adjacency eigenvalue satisfies |lambda| <= 2*sqrt(6) (i.e. max{lambda_2(G_n), |lambda_n(G_n)|} <= 2*sqrt(6))?

## Attempted claim

Does there exist an infinite sequence of connected non-bipartite 7-regular graphs G_n with |V(G_n)| -> infinity such that every nontrivial adjacency eigenvalue satisfies |lambda| <= 2*sqrt(6) (i.e. max{lambda_2(G_n), |lambda_n(G_n)|} <= 2*sqrt(6))?

## Research outcome

Target blocked on all four routes (arithmetic excluded since 6 is not a prime power; 2-lift tower needs the open Bilu-Linial two-sided iteration; prism surgery fails exactly at eigenvalue 5; random graphs give only eps-slack). Decision phase found no auditable emergent alternative, so the lane exits clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No infinite family was constructed or disproved: the investigation establishes a proof-theoretic block (missing two-sided signing iteration theorem) rather than a mathematical verdict on the target's truth. Finite computations (small-order census, signing search, greedy tower through 512 vertices, random-graph frequencies) support feasibility but prove nothing about infinitude. Literature conclusions rest on extracted text of Hall-Puder-Sawin (DOI 10.1016/j.aim.2017.10.042) plus standard facts about LPS/Morgenstern/Pizer degree sets and Friedman's theorem, without re-proving those results in-lane.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No infinite family was constructed or disproved: the investigation establishes a proof-theoretic block (missing two-sided signing iteration theorem) rather than a mathematical verdict on the target's truth. Finite computations (small-order census, signing search, greedy tower through 512 vertices, random-graph frequencies) support feasibility but prove nothing about infinitude. Literature conclusions rest on extracted text of Hall-Puder-Sawin (DOI 10.1016/j.aim.2017.10.042) plus standard facts…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
