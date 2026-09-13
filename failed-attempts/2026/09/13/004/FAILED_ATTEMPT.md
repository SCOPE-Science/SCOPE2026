# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Toroidal ATSP path gap at most 16
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1456
- **Disposition:** NO_RESULT
- **Domain:** ATSP path Held-Karp integrality gap
- **Method:** torus separator with narrow s-t cuts

## Problem

Fix the s-t path family (ATSPP) on n-vertex strongly connected digraphs whose underlying Held-Karp path-LP support embeds on the torus (orientable genus 1), with distinguished distinct endpoints s,t, nonnegative triangle-inequality costs, for all n >= 3 and all choices of s,t. Let LP_path(I,s,t) be the standard s-t path subtour-LP optimum (in-degree=out-degree=1 except s,t with degree imbalance, plus s-t cut constraints) and OPT_path(I,s,t) the minimum s-t Hamiltonian path cost. Is OPT_path(I,s,t)/LP_path(I,s,t) <= 16 for every such triple (I,s,t), provable by a torus separator recursion adapted to narrow s-t cuts that rounds any path-LP solution to an s-t path of cost at most 16*LP_path? A complete answer is either such a uniform proof for all n,s,t, or a rigorous toroidal (I,s,t) counterexample with certified path-LP optimum and certified s-t path lower bound violating 16.

## Attempted claim

Fix the s-t path family (ATSPP) on n-vertex strongly connected digraphs whose underlying Held-Karp path-LP support embeds on the torus (orientable genus 1), with distinguished distinct endpoints s,t, nonnegative triangle-inequality costs, for all n >= 3 and all choices of s,t. Let LP_path(I,s,t) be the standard s-t path subtour-LP optimum (in-degree=out-degree=1 except s,t with degree imbalance, plus s-t cut constraints) and OPT_path(I,s,t) the minimum s-t Hamiltonian path cost. Is OPT_path(I,s,t)/LP_path(I,s,t) <= 16 for every such triple (I,s,t), provable by a torus separator recursion adapted to narrow s-t cuts that rounds any path-LP solution to an s-t path of cost at most 16*LP_path? A complete answer is either such a uniform proof for all n,s,t, or a rigorous toroidal (I,s,t) counterexample with certified path-LP optimum and certified s-t path lower bound violating 16.

## Research outcome

Target blocked: naive tour reduction provably unbounded and no uniform separator-plus-narrow-cut proof closing at 16 found; bounded exact checks show no small-n refutation, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Naive tour-via-path reduction certified unbounded (D/LP=50); separator-plus-narrow-cut stitching has no closed uniform constant budget; small-n exact search (100 instances, max gap 1.0) cannot reach a gap above 16; known global lower bounds near 2 imply a counterexample needs a breakthrough family. No original increment survives Audit.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Naive tour-via-path reduction certified unbounded (D/LP=50); separator-plus-narrow-cut stitching has no closed uniform constant budget; small-n exact search (100 instances, max gap 1.0) cannot reach a gap above 16; known global lower bounds near 2 imply a counterexample needs a breakthrough family. No original increment survives Audit.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
