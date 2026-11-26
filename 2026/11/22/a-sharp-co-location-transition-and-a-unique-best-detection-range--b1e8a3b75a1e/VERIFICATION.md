---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification scope

An independent mathematical review reconstructed the exact logarithmic derivative and its single sign change above the fixed-width cut-off, verified both endpoint limits and the rare-detection scaling, and independently checked the numerical example by bisection. The analytic argument, not a grid search, proves the result for every admissible parameter. The fixed-width optimizer is credited as known.

The original `verify.py` and `verification_certificate.json` are unchanged supplementary evidence. In a directory with that script, `python3 verify.py` prints finite diagnostics to standard output; no inputs or additional packages are needed. The archived certificate reports 11,156 assertions including nine quadratures. The script and certificate were inspected but not rerun in the independent review. No formal verification, expert attestation, empirical validation, or priority certification is asserted.
