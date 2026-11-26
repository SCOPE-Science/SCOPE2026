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

The proof integrates an explicitly differentiated conditional distribution on its exact domain \(z<u<1\); no discretized or truncated integral is used to establish the CDF. The checker tests the copula margins, mixed density, conditional integral, product density, log-score transformation, moment antiderivatives and limits, and the factorization of the derivative used in the crossing argument. Run `python CHECK.py` with `sympy` installed; the checker contains 13 symbolic identities and 16 numerical/domain assertions. The numerical tests supplement rather than establish global identities. Historical novelty is qualified because the original 2022 full text and possible appendices were not accessible.
