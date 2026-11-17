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

The all-size proof reduces primitive two-orbits to cut-degree chip intervals, builds an exact sixteen-state polynomial transfer, and calculates the six-state antisymmetric characteristic polynomial. No finite-length experiment is used to prove an infinite-length statement.

Run `python3 verify_symbolic.py` (requires SymPy) to regenerate the matrix and determinant and test the full mass-discrepancy trace identity at lengths 3 through 8. Run `python3 verify_direct.py` (Python standard library only) to enumerate all cuts and mass coefficients at lengths 3 through 7 and verify physical two-step chip-firing for every cut-compatible configuration at lengths 3 and 4. `symbolic_output.txt` and `direct_output.txt` contain observed outputs. Exact transfer arguments cover all integers \(n\ge3\); finite direct checks do not independently certify the all-size proof or historical originality.
