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

# Verification record

The exact, reproducible checker is `verify_regular_hypergraph.py`. Run `python verify_regular_hypergraph.py` with Python 3; the only optional dependency is NetworkX for extra graph-atlas cases. The script does not import proof data or a hidden run-specific file. For every tested regular graph, it enumerates all strict coordinate-order permutations, independently obtains each Minkowski-sum exposed vertex, and compares that complete finite set against the two predicted families. It checks every predicted outer and inner squared radius, the center identity, and all candidate Euclidean diameter pairs. The seven-vertex graph-atlas tests use exact integral/rational comparisons. Observed replay: 16 admissible regular graph instances checked; all exact finite assertions passed.

The unrestricted proof is the four-step argument in RESULT.md: generic exposed coordinates; norm shell calculation; exact contact barycenter; nonnegative inner-product diameter equality and complement matching count. Finite tests are not an infinite mathematical proof. The existing Schrijver chromatic-number theorem is a cited mathematical input, not an independently reconstructed computational certificate. External independent audit and external certification have not been performed.
