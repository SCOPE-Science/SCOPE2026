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

Independently, place one edge at u=(0,0), v=(L,0) and put B=(b,h), h>0. A ray from B in direction w meets the lens up to the positive part of min((u−B)·w,(v−B)·w). On the right and left half-circles the respective controlling radial endpoints are a sin(alpha−phi) and q sin(beta−phi), positive for 0≤phi<alpha or beta, where a,q are the endpoint distances and alpha,beta the endpoint angles. Integrating half the squared radius gives (alpha a²+beta q²)/4−[a² sin(2alpha)+q² sin(2beta)]/8. The bracket is 2h[b+(L−b)]=2hL. This works even for an exterior perpendicular foot, when the frozen sector argument must not subtract both unsigned triangle areas. Summing over edges sums the fan triangle areas to A(P) and the split angles to the original interior angles. Completing the weighted square gives the unique interior minimizer, because all weights are positive and the vertices span P. Convex weights expressing B in a triangle show that any point in all three diameter disks equals B, so the pair sum gives double coverage in area. The formula and claims hold as stated.

## originality

FAIL

The full moving-point formula for all strictly convex polygons is an immediate equivalent-area consequence of Yankelevsky–Bruckstein's published exact union formula for the same disks (2016, Eq. (19), not just its Steiner minimizer). Adjacent lens multiplicity is pointwise total disk multiplicity minus the union indicator almost everywhere. Thus the earlier exact formula evaluates this energy, with the proposed minimizer and stability following by completing the square. The centered equilateral value is also explicitly recoverable from the earlier Resultary multiplicity spectrum. This is demonstrated prior coverage, not an access issue.

## value

FAIL

The overlap objective is geometrically natural, but this record's exact content is a direct re-expression of a previously evaluated union area: the linear half-plane cut makes adjacency count the redundancy pointwise. The weighted optimum and curvature are then square completion, and the triangle interpretation is the proper-block case with at most two memberships. The original record provides no nonmechanically implied exact statement worth preserving as a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
