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
# Verification evidence

`verify.py` is a standalone Python 3 script. It generates the graph independently from the adjacency rule, checks face membership through all subsets for \(m,n\in\{2,3,4\}\), and computes simplicial boundary ranks over the prime field of order 1009. It then constructs the barycentric subdivision of each original independence complex (not the proposed graph spine), passes to orbit chains of several genuinely generated finite groups, and compares their calculated quotient Betti numbers against the separate graph-spine orbit prediction. The group examples cover independent cyclic permutations, diagonal cyclic and symmetric actions, pure coordinate swap, swap plus diagonal rotation, and full natural symmetry for sizes up to four.

The same script evaluates the explicit barycentric-coordinate retraction in exact rational arithmetic on sampled simplices, confirms idempotence and full permutation equivariance, and checks the induced signed trace formula on every permutation of degrees two through six. The recovered output from the executable is:

`ALL_VERIFY_OK cases= 60 independence_faces= 369 barycentric_quotient_cells= 7038 local_retraction_checks= 104384 swap_character_checks= 872`

This establishes a finite reproducibility check of central formulas; it does not replace the unrestricted mathematical proof. Integral torsion-freeness, every-subgroup fixed-point descriptions, continuity across all real coordinates, and general-group statements are proved in `RESULT.md`, not by finite experimentation. The first-public-source date is taken from the original public posting of arXiv:2601.13432 rather than a journal or revision date.
