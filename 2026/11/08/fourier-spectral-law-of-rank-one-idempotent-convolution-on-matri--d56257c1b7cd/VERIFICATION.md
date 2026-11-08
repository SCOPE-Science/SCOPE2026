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

Run `python3 verify_idempotent_spectrum.py` from this package's directory. It requires Python 3 and no third-party libraries. The program enumerates and checks exact residue classes of additive Fourier coefficients, exact finite-field geometric eigenspaces, Gaussian mixed factorial moments, and finite inversion probabilities; it ends with `IDEMPOTENT_FOURIER_JOINT_MOMENT_CHECKS_OK`. The tested pairs are (2,2), (2,3), (2,4), (3,2), (3,3), with complete direct coefficient testing except (2,4). The exhaustive finite calculations neither prove all dimensions nor verify the infinite-dimensional limit; those are addressed by the algebraic arguments in `RESULT.md`. No independent validation has been undertaken.
