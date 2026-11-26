---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Coordinate swapping pairs the quadrant walks from the two roots through length m−2 without any truncation. Their near-side defects cancel, while the only far-side contribution at length m−2 is the unique straight walk from u to the opposite short side, interpreted as the empty walk when m=2. Therefore the difference of the defect moments is exactly +1 at that length and zero earlier. Round k+1 determines the length-k defect moment from the recursion of neighbour colours. The fixed-graph unary C² rank correspondence holds: to count neighbours and non-neighbours of lower-rank unary types one uses the previous colours, adjacency/equality and the global type totals. This proves the first split, rank and stabilization bound. An independent script at /workspace/audit-evidence/5/grid.py checked all 210 pairs 2≤m<n≤22, not just the 204 cases in the attached script (whose outer loop stops at m=18). That limited coverage does not affect the proof.

## originality

FAIL

The exact same pointed result, including the first defect difference and least unary rank, follows directly from actual passages of the earlier Resultary rectangular-grid theorem and the known logic correspondence. This is demonstrated coverage, not an inference from the global depth's title or a literature-access limitation.

## value

FAIL

The pointed locality effect is well motivated, but the stated deficit identity is a linear rewrite of the exact earlier walk coefficient, and the two logical and algorithmic consequences add no independent invariant. The record leaves no distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
