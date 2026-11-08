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

# Verification of the stated two-scale Brownian search theorem

The theorem is supported by four reproducible mathematical checks, all visible in `RESULT.md`: (i) the Brownian hitting-time Laplace transform and the one-attempt stopped survival integral, (ii) geometric-index scaling and a square-integrable stopped-martingale estimate, (iii) a conditional triangular-array central limit theorem using explicitly bounded third moments, and (iv) separation of successful and exhausted paths at the narrow deadline edge.

The companion `check.py` is self-contained. Executing `python3 check.py` reports `PASS: 76 exact-identity, integration, moment and asymptotic diagnostics`. Its numerical quadrature is independent of the closed-form moment formulas. It does not prove publication novelty or the infinite limits; the displayed analytic proof is required for those.

No independent scientific audit has been performed. In particular, the scientific priority comparison is limited to the three cited primary works, the described research-record queries, and relevant discoverable literature; a stronger result may exist outside this search.
