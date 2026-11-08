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

The proof is the meet-factorization and complementary rank-one norm estimates in `RESULT.md`. For any fixed radius, the two remainder bounds are uniform in the cyclic modulus because the phase difference has absolute value at most two and all inverse bounds factor out the complete power of its reciprocal.

Run `OPENBLAS_NUM_THREADS=1 python checks/verify.py` with Python 3.10+ and NumPy. This executes 90 two-sided inverse and determinant tests, plus sample spectral condition-number comparisons. On the checked run the program printed `FINITE_PHASE_BALL_CHECKS_PASS cases=90`, with maximum entrywise inverse residual approximately \(1.46\times10^{-14}\) and determinant relative error approximately \(1.09\times10^{-14}\). Such tests are finite numerical checks, not an all-parameter certificate. The theoretical estimate is supplied by the proof, not by extrapolation.
