# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-sided Ramanujan 2-lift stability of arithmetic Ramanujan base graphs
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20449
- **Disposition:** NO_RESULT
- **Domain:** Graph Theory
- **Method:** spectral trace-method and interlacing-polynomial analysis

## Problem

Let d=q+1 with q a prime power (e.g. d=6) and let G be a non-bipartite d-regular Ramanujan graph from the Lubotzky-Phillips-Sarnak / Morgenstern arithmetic family. Does G admit an edge-signing sigma:E(G)->{+-1} whose signed adjacency matrix A_sigma satisfies rho(A_sigma) <= 2*sqrt(d-1), equivalently a 2-lift H all of whose new eigenvalues lie in [-2*sqrt(d-1), 2*sqrt(d-1)] so that H is itself d-regular Ramanujan?

## Attempted claim

Let d=q+1 with q a prime power (e.g. d=6) and let G be a non-bipartite d-regular Ramanujan graph from the Lubotzky-Phillips-Sarnak / Morgenstern arithmetic family. Does G admit an edge-signing sigma:E(G)->{+-1} whose signed adjacency matrix A_sigma satisfies rho(A_sigma) <= 2*sqrt(d-1), equivalently a 2-lift H all of whose new eigenvalues lie in [-2*sqrt(d-1), 2*sqrt(d-1)] so that H is itself d-regular Ramanujan?

## Research outcome

Target blocked: two-sided Ramanujan signing for non-bipartite LPS graphs needs simultaneous max/min control beyond the one-sided MSS guarantee; canonical cover violates the strict interval; LPS-scale certification is exponentially infeasible. No independently valuable emergent finding; clean exit.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exhaustive signing search was verified only on small cubic Ramanujan graphs (n<=10) and heuristic search on random 6-regular Ramanujan proxies at n=20/30; no explicit LPS/Morgenstern graph at genuine scale (n>=60, m>=180) was constructed or certified, and no literature retrieval was consumed. The blocking diagnosis rests on the one-sided versus two-sided interlacing gap plus exponential scaling, not on a discovered counterexample.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exhaustive signing search was verified only on small cubic Ramanujan graphs (n<=10) and heuristic search on random 6-regular Ramanujan proxies at n=20/30; no explicit LPS/Morgenstern graph at genuine scale (n>=60, m>=180) was constructed or certified, and no literature retrieval was consumed. The blocking diagnosis rests on the one-sided versus two-sided interlacing gap plus exponential scaling, not on a discovered counterexample.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
