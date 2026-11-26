---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The sharpened coefficient is obtained analytically in `RESULT.md`. The two caps have combined outward horizontal first moment \(4r^2\) with respect to arclength, contributing \(16Lr^2\) to the ordered horizontal distance integral. Perimeter normalization contributes \(-2\pi^2Lr^2\) and the common opposite-side integral contributes \(-4Lr^2\) at the nonlogarithmic order. The remaining terms are bounded by \(O(r^3[1+\log(L/r)])\) before normalization. The unchanged `stadium_check.py` (NumPy and SciPy) evaluates ordered boundary pair integrals and reports a leading-logarithm diagnostic; those finite values do not certify the sharpened coefficient or the uniform remainder.
