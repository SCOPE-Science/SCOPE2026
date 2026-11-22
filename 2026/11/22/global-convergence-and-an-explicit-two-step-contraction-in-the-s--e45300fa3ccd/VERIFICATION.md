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

`CHECK.py` requires only Python's standard library. Invoke `python CHECK.py` from the directory containing that file. It compares the original max-map with its rational odds rewrite, verifies finite branch-entry and forward switching on 455 exact-rational cases, and tests the two-step logarithmic contraction against the explicit fixed point on 12,000 floating-point cases at six parameter values above the boundary. Results were checked after extracting the code from the packaged finding record.

The complete analytic proof of the infinite statement appears in `RESULT.md`. Exhaustive finite enumeration cannot certify a claim over all real parameters. No independent mathematical audit is represented by these checks. Full historical priority remains subject to further specialist inspection.
