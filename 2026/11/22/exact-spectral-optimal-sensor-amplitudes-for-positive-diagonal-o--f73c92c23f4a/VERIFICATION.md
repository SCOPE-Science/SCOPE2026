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

# Verification details

The proof requires strict total positivity of the actual finite Vandermonde Gramian, the checkerboard inverse sign rule, the Rayleigh quotient lower bound for the inverse top eigenvalue, and Perron–Frobenius identification of the equality eigenvector. Those steps are supplied explicitly in `RESULT.md`.

Run `python verify_optimal_sensor.py` in the same directory. The exact-rational checker requires only standard Python 3 and prints `OPTIMAL_ORBIT_SENSOR_RATIONAL_OK 885`. It tests generalized Gram minors, inverse signs, normalized positive rows, the exact three-mode allocation, and the positive-semidefinite equality certificate on two-, three-, and four-mode examples. A finite test suite is not a substitute for the universal analytic proof. No independent review or audit has been performed. The claimed result does not extend to repeated eigenvalues or an observation horizon shorter than the dimension minus one, where the optimal lower bound is zero.
