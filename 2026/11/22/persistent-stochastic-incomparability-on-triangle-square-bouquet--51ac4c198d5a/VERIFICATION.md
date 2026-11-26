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

The two sampling laws are on cardinalities, not on labeled maximal sets. The hub-selected class consists only of hub plus square antipode. Excluding the hub, one must take one vertex per triangle and then either the square antipode or its two neighbors; all such selections dominate the hub because r≥2. This yields counts (1,2^r,2^r). Under i.i.d. priorities, conditional on hub priority t all triangle priorities must exceed t for hub acceptance, and the independent square gate is (1−t)^2 plus the integral of 2u(1−u) from 0 to t (the first hub neighbor in the square appears at u<t but is blocked by the antipode). Beta integration gives (r+1)/((r+2)(2r+1)). For size r+1 the antipode must have the earliest of the three nonhub square priorities and at least one triangle priority must precede the hub, with independent probabilities 1/3 and 1−1/(2r+1). At size 2 the sequential CDF is greater than 1/(2r+3), itself greater than the static CDF. At r+1 the sequential CDF is less than (2r+3)/(3(2r+1))<1/2, and the static CDF exceeds 1/2. Thus the two outside signed mass differences are positive and the middle one is negative. Its magnitude is total variation and tends to 1/6. Taking the quotient of the two size-2 probabilities gives asymptotic equivalence to 2^r/r.

## originality

PASS

The known eight-vertex witness and its law are exactly the credited r=2 case. The distinct supported claim is the all-r enlargement with exact three-point laws, persistent crossing, TV limit and rare-size asymptotic. The inspected related results do not imply that package.

## value

PASS

This is a natural extension of the published witness, not an arbitrary finite census. It resolves whether incomparability persists when the number of identical triangle blocks grows. The rare event keeps one crossing strict despite its vanishing absolute mass, with polynomial versus exponential rarity, while the TV limit quantifies a discrepancy that does not vanish. This is useful exact information about the two ensembles, distinct from merely finding another crossing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
