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

A factor of period p and length 2p+1 is exactly an overlap, with p=1 testing triples. The search is exhaustive: every shorter prefix of a valid word is valid, and when appending a symbol only factors ending at the new symbol can become invalid. The displayed period limit should use the length of the extension, rather than |v| if v denotes the old prefix in that sentence; the actual code correctly uses the new length. The last-square recurrence counts disjoint choices of a final cut and hence ordered factorizations, not just existence. The block-based proof is also exhaustive: any eligible block has root length at most 16 since eight other squares use at least 16 letters, and no partial product with an overlap or insufficient length budget can extend to a candidate. My independent replay used left extensions with a full overlap check (runs of p+1 equalities at shift p) and forward DFS over all viable cuts into exactly nine squares. It checked 7,867 overlap-free words including the empty word, 416 at length 48, and reproduced no shorter solution, the exact two claimed words at length 48 and one factorization each with root-length sequence (3,2,2,2,6,2,2,2,3). The strings are both complements and reversals of each other.

## originality

FAIL

Shallit supplies the ten-square theorem and one length-48 witness, not the asserted minimum or equality classification. However, two distinct indexed records cover that complete classification under the same hypotheses: 52c025fc067a explicitly states the exact finding as k=9, and fc9c72e08d71 covers it in a much larger length census. This is exact coverage in the indexed corpus, not a claim of earlier historical priority.

## value

FAIL

Minimizing the length at the natural nine-square extremal threshold is a worthwhile question, but the exact answer and uniqueness assertions are already covered by stronger available classifications. The frozen result establishes no additional extremal property beyond those classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
