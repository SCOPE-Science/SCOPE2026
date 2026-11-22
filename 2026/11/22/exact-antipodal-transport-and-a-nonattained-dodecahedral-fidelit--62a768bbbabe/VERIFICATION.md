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

# Reproducibility and verification boundaries

Execute `python verify_spectral.py` and `python verify_coordinates.py` with compatible SymPy, NetworkX and NumPy. The first program builds the graphs through a named graph library, then verifies the complete exact eigenspace projectors including an explicit witness for all 282 unordered non-antipodal pairs. It also checks the two exact stationary-point polynomials and 16 Pell convergents; the infinite Pell identity is independently established in RESULT.md by a quadratic-unit norm argument. The second constructs graphs from exact Cartesian coordinates, checks spectra independently, and uses numerical diagonalization at three sample times only as corroboration.

The exact dodecahedral result additionally requires the analytic irrational-torus density argument and endpoint-convexity optimization given in RESULT.md. Finite tests alone do not prove the density limit, and the closed-form proof is indispensable. The finite exhaustive projector assertions are proved by exact exhaustive finite computation with transparent algorithms. No unverified external result is used as a computational certificate.

Independent validation has not been performed.
