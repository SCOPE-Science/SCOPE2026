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

# Reproducibility notes

`verify.py` (Python 3, standard library) constructs graph-vertex automorphism groups from explicit permutations, finds their vertex orbits, and enumerates all admissible orbit-union faces using the graph-clique condition. It independently computes reduced simplicial homology over \(\mathbb F_2\) by exact binary Gaussian elimination and compares against the predicted weighted-threshold wedge multiplicities. The extraction was run and the completed output is preserved as `verify_output.txt`.

The tests cover 124 group/parameter cases, with 20,554 enumerated orbit-simplex faces, including an explicit mixed-dimensional example and a nontrivial subgroup with empty geometric fixed locus. They check sample instances only. Correctness in all sizes and integral homotopy type follows from the complete symbolic proof in `RESULT.md`; the finite checks do not establish an infinite theorem by themselves. No independent mathematical audit has been performed.
