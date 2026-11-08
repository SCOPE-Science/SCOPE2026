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

The proof's universal steps are the cooperative phase-plane classification, backward stable-manifold continuation, and convergence of the exact weighted-product integral. Those are analytical arguments, not a finite check.

To repeat the bundled checks, run `python verify.py` from the directory containing that file. It requires no nonstandard packages. The program checks 2,187 exact rational cancellation identities, equilibrium and Jacobian relations, and three separately integrated parameter cases. It reports `VERIFY_OK 2292 exact rational and numerical checks`.

Numerical integration uses the center of the saddle stable eigenvector, followed by fourth-order integration in logarithmic donor density. Rounding, discretization, and initializing the manifold at a finite displacement are numerical limitations. The checks do not establish completeness of the separatrix or global basin uniqueness; these require the proof in RESULT.md. No external validation has been performed.
