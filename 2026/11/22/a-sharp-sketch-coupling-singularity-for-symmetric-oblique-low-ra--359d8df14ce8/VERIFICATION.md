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
# Reproduction and evidence

Run `python3 verify.py` with a Python 3 standard-library installation. The program prints a `VERIFY_OK` line and a count of passed assertions. It performs direct rational-matrix identities for the rank-one oblique projector, exact endpoint-moment algebra, numerical checks of the integral identities for three and four sketch rows, and seeded finite Gaussian ratio checks.

The mathematical proof in RESULT.md establishes that the joint inverse powers of two nondegenerate correlated Gaussian vectors are integrable exactly below their spatial dimension, that singular perfect sharing changes the exponent, and that the Laplace integral diverges at the stated rates. The verifier is a reproducibility supplement, not a substitute for infinite-dimensional probability integration or a proof of a tail limit. All floating-point quadrature tolerances are diagnostic and are not used in the proof.

The result concerns one fixed pair of rank-one matrices in arbitrary sufficiently large ambient dimension and exact real Gaussian sketching. No independent mathematical audit or external certification has been performed.
