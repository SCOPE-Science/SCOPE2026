# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit Dolgopyat UNI bound for named cat-map suspension flow
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1778
- **Disposition:** NO_RESULT
- **Domain:** hyperbolic dynamics
- **Method:** Dolgopyat temporal distance and roof non-cohomology

## Problem

Let B = [[2,1],[1,1]] be the cat automorphism of T^2 and r_star(x1,x2) = 1 + 0.04*sin(2*pi*x1) + 0.03*cos(2*pi*x2), with distinct periodic averages over two explicit B-orbits (e.g. the fixed point at 0 versus an explicit period-3 orbit) so r_star is not cohomologous to a constant. Let phi^t be the suspension Anosov flow over B with roof r_star on the compact 3-manifold mapping torus M_B, with temporal distance function Delta over local stable/unstable quadrilaterals. Prove or disprove that there exist explicit scales r0 = 0.05 and c0 = 0.001 such that for every z in M_B there are y^u in W^u_{r0}(z), y^s in W^s_{r0}(z) with normalized temporal oscillation |Delta(z; y^u, y^s)| >= c0*d(y^u,z)*d(y^s,z), i.e. an explicit Dolgopyat uniform non-integrability lower bound for this contact-type suspension. A complete answer proves the uniform oscillation bound by finite periodic-average plus interval holonomy data, or rigorously exhibits a sequence of quadrilaterals of size at most r0 with vanishing normalized oscillation despite the verified non-cohomology, i.e. a new cancellation mechanism.

## Attempted claim

Let B = [[2,1],[1,1]] be the cat automorphism of T^2 and r_star(x1,x2) = 1 + 0.04*sin(2*pi*x1) + 0.03*cos(2*pi*x2), with distinct periodic averages over two explicit B-orbits (e.g. the fixed point at 0 versus an explicit period-3 orbit) so r_star is not cohomologous to a constant. Let phi^t be the suspension Anosov flow over B with roof r_star on the compact 3-manifold mapping torus M_B, with temporal distance function Delta over local stable/unstable quadrilaterals. Prove or disprove that there exist explicit scales r0 = 0.05 and c0 = 0.001 such that for every z in M_B there are y^u in W^u_{r0}(z), y^s in W^s_{r0}(z) with normalized temporal oscillation |Delta(z; y^u, y^s)| >= c0*d(y^u,z)*d(y^s,z), i.e. an explicit Dolgopyat uniform non-integrability lower bound for this contact-type suspension. A complete answer proves the uniform oscillation bound by finite periodic-average plus interval holonomy data, or rigorously exhibits a sequence of quadrilaterals of size at most r0 with vanishing normalized oscillation despite the verified non-cohomology, i.e. a new cancellation mechanism.

## Research outcome

Target blocked: rigorous certification of the explicit Dolgopyat UNI bound proved structurally infeasible within the pass (validated grid-elimination pilot certified 0.0 with sharp Lipschitz bounds demanding ~1e9 boxes); non-rigorous evidence favors truth but is not a result, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Non-rigorous vectorized grid evidence (200x200 base grid, 144-pair menu, N=14/16) strongly suggests the claimed uniform bound holds with large margin, but grid sweeps are not proofs and truncation at N=12 produced false near-zeros; no rigorous certificate, disproof, or independently valuable proved increment was obtained, and Hölder-only regularity with lam*mu=1 per-level non-decay blocks the attempted validated-enclosure route.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Non-rigorous vectorized grid evidence (200x200 base grid, 144-pair menu, N=14/16) strongly suggests the claimed uniform bound holds with large margin, but grid sweeps are not proofs and truncation at N=12 produced false near-zeros; no rigorous certificate, disproof, or independently valuable proved increment was obtained, and Hölder-only regularity with lam*mu=1 per-level non-decay blocks the attempted validated-enclosure route.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
