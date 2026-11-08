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

# Reproduction and limits

From the directory containing this file, execute `python3 check.py` (Python 3 standard library only). It constructs the complete sixteen-state dynamic recurrence from the explicit binomial rule, checks the length-sixteen table and the exact length-nineteen score-and-count shift, compares every five-to-twelve-bit input against direct enumeration of all distinct permuted outputs and two independent counting formulas, and verifies the initial maximizing table. The recurrence with the fully checked identity proves the formulas for unbounded lengths; brute-force output enumeration only provides finite independent corroboration.

The expected final marker is `ALL_CERTIFICATES_OK`. This is an integer-arithmetic correctness check for the stated scope, not independent review and not an exhaustive historical-priority search. Publication priority and larger channel parameters are not established.
