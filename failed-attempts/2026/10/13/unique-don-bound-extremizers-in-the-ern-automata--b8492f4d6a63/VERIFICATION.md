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

FAIL

The statement is true, but the frozen lower-bound proof (RESULT.md line 34) does not establish its greedy induction. At the first admissible inverse b step, an exact predecessor may replace 0 by n−1 without growing; the proof does not exclude following such a step and growing later from a different set. The upper bound and the strict bound for noncanonical sets both follow from the least cyclic boundary and are correct. The lower bound can be independently established by full inverse images: starting from S_k, any word reaching it exactly has full inverse image Q. Until Q is first attained, a nonempty proper cyclic interval remains an interval. An inverse a moves its first point back by one; a growing inverse b requires its first point to be 0 and moves it to n−1; a shrinking inverse b removes only its last point (and an empty set cannot return). Hence before the first growth and between each pair of growths there must be at least n−1 inverse rotations. At least n−k growths are needed, proving the asserted lower bound. The word (ba^(n−1))^(n−k) reaches S_k by the verified extension identity. Independent bit-mask BFS (python3 /workspace/branches/independent_checks.py 1) checked every nonempty subset and each unique maximizer for 2≤n≤12; this is not the all-n proof. No revision is submitted because the theorem is already covered.

## originality

FAIL

A distinct earlier Resultary theorem supplies exactly the same distances and equality cases upon complementing the target. The full inverse-action normal form, not just the similar numerical bound or a guess about avoiding vs reaching, makes the reduction valid for every target.

## value

FAIL

A sharp layerwise equality classification would be useful for exact-image reachability, but here it is already mechanically available by complement and the prior shortest-avoider normal form. This restatement, with no new distance or invariant beyond the prior result, does not meet the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
