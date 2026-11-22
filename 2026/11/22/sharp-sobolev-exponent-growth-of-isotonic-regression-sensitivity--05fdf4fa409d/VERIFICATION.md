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

The standalone checker `check_isotonic_wp.py` uses exact rational arithmetic to build local gradient transfer matrices from step-function inputs across every consecutive-block partition for dimensions 2 through 10. It verifies the exact row/column sum inequalities and that their global maximum values are respectively \(n/2\) and \(1\). It then evaluates genuine finite pairs through an independent PAVA implementation for the three-block lower extremizer and the two-block exact \(p=\infty\) extremizer, at every dimension 3 through 54. Finally, it tests 2,400 random two-input pairs at five exponents.

Expected final output: `ALL_ISOTONIC_WP_CHECKS_PASS`.

The checks do not certify absence of historical equivalents, do not replace the general analytical proof, and do not supply independent auditing. The exact finite-dimensional norm for interior \(p\) remains unproved.
