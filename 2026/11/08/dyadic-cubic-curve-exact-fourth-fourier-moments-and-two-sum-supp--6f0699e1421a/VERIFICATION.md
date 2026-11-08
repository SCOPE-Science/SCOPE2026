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

# Verification of dyadic cubic-curve two-sum laws

Run `python check_cubic_dyadic.py` with Python 3. The checker uses the standard library only and independently enumerates ordered two-sums. Its predicted branch uses the proved valuation formula; square-root root counts are separately cross-checked against brute-force squaring.

Observed: every square fiber and its second moment matched for moduli of depth 1 through 10. Every target pair, including zero-count targets, matched the predicted cubic-curve convolution for depths 1 through 10. The computed energy and sumset sizes agreed with the closed formulas at every depth. The final output was `DYADIC_CUBIC_CURVE_CONVOLUTION_CHECK_PASS`.

The algebraic proof in RESULT.md is valid for all positive depths. These finite experiments are not an infinite proof and do not independently establish historical priority, unrestricted extension bounds, or optimizer classifications.
