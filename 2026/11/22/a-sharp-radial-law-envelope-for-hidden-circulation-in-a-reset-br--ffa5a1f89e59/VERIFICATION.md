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

The analytic result is reconstructed in `RESULT.md`: the last-reset renewal representation proves existence and the high-reset weak limit; a unique matrix Lyapunov solution and conditional means prove equality of all stationary lag covariances; a scalar weighted-median duality proves the sharp interval; an antipodal axis construction attains each value; a Gaussian Laplace integral and an explicit rational finite-rate bound establish the opposite-sign and reversal claims.

Run `python proof_check.py` in the directory containing the two files, using Python 3 and SymPy. The checker verifies exact stationary covariance identities, the two-radius sharp envelope and strict finite-rate sign inequalities. The conclusions are infinite-domain mathematical claims supported by the proofs, not extrapolations from checks of finitely many examples.

The claim does not identify reset jumps with continuous-flight angular velocity. It does not assert equality of stationary radial distributions. The proof uses positive-temperature Gaussian smoothing, boundedness of the angular ratio and a nonzero reset radius almost surely; its priority assessment is not an independent literature audit.
