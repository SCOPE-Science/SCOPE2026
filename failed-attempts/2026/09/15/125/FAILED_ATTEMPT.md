# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Mutation-graph rigidity for monotone tori in the cubic del Pezzo
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20364
- **Disposition:** NO_RESULT
- **Domain:** Symplectic Geometry
- **Method:** Floer-theoretic superpotential and wall-crossing analysis

## Problem

Let X=Bl_6 CP^2 with monotone symplectic form and let (L,{D_i}) be the Lagrangian seed realizing the cubic-surface LG seed of Pascaleff-Tonkonog Table 1. Let G be its infinite iterated Lagrangian-mutation graph and L_v the monotone torus at vertex v with disk potential W_v computed by the wall-crossing formula. If v,w lie in distinct orbits of the finite automorphism group of the initial seed, are L_v and L_w pairwise non-Hamiltonian-isotopic in X, as detected by GL(2,Z)-inequivalence of W_v,W_w? Decide.

## Attempted claim

Let X=Bl_6 CP^2 with monotone symplectic form and let (L,{D_i}) be the Lagrangian seed realizing the cubic-surface LG seed of Pascaleff-Tonkonog Table 1. Let G be its infinite iterated Lagrangian-mutation graph and L_v the monotone torus at vertex v with disk potential W_v computed by the wall-crossing formula. If v,w lie in distinct orbits of the finite automorphism group of the initial seed, are L_v and L_w pairwise non-Hamiltonian-isotopic in X, as detected by GL(2,Z)-inequivalence of W_v,W_w? Decide.

## Research outcome

Target BLOCKED: infinite mutation-graph orbit-injectivity for cubic-del-Pezzo tori is explicitly open in the admitted source (Remark 4.17); routes R1 (seed reconstruction plus exact mutation engine), R2 (exact depth<=2 collision census, no collision found), and R3 (literature status check) match output/target_exit.json; deeper search blows up. CLEAN_EXIT with no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Finite exact computation to mutation depth 2 cannot decide an infinite-graph injectivity claim; coarse Newton-polytope fingerprints (term count, area, Pick data, edge lengths) do not decide GL(2,Z)-equivalence of potentials; the Hamiltonian-vs-GL detection step and the full wall-crossing identification are taken from the cited literature rather than re-proved; deeper enumeration was computationally infeasible in this pass (depth-5 probe timed out).

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Finite exact computation to mutation depth 2 cannot decide an infinite-graph injectivity claim; coarse Newton-polytope fingerprints (term count, area, Pick data, edge lengths) do not decide GL(2,Z)-equivalence of potentials; the Hamiltonian-vs-GL detection step and the full wall-crossing identification are taken from the cited literature rather than re-proved; deeper enumeration was computationally infeasible in this pass (depth-5 probe timed out).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
