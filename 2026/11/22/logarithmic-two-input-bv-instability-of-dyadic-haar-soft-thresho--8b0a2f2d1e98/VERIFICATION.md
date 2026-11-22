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

# Verification record

The self-contained Python 3 standard-library program `verify.py` enumerates the complete sharp finite cut/mask expression by integer arithmetic for depths one through eight. It checks the exact rational sequence \(1,3/2,2,21/8,3,117/32,4,597/128\), and tests the disjoint-support lower-bound construction at depths four, eight, twelve and sixteen with exact fractions. It separately checks 600 seeded two-input examples of the actual soft-threshold operator; those numerical examples are supplementary only.

The general theorem relies on the chamber Jacobian derivation, the exact elementary-step decomposition of path variation, the one-Haar-detail-per-scale identity, and a disjoint-support argument. The enumerator is not an infinite proof and the observed finite-depth values are not asserted as a general closed formula. All files required to run the checks are present in the package; run `python3 verify.py` without third-party modules. Independent validation has not been performed.
