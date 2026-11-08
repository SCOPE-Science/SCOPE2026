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

`check.py` was run using Python, NumPy and SymPy. Observed output:

`VERIFY_OK symbolic_characteristic_polynomials=2 finite_differences=4 stable_period_two_orbits=2 sharp_boundary=2`

The program verifies both symbolic matrix characteristic polynomials; compares the exact linearized full map with centered finite differences in both tangent directions for two phase configurations; iterates nearby points around both cycles; and checks the sharp transition on both sides of the step threshold and the concentration threshold. These are genuine local reproducibility checks, not a replacement for the analytic quantifier-complete proof and not independent scientific validation.

The theorem does not require code to perform a global parameter enumeration. No external files, proprietary code, or third-party articles are required for the checker. The full-map denominator is checked to be nonzero at each specified cycle by the strict hypothesis.
