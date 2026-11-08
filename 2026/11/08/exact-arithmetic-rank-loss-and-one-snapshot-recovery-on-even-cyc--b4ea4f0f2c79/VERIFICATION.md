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

The standalone `CHECK.py` uses exact rational arithmetic to build the normalized nearest-neighbor evolution on every even cycle with half-order between 2 and 11. It tests all 120 nonzero sensor separations at horizons \(m\) and \(m+1\). It independently computes Gaussian-elimination ranks and compares them to the two rank formulas. It also checks 80 absolute determinant identities at the minimal horizon. The program terminated with `CHECK_OK exact_ranks= 120` and no assertion failure.

The proof for arbitrary cycle length and any injective spectral filter is based on Fourier eigenspace visibility, nonzero Vandermonde minors, and explicit zero constraints. Finite arithmetic experiments are not used as an infinite-family proof. The prior literature comparisons are same-model only, and independent mathematical and priority audits have not been performed.
