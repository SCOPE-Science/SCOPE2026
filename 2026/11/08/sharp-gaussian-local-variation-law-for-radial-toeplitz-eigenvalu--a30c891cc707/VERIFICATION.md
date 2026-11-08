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
# Reproducibility and verification
The proof uses the exact polar-coordinate probability law, the strictly convex Laplace phase, \(L^1\) convergence to two translated normal densities, and the smooth-cutoff construction. The Gaussian constant is \(4\Phi(\eta)-2\) because the supremum over unit-bounded symbols is the \(L^1\) distance of densities, rather than the half-normalized total variation distance. The source's published single-exponent discontinuous-symbol example is not assigned to this result.

Run the included `CHECK.py` using Python 3 (standard library only). It integrates normalized saddle densities numerically and compares the predictions for several fixed powers, degree gaps and the exactly Gaussian \(\alpha=2\) case. Numerical diagnostics are finite and do not verify an infinite statement. A mathematical audit by an independent party has not been performed.
