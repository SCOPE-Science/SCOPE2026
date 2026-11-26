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

For a nonzero point the diameter condition is |z|²≤z·v, so at most one disk from each opposite pair contains z. In each quadrant the matching vertex dominates |z|² term by term, giving coverage; the origin is exceptional and immaterial to area. In the first quadrant the extra disk is equivalent to u²+v²≤|au−bv|. One lobe is a segment of the circle centered at (a/2,−b/2) of radius √(a²+b²)/2, with the segment above y=0 cut additionally at y=b. The two segment offsets are b/2 and 3b/2; the second segment exists exactly at a²>8b². The transposed lobe gives the other contribution. This reproduces the area formula. With T=√(λ²−8), the subtraction has numerator (2/9)T³+O(T⁵), giving 2^(5/4)/9 in the correction and the claimed C¹ but not C² behavior. The above-threshold derivative has numerator (T²+7) arctan(3/T)−3T; averaging (T²+s²)^−1 over s∈[0,3] gives a strict lower bound from Jensen using the mean of s² equal to 3. Below threshold the derivative is positive for λ>1. Expanding the complementary arctangent expression at infinity yields 1−3/(2λ²)+O(λ⁻⁴). Independent polar midpoint quadrature of min{a/cos φ,b/sin φ,|a cos φ−b sin φ|}² on [0,π/2], divided by 2ab, agreed with the formula to within 1.1×10⁻⁷ at aspect ratios 1, 2, √8, 2.9, 4, 15 and 60; the analytic checks, not these samples, establish the theorem.

## originality

FAIL

The principal unequal-rectangle area profile, clipping threshold and leading nonanalytic transition are already covered by a distinct indexed exact one-coverage profile on the identical geometry. Outside the origin and a set of zero area, exactly one or two disks cover each point, so q=1−F. The change from a polar correction to a circular-segment correction does not create a new invariant. This is demonstrated equivalent coverage, not a finding that either same-day record came first. The checked equivalent source does not explicitly state strict monotonicity; that genuine distinction does not make the central claim in the frozen package distinct.

## value

PASS

The monotonicity refinement answers a natural comparative question: in this fixed covering, an observed double-coverage fraction in the interior of the range determines eccentricity uniquely and orders rectangles by depth. Proving that sign across the clipping transition requires a nontrivial inequality, not mere evaluation of the known profile. The duplicate area law and onset are not counted as new value, and this assessment does not validate the frozen finding overall.

The dated certificate retains the supplied scientific assessment, sources and limitations.
