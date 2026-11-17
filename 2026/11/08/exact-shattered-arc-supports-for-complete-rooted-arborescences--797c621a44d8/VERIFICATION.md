---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS: All-positive trace forces a directed branching. A putative support of n−1 arcs is a spanning arborescence and cannot realize the labeling forbidding every root-outgoing support arc while retaining others. For any branching of size at most n−2 and any positive subset P, the P-forest has t=n−|P| components and at most |S|−|P|<=t−2 blocked root attachments among t−1 nonroot components. Attach all open components directly to the root and each blocked component by an arc from one open component; the branching indegree rule guarantees every new arc avoids negative queries. The rooted-forest count det(nI−J)=k n^{n−k−1} establishes the face polynomial including n=2. Fresh exhaustive direct parent/cycle enumeration matched all supports at n=2..5 (2,16,512,65536 tested).

## originality

PASS

PASS best-of-knowledge: exact all-trace arc support theorem and all-order enumeration not implied by inspected branching optimization/packing or vertex-neighborhood VC results.

## value

PASS

PASS: Full face-by-face shattering classification of a canonical connectivity-constrained directed concept family is a natural combinatorial invariant; the all-trace property reduces to precisely two branching checks and a tight global size cutoff and yields an exact count of all faces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
