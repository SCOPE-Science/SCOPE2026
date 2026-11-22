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

# Verification of the geometric theorem

The proof is entirely analytic. The area-maximization code is diagnostic only and requires no external libraries. Run `python3 checker.py` in the directory containing it and the present artifacts.

The checker (1) evaluates the explicit three branches and critical equality configurations, (2) compares against a dense brute-force one-dimensional envelope at a fixed grid of cut levels, (3) evaluates many explicit feasible rectangles at arbitrary orientation, checking that none exceeds the proved upper bound, and (4) tests the differentiability values and thin-cap limiting ratio. Its random input uses a fixed seed, permitting exact replay. The program prints a final count of passed assertions; this does not certify continuous infinite cases or original priority.

The unrestricted-orientation step is independently explained algebraically in RESULT.md. It replaces any rotated feasible rectangle by a cut-parallel rectangle of the same area using the maximum-of-four-norms identity; all continuous extremizers then follow from a single-variable derivative whose nonzero stationary root is explicitly \(q(h)\). The limiting coefficient uses the standard circular-segment area integral, not fitted data.

No separate independent mathematical audit has been performed. The first-public date records prior context, not a date of publication of this theorem.
