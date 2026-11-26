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

For fixed strictly separated balls the indicator is the sum, and the real radial amplitude is r^(d/2) R^(-d/2) J_(d/2)(2πrR). Squaring its normalized asymptotic gives the stated weights and an O(R^-1) error; the off-diagonal term gets the extra O(R^(-(d-1)/2)) angular Bessel factor. For irrational ratio the time average of every nonconstant torus character tends to zero; compactness, tail recurrence and the vanishing error give both extrema and the continuous-test-function law. In rational ratio p:q the zeros and unit maxima have target phases (d+3)/4 and (d+1)/4 modulo 1 in the doubled phase convention. Eliminating the real phase gives qk−pℓ=(p−q) times the target, and coprimality makes integrality necessary and sufficient, including p=q=1. In d=3 and ratio 1:2 the normalized expression is z+4(2z−1)^2=16(z−15/32)^2+31/64, with maximum 5 on [0,1]. The companion code was inspected, not run; these are analytical checks, not formal verification.

## originality

FAIL

The headline lower-envelope claim is materially covered by a distinct indexed finding on all finite disjoint ball unions: that record states the same two-ball criterion, a stronger exact lower-envelope formula, and the same leading asymptotic. Its catalog date matches this record, so this is demonstrated coverage, not a finding about temporal priority or authorship. The upper criterion and explicit arcsine law are not stated in the inspected matching Finding; they are useful descriptions but routine consequences of that same expansion (phase complementation and standard continuous-time Weyl averaging), not a supported independently distinct surviving contribution on this evidence. No repair is proposed merely by deleting the covered clauses.

## value

PASS

At the package level the problem is meaningful: determining when the sharp upper-decay scale also bounds the energy below, despite the zeros of individual balls, is more informative than an upper estimate. The explicit benchmark and frequency law aid interpretation, but this value cannot overcome demonstrated coverage of the original package; the routine remaining consequences are not offered as a standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
