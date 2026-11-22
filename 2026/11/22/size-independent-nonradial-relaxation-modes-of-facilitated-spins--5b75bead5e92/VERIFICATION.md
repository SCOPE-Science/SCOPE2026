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

# Verification record

Run `python verify_fa_biclique.py` with NumPy and SciPy. It independently constructs the \(2^m\)-state single-shore heat-bath operator and a full \((2^{m+n}-1)\)-state active FA-1f generator. It checks the unique subunit eigenvalue against the secular equation and verifies the constructed product-contrast eigenfunction directly in the full matrix action for 35 triples. The maximum allowed residual is \(2\cdot10^{-9}\); all 35 checks passed in the local run.

The code does not certify every integer or real parameter: that universal assertion follows instead from the rank-one secular equation and exact invariant-subspace proof. Full spectral-gap equality, finite-time total-variation mixing, and independent validation are not established.
