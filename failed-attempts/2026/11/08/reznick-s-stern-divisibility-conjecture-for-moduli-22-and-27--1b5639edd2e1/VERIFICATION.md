---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The transition pair (s(n),s(n+1)) evolves by (a,a+b)/(a+b,b), preserving gcd(a,b,d)=1. Primitive state counts are 360 for 22 and 648 for 27, so the block diagonal exact integer operator has dimension 1008; Cayley–Hamilton makes the first 1008 zero differences sufficient for every r≥0. Independently recomputed all 1008 integer levels from the primitive transition maps; exact counts coincide and SHA-256 of newline-delimited common sequence is e7ca1f54991a09ebd233ffc4a45d8d30cfb2e37be2337307e037ddb3a924bd8d. The r=0 count includes s(0)=0. The infinite conclusion is justified by the recurrence, not extrapolated from a finite test. The certificate is reproducible but no symbolic 1008-state characteristic polynomial was requested or established.

## originality

FAIL

The October 18 published complete Stern 22–27 theorem proves exactly T(2^r;22)=T(2^r;27) for every r≥0, and a strictly stronger rational generating function for common dyadic block counts. Its inspected 36+36 projective-state recurrence proof has 72 exact base terms, so the new raw 360+648-state certificate establishes no surviving original claim.

## value

PASS

Resolving Reznick’s explicitly stated 22–27 conjecture is a mathematically meaningful target and the exact finite-state certificate is correct; this does not overcome complete earlier scientific coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
