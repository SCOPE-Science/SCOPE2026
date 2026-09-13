# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Restricted assignment configuration-LP gap at most 7/4
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1630
- **Disposition:** NO_RESULT
- **Domain:** scheduling approximation
- **Method:** configuration LP local search rounding

## Problem

For restricted assignment makespan minimization (m unrelated machines; each job j has a single size p_j and a nonempty eligible machine set E_j, so processing times are p_{ij} in {p_j, infinity}; guess T normalized to T=1; the configuration LP has variables over machine configurations, i.e. subsets of jobs simultaneously schedulable on one machine with total size at most 1, requiring each job to be covered and each machine to use a convex combination of its configurations): is the worst-case ratio OPT/T over all instances with feasible configuration LP at T=1, ranging over all finite m, all job counts, all sizes p_j > 0 and all eligible sets, at most 7/4? A complete answer either proves that every such instance admits an integral schedule of makespan at most 7/4, or exhibits one explicit instance with a rigorously verified feasible configuration-LP solution at T=1 and a proof that every integral assignment has makespan strictly greater than 7/4.

## Attempted claim

For restricted assignment makespan minimization (m unrelated machines; each job j has a single size p_j and a nonempty eligible machine set E_j, so processing times are p_{ij} in {p_j, infinity}; guess T normalized to T=1; the configuration LP has variables over machine configurations, i.e. subsets of jobs simultaneously schedulable on one machine with total size at most 1, requiring each job to be covered and each machine to use a convex combination of its configurations): is the worst-case ratio OPT/T over all instances with feasible configuration LP at T=1, ranging over all finite m, all job counts, all sizes p_j > 0 and all eligible sets, at most 7/4? A complete answer either proves that every such instance admits an integral schedule of makespan at most 7/4, or exhibits one explicit instance with a rigorously verified feasible configuration-LP solution at T=1 and a proof that every integral assignment has makespan strictly greater than 7/4.

## Research outcome

Target blocked: resolving whether the restricted-assignment configuration-LP gap is at most 7/4 proved infeasible in-session. Exact per-pattern maximization capped small shapes at gap 1.5, broad stochastic search over thousands of instances stalled at OPT ~1.32, local climbs froze at the classical 1.5 seed, and the positive proof needs heavy machinery beyond a from-scratch session. Clean exit with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete resolution was established: neither a proof that all configuration-LP-feasible instances schedule within 7/4 nor a verified witness instance with integer optimum above 7/4 was found. Computational search covered small eligibility patterns exactly and thousands of larger instances stochastically, but the space of large instances is unbounded and was only sampled, so these negative results do not bound the true gap. All scripts and logs are retained in the workspace for reproducibility.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete resolution was established: neither a proof that all configuration-LP-feasible instances schedule within 7/4 nor a verified witness instance with integer optimum above 7/4 was found. Computational search covered small eligibility patterns exactly and thousands of larger instances stochastically, but the space of large instances is unbounded and was only sampled, so these negative results do not bound the true gap. All scripts and logs are retained in the workspace for reproducibilit…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
