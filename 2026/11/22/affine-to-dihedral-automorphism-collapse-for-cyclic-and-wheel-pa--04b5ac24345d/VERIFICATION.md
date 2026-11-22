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

# Finite reproducibility checks

Run `python3 verification.py` using Python 3. The program enumerates **all** vertex permutations for the cycle sizes \(3\le n\le8\) and wheel rim sizes \(5\le n\le7\), tests whether each permutation preserves equality of positive distance classes, and compares the accepted sets to explicit affine and dihedral vertex permutation families. This directly checks the nontrivial finite normalizer assertion for each selected case, rather than merely comparing their cardinalities. The output terminates with `AFFINE_DIHEDRAL_METRIC_NORMALIZERS_VERIFIED` when successful.

The structural proof that every abstract automorphism is spatial, and the unrestricted cycle and wheel classifications, are mathematical arguments in `RESULT.md`, not conclusions inferred from the finite checker. No independent audit has been performed. The source comparison does not establish historical uniqueness.
