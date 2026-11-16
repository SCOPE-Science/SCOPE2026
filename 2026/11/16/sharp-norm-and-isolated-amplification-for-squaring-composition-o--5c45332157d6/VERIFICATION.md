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
# Reproducibility and scope

Reconstruct the canonical norm from its reproducing kernel, rather than from a merely equivalent atomic Dirichlet norm. The proof in `RESULT.md` derives the even/odd exact isometric decomposition, the block operator \(L\), its essential norm, and the unique eigenvalue \(\lambda_*>4\) of \(LL^*\). The displayed rational extremizer is the adjoint image of the decaying eigenvector.

Execute `python CHECK.py` to test the cubic root, the explicit source-to-target squared-norm ratio, Taylor-coefficient eigen-relations, finite partial sums, and weakly-null approximate shift vectors. The checker requires only standard Python and prints its actual number of passed finite checks. No finite truncation, numerical test, or source-search absence is used as an infinite-dimensional or global novelty certificate.

The exact assertion applies only to the canonical \(\mathcal H((1+z^2)/2)\) norm and squaring self-composition. External independent mathematical review and exhaustive publication-priority verification were not performed.
