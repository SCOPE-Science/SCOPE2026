---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For an interior point in the positive quadrant the largest corner projection strictly exceeds the squared norm; membership in just one closed disk requires the squared norm to strictly exceed the second projection |tx-y|. Axes tie. In polar coordinates the radial fiber has lower endpoint |t cos(theta)-sin(theta)| and upper endpoint min(t/cos(theta),1/sin(theta)). The only loss of a nonempty fiber occurs for 1/t<tan(theta)<t at 2 tan(theta)^2 - t tan(theta) + 1 <= 0. The double root removes the entire ray already at equality. The positive fibers are open intervals with continuous endpoints and hence connected over each surviving angular interval. Independently, Cartesian slicing yields F(t)=3/2-(1/(2t))*integral from 0 to min(3,sqrt(1+t^2)) of sqrt(1+t^2-z^2) dz. Indeed the two excluded horizontal widths are (sqrt(t^2+4y(1-y))-t)/2 and sqrt(max(0,t^2-4y(y+1))); they are disjoint. The omitted circular cap has height h=sqrt(1+t^2)-3. Rescaling its integral yields h^(3/2) times a smooth positive factor, proving C^1, failure of twice differentiability, and the stated coefficient 2*2^(1/4)/9. Differentiation of G_t confirms the equivalent angular antiderivative.

## originality

FAIL

A distinct indexed same-day record on the identical centered rectangle, A sharp twofold-overlap transition for rectangular Thales coverings, explicitly establishes almost-everywhere multiplicities one and two, the entire exact twofold area law, the critical aspect ratio, and the same cusp with opposite sign. The frozen area fraction and singular expansion therefore duplicate that coverage by complementation. The other record does not print the singleton component count, but its exact pointwise lobe description gives it directly, including the critical equality with the stated closed disks. No publication order is inferred from the shared date.

## value

FAIL

The singleton area and its cusp are natural, but the frozen contribution restates an already determined area profile. The change in component count is a useful geometric interpretation; after the exact lobes and their threshold contact are known, it follows by intersecting their radial bounds with the open rectangle. This leaves no substantively independent exact invariant here to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
