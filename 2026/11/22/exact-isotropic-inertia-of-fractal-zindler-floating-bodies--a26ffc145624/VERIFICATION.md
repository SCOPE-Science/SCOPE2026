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

For a truncation q=h_N, p=q', differentiation gives z'=-r u+(q+q'')u', and det(z,z')=q(q+q'')+r(r+p). To check Jordan geometry directly, put M=β/(α−β). For either a truncation or the limit, |q'|<=M. If two parameters at shorter circular separation d in (0,π] mapped to the same point, projection onto the midpoint radial unit vector would give (q(t)−q(s))cot(d/2)=2r+q'(t)+q'(s). The left side has absolute value at most 2M, the right side exceeds 2M because r>2M. Thus the curves are simple; the homotopy scaling q to zero has positive tangential component r+λp, so winding about the origin is +1. The smooth Green formula for J uses one quarter of the integral of |z|² det(z,z'); half-period oddness kills odd degrees, and integrating q³q'' and qp²q'' by parts gives the claimed reduced quartic q⁴−2q²p²−p⁴/3. After cancellation of opposite equal frequencies, a largest unmatched frequency cannot be balanced by at most three lower ones. Same-index fourth averages are 3/8 or, for sin²cos², 1/8; distinct pairs contribute the products of second averages. This yields 3A_N²/4−3C_N/8, 3B_N²/4−3D_N/8, and A_N B_N/4−E_N/8. All five geometric sums have the stated limits since α>β. The construction source establishes boundary area zero for the limit. Uniform convergence of the boundaries then stabilizes the winding index, hence region membership, off that null boundary; common bounded support permits dominated convergence for J. No differentiating the fractal boundary is needed. The rotation by 2π/β fixes the region and its centroid; it forces a symmetric second-moment matrix to be scalar, as the angle is neither zero nor π. Subtraction of S²/(2π) gives the stated constant remainder and positive exact πB coefficient. This is for the stated large-r lacunary construction, with unnormalized area moments about the rotational center. The NumPy truncation script was read, not executed; these independent checks are analytic.

## originality

PASS

Pass the exact polar moment and equal-area disk excess of this lacunary Jordan region. The construction, its area and convergence are prior inputs; scalarity alone follows at once from its already known symmetry. Neither these inputs nor the inspected same-day approximant theorem supplies the scalar value, which requires the quartic Fourier moments and limiting passage.

## value

PASS

The same natural floating-body family has an r-independent area correction but a strictly positive and exact r² inertia correction relative to its equal-area disk. The full centroidal second moments are useful for comparing shapes when the boundary is nonrectifiable and direct smooth moment formulas are not justified. The finding computes a natural invariant throughout the construction's parameter range, not an isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
