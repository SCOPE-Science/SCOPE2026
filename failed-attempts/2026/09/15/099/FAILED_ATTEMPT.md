# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Trilinear bi-orthogonality-free l^2-decoupling for the hyperbolic paraboloid in R^5 from trilinear restriction
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20326
- **Disposition:** NO_RESULT
- **Domain:** Harmonic Analysis
- **Method:** polynomial partitioning and decoupling analysis

## Problem

Let n=5, d=3, H={(xi,Q(xi)):xi in [-1,1]^4} in R^5 with Q(xi)=xi1^2+xi2^2-xi3^2-xi4^2, N_{1/R}(H) its 1/R-neighbourhood, and p_c=3. Formulate a quantitative transversality condition for triples tau_1,tau_2,tau_3 in [-1,1]^4 generalizing Demeter-Wu transversality (no ruling line of H meets two distinct H_{tau_j}) and let C(R) be the smallest constant in the trilinear analogue of Demeter-Wu (1.3) at p_c for all transverse triples and all f_j Fourier-supported in N_{1/R}(H_{tau_j}). Prove, using only the known trilinear restriction theorem in R^3 (Bennett-Carbery-Tao) via a bi-orthogonality-free induction/broad-narrow scheme extending Demeter-Wu Propositions 2.2-2.3 including the analogue of their inequality (2.5), that for every epsilon>0, C(R) <<_epsilon R^epsilon for all R>=1. The bound is asymptotic with R^epsilon-loss (not endpoint C(R)<<1) and unconditional (must not assume the full Restriction Conjecture).

## Attempted claim

Let n=5, d=3, H={(xi,Q(xi)):xi in [-1,1]^4} in R^5 with Q(xi)=xi1^2+xi2^2-xi3^2-xi4^2, N_{1/R}(H) its 1/R-neighbourhood, and p_c=3. Formulate a quantitative transversality condition for triples tau_1,tau_2,tau_3 in [-1,1]^4 generalizing Demeter-Wu transversality (no ruling line of H meets two distinct H_{tau_j}) and let C(R) be the smallest constant in the trilinear analogue of Demeter-Wu (1.3) at p_c for all transverse triples and all f_j Fourier-supported in N_{1/R}(H_{tau_j}). Prove, using only the known trilinear restriction theorem in R^3 (Bennett-Carbery-Tao) via a bi-orthogonality-free induction/broad-narrow scheme extending Demeter-Wu Propositions 2.2-2.3 including the analogue of their inequality (2.5), that for every epsilon>0, C(R) <<_epsilon R^epsilon for all R>=1. The bound is asymptotic with R^epsilon-loss (not endpoint C(R)<<1) and unconditional (must not assume the full Restriction Conjecture).

## Research outcome

Target blocked on routes A (transversality), B (slice-freeze to BCT R^3), and C ((2.5)-analogue induction): the 5D phase coupling and ruling-plane narrow term cannot be handled with only R^3 BCT bi-orthogonality-free. CLEAN_EXIT filed in output/target_exit.json; no fallback exists and no emergent finding met Audit.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Target-only topic with no fallback. Three concrete routes were attempted and each failed at an explicit structural step confirmed by a reproducible script (output/artifacts/slice_coupling_check.py): (A) pairwise-|Q| transversality cannot control narrow clusters near 2D ruling planes; (B) slice-freeze reduction leaves an x5-chirp varying by ~2R radians with ~2R-slab triangle loss far above R^epsilon; (C) Fubini-Minkowski broad-narrow induction needs forbidden bi-orthogonality or unfunded ruling-plane input. No local theorem or lower bound was proved, so no EMERGENT_FINDING met the independent-value bar.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Target-only topic with no fallback. Three concrete routes were attempted and each failed at an explicit structural step confirmed by a reproducible script (output/artifacts/slice_coupling_check.py): (A) pairwise-|Q| transversality cannot control narrow clusters near 2D ruling planes; (B) slice-freeze reduction leaves an x5-chirp varying by ~2R radians with ~2R-slab triangle loss far above R^epsilon; (C) Fubini-Minkowski broad-narrow induction needs forbidden bi-orthogonality or unfunded ruling-…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
