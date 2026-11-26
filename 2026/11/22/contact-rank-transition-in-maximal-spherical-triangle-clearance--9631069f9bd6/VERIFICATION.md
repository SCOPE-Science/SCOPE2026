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

The shortest distance to the boundary equals the smallest distance to a supporting circle: a shortest arc to a minimizing circle cannot leave through any side earlier than that minimum. The nearest point z in the normals' convex hull gives n_i·(z/||z||)≥||z|| by projection, whereas min_i n_i·x≤z·x≤||z||, with equality only at o=z/||z||. A single vertex cannot minimize since moving toward a distinct unit normal initially decreases the norm. A two-weight optimum is the midpoint, yielding precisely the stated Gram test, and two distinct eligible pairs would contradict uniqueness. With three positive weights the tangent normals positively span the plane, so for some c>0 one inward tangent dot product is at most −c times the tangent norm, giving a uniform O(ε) localization (first restrict to the chart by uniqueness). The scaled half-planes converge to the bounded circumscribed triangle and its area equals inradius times semiperimeter, giving C_3. With two positive weights the exact pair inequality gives s=O(ε) and t=O(sqrt(ε)), and rescaling gives |u|+(r/2b)t²≤1. The unused constraint is either slack or has a nonzero component in the transverse direction, the latter by linear independence. At criticality its rescaled inequality selects one half of the parabolic area; the truncated domain need not be a half at positive ε. The rescaled area elements converge to constant densities on bounded sets with null limiting boundaries, giving both tail coefficients and conditional laws. Spherical excess supplies the displayed normalization A. An independent latitude and angular-interval integral retaining all three inequalities gives, at ε=10^−5, scaled areas 5.196116, 1.892526 and 3.771251 against 5.196152, 1.885618 and 3.771236 for an octant, an asymmetric critical triangle and a strict two-contact triangle, respectively.

## originality

PASS

The two-versus-three geometric contact distinction is prior, and the strict two-weight local law (including the marked geometry) overlaps the indexed spherical-lune result. The inspected sources do not cover the combined triangle endpoint theorem, notably the exact coefficient and conditional tangent geometry when three weights are positive and the half-law for the three-tight, two-positive critical case. No priority for the standalone lune law is inferred from a same-day index date.

## value

PASS

Contact count alone does not predict the clearance tail: critical and three-positive-weight triangles both have three geometric contacts, but differ in exponent and conditional geometry. The Gram test, exact constants, and limiting area laws make this distinction computable for the full fixed proper triangle class. The zero-multiplier half-law is a concrete, independently useful transition boundary beyond the ordinary strict lune case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
