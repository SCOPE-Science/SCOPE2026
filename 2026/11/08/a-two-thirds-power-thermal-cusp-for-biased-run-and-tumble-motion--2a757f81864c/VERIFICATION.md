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

Run `python VERIFY.py` with Python 3, NumPy and SciPy. The checker independently integrates the beta-weighted stationary distribution by Jacobi quadrature; obtains the symmetric critical value by a confluent-hypergeometric root; computes the logarithmically singular coefficient by adaptive quadrature; checks the Kummer-derived second and fourth weighted moments; compares athermal moments against the two-state process-generator identities; and solves the double-stationarity equations for signed asymmetry at three base rates. It completed 101 deterministic checks.

For the reference point \(\ell=1/2\), \(s_\ell=0.3164643403484473\ldots\) and \(A_\ell=1.0116863052989679\ldots\). The numerical assertions only cover the sampled parameter values and do not establish a universal root count or an asymptotic theorem. The analytic proof uses the exact stationary balance, the Gaussian heat equation, a standard strict zero-number theorem, a confluent-hypergeometric differential equation, and a rescaled implicit-function argument. Public source comparisons establish an informed novelty assessment, not a certification of priority. No independent audit has been performed.
