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

# Verification scope

The package provides two standalone Python 3 programs plus their actual text outputs. Run `python3 verify_bruteforce.py` and `python3 verify_borders.py` from the extracted package directory. Both programs construct or symbolically predict MCS endpoint sets without external dependencies. The first checks 97 direct word instances, the second checks 48 independent factor-index instances and 4,335 larger bridge/cut instances.

The finite calculations validate stated examples and detect errors in endpoint inclusions or boundary cases, but are not exhaustive over arbitrary positive input parameters. The infinite-family result uses the mixed-phase and unary-border arguments and the cut analysis in `RESULT.md`. See its prior-work discussion for the relation to the general run-length-encoded classification and general internal-cut bounds.

Self-review: passed. Independent audit: not yet performed.
