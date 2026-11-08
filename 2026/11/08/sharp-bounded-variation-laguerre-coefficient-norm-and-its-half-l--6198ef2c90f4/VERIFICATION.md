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

The standalone `CHECK.py` uses only Python, SymPy, SciPy, and NumPy. It checks the primitive identity, associated differential equation, and exact Sonin derivative symbolically for degrees 1--12; evaluates the actual finite-degree maximizers at all Laguerre roots and compares them with the two nearest to \(1/2\) for degrees 1--100; confirms the exact envelope upper bound there; and checks the limiting envelope numerically at degrees 100, 200, 400, and 800. These tests are finite and do not certify the universal result. The universal result follows from the exact algebraic identities and DLMF compact-uniform Plancherel--Rotach asymptotics. The constants and range of normalizations are stated in `RESULT.md`.

The relevant 2023 piecewise-Laguerre source was not accessible in full text, and an equivalent older derivation under different terminology remains possible. No independent mathematical audit was conducted.
