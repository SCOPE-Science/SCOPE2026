# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Toroidal ATSP Held-Karp gap at most 12
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1453
- **Disposition:** NO_RESULT
- **Domain:** ATSP Held-Karp integrality gap
- **Method:** torus separator recursion rounding

## Problem

Fix the family of asymmetric TSP instances on n-vertex strongly connected digraphs whose Held-Karp subtour-LP support (underlying undirected graph) embeds on the torus (orientable genus 1) with nonnegative costs satisfying the triangle inequality (shortest-path metric), for all n >= 3. Let LP(I) be the subtour-elimination (Held-Karp) LP optimum and OPT(I) the minimum closed tour visiting every vertex. Is OPT(I)/LP(I) <= 12 for every such instance I, provable by a genus-adapted torus balanced-separator recursion that rounds any Held-Karp solution to a tour of cost at most 12*LP(I)? A complete answer is either such a proof for all n and all toroidal instances, or a rigorous counterexample toroidal instance with certified LP optimum value and certified tour lower bound violating the factor 12.

## Attempted claim

Fix the family of asymmetric TSP instances on n-vertex strongly connected digraphs whose Held-Karp subtour-LP support (underlying undirected graph) embeds on the torus (orientable genus 1) with nonnegative costs satisfying the triangle inequality (shortest-path metric), for all n >= 3. Let LP(I) be the subtour-elimination (Held-Karp) LP optimum and OPT(I) the minimum closed tour visiting every vertex. Is OPT(I)/LP(I) <= 12 for every such instance I, provable by a genus-adapted torus balanced-separator recursion that rounds any Held-Karp solution to a tour of cost at most 12*LP(I)? A complete answer is either such a proof for all n and all toroidal instances, or a rigorous counterexample toroidal instance with certified LP optimum value and certified tour lower bound violating the factor 12.

## Research outcome

Target blocked on all three concrete routes (thin-tree constant, circular separator charging, negative small-instance counterexample search); clean exit with no claim and no valuable increment.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete proof or counterexample for the factor-12 toroidal Held-Karp gap was established. Evidence is limited to two small exact torus-grid instances (n=9 and n=12, both gap 1.0) plus constant audits against the thin-tree budget and separator recurrence; larger or asymmetric families were not computationally reachable, and no novel lemma or construction was produced.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete proof or counterexample for the factor-12 toroidal Held-Karp gap was established. Evidence is limited to two small exact torus-grid instances (n=9 and n=12, both gap 1.0) plus constant audits against the thin-tree budget and separator recurrence; larger or asymmetric families were not computationally reachable, and no novel lemma or construction was produced.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
