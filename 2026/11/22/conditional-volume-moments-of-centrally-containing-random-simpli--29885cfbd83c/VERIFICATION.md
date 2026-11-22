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

# Reproduction and scope of the mathematical checks

With Python 3, NumPy and SymPy installed according to `checks/requirements.txt`, execute from the package root:

```sh
python checks/verify.py
```

The standalone script checks all coefficients of the conditional first-three-volume-moment expansion symbolically, verifies the strict rational inequality used to certify negative skewness, and repeats finite-sample checks for independent sphere-uniform simplices in dimensions two, three and four. It enumerates every sign pattern on several sampled point configurations to verify the unique two-orbit-successes argument and the sign-invariance of unsigned minors. Finally, in three dimensions, it independently estimates each of the three distinct cubic minor correlations and the conditional third volume moment under fixed-seed sampling. A successful run prints `ALL_CHECKS_PASSED`.

These tests do not constitute exhaustive numerical validation of all distributions or an infinite mathematical proof. The all-dimensional and moment identities rest on the sign-orbit, determinant-expectation and angular-integration proof in `RESULT.md`. No independent audit or certification has been performed.
