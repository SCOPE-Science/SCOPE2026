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

# Verification record

Run the standard-library script with `python3 verify.py`. It enumerates each old point's status (strictly below, strictly above, or incomparable to a new point), directly verifies transitivity requirements, builds the resulting bivariate count, and checks it against the independent polynomial formula. The four tested cyclic sizes are \(n=3,4,5,6\), whose total counts are \(56,109,225,496\). The script also checks the Lucas total for each size and finishes with `VERIFY_OK`. Its expected output is embedded separately as `verification_output.txt`.

The infinite-size theorem is proved by the ideal/filter decomposition and the transfer-matrix analytic argument in `RESULT.md`; finite checks do not establish the asymptotic. In particular, the displayed covariance comes from differentiation of the larger eigenvalue \(\lambda_+(x,y)\) near \((1,1)\), not from a regression against numerical data.

This is a reproducible mathematical consistency check, not independent validation or an external audit.
