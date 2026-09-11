# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit 5-chromatic K6-minor-free graph needing seven lists
- **Round:** 2026-09-07-first-light-01
- **Lane:** 805
- **Disposition:** NO_RESULT
- **Domain:** Structural Graph Theory
- **Method:** explicit construction via apex extension of planar list-obstruction gadgets with logged case analysis

## Problem

Construct and certify an explicit finite simple graph G with no K6 minor such that G is 5-chromatic but not 6-choosable: provide the vertex and edge lists, a proper 5-coloring, a proof that no 4-coloring exists, an explicit 6-list assignment admitting no proper list-coloring with a complete obstruction log, and a certificate that G has no K6 minor.

## Attempted claim

There exists an explicit finite simple K6-minor-free graph G with chi(G)=5 that is not 6-choosable (hence chi_l(G)>=7); the graph, its 5-coloring, its 5-chromaticity proof, its obstructing 6-list assignment, and its K6-minor-freeness certificate are all logged.

## Research outcome

Target blocked: the admitted apex-planar route is mathematically void (list-join bound chi_l(H+a)<=chi_l(H)+1 plus Thomassen 5-choosability implies every apex-planar graph is 6-choosable), small orders and multi-apex joins are eliminated, and no bounded non-apex candidate exists. NOT_PRESET lane: no preset fallback exists so PRESET_FALLBACK is forbidden; the only target-work fragments (join bound, K5 check, greedy facts) are folklore/trivial and fail Audit, so no EMERGENT_FINDING. Clean exit.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No explicit K6-minor-free chi=5 non-6-choosable graph constructed; chi_l>=7 leg unachieved on every bounded candidate.', 'Non-apex route (large probabilistic-type constructions) not attempted: unbounded in-budget with exponential obstruction/minor logs and no concrete small candidate.', 'No emergent finding claimed: join-bound observation and K5 checks are folklore/trivial and would fail Audit originality/value.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No explicit K6-minor-free chi=5 non-6-choosable graph constructed; chi_l>=7 leg unachieved on every bounded candidate.', 'Non-apex route (large probabilistic-type constructions) not attempted: unbounded in-budget with exponential obstruction/minor logs and no concrete small candidate.', 'No emergent finding claimed: join-bound observation and K5 checks are folklore/trivial and would fail Audit originality/value.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
