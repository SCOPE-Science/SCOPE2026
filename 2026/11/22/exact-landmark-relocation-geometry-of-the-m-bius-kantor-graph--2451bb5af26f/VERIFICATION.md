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

Two independent executable checks use the same mathematical definitions in different graph encodings:

- `verify_gp.py`: \(GP(8,3)\) edges, witness-mask exhaustive basis test, full legal moves and all-source breadth-first searches; direct computation of the graph-automorphism action.
- `verify_lcf.py`: isomorphic \([5,-5]^8\) cycle/chord graph, direct signature enumeration, all-pairs Floyd–Warshall shortest paths and a separate automorphism backtracker.

Both enumerate all \(\binom{16}{4}=1,820\) candidate four-sets and all \(51,040\) unordered pairs of the \(320\) optimum sets. Both assert the exact diameter, degree and orbit results. Reproduce from the files attached to the same finding using `python3 verify_gp.py` and `python3 verify_lcf.py`. The supplied `verified_gp.txt` and `verified_lcf.txt` record actual passing local executions, including both completion markers.

The finite search cannot establish results for larger generalized Petersen graphs. Source searches and self-review do not replace independent audit or establish universal priority against inaccessible manuscripts.
