---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The four-subsequence dynamic recurrence counts all 16 patterns exactly and the independent direct four-index combination algorithm agrees at the explicit 14-bit witnesses. Independently enumerated every 2^13=8192 and 2^14=16384 binary word, obtaining respectively 8176 and 16328 exact integer four-deck fibers; no mixed R<=2 vs R>2 group at n=13, exactly one mixed group at n=14: x=01111100111110 (two 1-runs) and y=10101111110101 (five). Each has the displayed common 16-vector summing to C(14,4)=1001. Four-deck equality implies three-deck equality by the exact double-counting (n-3) formula, and leading-zero padding preserves four-deck equality and one-run categories; thus no shorter n>=4 collision, and collisions at every n>=14. Angal et al. Thm 1.3 proves the separate r(B2)<=5 upper bound; the new witness proves lower bound. Verified full enumerators from actual package; complete finite enumeration here is exhaustive for 13,14 only, not for all lengths.

## originality

PASS

Best-of-knowledge matching theorem search found no logically dominating already published result after comparing actual statements; relevant uninspected primary literature and older methods are recorded as residual risks.

## value

PASS

The exact first cross-class collision is a natural minimum-length obstruction for unrestricted recognition of bounded one-run classes, and the complete first-boundary fiber census proves sharpness of a previously only upper-bounded reconstruction order. The finite boundary is mathematically motivated by the published r(B2)<=5 bound; the explicit single pair and zero-padding give an exact reusable witness. No claim of all-long-length census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
