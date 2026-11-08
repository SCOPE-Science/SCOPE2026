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

## Exact-reproducibility checks

Run `python3 verify.py` using Python 3 with its standard library. The exact rational checker tests the affine and reduced vector fields on 80 sample states across four sectors, the radial identity, the strict angular positivity for sample points, the necessary cyclic dot-product relation, the whole-plane square/diamond example, and two parameter choices violating the positivity boundary. It reports `VERIFY_OK exact_sector_states=80 nonuniform_rates=4 square_full_plane=1 sign_boundary_counterexamples=2`.

The proof in RESULT.md uses exact algebra and a global monotone-gauge argument; finite tests cannot prove global well-posedness or the impossibility of extra cycles. No external audit or expert verification is represented by this document.
