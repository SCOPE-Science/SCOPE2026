# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Conway 99-graph existence
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1866
- **Disposition:** NO_RESULT
- **Domain:** algebraic graph theory
- **Method:** spectral feasibility and SAT search

## Problem

Does there exist a strongly regular graph with parameters (v,k,lambda,mu) = (99,14,1,2), i.e. a 14-regular graph on 99 vertices in which every pair of adjacent vertices has exactly one common neighbour and every pair of distinct non-adjacent vertices has exactly two common neighbours? A complete answer is either an explicit adjacency construction verified to satisfy all four parameters or a rigorous mathematical proof that no such graph exists.

## Attempted claim

Does there exist a strongly regular graph with parameters (v,k,lambda,mu) = (99,14,1,2), i.e. a 14-regular graph on 99 vertices in which every pair of adjacent vertices has exactly one common neighbour and every pair of distinct non-adjacent vertices has exactly two common neighbours? A complete answer is either an explicit adjacency construction verified to satisfy all four parameters or a rigorous mathematical proof that no such graph exists.

## Research outcome

SRG(99,14,1,2) (Conway 99-graph) could not be decided: all classical feasibility checks pass and global construction is infeasible in-session, so a CLEAN_EXIT with NO_RESULT is returned.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No construction or nonexistence proof was produced; spectral, Krein, and local-counting checks all passed without yielding an obstruction, and global search (~10^150 completions) was computationally out of reach without SAT infrastructure. All intermediate findings are classical facts, not original results.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No construction or nonexistence proof was produced; spectral, Krein, and local-counting checks all passed without yielding an obstruction, and global search (~10^150 completions) was computationally out of reach without SAT infrastructure. All intermediate findings are classical facts, not original results.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
