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

# Verification

Run `python verify.py` in the same directory; only the Python standard library is needed. The actual packaged script completed with: `PASS: 702 exact assertions; exhaustive iid words through n=9 and forward shuffle distributions through n=7.`

It enumerates binary words for \(n=2,\dots,9\) at \(p\in\{1/5,3/10,1/2,7/10,4/5\}\), verifying the full first and second moment identities and each site-resolved mixed covariance as exact rational equalities. For \(n\le7\), an independent implementation enumerates every binomial cut and order-preserving interleaving and compares entire probability distributions with the inverse stable-sort construction. All exact finite threshold predictions and the strictly positive Gaussian covariance determinant are also checked for those parameters.

These finite computations check the algebra, the shuffle interpretation and implementation. The all-size and asymptotic assertions depend instead on the explicitly written overlap and one-dependent triangular-array proofs in `RESULT.md`. Independent external review has not occurred.
