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

# Verification of exact harmonic spectra

Direct substitution into the cubic vector field gives the angular identity and unit-circle invariance. The proof derives an actual rigid rotation in the original physical-time variable by half-angle change of coordinates. The absolute Fourier series of a Blaschke factor, orthogonality of uniform circle characters, Parseval and a geometric tail estimate give the finite-parameter and endpoint statements analytically.

`check_spectrum.py` performs deterministic finite quadratures at four parameters and several time lags, tests both rotation orientations and compares the vector field's angular velocity with its claimed sinusoidal representation. Passing the numerical tests cannot certify the infinite Fourier series or weak convergence; these depend on the analytic steps stated in RESULT.md.

No independent validation or external certification was carried out. The claim is restricted to one observable on the exact periodic orbit with uniform physical-time phase sampling.
