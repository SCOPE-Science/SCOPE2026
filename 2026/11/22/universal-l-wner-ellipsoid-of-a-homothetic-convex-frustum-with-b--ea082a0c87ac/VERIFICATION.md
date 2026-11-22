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

# Reproducibility of the universal Löwner contact formulas

Run `python3 verify_frustum.py` in this directory using Python 3's standard library. The expected final line begins `VERIFY_OK`. The script validates exact rational endpoint contact gauges, lifted mean and covariance, positive contact weights, and containment of 11 intermediate cross-sectional disk points in each of 969 configurations (dimensions 2–20, 51 center parameters each). It separately tests cone/prism boundary identities in dimensions 2–29 and radical-equation identities at 54 floating-point parameter combinations.

The computation does not prove an infinite theorem or certify historical novelty. The proof uses the general Löwner–John contact characterization for an arbitrary convex base and verifies every contact identity analytically.
