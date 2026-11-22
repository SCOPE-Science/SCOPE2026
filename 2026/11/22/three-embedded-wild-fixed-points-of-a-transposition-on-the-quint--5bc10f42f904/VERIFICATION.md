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

# Verification evidence and limits

Use Python 3 and SymPy 1.10 or newer. In a directory containing the attached file run `python3 verify_fixed.py`. The exact-chart checks verify the involution, the fixed equations, the special-fiber relation, and the tangent linear part. The standalone finite-field enumeration includes every point of the blowup over six small prime fields, not just the affine part; the resulting fixed-point counts are respectively \(3,7,9,11,15,17\) for characteristics \(2,3,5,7,11,13\). The observed marker is `M05_TRANSPOSITION_WILD_EMBEDDED_FIXED_SCHEME_VERIFIED`.

The universal claim is proved symbolically in RESULT.md; the finite counts are corroborations, not an extension-field or infinity certificate by themselves. The characteristic-two embedded nilradical follows from the exact local quotient and is checked algebraically. The proof assumes the standard integral blowup identification with \(\overline M_{0,5}\). No independent mathematical audit was performed.
