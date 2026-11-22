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

# Verification
The complete arithmetic proof appears in `RESULT.md`. Run the standalone Python-standard-library checker with `python3 verify_delannoy7.py`; its observed output is `PASS: 17262 exact finite assertions` followed by a description of checks. The checker constructs every carry matrix from digit sums, tests signs against integer Delannoy coefficients, compares noncyclic finite-block correlations with exact transfer expressions, and exhaustively checks all shifts under \(7^5\) for the asserted extremizers. The norm and equality proof, not this finite search, covers all positive shifts and arbitrarily large blocks.

Limitations: no infinite computational enumeration is asserted, no externally checked proof is claimed, and no independent mathematical audit has been performed.
