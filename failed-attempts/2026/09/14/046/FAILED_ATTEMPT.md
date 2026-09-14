# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Global triangle-free Ramsey–Turán density between one-third and one-half
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20002
- **Disposition:** NO_RESULT
- **Domain:** Extremal Combinatorics
- **Method:** flag-algebra stability analysis

## Problem

Let ex_3(n,s) be the maximum number of edges in an n-vertex triangle-free graph with independence number at most s, and for each integer j≥1 let g_j(n,s)=j(j−1)n²/2−j(3j−4)ns+(3j−4)(3j−1)s²/2. Is ex_3(n,s)=min_{j≥1} g_j(n,s) for every pair of integers n/3<s≤n/2 (equivalently, is the triangle Ramsey–Turán density f_3(α) equal to the associated piecewise-quadratic function for every α∈(1/3,1/2])?

## Attempted claim

Let ex_3(n,s) be the maximum number of edges in an n-vertex triangle-free graph with independence number at most s, and for each integer j≥1 let g_j(n,s)=j(j−1)n²/2−j(3j−4)ns+(3j−4)(3j−1)s²/2. Is ex_3(n,s)=min_{j≥1} g_j(n,s) for every pair of integers n/3<s≤n/2 (equivalently, is the triangle Ramsey–Turán density f_3(α) equal to the associated piecewise-quadratic function for every α∈(1/3,1/2])?

## Research outcome

Target (global Andrasfai formula for triangle Ramsey-Turan numbers on n/3<s<=n/2) is BLOCKED: it is a genuine open conjecture needing infinite-family methods, and four concrete bounded routes found confirmation at small orders but no proof and no counterexample, so a CLEAN_EXIT with NO_RESULT is returned.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Small-order ILP verification covered only n<=8 to optimality; exhaustive circulant scan to n=35 covers only vertex-transitive examples; heuristic searches (annealing, blow-up hill-climbing) are incomplete by design; literature status rests on one fetched paper version. None of these limitations affect the NO_RESULT verdict, since no claim is made.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Small-order ILP verification covered only n<=8 to optimality; exhaustive circulant scan to n=35 covers only vertex-transitive examples; heuristic searches (annealing, blow-up hill-climbing) are incomplete by design; literature status rests on one fetched paper version. None of these limitations affect the NO_RESULT verdict, since no claim is made.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
