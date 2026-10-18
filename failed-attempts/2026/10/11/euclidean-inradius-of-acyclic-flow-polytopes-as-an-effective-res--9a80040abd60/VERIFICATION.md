---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

FAIL

The proof asserts aff(F_G(a))=x0+ker B for an arbitrary feasible netflow; this can fail when some coordinate is identically zero on the nonnegative-flow fiber. Explicit counterexample: V={0,1,2,3}, E ordered (0→1),(0→2),(1→2),(0→3),(2→3), netflow a=(1,0,−1,0). The directed graph is acyclic, its underlying undirected graph is connected, a is integral and sums to zero, and F_G(a)={x(t)=(t,1−t,t,0,0):0≤t≤1}, a positive-dimensional segment of intrinsic length sqrt3. Its actual inradius equals sqrt3/2≈0.8660254038. All and only x01,x02,x12 are nontrivial coordinate facets. The full-graph Laplacian gives 1−R for these edges (3/8,1/2,3/8), respectively (and 3/8 on both forced-zero edges). Nontrivial lower ideals S={0} and S={0,1} have a(S)=1 and C(S)=sqrt(3/8)+sqrt(1/2); S={0,1,2} has C=0. Thus the claimed formula returns 1/[sqrt(3/8)+sqrt(1/2)]=4/(sqrt6+2sqrt2)≈0.7578747639, not sqrt3/2. Indeed the actual affine tangent is span(1,−1,1,0,0), strictly smaller than ker B, so full-graph cycle projections give incorrect facet-distance factors. Numerical evaluations only illustrate an exact inequality of radicals; rational Laplacian leverage and segment parameterization were calculated independently. Existing three bundled tests happen to have full-dimensional affine incidence fibers, so VERIFY_OK does not validate this missing hypothesis. Original universal claim is false and must be rejected, not passed with a disclaimer or a purely prospective fix.

## originality

PASS

As a candidate mathematical formulation, the exact full-graph-resistance lower-ideal ratio is not stated by the consulted incidence-polytope primary literature; this originality judgment is independent of and does not diminish its decisive falsity. No valid new mathematical result is accepted from this record.

## value

PASS

Finding an effective-resistance-based metric inradius and full center characterization for all DAG netflow polytopes is a motivated mathematical problem; exact cut constraints and intrinsic affine metrics matter for optimization and graph geometry. The attempted theorem fails, but its precisely exposed forced-support boundary provides a substantive instructive obstruction to the proposed formula. This value axis concerns the mathematical question and obstruction, not any approval of the false universal claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
