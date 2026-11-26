---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With at most two pebbles, after a move there is at most one stationary vertex to match, and every vertex on a board with both sides at least two has a neighbor and a distinct nonneighbor. For equal capped parameters at k>=3, after removal of a pebble at most k-1 coordinates on each axis are in use. Matching each axis by its own partial bijection preserves equality and sharing a coordinate; a fresh paired value exists on a small axis by exact equal sizes and on a large axis because its size is at least k. This works for arbitrarily many rounds. A clique of size at least three must share one coordinate, and an independent set changes both coordinates in every pair; maximum sizes are max(a,b) and min(a,b). Clique and independent-set formulas with up to k variables recover both truncated sizes. Counting the unordered truncated pairs, minimizing their products within a class, and enlarging a largest side to witness non-definability below max(a,b)+1 give all stated corollaries. This is a relative width, not a defining width among all graphs. The frozen scripts and stdout are bounded corroboration inspected but not executed; the permanent strategy is the universal proof. The extensional checker prunes subsets and does not independently exhaust every clique for the common-coordinate assertion.

## originality

FAIL

The distinct Resultary mixed-alphabet Hamming theorem 808bb86c4b0b directly covers the full frozen statement with precisely its language, width and depth, by taking two factors. The numerical and hierarchy corollaries follow mechanically as well. The theorem is correct but covered; this decision does not infer authorship or priority merely from catalogue dates.

## value

FAIL

The invariant and family are natural, and the clique/independence proof is a clear elementary explanation for rectangles. But the submission's mathematical claims are a direct two-factor specialization, with only mechanical consequences for counts, minimum order, defining width and width hierarchy. It does not establish a distinct structural lemma or other worthwhile unresolved fact beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
