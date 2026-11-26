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

The formulas and classifications are correct. In the constrained range, a missed shore forces every vertex of the other shore to be selected, violating capacity. The frozen proof's singleton sentence is incomplete: if S={j} then b_j is undominated when j is not in T; if j is in T, the selected b_j instead has n−1 neighbors outside, also impossible. Thus both sizes are at least two. In the intersecting case a selected matched pair imposes both sizes at least q=n−k, which is sufficient regardless of intersection; in the disjoint case both sizes must be at least max(2,r) for r=q−1, which is sufficient when disjoint supports fit. This gives 2r only for r≥2 and 2r≤n. Otherwise either r=1 or disjoint supports are infeasible, so precisely the arbitrary q-by-q choices minimize. For k≥n−1 no singleton or same-shore pair dominates, and a cross-shore pair dominates exactly when its indices agree. Independent finite profile checks for n=3..50 (1,224 cases), and direct adjacency enumeration for n=3..6 (14 cases, 5,440 distinct subsets), agreed. The independent check and replay are branches/crown-check/verification/verify.py and replay.txt; the original verification/verify.py and verification/replay.txt were inspected, not executed. The frozen profile code shortcuts k=n−1, and its comment about singleton shores is too broad; only the direct small-graph branch tests that endpoint independently. The arbitrary-n argument does not depend on any replay.

## originality

FAIL

The nontrivial content is covered by a distinct indexed result: the November 8 crown capacity profile states the same constrained minima and counts and moreover enumerates all feasible sets. This is a finding of equivalent/stronger current coverage, not a claim that the November record predates the assigned record or establishes historical priority. The only unmatched regime is the elementary ordinary-domination endpoint, which is not a substantive distinct remainder. The October 13 partial matching-deletion result also covers the k=n−2 slice; same-day dating gives no order. No repair is justified merely by correcting the singleton argument or citation.

## value

PASS

The constrained threshold and optimum classifications are intrinsically useful mathematical information about matching deletion from the standard biclique. The ordinary-domination endpoint on its own is routine and would not justify a narrower finding. The substantive classification does not survive the independent originality comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
