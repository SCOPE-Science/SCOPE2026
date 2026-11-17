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

Run `python3 verify_quartic_nd.py` with Python 3 and NumPy. On the saved package, it reports:

`QUARTIC_ND_SUPPORT_PASS exact_dimensions=198 random_tangent_pairs=24000 d3_volume_consistency=1`

Checks: exact rational endpoint curvature degeneracies and volume Taylor coefficient for 198 dimensions, and 24,000 independently sampled tangent-pair inequalities. The three-dimensional predecessor is used only as a calibration. The infinite all-dimensional statement is proved by the algebraic estimates in `RESULT.md`; numerical checks alone would not establish it. Independent mathematical audit: not performed.
