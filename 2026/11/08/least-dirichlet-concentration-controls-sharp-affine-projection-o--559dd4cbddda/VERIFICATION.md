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

The analytic proof uses the explicit \(N\)-by-\(N\) Dirichlet Gram inverse, exact beta truncated integrals, conditional Jensen with a positively crossed kink, strict triangle inequality on an interior open set, and a uniform second-moment bound for the gamma limit. Each step is valid for every \(N\ge2\) and all strictly positive Dirichlet weights.

The attached `checker.py` was executed in a Python installation with SymPy and SciPy. It verified 373 exact Gram, integer beta and uniform-volume identities; 24 noninteger quadrature and parameter-order identities; and four gamma-scaling instances. The expected final output is `ALL_AFFINE_DIRICHLET_CHECKS_PASSED`. Finite tests are supplementary, not a substitute for the universal argument. The prior uniform-volume formula is intentionally treated as known.

The theorem does not address higher-degree orthogonal projectors, other distributions, or boundary-concentrated measures. No independent audit or certification has been performed.
