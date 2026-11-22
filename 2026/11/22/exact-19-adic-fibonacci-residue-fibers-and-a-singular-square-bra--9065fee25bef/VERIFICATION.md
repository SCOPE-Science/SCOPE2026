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

# Reproduction and verification

Run `python3 CHECK.py` in the same directory, requiring Python 3's standard library only. It computes all values of the Fibonacci recurrence through one least period modulo \(19\), \(19^2\), \(19^3\), and \(19^4\), and constructs independently predicted target-fiber counts using the stated baseline and square-root congruence. Each target multiplicity agrees exactly at all four precisions; image sizes are \(12,210,3981,75621\), and maximum fiber counts are \(3,19,38,361\), respectively. It checks that no tested prime-factor divisor of the proposed period is a period.

The universal correctness assertion is supported instead by the proof of the matrix period, eighteen analytic branches, the seventeen regular isometries, the singular Lucas-coordinate square normal form, and standard square-root counts. Finite testing cannot prove the quantified result. The limiting density and image counts are published earlier; the new statement concerns per-target multiplicities and extremal fibers. No independent mathematical audit has been performed.
