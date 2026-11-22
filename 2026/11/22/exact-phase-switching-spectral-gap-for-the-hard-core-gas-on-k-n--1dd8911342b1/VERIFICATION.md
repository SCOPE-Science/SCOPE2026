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

The all-length statements are derived analytically from reversible-sector interlacing, the independent-site binomial resolvent, Dirichlet-ground-state strictness, and a fixed-activity inverse-binomial-moment asymptotic. No finite experiment is offered as proof of an infinite statement.

`CHECK_EXACT.py` uses exact rational elimination and checks 108 independent shifts/activity/size combinations of the cofactor identity. `CHECK_DENSE.py` independently enumerates all hard-core configurations, builds the reversible symmetric generator, computes its gap, and compares it to the scalar root for 21 cases; it tests strict finite-size decrease in these cases. Both completed successfully in the reviewed environment. To reproduce: run `python CHECK_EXACT.py` (Python standard library), then `python CHECK_DENSE.py` (NumPy and SciPy required).

The external comparison is limited to accessible primary material; an earlier paper on Ehrenfest urn first-passage theory was not accessible in full. The article's abstract and context were considered, not labeled as a negative full-text comparison. Independent audit and external validation have not been performed.
