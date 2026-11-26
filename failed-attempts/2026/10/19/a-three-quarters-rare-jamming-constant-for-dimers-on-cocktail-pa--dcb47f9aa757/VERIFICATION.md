---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With independent identical continuous edge priorities the next accepted edge is uniform among the edges on uncovered vertices, by deferred exposure of the permutation. For p intact forbidden pairs and s singletons the counts of the three unordered endpoint types are binom(s,2), 2ps and 2p(p−1) and exhaust the eligible edges. An even uncovered set of size at least four always has a feasible edge; at size two it jams exactly for a deleted pair. A given intact pair has 2(m−2) incident eligible edges at size m; the one-step survival bounds telescope to (1). Two specified intact pairs have 4m−12 incident eligible edges; summing the exponential bound over even m gives the stated harmonic factor and E[Q_k(Q_k−1)]=O(k⁴/n²). With exactly one pair left the telescoping survival product equals 3/(4k²−1). Bounding the probability of two or more intact pairs by half the factorial moment gives (3); the main term is 3/(4n), and k=floor(n^(1/5)) balances 1/(nk) and k⁴/n². The expectation of the uncovered fraction is P_n/n. Independent exact recursion on labeled subsets reproduced P_2 through P_5 and computed P_6=562248/6062875 and P_7=634107503/7766542875; replay with python3 /workspace/branches/d8630442-8c97-4819-862c-7b8a4e34c368/subset_dp_check.py. The supplied verification files were inspected, not executed; the bounded table does not establish the limit.

## originality

FAIL

A distinct indexed record on precisely the same random process gives the identical finite recurrence and table and a stronger finite error bound for the same 3/4 constant. Two broader catalogue results also cover the matching-deletion case. This decision concerns substantive coverage at review, not historical priority: the overlapping catalogue entries are later-dated than the frozen one.

## value

FAIL

The rare failure probability on this dense natural graph is a worthwhile invariant: a limiting matched fraction of one misses it. Relative to the exact recurrence, identical table and sharper law now covering it, however, there is no additional independently useful claim. The original proof shares the intact-pair survival mechanism and gives a weaker error, not a substantively new scope or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
