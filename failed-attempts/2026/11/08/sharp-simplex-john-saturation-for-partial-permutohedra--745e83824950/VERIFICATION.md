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

The simplex envelope has center S/(m+1)1 and covariance S²/[m(m+1)](I-J/(m+1)); subset-indicator support is S/(m+1)[s+sqrt{s(m+1-s)/m}]. For m>=n, direct comparison with B_s=s(2n-s+1)/2 is valid for every cardinality; strict support yields only lower and total contacts for m>n, with singleton upper touches at m=n. For 2<=m<n, max coordinate=2S/(m+1)>n so the simplex ellipsoid cannot be the John ellipsoid. Unique enclosing-simplex optimum yields strict volume loss, with m=1 an interval exception. Independent exact rational support checks on (m,n)=(1,5),(2,4),(3,3),(6,3),(12,8) matched the boundary.

## originality

FAIL

Already covered exactly by published October 18 full all-parameter partial-permutohedron John ellipsoid theorem. That earlier primary RESULT explicitly states the same simplex-envelope ellipsoid for m>=n, the identical m=n contact transition, same volume from shape matrix, and treats the complementary capped-cube regime. The current threshold iff m=1 or m>=n is an immediate restriction of this strictly stronger theorem, not a new formulation.

## value

FAIL

The sharp transition is a natural geometry question, but its complete answer and contacts are already in the stronger published all-parameter classification. No new independent mathematical gap or non-implied invariant survives; an alternate elementary proof and finite checks do not create scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
