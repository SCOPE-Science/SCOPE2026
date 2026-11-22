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

# Verification record

The geometric proof derives all probability constants from the explicit four-facet representation. Reproducibility is provided in `check.py` (Python, NumPy and SciPy): it compares facet-intersection and chamber formulas, checks seven exact-CDF quadratures against independently sampled directions, and computes direct survival integrals to avoid loss of precision near the upper endpoint. The finite checker passed; its Monte Carlo tests cannot certify global inequalities or infinite limiting statements. These follow analytically from the factored polynomial, the local Taylor expansions, and local area convergence established in `RESULT.md`.

The 2005 primary intersect-distribution paper could only be inspected at bibliographic/abstract level; its complete text was unavailable. It addresses a different translated-line sampling ensemble in the accessible description. Unexamined historical material remains a priority risk. Independent validation and independent audit have not been performed.
