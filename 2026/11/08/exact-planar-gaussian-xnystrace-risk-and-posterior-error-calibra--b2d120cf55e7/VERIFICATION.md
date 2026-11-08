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

# Verification instructions and limits

Run `python verify.py` in an environment with Python 3, NumPy, SciPy and SymPy available. The script prints the reference execution results stored in `verification_output.txt`. It checks exact symbolic factorizations of both sharp inequalities, exact benchmark fractions, high-accuracy independent quadrature for angular Fourier moments, and direct numerical evaluation of the original Gaussian leave-one-out estimator with deterministic random seed `20261105` and 180000 probe pairs per spectrum. The recorded execution passed every assertion.

The independent quadrature and seeded sampling are *finite numerical checks*, not proofs for all eigenvalues or all random inputs. The infinite proof is in `RESULT.md`, Steps 1–4; in particular it uses Gaussian moment identities, absolute convergence of the Poisson kernel, independent angular integrations, and positivity of explicit polynomials. Numerical comparison is restricted to the original unnormalized estimator; substituting the optional residual-normalized variant changes the theorem. The status in the front matter records that independent audit has not been performed.
