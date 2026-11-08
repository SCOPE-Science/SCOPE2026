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

# Reproduction

Run `python3 verify.py` in the directory containing the seven public files. It executes exact-rational enumeration of independent random masks and Rademacher probes, independent computation of three masked matrix-vector products, and deterministic optimization and asymptotic tests. The numerical optimizer relies on a bisection of the analytically proved strictly monotone KKT equation. The printed count is the number of completed assertions; neither enumeration nor floating-point tests establish the universal theorem, which is proved in RESULT.md. This is not independent validation.
