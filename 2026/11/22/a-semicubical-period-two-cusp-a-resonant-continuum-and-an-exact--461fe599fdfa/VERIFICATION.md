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

# Verification record

The proof in RESULT.md establishes the infinite-domain assertions algebraically. A standalone Python 3/SymPy checker `verify.py` repeats the exact factorization of the two-cycle equations, symmetric trace and determinant calculations, resonant interchange and monodromy, and rational checks of the explicit sink slice. It prints `AFFINE_CUBIC_PERIOD_TWO_VERIFY_OK` on success.

The exact existence equivalence includes all real \(b,m\) and all \(c\ne0\); direct substitution verifies that the degenerate parameter locus contains the full family and no extra primitive-two orbit. Finite sample trajectories in the script are only diagnostics. Strict Schur inequalities and elementary quadratic sign arguments, not sampling, supply the stability classification.

The check does not address independent priority, global attracting basins, high-period orbits, or nonlinear dynamics at neutral multipliers. Independent audit has not been performed.
