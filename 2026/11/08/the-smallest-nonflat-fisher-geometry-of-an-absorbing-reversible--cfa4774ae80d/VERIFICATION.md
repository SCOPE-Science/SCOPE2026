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

## Reproduction

Run `python check.py` with Python 3 and SymPy. This standalone program independently propagates exact rational transition probabilities for both graphs for 64 successive times and 25 weight pairs per graph, compares the results to the claimed closed-form masses, and checks Fisher identities and curvature by symbolic differentiation. The extracted-package run returned `PASS: 3296 exact rational/symbolic checks`.

The infinite-time results do not depend on finite enumeration: the proof in `RESULT.md` derives the entire law through a Bernoulli/geometric renewal decomposition and computes the metric by exact expectation. The rank and curvature hold for all strictly positive edge weights, with no numerical extrapolation. The graph-size minimality uses the exhaustive list of connected simple undirected graphs on at most three vertices (path and triangle), not a truncated computational census. The Python checker is supplemental and assumes SymPy for the symbolic curvature step; the calculus identities are independently displayed in `RESULT.md`.

No independent mathematical audit has been performed. Historical-priority risk remains for any unlocated older graph-specific curvature analysis.
