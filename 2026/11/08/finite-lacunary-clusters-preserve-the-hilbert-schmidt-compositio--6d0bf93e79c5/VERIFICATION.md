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
The proof is analytical. The critical step is a Toeplitz-block compression of multiplication by \(h=(\varphi-\varphi(0))^k\) from exceptional coefficient clusters into good coefficient clusters. The finite block has diagonal \(h_\ell\ne0\); off-diagonal cross-cluster blocks form a Hilbert–Schmidt remainder because lacunary differences have uniformly bounded multiplicity. This gives a tail lower bound and recovers the missing energy from finitely many shifted powers of the symbol. The other direction follows from a monotone lacunary charging estimate, and failure of the threshold is witnessed by an outer-modulus construction and the finite-union Paley inequality.

Run the included `check_clusters.py` with Python 3. The checker prints `LACUNARY_CLUSTER_EXACT_BLOCK_CHECK_OK 1518` after checking the exact triangular Toeplitz block relations, leading coefficients, good-row separations, finite difference-multiplicity bounds and truncated convolution examples. No third-party Python libraries are needed. These finite checks do not verify the infinite-dimensional compactness statement, the outer-function existence theorem, or publication originality; those require the mathematical arguments and literature comparisons in `RESULT.md` and `REVIEW.md`. Independent validation has not been performed.
