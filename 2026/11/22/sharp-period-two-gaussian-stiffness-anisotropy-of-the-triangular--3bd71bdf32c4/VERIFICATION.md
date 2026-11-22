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

The supplied `verification/check.py` needs only the Python 3 standard library. Run from the package directory:

```sh
python3 verification/check.py
```

It checks the exact density/orthogonality normalization, compares a direct two-dimensional lattice sum with the independent product of one-dimensional shifted sums, compares direct real-space second derivatives with the Jacobi-product curvature, samples the strict inequality \(\lambda_A>3\lambda_B\), and checks the two asymptotic scales numerically. The expected result is 49 assertions passed.

The analytic proof is in `RESULT.md`: the nonstandard step is the strict monotonicity of \(\,x/\sinh(cx)\,\) for positive \(x,c\), applied termwise to an absolutely convergent theta-curvature series. Finite computations cannot certify the all-parameter inequality, the uniqueness of literature priority, or other untested periodic modes. Independent audit has not been performed.
