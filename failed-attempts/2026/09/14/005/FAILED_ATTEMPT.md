# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Triangle-free 5-chromatic plane unit-distance graph under 800 vertices
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1816
- **Disposition:** NO_RESULT
- **Domain:** Hadwiger-Nelson triangle-free plane graphs
- **Method:** triangle-free rhombus assembly and 4-color SAT certification

## Problem

Does there exist a triangle-free finite unit-distance graph in the Euclidean plane with at most 800 vertices whose chromatic number is at least 5? Objects: finite point sets P in R^2 with unit-distance edges and with no three vertices pairwise at distance 1 (graph girth at least 4). Scope: all triangle-free cases with |P|<=800. Requested conclusion: decide existence of a triangle-free 5-chromatic example versus provable non-existence over the whole range. A complete answer is either (A) explicit coordinates for such a triangle-free P plus a machine-checkable certificate of non-4-colorability and triangle-freeness, or (B) a rigorous proof that every triangle-free unit-distance graph on <=800 vertices in the plane is 4-colorable.

## Attempted claim

Does there exist a triangle-free finite unit-distance graph in the Euclidean plane with at most 800 vertices whose chromatic number is at least 5? Objects: finite point sets P in R^2 with unit-distance edges and with no three vertices pairwise at distance 1 (graph girth at least 4). Scope: all triangle-free cases with |P|<=800. Requested conclusion: decide existence of a triangle-free 5-chromatic example versus provable non-existence over the whole range. A complete answer is either (A) explicit coordinates for such a triangle-free P plus a machine-checkable certificate of non-4-colorability and triangle-freeness, or (B) a rigorous proof that every triangle-free unit-distance graph on <=800 vertices in the plane is 4-colorable.

## Research outcome

Target blocked on both resolutions and the bounded adjacent alternative failed: nine triangle-free assemblies through 800 vertices all 4-colorable, SA embeddings of Mycielski M4/M5 failed, seven candidates all 3-colorable; no auditable result, exiting clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exact UNSAT certification at 800-vertex scale is infeasible with stdlib-only tooling; the search explored bounded random rhombus assemblies and simulated-annealing embeddings rather than the full continuum of plane point sets, so these negative results do not prove target non-existence. All DSATUR UNSAT claims are limited to small controls (Moser k=3, M4 k=3, M5 k=4); no large-graph non-colorability is claimed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exact UNSAT certification at 800-vertex scale is infeasible with stdlib-only tooling; the search explored bounded random rhombus assemblies and simulated-annealing embeddings rather than the full continuum of plane point sets, so these negative results do not prove target non-existence. All DSATUR UNSAT claims are limited to small controls (Moser k=3, M4 k=3, M5 k=4); no large-graph non-colorability is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
