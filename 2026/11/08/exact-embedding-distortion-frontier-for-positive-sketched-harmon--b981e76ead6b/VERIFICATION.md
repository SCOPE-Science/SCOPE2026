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

# Verification notes

The proof is analytic, using the spectral inclusion \((\lambda-1)(\lambda-\kappa)\le0\), a scalar optimization and a sharp real two-dimensional construction. The scalar pencil has \(G=2\kappa-\varepsilon\sqrt\kappa(\kappa+1)\) and \(F=\kappa(\kappa+1-2\varepsilon\sqrt\kappa)>0\); this is the decisive sign computation.

The reproducible supplementary script `VERIFY.py` needs Python 3 and NumPy. Running `python VERIFY.py` returned `VERIFY_OK 783 checks`: 28 deterministic sign and squared-norm embedding checks, four exact angle-equality tests, 750 independent randomized five-dimensional Krylov-pencil checks and one exact-rational boundary identity. The random tests cover finite cases only and do not prove the universal quantified statement. The script checks numerical eigenvalue real parts and positivity of the Hermitian Gram component.

Only the right-half-plane location of reduced harmonic Ritz eigenvalues is established. Additional conditions are required for convergence of a restarted matrix-function method; nonnormal and floating-point regimes are outside scope. The proof and computation have not undergone independent mathematical audit.
