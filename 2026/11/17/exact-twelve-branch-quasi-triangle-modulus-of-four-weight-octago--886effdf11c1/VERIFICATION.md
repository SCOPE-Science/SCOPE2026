---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: q is even, continuous, strictly positive and absolutely homogeneous by conewise positive interpolation on the eight specified UNNORMALIZED rays. In dimension two its two-summand concavity constant C(q)=max_{z in conv{q<=1}}q(z): the upper bound follows from unit-ball convex combinations; the reverse uses a supporting segment joining two original unit-ball points. Here the unit ball is exactly the union of eight triangles with vertices 0 and consecutive radial points u_i/c_i, so its convex hull is their polygonal hull. Maximization of the cone-linear q over the hull occurs at a ray/hull-edge crossing or an original unit vertex. Exact chord-ray relation u_i=s*u_j+t*u_k yields ratio c_i/(s*c_j+t*c_k); the twelve antipodal classes exhaust strict crossings and the baseline 1. Each of the twelve parameter witness quadruples strictly and uniquely maximizes its indicated term. Independently checked all twelve strict branch witnesses exactly by rational arithmetic. No claim for dimensions beyond 2, normalized diagonal rays or zero weights.

## originality

PASS

PASS best-of-knowledge: Unser (2026) Theorem 2.4 gives the general continuous quasi-norm criterion and only the upper bound C<=M/m, and its conic-spline construction supplies the fan geometry, but the inspected sections do not give this particular sharp four-parameter twelve-branch modulus or irredundancy witnesses. General Banach-envelope convexification and planar polytope geometry are antecedents; the present full optimal multi-parameter rational phase classification is not an immediate displayed known table. An unindexed polyhedral-gauge optimization formulation may cover it.

## value

PASS

PASS: The canonical centrally symmetric eight-ray four-weight family is a natural small but genuinely nonconvex polyhedral quasi-norm class introduced by conic spline parameterization; its exact optimal constant is a useful fine invariant not determined by general norm-equivalence bounds. Twelve indispensable phase branches classify sharp extremizers and control quasi-triangle estimates across the whole positive parameter orthant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
