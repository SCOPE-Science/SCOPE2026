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

The stated law is correct. After a first vertex a_i, either a second A vertex takes color 1 before b_i, forcing a two-color side partition, or b_i closes a paired color 1 (probability 1/n). At least two interposed B vertices force exactly three colors. Zero or one interposed vertex has combined probability 3/[2(2n-1)] and gives one plus the smaller crown color count. The frozen proof's literal uniform-order assertion for one interposed vertex is false: the induced order is uniform conditional on starting on side B. The side-exchange automorphism gives precisely the same color-count distribution conditional on either starting side, so it justifies the recurrence without changing the claim. The n=2 base is two disjoint edges; maximum degree yields the bound n. The factorial expression follows by splitting odd/even factors; the tail ratio is at most 2/7 for the relevant m=n-k+3≥4, bounding the remainder after the first two terms. Independent direct permutation counts for n=2,3,4,5 agreed, including (2903040,574560,108000,43200) for colors 2 through 5 at n=5. Replay: /workspace/branches/b72df666-d704-4f8f-b5e8-83e6f97d7207/direct_crown_check.py and direct_crown_check.log. The frozen memoized n≤7 output was inspected, not executed; bounded checks do not certify the infinite law.

## originality

FAIL

A distinct indexed record demonstrably covers the full same exact law, extremal count, and expansion, with a partial-order proof. This is a rejection for equivalent coverage, not an inference that the overlapping record predates the frozen work or that Ye et al. proved the exact law.

## value

FAIL

The complete crown law is a useful benchmark and advances the motivating upper bound, but the full benchmark already exists as an indexed exact finding. There is no distinct quantitative or structural claim left in this submission once that overlap is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
