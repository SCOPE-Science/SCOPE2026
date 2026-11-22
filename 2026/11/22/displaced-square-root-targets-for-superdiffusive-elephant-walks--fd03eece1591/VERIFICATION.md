---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytical proof in `RESULT.md` establishes the claim using the published superdiffusive lattice local limit theorem, a normalized future martingale functional central limit, a maximal martingale tail bound, and Brownian range geometry. The lower-order lattice rounding in the target position is allowed. It distinguishes the finite-horizon hitting limit from the infinite-horizon approximation and does not treat finite numerical evidence as a limit proof.

The standalone Python checker `verify.py` runs exact rational checks of the transition and martingale identities, compares singleton-hitting dynamic programming with direct tree enumeration in finite samples, checks elementary deterministic oscillation inequalities and reproduces seeded Brownian-grid diagnostics for the continuous range functional. Numerical diagnostics are finite-mesh checks only; they are not proofs of convergence, historical priority or independence.

The corresponding prior source is arXiv:2611.01279v1 (submitted 2026-10-31), with supporting local limit theorem arXiv:2609.14753v1 (submitted 2026-09-13). No external mathematical validation has been performed.
