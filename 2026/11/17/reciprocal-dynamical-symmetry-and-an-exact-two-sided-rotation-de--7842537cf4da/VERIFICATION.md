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

Run `python verify.py` with Python 3, SymPy and mpmath available. A successful run prints the PASS line. The checker directly tests the polynomial parameter-conjugacy identity, exact depth reduction, integral first and second moments, derivatives, reciprocal moment identities, integrated flux identity and its sharp critical coefficient. Seven distinct \(\sqrt\varepsilon\) values on both sides of one and three interior tail thresholds per parameter are used for 21 independent high-precision integral comparisons. The exact uniform-action density, all-parameter reciprocal survival formula, and the monotonicity inequality are proved in RESULT.md; the numerical tests do not substitute for infinite-parameter proof. No independent audit or external formal proof certification is claimed.
