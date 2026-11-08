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
# Reproducibility and scope

Run `python3 checker.py` with Python 3.9 or newer; no dependencies beyond the standard library. Its fourth-degree spherical cubature uses exact rational weights: weight \(2/[n(n+2)]\) on each positive coordinate axis and weight \(n/[(n+2)2^n]\) on each normalized sign vector, with axis sign irrelevant to even polynomials. The separate-product and whole-sphere Gram forms are evaluated for a full basis of quadratic spherical harmonics. It returns `CLIFFORD_EXACT_CHECKS_PASS 4779` when all assertions pass.

The program verifies dimension-specific finite Gram identities; it is not an exhaustive test over every dimension or radius. The general four-eigenvalue spectrum and strict minimax optimizer claims are proven symbolically in `RESULT.md`. Inputs are exactly harmonic homogeneous degree-two polynomials on the real unit sphere, with complex coefficients permitted. There is no finite-data or noisy measurement claim. No independent audit evidence is supplied.
