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

The mathematical evidence is the explicit stationary renewal representation, an integrable dominated-convergence envelope for every fixed nonzero excursion threshold, and positive-integrand asymptotics for the exact mixed-moment boundary. These establish the claims for all admissible parameters without relying on numerical samples.

To repeat finite consistency tests, execute `python verify.py` using Python's standard library. The script evaluates two independently parametrized normalizing integrals, exact stationary event probabilities for multiple particle numbers and excursion shapes, and the conditioned Rayleigh-moment limit. Its test tolerances and bounded sample ranges are declared in the code. Finite checks cannot certify an infinite-limit theorem, and independent validation has not been performed.
