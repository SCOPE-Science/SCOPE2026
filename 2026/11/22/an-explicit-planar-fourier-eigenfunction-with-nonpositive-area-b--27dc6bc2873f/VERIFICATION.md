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

# Mathematical verification

The standalone `CHECK.py` uses exact rational arithmetic from Python's standard library and was executed from the delivered package directory. It verifies the full Laguerre expansion, produces an eight-element exact Sturm chain, checks all four sign-variation strings and exact endpoint evaluations, and returns `CHECK_OK Laguerre_identity=exact Sturm_signs=4,4,3,3 positive_root_count=1 area_upper=183/100`.

The derivation of the Fourier \(+1\) eigenvalue is the analytic generating-function identity in `RESULT.md`; the checker is not a substitute for that argument. The proof determines the negative set over the entire noncompact plane by Sturm's theorem, not by finite enumeration or grids. No claim is made that the numerical location of the root is an independent certification, and no outside review has been performed.
