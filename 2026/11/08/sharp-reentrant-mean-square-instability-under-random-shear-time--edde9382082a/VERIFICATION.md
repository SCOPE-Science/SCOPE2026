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

Run `python check.py` in the same directory to enumerate length-\(n\) independent choices of unscaled shears with exact fractions, compare the entire mean vector with a product of averaged matrices, compare second-moment multipliers for all enumerated states, and calculate the critical threshold and a concrete instability window with double-precision bisection. The output begins `VERIFY_OK` on success.

The checked exact values for the example \(a=1\), \(k=4\), \(h=4/5\) are bounded numerically by \(1.23560669012<f(h)<1.23560669014\) and \(0.71875160405<g(h)<0.71875160408\). The source proof verifies every positive real \(a,k,h\), every integer \(n\ge0\), and the neutral endpoints by explicit formulas; enumeration cannot establish these infinite claims.

The computation uses only the Python standard library. No third-party certificates or independent validation are claimed. Publication precedence requires independent assessment.
