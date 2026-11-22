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

# Verification

The analytical proof in `RESULT.md` establishes strict convexity, global edge-by-edge uniqueness, the tree cut coefficients and the three-phase minimizer. The all-integer cutoffs are certified by four polynomial sign identities in \(h=m-3\) (each coefficient uniformly signed) and direct small-branch substitutions.

`VERIFY.py` is a standalone companion using Python, SymPy and NumPy. Execute `python VERIFY.py` in the directory containing this package. It symbolically reconstructs the two cubic polynomials and proves the sign-list certificates by exact algebra; it then tests finitely many parameter values, compares weighted-tree reciprocal eigenvalue sums with direct spectral calculations, and tests a feasible asymmetric perturbation. Its expected diagnostic output is `PASS symbolic all-integer cutoff certificates and 322 finite diagnostics`. A finite numerical run does not independently certify all integers or literature novelty.

No independent mathematical audit, external proof assistant or external scientific validation is claimed.
