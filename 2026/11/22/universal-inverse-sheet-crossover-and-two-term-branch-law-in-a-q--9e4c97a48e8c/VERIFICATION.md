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

The second output forces q=v−x. The first then imposes a sine level on the cubic phase Φ=ω[−bx³+2bvx²+(1+b−bv²)x], or on ωx at b=0. These phases are surjective, so each attainable target has infinitely many polynomial inverse roots across distinct phase levels, finitely many per level, and no inverse exists outside the stated strip. Each closed phase interval meets one progression of spacing 2π at the endpoint levels or two disjoint progressions at interior levels. The per-interval count differs from κ times length/π by at most two. Splitting into at most three strictly monotone pieces and subtracting at most two duplicated turning-point solutions bounds the variation count error by eight, uniformly even as b→0. For fixed b>0, the derivative is a downward quadratic with the two displayed zeros, hence the compact central increase contributes twice its phase increment in addition to Φ(−R)−Φ(R). That endpoint difference is exactly 2ωbR³−2ω(1+b−bv²)R; the even term cancels. At b=0 the variation is 2ωR. For fixed t,v at R=t/√b, rescaling shows √b times the variation equals ω∫[−t,t]|1−3s²+4v√b s+b(1−v²)|ds. The integral without ω differs from the claimed limiting integral by at most 4|v|t²√b+2t b|1−v²|; integrating |1−3s²| yields the stated breakpoint and profile, with Ψ′(t)=2|1−3t²| (zero at the breakpoint, not a sign change of Ψ′). In coordinates x,v the determinant equals a cosΦ·∂Φ/∂x, since the coordinate change has determinant one. This proves the at-most-two interior critical points for positive b, no such point at b=0, and all-critical endpoint levels. The inspected uploaded diagnostics were not executed; the integer-interval argument and explicit estimates prove the quantifiers, including exact turning-point hits.

## originality

PASS

Credit the already published map, standard variation method, and exact overlap in the leading Model 1 law, b=0 law and basic image/criticality in the same-day eight-map record. Its proof even recovers the fixed-coupling linear coefficient by substituting the cubic into its endpoint-variation estimate. That record explicitly credits this frozen Model 1 result as background and does not present an independent crossover theorem. The sharp fixed-charge scaled crossover and its explicit breakpoint/profile distinguish the assessed result from the inspected independent comparisons; same-day order is not inferred.

## value

PASS

The cutoff and dimensionless crossover variable have a mathematical reason: the cubic memory term competes with the linear phase when bR² is of order one. The profile identifies where internal phase turning points enter the window and quantifies the transition for all fixed scaled radii, adding useful information to the leading growth orders alone. The target-sensitive linear correction distinguishes finite-window defects. This is valuable one-step inverse geometry in the stated plane; most large-window branches cannot appear as recurrent orbit states in the signal strip.

The dated certificate retains the supplied scientific assessment, sources and limitations.
