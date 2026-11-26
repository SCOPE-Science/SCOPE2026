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

# Reproduction and limits

The proof in `RESULT.md` establishes the two-term upper tail and polar conditional law. The original supporting `check.py`, unchanged, can be run with Python 3, NumPy and SciPy. Its `upper_tail` routine integrates the polar area obtained by numerically solving the exact width equation, without using the asserted expansion for the integrand. The earlier recorded second-coefficient estimates were approximately 0.01573328684, 0.01567892625 and 0.01565190918 for deficits 0.02, 0.01 and 0.005, respectively, compared with the analytic value 0.015625. The script also retains lower-tail diagnostics from the original broader scope; those are not part of the corrected finding. Finite quadrature does not certify asymptotic error bounds, uniformity, or the contact and total-variation conclusions.
