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

# Verification and limitations

The included standalone `check.py` can be run using `python check.py` with Python 3 and (for hull comparisons) NumPy and SciPy. Its first stage is pure-standard-library rational arithmetic. It verifies the exact polar/primal formulas, their normalized volume product, the stated difference identity, and its signs for 199 positive page counts.

The second stage constructs explicit integer vertex coordinates for the symmetric edge polytope and computes the vertices of the dual half-space intersection. For \(1\le m\le4\), it finds facet triangulations and evaluates the volume of each origin-to-facet simplex with an exact integer Bareiss determinant. The resulting rational volumes and the product match the formulas for dimensions two through five. The geometric solver is used to find facet incidence, not to determine final exact determinant values; this remains a finite numerical-geometric triangulation check, not a global formal certificate.

The infinite-dimensional parameter statement is proved analytically: a one-variable integral gives the polar volume for every integer \(m\ge1\), a support-function identity gives the primal volume, and the exact difference plus induction proves the unique maximum. A finite checker run alone would not prove any all-parameter statement.

The literature comparison and self-review are not independent auditing. No independent mathematical audit has been performed. The public claims concern the specified graph family and the stated affine-invariant normalization only.
