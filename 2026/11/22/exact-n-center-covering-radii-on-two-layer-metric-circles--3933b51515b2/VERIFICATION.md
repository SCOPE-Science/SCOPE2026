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

The formula survives unchanged. The original odd-N construction incorrectly says every pair of adjacent covering arcs touches at the gap midpoint in the minority sheet. On an unlike-label gap the radii b and b-s are unequal, so the meeting point is at distance equal to the starting radius, not generally at the midpoint. The corrected complete RESULT.md replaces that sentence with the directed-gap criterion: distances from a point x along a gap of length g to the endpoint projections are at most x and g-x, so radii with sum at least g cover it. Same-label and unlike-label gaps satisfy this criterion on both target sheets, and the odd gap lengths sum to L. The lower bound splits at r=s: when r<s each sheet requires its own ceil(L/(2r)) centers, and when r>=s the lesser sheet arclength bound is 2rN-2s max(n0,n1), giving b=(L+2sh)/(2N). The separate equal-spacing construction attains a=L/(2k), including s=a, and the mixed construction applies for s<a where b>s. For N=1 the antipode in the other sheet forces and attains L/2+s. This proves the exact formula for all positive real parameters and the stated parity and endpoint behavior. The original exact-fraction interval-union checker was inspected, not executed; its 7200 recorded rational cases are supplemental, and the repair does not change its tested constructions or any verification status.

## originality

PASS

The corrected statement credits the applicable tree-factor covering-number inequality and the standard one-circle ingredients. The overlapping separated-regime obstruction is thereby accounted for. The parity-sensitive mixed-regime bound, the placement attaining it on both circles, and the complete exact formula do not follow from the inspected broader bounds, Finsler asymptotics, or finite prism enumeration.

## value

PASS

A two-point factor is the simplest discrete fiber in a natural product-covering problem. In the mixed regime the worse sheet limits cover length and produces a sharp parity effect that the general product bound misses. The exact transition from coupled to separated placement, with realizers for every budget and scale, is a useful benchmark for stronger product-covering bounds, not a sampling result or a restatement of the usual circle formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
