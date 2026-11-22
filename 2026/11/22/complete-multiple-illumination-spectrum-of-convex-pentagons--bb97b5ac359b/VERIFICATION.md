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

Run `python3 verify.py` with Python 3. The checker's input is fully internal to that source file, and its tests use only exact integer operations and the Python standard library.

The checker enumerates all 26,277 rational exterior-turn patterns with denominator from five through thirteen, verifies the illuminated-vertex incidence graph against both adjacent and nonadjacent compatibility inequalities, verifies the one-/two-failed-test classification and incompatible-triple lower bound, and applies an exact finite-state multicover search to all 31 incidence profiles for multiplicities one through four. It checks strict boundary equalities in 12,120 cases and integer cross products for a concrete nonsymmetric pentagon.

Expected terminal summary: `PASS: 26277 exact rational-turn pentagons; 1287 favorable, 24990 other; 12120 boundary cases; 31 incidence profiles; all incidence profiles m=1..4.`

These computations are corroborative. The unbounded assertion for every genuine convex pentagon and every positive multiplicity is proved by the common-open-semicircle characterization, the identity for sums of separated exterior-angle pairs, and explicit matching lower and upper bounds. The code does not check every real exterior angle or infinitely many multiplicities.
