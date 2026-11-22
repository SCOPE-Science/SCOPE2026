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

# Reproduction and scope

Run `python checker.py` using Python 3.10+. It uses only the standard library and contains the exact parameter fractions, risk comparisons, finite Taylor bounds and high-/low-noise limit identities. The exact rational derivation and the intermediate value theorem, not a numerical grid, establish the claimed existence of at least two crossings.

The program separately evaluates several floating-point values as a check of sign conventions, but these finite samples are not an exhaustive zero count. This statement does not certify global dynamics, empirical risk response or historical priority.
