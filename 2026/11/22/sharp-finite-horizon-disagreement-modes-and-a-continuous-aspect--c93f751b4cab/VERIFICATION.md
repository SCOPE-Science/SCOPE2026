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

# Verification and reproducibility

Running `python check_gossip.py` under a standard Python 3 interpreter requires no third-party modules, files, or network access. The observed output contains `PASS 17019 total checks including asymptotic spectral-root tests`.

The checker uses rational arithmetic to construct full pairwise orthogonal-projection matrices, evolves complete covariance matrices and separately evolves the claimed three-coordinate recurrence. It compares their entries across nine horizons for several shore pairs, then verifies ordering and improvement for hundreds of additional rational parameter/horizon combinations. It separately verifies the claimed limiting spectral equation and convergence estimates numerically.

The all-horizon and all-size proof consists of the covariance decomposition, coupled reset-ordering lemma, positive-matrix Perron argument and the explicit perturbation limits in RESULT.md. The checker does not independently certify an infinite mathematical theorem or publication priority. The external audit status in the front matter records that no independent audit has been performed.
