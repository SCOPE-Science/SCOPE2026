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
# Reproducibility checks

Invoke `python verify.py`. The deterministic executable performs exact rational transition identities and floating-point root/inequality tests, then prints `VERIFY_OK 2441 checks`. Independent external validation is not reported or implied. The general statements rely on the full analytic proof in `RESULT.md`; these finite tests are diagnostic, not exhaustive.

No remote data, random input file or external solver service is required. Python 3.11+, SciPy and the Python standard library suffice. Check assumptions, limits, and the distinct performance definitions before reusing the statements.
