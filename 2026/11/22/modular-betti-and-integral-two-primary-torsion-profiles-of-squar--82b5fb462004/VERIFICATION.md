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

# Reproducibility

From the directory containing the included program run `python3 verify.py`. It uses Python's standard library only and terminates with `MODULAR_ALMOST_ABELIAN_BETTI_VERIFIED` on success. It directly assembles the complete alternating Chevalley–Eilenberg differential, calculates finite-field ranks, and verifies the stated characteristic-two Betti polynomials and integral two-primary rank predictions against independent characteristic-zero ranks. The program is a finite consistency test; the algebraic proof in `RESULT.md` covers every specified dimension and characteristic-two field.

An additional independent exact integer Smith-normal-form calculation of the complete differential matrices confirmed one order-two factor in degree four at rank three and the respective factors (4,2,4) in degrees four, five and six at rank four; the general orders or odd-primary factors have not been determined. No independent mathematical audit has been performed.
