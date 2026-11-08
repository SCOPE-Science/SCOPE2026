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

The proof of the all-direction threshold and asymptotics uses the exact Fourier product formula and finite trigonometric-polynomial averaging, with the nonzero-frequency integrals controlled by Dirichlet's test/integration by parts. The finite residue formula is calculated independently using signed exponential sums and the expansion of squared sines.

Execute `python verify.py` in the same directory as this file using the Python 3 standard library. The execution returned `FOURIER_CUBE_CRITICAL_RESIDUES_OK 7198`. The script checks all positive integer triples with coordinates from 1 through 12; all positive integer tuples of lengths 1 through 6 with coordinates from 1 through 4; and periodic quadrature examples. It does not establish the theorem for arbitrary real frequencies; that follows from the analytic argument in RESULT.md.

All asymptotics are fixed-direction statements. The error at the critical exponent may grow near a resonance. No independent mathematical audit or external certification has occurred.
