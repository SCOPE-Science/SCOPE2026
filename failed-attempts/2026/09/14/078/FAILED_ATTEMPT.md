# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Deterministic logarithmic-girth near-Ramanujan graphs in every degree
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20063
- **Disposition:** NO_RESULT
- **Domain:** Spectral Graph Theory
- **Method:** interlacing polynomial and 2-lift covering techniques

## Problem

For every fixed integer d >= 3 and every fixed epsilon > 0, does there exist a deterministic algorithm running in time poly(n) which, for all sufficiently large admissible input sizes n, outputs a connected simple d-regular graph G_n on N = n(1+o(1)) vertices such that, for some constant c_d > 0, girth(G_n) >= c_d log_{d-1}(N) and max{|lambda| : lambda is a nontrivial adjacency eigenvalue of G_n} <= 2 sqrt(d-1) + epsilon, where nontrivial excludes d and, when G_n is bipartite, -d, and dN is even?

## Attempted claim

For every fixed integer d >= 3 and every fixed epsilon > 0, does there exist a deterministic algorithm running in time poly(n) which, for all sufficiently large admissible input sizes n, outputs a connected simple d-regular graph G_n on N = n(1+o(1)) vertices such that, for some constant c_d > 0, girth(G_n) >= c_d log_{d-1}(N) and max{|lambda| : lambda is a nontrivial adjacency eigenvalue of G_n} <= 2 sqrt(d-1) + epsilon, where nontrivial excludes d and, when G_n is bipartite, -d, and dN is even?

## Research outcome

Target blocked on all three concrete routes (R1 LPS degree reduction, R2 iterated 2-lifts, R3 random-regular derandomization) per quantitative recovery test; no credible target route and no independently valuable emergent finding remain, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No deterministic joint construction was produced and no impossibility proof was established. The blockage evidence is quantitative and local: LPS gap arithmetic, lift girth stagnation, and short-cycle first moments rule out the three concrete derandomizable routes, but do not resolve whether the target claim itself is true or false.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No deterministic joint construction was produced and no impossibility proof was established. The blockage evidence is quantitative and local: LPS gap arithmetic, lift girth stagnation, and short-cycle first moments rule out the three concrete derandomizable routes, but do not resolve whether the target claim itself is true or false.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
