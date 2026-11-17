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

# Verification and limits

Exact checks: Python 3 `verify_certificate.py` uses integer powers and `fractions.Fraction` to verify the strict radical bounds, \(r^{198}<1/400\), the rational identity \(D_{\mathrm{bound}}=496253/189120000\), and positivity of the norm witness. The proof uses the published trace-norm formula and principal-corner pinching and does not enumerate the enormous finite tree.

No independent mathematical audit, direct optimization of the full Schur norm, or minimal-core classification has been performed.
