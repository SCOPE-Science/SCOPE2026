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

Run `python CHECK.py` with SymPy installed. The script constructs graph Laplacian restrictions, solves the Sylvester equations exactly, checks both triangle comparison factorizations in the rational function field, proves that all monomial coefficients of the numerator and denominator are strictly positive, and checks all four rational four-cycle errors and their ordering. No numerical quadrature, floating-point tolerance, or finite-experiment extrapolation is required.

The continuous-time formula is justified by matrix-exponential convergence on the common zero-sum subspace. For positive conductances each single-edge-deleted triangle or four-cycle is connected, so the Sylvester solution is unique. The symbolic checks certify the needed finite polynomial identity; the argument applies to every positive real weight, not merely rational examples.

Independent audit has not been performed. Historical priority is not certified.
