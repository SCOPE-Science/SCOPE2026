---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The sector proof gives the analytic result. For a bounded numerical comparison run `python3 verify_polar_defect.py` from this directory, using only the Python 3 standard library. The script evaluates shadow lengths and polar vertex extrema on an angular grid for \(N=4,6,8,10,12,16,20,32\). It compares the discrete squared fits to the exact formulas and tests the uniform error at selected scales including the analytic optimum. The grid tests are not exhaustive in either the scale or direction and do not certify the infinite-family calculation or any statement of historical priority.
