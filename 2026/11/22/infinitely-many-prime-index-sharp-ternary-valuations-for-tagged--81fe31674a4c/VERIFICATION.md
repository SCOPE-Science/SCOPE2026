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

# Mathematical verification and limits

The exact-arithmetic script `verify.py` recalculates finite Euler products by logarithmic differentiation; it checks the normalized tagged-part dissection, the first 3-adic scale congruence, the eta modularity congruences and rational cusp orders, and sample prime coefficients. No raw computational trace is used as an infinite-prime proof: that follows from the cited Deligne--Serre Hecke theorem, applied to the holomorphic weight-five form whose cusp orders are proved in RESULT.md. The higher-level sharpness relies on the explicit published integral internal congruences. Neither external independent audit nor automated infinite certification is asserted.
