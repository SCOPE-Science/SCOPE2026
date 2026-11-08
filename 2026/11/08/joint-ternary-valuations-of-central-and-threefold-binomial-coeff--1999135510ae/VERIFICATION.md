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

# Exact-arithmetic verification

The included `verify.py` enumerates all \(n\) with \(0\le n<3^r\), separately for \(r=0,1,\ldots,9\), and obtains valuations from Legendre's factorial formula rather than the stated transition matrix. It independently generates the matrix coefficient distribution, checks all coefficients and sums, support, and the exact means, variances and covariance using `fractions.Fraction`. It also forms 301 actual pairs of integer binomial coefficients and divides out powers of three.

Execute `python3 verify.py` (standard-library Python only). Actual result:

```text
VERIFY_OK levels=0..9 direct_indices=29524 integer_binomial_cases=301 joint_polynomials=PASS support=PASS exact_moments=PASS
```

No finite enumeration certifies the theorem for all depths. The unrestricted result rests on the explicit carry-table proof, transfer-matrix identity, elementary Markov covariance calculation, constructive support argument, and analytic eigenvalue proof. Independent audit has not been performed.
