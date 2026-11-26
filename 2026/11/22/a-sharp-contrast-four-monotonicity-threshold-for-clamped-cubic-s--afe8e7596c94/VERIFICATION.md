---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The clamped Hermite C² equations give m₁=(4a+3b−c)/5 and m₂=(−a+3b+4c)/5 on the unit mesh. The three derivative quadratics are linear in the increments. After normalization their pointwise lower envelopes on [1,4]³ are computed by the signs of their coefficients. On the first cell the minima are 3t² and t(24−21t)/5 on either side of 2/3; on the middle cell the outer lower-envelope quadratics have discriminant −8 after removal of the common positive factor, and the middle minimum is 3(2t−1)². Reflection handles the final cell. None of these cubics can be constant on a cell with positive increment, so nonnegative derivative also gives strict increase as a function. For (1,R,1) and (R,1,R) the common slope is 3(R+1)/5>3 when R>4; the first pattern has negative derivative just right of zero, and the second has midpoint derivative 3(4−R)/10. With gaps (h,1,h) and increments (r,1,r), the common slope 3(r/h+h)/(3h+2) must be at most both 3r/h and 3, giving h²/(3h+1)≤r≤2h(h+1). Covering [1/R,R] forces R below four for h≠1: the upper constraint increases in h, the reciprocal lower constraint decreases, and they intersect at four. Finally the exact endpoint minimum is −4re³/[27(1+e)²] for e=m/r−3; at r=1/4−ε this is −4096ε³/125+O(ε⁴). With d=m−3=3ε/5 at r=4+ε, integrating the central derivative between its zeros gives the drop (2d/3)√[d/(24+12d)] and hence the stated coefficient and exponent. No claims of optimality beyond reflection-symmetric grids were used.

## originality

PASS

The interval Hermite criterion is prior machinery; the assessed contribution is its global robust counterpart for a fixed four-knot C² clamped construction with zero endpoint derivatives, plus the reflection-symmetric mesh optimum and distinct loss laws. Closest indexed robust-contrast results are for natural splines, with different end conditions and, on nonuniform grids, a different contrast measure. The accessible literature gives single-cell tests or a nonrepairability statement with different quantifiers, not the present exact robustness claims. This is a bounded assessment rather than a historical priority conclusion.

## value

PASS

Four knots give the smallest setting with separate boundary and central cells that can fail in distinct ways under the same fixed flat-endpoint rule. The exact raw-increment bound is actionable for using the prescribed C² interpolant, and the nonuniform comparison explains why an alternate symmetric knot placement cannot improve worst-case guarantees. The quantified losses distinguish an onset at the endpoint from an interior pocket rather than merely finding isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
