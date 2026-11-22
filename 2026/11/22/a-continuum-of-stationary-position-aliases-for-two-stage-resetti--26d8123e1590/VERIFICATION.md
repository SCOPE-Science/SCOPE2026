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

# Verification and scope

The included `verify.py` executed successfully and reported `PASS ... checks= 192`. It uses separate quadrature of the Brownian heat kernel weighted by the Erlang survival function, of the endpoint kernel weighted by the Erlang event density, and of the return local-time kernel for four return exponents at three positive positions and three diffusivity-rate pairs. It independently evaluates the limiting example, the exact radial moment/CDF formulas, the total variation formula and phase-dependent inverse recovery. The three general moment formulas are also tested symbolically with SymPy. Quadrature at integrable endpoint singularities is checked at relative-or-absolute tolerance 1e-12. No finite numerical test establishes the continuous-parameter or infinite-time theorem; these follow from the explicit renewal-reward proof in RESULT.md. No external or independent audit was performed.
