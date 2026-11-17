---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: a rooted alternating matrix has rank rank(A) or rank(A)+2 according to whether the root row lies in Row(A); the direct sum criterion factorizes for t squares. A deleted-root three-path gives P=1+q(q²-1)z and Q=q²+q²(q²-1)z; the character count over odd F_q is q^{3t+1-2r} per rank-2r central form. The total mass is q^{4t} and the degree-square sum is q^{7t+1}. Fresh direct finite-field enumeration confirmed every q=2,3 t=2 specialization. The analytic argument—not these finite checks—covers arbitrary q,t.

## originality

FAIL

FAIL: an earlier arbitrary one-vertex bipartite rank-gluing theorem and its explicitly evaluated two-4-cycle case cover the full t-square bouquet by induction; the Lie-character conversion is established background.

## value

FAIL

FAIL: an all-parameter character table for a canonical cactus is potentially useful, but here it is a direct previously implied rooted-gluing specialization plus routine Kirillov/Heisenberg conversion, not a previously unknown natural invariant requiring new mathematical work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
