---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Outside-neighbor count for absent root edge uv is d_H(u)+d_H(v); fort iff no simultaneous degree-zero and degree-one root vertices. If every root covered, minimal fort is an inclusion-minimal edge cover, hence spanning star forest; if some isolate, every nonempty fort contains a cycle, and minimality forces precisely one cycle omitting at least one vertex. Count labeled stars via exponential formula and cycles via (k−1)!/2, with unique treatment of K_2 component. Independent direct line-graph fort and proper-subset tests for n=4,5,6 produce {2:3,3:8}, {3:40,4:20}, {3:35,4:195,5:78}. Infinite proof is independent of these finite checks.

## originality

FAIL

Same triangular-graph L(K_n)=J(n,2) minimal-fort star-forest/proper-cycle classification and exact full cardinality enumerator published October 13, 2026, and repeated with strictly stronger all-fort enumerator November 2. Original source omitted both decisive earlier works.

## value

FAIL

FAIL: although exact minimal-fort enumeration is a naturally valuable invariant, it was already completely established by two earlier publications, the latter also counting all forts; the submitted support formula n>=5 is a direct routine corollary, not a new value-bearing result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
