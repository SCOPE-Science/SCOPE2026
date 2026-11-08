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

Run `python verification.py` in an environment with Python 3 and SymPy. The script performs exact rational symbolic calculations and has been executed against the companion source successfully.

The exact checks cover a triangle (degree 0), parallelogram (0), trapezoid (1), pentagon (2), centrally symmetric hexagon (2), and noncentrally symmetric parallel-paired hexagon (3). For every example, the script verifies two affine-precision identities, normalized vertex behavior, explicit facet-restriction factorization, and vanishing on each finite nonadjacent-line intersection. It also checks ranks \(5\) and \(6\) of the residual-conic interpolation matrices for the two hexagons. All tests passed.

The mathematical theorem for all polygons is proved by the facet/restriction and polynomial-divisibility argument in RESULT.md, together with the cited pre-existing classification of Wachspress adjoint degree. Finite symbolic checks do not establish the theorem by themselves. Independent mathematical validation has not been performed.
