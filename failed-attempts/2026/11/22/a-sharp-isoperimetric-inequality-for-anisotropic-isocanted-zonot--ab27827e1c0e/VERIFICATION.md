---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For positive lengths all facet normals are the unit vectors ±e_i and ±(e_i−e_j)/sqrt(2). Coordinate facets have the indicated products of widths; projecting the diagonal into the orthogonal complement of the other d−2 coordinate directions gives the factor sqrt(2)a in the remaining facet areas. The determinant formula gives the volume. With the record's dimensionless variables the quotient reduces to 2^d(d+Bp)^d/[P(1+dp)^(d−1)]. Its logarithmic derivative has the sign of B(1+p)−d(d−1), hence the interior minimum stated in RESULT.md. The normalized Newton inequalities telescope to E_d≤E_2^(d−1), and B≤sqrt(2) binom(d,2), with equality in the latter only for equal normalized lengths. This includes d=2. Substitution yields the stated sharp constant and a/b=sqrt(2)−1. A separate fixed-normal Wulff proof below also recovers the exact constant and equality. Replay: RESULT.md lines 23–47 and the support-function argument in this review; VERIFICATION.md and check_zonotope.py were inspected, not executed.

## originality

FAIL

The central inequality, constant, and equality case are a direct specialization of the pre-existing Wulff inequality to a fixed finite set of facet normals. The proof here differs from the published anisotropic inequality proof, but is not a new extremal claim. The difference from the unrestricted zonotope optimum does not resolve this stronger prior implication.

## value

FAIL

The geometric question is natural and the symmetric rigidity is useful to state, but the inequality claimed as the independent finding is mechanically implied once the known tangent configuration is expressed through its fixed facet normals. The facet and determinant formulas are standard evaluations; the alternate Newton proof gives an elementary exposition, not an additional phenomenon or a quantitative stability theorem. No independent valuable remainder requiring a substantive repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
