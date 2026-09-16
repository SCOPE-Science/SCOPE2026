# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact regularity and Rees-Sagbi presentation for cover ideals of nonbipartite unicyclic graphs
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20503
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** Grobner degeneration and Sagbi-basis analysis

## Problem

Let G be a connected nonbipartite unicyclic graph with unique odd cycle C_{2k+1} (k>=1) and arbitrary rooted trees attached at its vertices, over a field K, and let J(G) be its vertex cover ideal. Determine for every integer s>=1 the finite exact values reg(J(G)^{(s)}) and reg(J(G)^s), and decide whether reg(J(G)^{(s)})=reg(J(G)^s) holds for all s>=1, via an explicit finite Sagbi/Grobner presentation of the ordinary Rees algebra R(J(G)) and the symbolic Rees algebra R_s(J(G))=directsum_{s>=0} J(G)^{(s)}t^s and its (1,0)-regularity.

## Attempted claim

Let G be a connected nonbipartite unicyclic graph with unique odd cycle C_{2k+1} (k>=1) and arbitrary rooted trees attached at its vertices, over a field K, and let J(G) be its vertex cover ideal. Determine for every integer s>=1 the finite exact values reg(J(G)^{(s)}) and reg(J(G)^s), and decide whether reg(J(G)^{(s)})=reg(J(G)^s) holds for all s>=1, via an explicit finite Sagbi/Grobner presentation of the ordinary Rees algebra R(J(G)) and the symbolic Rees algebra R_s(J(G))=directsum_{s>=0} J(G)^{(s)}t^s and its (1,0)-regularity.

## Research outcome

Uniform exact-regularity plus finite Rees-Sagbi presentation target for cover ideals of all nonbipartite unicyclic graphs is blocked by unbounded tree-parameter dependence; salvageable fragments are classical prior art, so the lane exits clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exhaustive verification was limited to small graphs (n<=8, s<=5) by the exponential s-cover search space; homology computations used pure-Python rational arithmetic on small complexes; no per-tree-shape resolution computations for large attachments were attempted after the uniformity obstruction and literature barrier were established.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exhaustive verification was limited to small graphs (n<=8, s<=5) by the exponential s-cover search space; homology computations used pure-Python rational arithmetic on small complexes; no per-tree-shape resolution computations for large attachments were attempted after the uniformity obstruction and literature barrier were established.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
