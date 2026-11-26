---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The expansion on the tangent hyperplane gives the cone criterion Av proportional to Aᵗv^[4]; rescaling normalizes it uniquely up to F4*. Invertibility gives smoothness and, on a normalized isotropic line, the two-sided tangent radical is precisely that line, so the quotient plane cubic is smooth. The affine equations v_i^4−(Cv)_i have disjoint leading monomials in a graded order and invertible Jacobian C, so have exactly 4^5 reduced roots over the closure. Iteration bounds the field by F_{2^{2h}} for h the order of C. Our independent binary-RREF enumeration found 495 nonzero isotropic solutions in each of the 13 cases. Counting projective Frobenius fixed vectors by cross products for every divisor of 2h, dividing by three, and applying divisor inversion confirms every row and exactly ten distinct partitions. Separately, a different generating set and vectorized closure reproduced thirteen disjoint congruence classes of exactly the table's sizes, summing to |GL5(F2)|=9,999,360. The degree and zeta conclusions follow from those same closed-point lengths.

## originality

PASS

Pass for the complete threefold splitting classification, not for the thirteen coefficient classes or the 165-point geometric count. There is demonstrable prior coverage of the fifteen degree-five points of the Klein row via the marked Gauss fixed scheme, but not the full row or census. This partial implication is credited below; it does not cover the 150 other points in that row or any other row by the same argument.

## value

PASS

The exact Frobenius action on a distinguished finite cone-center locus answers a descent question not settled by geometric equivalence or rational Fano-line counts. In particular it identifies late first or full splitting (degrees five and 24), and gives the point counts over arbitrary extensions. This precise arithmetic information is useful in studying which distinguished tangent cones are available over a given finite field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
