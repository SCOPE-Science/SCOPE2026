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

Run `python verify.py` with Python 3 and NumPy. The deterministic test invokes the exact two-node derivative/norm identities, direct ring assembly, Fourier block spectra, characteristic polynomial coefficients, interior and exterior CFL probes, the resonance relation on several ring lengths, and the small/large shape asymptotics. The observed local output was `VERIFY_OK checks 1938 critical_beta 1.762747174039086 critical_nu 0.8022781617244772 resonance_verified True`.

The exact all-phase proof is in `RESULT.md`, by applying the degree-two Schur criterion to a Fourier characteristic polynomial. Finite tests cannot certify all wavenumbers and do not establish historical novelty. No independent audit has been performed.
