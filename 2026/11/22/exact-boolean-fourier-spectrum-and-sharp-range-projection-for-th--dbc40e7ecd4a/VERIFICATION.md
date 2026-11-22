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

# Reproducible mathematical verification

Run `python3 verify_ag23.py` with Python 3 and only its standard library. The actual packaged script completed successfully with 3,123 exact integer assertions. It builds the affine plane by two arithmetically separate constructions as triples with coordinate sum zero and as translated one-dimensional directions. It checks all 36 point pairs, all 72 bases, all 512 signed Fourier multipliers, their analytic formulas and multiplicities, the exact Fourier support, and the complete projection kernel by an integer Walsh transform.

The checker also verifies the Fourier projection symbol by an independent direct sum for each of 512 characters, the projection Plancherel identity, and the claimed absolute-kernel sum 3,104. Dividing by 512 yields the endpoint operator norm \(97/16\). The geometric line-incidence argument and the translation-averaging optimality proof are contained in `RESULT.md` and are independent of these finite tests.

Limits: computation checks a fixed nine-point finite system only. It does not establish an infinite-family theorem, mathematical historical priority, or an independent audit. The reviewer status is restricted to a self-review; external validation has not been performed.
