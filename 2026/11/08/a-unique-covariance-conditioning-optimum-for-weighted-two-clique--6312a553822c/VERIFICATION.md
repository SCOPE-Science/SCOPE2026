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

# Reproducible checks and scope

From the extracted finding directory, run `python3 artifacts/verify.py` (Python 3 standard library only). It builds all acyclic-orientation vertices by restricting global vertex permutations to both cliques, without using the independent-clique formula in the construction. The program removes duplicate vertex vectors and checks that their count is \(a!b!\); it then evaluates the vertex covariance using exact fractions and compares every matrix entry with \(uL_{K_a}+vL_{K_b}\). It tests contrast eigenvectors, an exact principal minor/pseudodeterminant identity, and a grid of exact instances of the global ratio-penalty identity.

Successful replay on the packaged source reports:

`TWO_CLIQUE_WEIGHTED_COVARIANCE_CHECKS_PASSED profiles=6 vertices=2068 covariance_entries=217 tuning_profiles=1014`

The finite profiles include both clique sizes equal and unequal, and two different positive weights. They are not exhaustive for all sizes or real weights; the exact spectrum and the global minimizer follow from the rank-permutation, invariant-subspace and algebraic proofs in `RESULT.md`. No machine-formal proof, expert validation, or independent mathematical audit is claimed.
