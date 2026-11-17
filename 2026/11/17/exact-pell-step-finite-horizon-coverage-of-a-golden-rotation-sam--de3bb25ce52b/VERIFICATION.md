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

# Verification evidence

The included `verify.py` checks nine exact high-precision Pell residuals and determinant/parity identities, all positive best lags up to \(5472\), and eight directly enumerated sampled-set union densities at \(N=100000\) against their analytic circular-union values. Successful output:

```text
VERIFY_OK Pell_identities=9 horizon_minimizers=5472 direct_density_tests=8
FINITE_CHECK_ONLY: irrational equidistribution and infinite staircase follow analytically
```

A finite computation is not an exhaustive certificate for all horizons. The proof of infinite-horizon optimality uses a unimodular integer basis and three sign cases; the phase-independent limiting density relies on irrational equidistribution. Both steps are explicitly presented in the main result. The code requires Python 3 standard library only. Independent mathematical review has not been performed.
