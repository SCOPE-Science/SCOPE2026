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

# Reproducible mathematical checks

Run `python verification.py` with Python 3 and SymPy. The checker uses exact rational coordinates and exact linear-algebra rank, with no numerical tolerance. It verifies polynomial affine precision, vertex evaluation, the residual-point interpolation rank and adjoint degrees for a parallelogram, a generic quadrilateral, a trapezoid, a generic pentagon, and a centrally symmetric hexagon. The observed minimum residual degrees are \(0,1,1,2,2\), as proved. For a product of two non-parallelogram quadrilaterals, it verifies all 16 product numerators and all four affine-precision coordinates and obtains common denominator degree two.

The unbounded part of the proof is the disjoint-variable top-degree-monomial argument together with residual-point line restriction, not finite interpolation enumeration. The checks do not prove novelty, general uniqueness of barycentric coordinates, or extend the theorem to excluded polygon shapes. An independent mathematical audit has not been performed.
