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

# Reproducibility and proof limits

From a complete extracted package, run `python3 verify_threefold.py`. The standard-library script tests four parameters in the stated open interval against the exact competitor identity, two cyclic permutations of a nontrivial phase triple, nine Fourier-Hessian instances by periodic quadrature, and twelve graph-flow derivative identities. Expected output is `VERIFY_OK interval=4 cyclic_shifts=2 hessian_cases=9 polynomial_flow_cases=12`.

The actual mathematical certificates are Steps 1–6 of RESULT.md: the global Hilbert variance identity and compact aligned sums, the exact three-phase competitor, the phase-invariant \(W/Z^2\) separating global means, the normal-slice Hessian with lower bound \(2(1-2u)\), and polynomial-flow transverse equations. Numerical quadrature and finite sample tests do not prove the infinite-dimensional Hessian assertion or the global optimization bound. No claim is made about sharpness of the sufficient parameter range or exact global mean count. No independent review has been performed.
