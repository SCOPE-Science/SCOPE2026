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

# Reproducibility and boundaries

Run `python verify.py` from the same extracted directory with `numpy` and `sympy` installed. The file contains an exact rational two-agent certificate, then deterministic seeded floating-point tests for 168 symmetric positive-definite consensus matrices of sizes two through eight with positive heterogeneous curvatures. The checks compare the computed smallest generalized eigenvalue against the nonpermanent eigenvalue modulus below, at, and above the threshold.

The verifier is a supplementary calculation, not a machine proof of the theorem for arbitrary dimensions and parameters. The analytic argument in RESULT.md addresses infinite families. In particular, the theoretical exclusion of nonreal unit-circle crossings and the accessibility of unstable eigenmodes are proved algebraically, not inferred from finite enumeration. Matrix conditioning and floating-point eigensolver error are not evaluated as a numerical robustness guarantee.
