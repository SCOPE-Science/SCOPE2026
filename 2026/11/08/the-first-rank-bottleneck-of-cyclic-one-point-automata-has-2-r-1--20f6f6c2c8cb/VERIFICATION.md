---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The rank and word-count assertions were independently tested using the subset power automaton. The accompanying `verify.py` runs exact BFS over reachable nonempty image subsets for each \(5\le n\le14\), \(2\le r<n/2\); it checks 130 target-rank thresholds, including the shortest path multiplicity for each. Constructive witnesses were replayed in 6,138 cases for \(2\le r\le11\). All tests passed. These finite runs do not prove the universal result.

To reproduce: `python verify.py` (Python 3 standard library only). The proof's critical nonstandard step is the explicit co-moving-hole update, not the observed finite data. For \(T\le2r<n\) the timestamp representation is injective, and a letter \(b\) either adds occupancy at time \(t\), moves it from time \(t-r\) to \(t\), or is ineffective. This yields both the \(T\ge2r\) lower bound and complete equality classification.

Independent scientific audit and independent validation have not been performed.
