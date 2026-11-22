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

The geometric derivation uses the oriented spherical solid-angle identity, the exact small-circle intersection geometry, and Gauss--Bonnet with corner terms. The strict ordering follows from a displayed strictly positive derivative. The two degenerate-base laws follow by explicit limits of the full CDF.

Run `python checks/lexell_area_checker.py` with Python, NumPy and SciPy to compare against independent conditional-arcsine quadrature and test the limiting cases. Such finite numerical checks are diagnostics only. The probability law is conditional on one fixed edge and an entire-sphere uniform apex. Historical novelty has not been independently certified. An independent mathematical audit has not been performed.
