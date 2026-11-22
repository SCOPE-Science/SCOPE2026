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

# Reproducibility and limits

Run `python3 checker.py` from the package directory. It reports `MONOMIAL_LOG_EDGE_DIAGNOSTIC_OK 7818` and checks 7,818 finite assertions using the Python standard library. Independent arithmetic path enumeration and tridiagonal sine-vector checks support the displayed exact identities. The infinite spectral edge and fixed-rank limit follow from the analytic truncation and min-max proof in `RESULT.md`, not from finite tests. Independent mathematical audit has not been performed.
