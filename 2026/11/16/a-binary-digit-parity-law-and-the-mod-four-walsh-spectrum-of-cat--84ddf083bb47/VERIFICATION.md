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

# Reproducible mathematical checks

Run `python verify_dyck_fourier.py` in a standard Python 3 environment; there are no third-party dependencies.

The checker separately counts up-steps by integer path dynamic programming for every coordinate in semilengths \(1\) through \(100\), with the proposed parity interval computed only from the binary digits of \(n+1\). It also generates all Dyck incidence vectors through semilength \(10\), calculates complete unnormalized integer Walsh transforms, and compares every multiplier with the predicted residue modulo four. Total exhaustive Fourier positions checked: \(1{,}398{,}100\). Its successful output is `DYCK_POSITION_PARITY_AND_MOD4_PASS all_positions_n_le_100 exhaustive_fourier_coefficients 1398100`.

Finite tests do not prove the infinite assertion. That proof is the marked-path generating-function identity and characteristic-two coefficient extraction in `RESULT.md`. The checker does not establish novelty, complete rank, exact nonzero magnitudes, or independent validation.
