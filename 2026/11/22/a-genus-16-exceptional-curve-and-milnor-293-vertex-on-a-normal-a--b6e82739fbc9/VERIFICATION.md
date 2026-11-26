---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Reproduction and limits

Run `python3 verify.py`. The check uses standard-library arithmetic in the basis \(1,\zeta\) of \(\mathbb Q(\zeta)\), \(\zeta^2+\zeta+1=0\). It verifies the arrangement incidence and transverse conic example, and reproduces the numerical consequences of the cover and Euler stratification. It does not certify normality, the finite birational chart construction or minimality; those follow from the proof. The Euler–Milnor computation is a consistency check against the separate Milnor-jump classification, not a separate novelty claim.
