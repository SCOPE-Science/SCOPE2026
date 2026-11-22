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

# Verification

The full scientific claim is proved analytically in `RESULT.md`. For a standalone implementation check, execute `python check.py` with Python, NumPy and SciPy installed. The deterministic seeded replay's console values are reproduced in `check-output.json`.

Checks cover published biased within-group variance normalization, the exact scaled-Student tail at seven sample sizes, the closed-form two-degree tail, a finite-dimensional Gaussian linear-kernel control, Gaussian-kernel finite-dimensional Monte Carlo, and coupled RBF/linear comparison. Random simulation errors have no bearing on the infinite-dimensional proof. The proof's quantitative statement is convergence in distribution only, without a uniform-in-d error bound or claim of independence certification.
