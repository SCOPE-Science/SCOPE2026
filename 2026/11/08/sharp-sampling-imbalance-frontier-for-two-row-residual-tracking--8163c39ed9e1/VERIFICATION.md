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

The standalone `verify.py` reconstructs the exact state and covariance dynamics for the claimed two-row method. A successful run reports `VERIFY_OK symbolic covariance determinant, six eigenvalues at zero, derivative, 45 rational one-step tests, and sample crossing checks`.

The determinant identity and zero-step characteristic polynomial are symbolic rational-function checks. The one-step tests compare the covariance-map lift with direct averaging over both possible updates at rational parameter values. Four numerical spectral-crossing checks probe representative cases; they are not a proof for all probabilities or time steps.

The proof of necessity uses the positivity of the covariance map on the positive-semidefinite cone and finite-rank covariance decompositions; the exact cubic monotonicity and the mean-error identity are analytic. No external or independent mathematical audit has been conducted. The historical originality comparison remains qualified by possible inaccessible or unindexed exact analyses of nonuniform two-component SAGA.
