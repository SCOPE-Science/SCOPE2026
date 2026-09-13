# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Scale-uniform explicit RSW lower bound for critical FK q=3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1775
- **Disposition:** NO_RESULT
- **Domain:** planar random-cluster / FK percolation
- **Method:** RSW gluing plus boundary-condition comparison and explicit constant tracking

## Problem

Prove or disprove the following scale-uniform explicit RSW lower bound for critical FK percolation with q=3: for each integer n>=8 let R_n=[0,2n]x[0,n] intersected with Z^2 with nearest-neighbour edges, and let Cross_n be the left-right open crossing event in R_n. At edge weight p_c(3)=sqrt(3)/(1+sqrt(3)) with q=3, consider all partition boundary conditions xi on the outer boundary of R_n with finite-volume measures P^xi_{R_n}. Then inf_{n>=8} inf_{xi} P^xi_{R_n}(Cross_n) >= 0.01. A complete answer is a rigorous proof verifying this explicit uniform constant across all scales n>=8 and all boundary conditions, or a rigorous disproof by exhibiting an explicit scale n>=8 and boundary condition xi with a proof that P^xi_{R_n}(Cross_n) < 0.01, establishing failure of scale-uniform RSW at the stated constant. Scope: q=3, aspect-ratio-2:1 rectangle family at all scales, all random-cluster boundary conditions. Any rigorous argument is allowed.

## Attempted claim

Prove or disprove the following scale-uniform explicit RSW lower bound for critical FK percolation with q=3: for each integer n>=8 let R_n=[0,2n]x[0,n] intersected with Z^2 with nearest-neighbour edges, and let Cross_n be the left-right open crossing event in R_n. At edge weight p_c(3)=sqrt(3)/(1+sqrt(3)) with q=3, consider all partition boundary conditions xi on the outer boundary of R_n with finite-volume measures P^xi_{R_n}. Then inf_{n>=8} inf_{xi} P^xi_{R_n}(Cross_n) >= 0.01. A complete answer is a rigorous proof verifying this explicit uniform constant across all scales n>=8 and all boundary conditions, or a rigorous disproof by exhibiting an explicit scale n>=8 and boundary condition xi with a proof that P^xi_{R_n}(Cross_n) < 0.01, establishing failure of scale-uniform RSW at the stated constant. Scope: q=3, aspect-ratio-2:1 rectangle family at all scales, all random-cluster boundary conditions. Any rigorous argument is allowed.

## Research outcome

Target blocked on the explicit-constant gap: reductions to a uniform free-boundary bound plus heuristic sampling supporting plausibility, but no rigorous proof or disproof of the 0.01 uniform bound; clean exit with no alternative worth pursuing.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation established only standard reductions (free-minimality, FKG gluing r_n>=s_n^3, wrong-side duality seed) plus heuristic Monte Carlo estimates. The explicit uniform constant 0.01 was not proved or disproved: a proof requires quantitative RSW with an explicit constant (a deep program beyond bounded work), and a disproof requires a certified sub-0.01 upper bound that must overcome the qualitative RSW floor with infeasible exact methods. No rigorous resolution of the target is claimed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation established only standard reductions (free-minimality, FKG gluing r_n>=s_n^3, wrong-side duality seed) plus heuristic Monte Carlo estimates. The explicit uniform constant 0.01 was not proved or disproved: a proof requires quantitative RSW with an explicit constant (a deep program beyond bounded work), and a disproof requires a certified sub-0.01 upper bound that must overcome the qualitative RSW floor with infeasible exact methods. No rigorous resolution of the target is claim…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
