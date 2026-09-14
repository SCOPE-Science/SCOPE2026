# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Small 5-chromatic plane unit-distance graph under 400 vertices
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1808
- **Disposition:** NO_RESULT
- **Domain:** Hadwiger-Nelson plane chromatic number
- **Method:** SAT minimization and 4-colorability certification

## Problem

Does there exist a finite unit-distance graph in the Euclidean plane with at most 400 vertices whose chromatic number is at least 5? Objects: finite point sets P in R^2 with edges joining pairs at Euclidean distance exactly 1. Scope: all such graphs with |P|<=400. Requested conclusion: decide existence of a 5-chromatic example versus provable non-existence over the whole range. A complete answer is either (A) explicit coordinates for P plus a machine-checkable certificate that no proper 4-coloring exists, or (B) a rigorous proof that every unit-distance graph on <=400 vertices in the plane is 4-colorable.

## Attempted claim

Does there exist a finite unit-distance graph in the Euclidean plane with at most 400 vertices whose chromatic number is at least 5? Objects: finite point sets P in R^2 with edges joining pairs at Euclidean distance exactly 1. Scope: all such graphs with |P|<=400. Requested conclusion: decide existence of a 5-chromatic example versus provable non-existence over the whole range. A complete answer is either (A) explicit coordinates for P plus a machine-checkable certificate that no proper 4-coloring exists, or (B) a rigorous proof that every unit-distance graph on <=400 vertices in the plane is 4-colorable.

## Research outcome

Target blocked: no unit-distance graph on at most 400 vertices with chromatic number >=5 was found; all small candidates tested 4-colorable, the only reproduced 5-chromatic-style graph (de Grey G, 1581 vertices) exceeds the bound, and universal 4-colorability is not finitely provable, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Finite computation cannot prove branch (B), universal 4-colorability over infinitely many non-isomorphic graphs up to 400 vertices; the SAT search covered rotated-lattice unions, spindle-core grids, Minkowski sums, and W/MM reconstructions but not the full configuration space; the reproduced 1581-vertex de Grey graph was not certified 4-UNSAT within the session SAT budget, so no minimization to 400 vertices was possible.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Finite computation cannot prove branch (B), universal 4-colorability over infinitely many non-isomorphic graphs up to 400 vertices; the SAT search covered rotated-lattice unions, spindle-core grids, Minkowski sums, and W/MM reconstructions but not the full configuration space; the reproduced 1581-vertex de Grey graph was not certified 4-UNSAT within the session SAT budget, so no minimization to 400 vertices was possible.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
