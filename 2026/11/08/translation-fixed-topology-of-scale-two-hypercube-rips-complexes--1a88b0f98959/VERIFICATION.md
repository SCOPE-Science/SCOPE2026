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

# Reproducibility and limits

The standalone Python program `verify.py` enumerates all binary linear subspaces in dimensions two through six, omitting only the identity subgroup. It creates the vertex orbits directly, tests orbit diameters, constructs edges by checking all cross-coset pairs, and tests for triangles. For cyclic subgroups it compares the graph with the ordinary smaller hypercube by graph isomorphism; for rank-two admissible subgroups it checks that the fixed orbit complex is a discrete set of the exact predicted size. For forbidden subgroups it checks that the fixed locus has no orbit vertices. The program additionally tests every one-dimensional subgroup with a word of weight one or two in dimensions seven and eight.

Output: `ALL_VERIFY_OK`; cases: 3,346. The output is saved as `verify_output.txt`. Reproduce with `python verify.py` after installing `requirements.txt`. Computation is finite and supports but does not prove the all-dimensional theorem. The symbolic proof identifies the coset graph and handles all dimensions and translation subgroups.

The theorem gives geometric fixed-point spaces, not homotopy fixed points in the mapping-space sense. It does not assess independent mathematical validation; such an audit has not been performed.
