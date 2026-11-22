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

Run `python verify_eight_caps.py` using NumPy and SymPy. The program independently constructs the cap-axis parametrization and its angular even moments, checks exact full-sphere norms, derives all three concentration eigenvalue branches, verifies the three difference factorizations, the unique radical crossing, and the thin-cap limit.

The program additionally constructs all seven cubic harmonic basis functions and performs direct 7-by-7 Galerkin integration over all eight caps for six apertures (including the tangency threshold and the crossing). Its 14-point Gauss–Legendre polar and 32-point angular quadratures agree with the exact diagonal spectrum at absolute error below \(5\times10^{-12}\), including off-diagonal entries; the trace checks independently match the area fraction \(4(1-h)\).

These finite numerical tests are consistency checks, not an infinite proof. The exact symbolic identities plus the proof in RESULT.md establish the stated result for the full continuous interval. The program does not assess global publication priority or provide independent mathematical certification.
