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

# Verification and reproducibility

The theorem uses exactly four graph edges and centered graph balls of radii zero, one and two. The six branch identities and both positive-cone matrix certificates are printed in RESULT.md. The independent Python 3 standard-library script `checker.py` recomputes the six symmetric rational branch matrices, checks the algebraic eigenvalue relation, determinant signs, and equality extremizer, and performs 5,000 deterministic direct input tests. Execute `python3 checker.py` in a directory containing this file; its output starts with `PASS`.

Only the explicit mathematical inequalities in RESULT.md prove the global real and complex statement. The sample tests are not exhaustive over the continuum. Review is same-model only; independent audit is unperformed.
