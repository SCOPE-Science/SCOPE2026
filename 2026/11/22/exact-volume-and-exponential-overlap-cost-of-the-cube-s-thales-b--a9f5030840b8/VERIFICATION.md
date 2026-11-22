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

# Verification of the cubical Thales-ball volume theorem

Execute `python verify_thales_volume.py` using Python 3 (only its standard library is needed). The verifier expands the positive half-normal moment coefficients, checks exact values \(U_1=2\), \(U_2=2+\pi\), \(U_3=2+4\pi\), \(U_4=2+10\pi+\pi^2\), and \(U_5=2+20\pi+41\pi^2/6\), solves the defining Gaussian saddle equation, checks its variance and growth base, and compares exact finite volume ratios with the leading asymptotic at dimensions 16, 32 and 64. A separate deterministic angular quadrature checks the two-dimensional radial integral, and a seeded Gaussian-direction Monte Carlo check tests the three-dimensional radial integral.

The finite integrations have numerical tolerances and the asymptotic checks are finite-dimensional corroboration only. Neither the geometric set identity, the exact all-dimensional coefficient identity, nor the asymptotic theorem follows merely from passing these tests. Their arguments appear in `RESULT.md`.
