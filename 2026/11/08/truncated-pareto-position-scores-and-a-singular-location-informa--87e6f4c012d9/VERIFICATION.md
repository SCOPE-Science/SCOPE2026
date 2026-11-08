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
# Independent check instructions and scope

Run `python verify_score.py` with Python 3, SciPy and NumPy. The observed result from the packaged script is `47 tests passed`, with the quoted critical Hellinger ratio sequence.

The script independently computes the Lambert-profile \(u(x)\), verifies the continuum gas flux residual and mass, checks the probability normalization and five score moments on several parameter choices, and numerically measures the Hellinger transition at the marginal cusp. A finite test grid cannot certify all positive parameters or the small-shift limit. Those statements are addressed by the explicit pushforward, integration and translation-cusp proofs in RESULT.md. No experimental or independent replication certification has been performed. The metastable stationary gas is a mean-field branch, not a finite-particle probabilistic limit theorem.
