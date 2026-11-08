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

The analytic proof supplies all quantifiers and works for arbitrary fixed nonzero continuous perturbations. The exact central-deletion integral is checked independently using the elementary antiderivative of tangent. Running `python3 checks/notch_lebesgue.py` supplies numerical convergence checks at three increasing cutoffs, an additional complex one-sided notch and a direct Fourier sum identity check. None is presented as a proof for all cutoffs. No independent audit has been performed.

Observed checker output from the package source:

```text
PUNCTURED_LEBESGUE_CHECK_PASS central_limit=0.219078028909 n_tests=3 complex_gap=0.356668572
n=80 central_norm_gap=0.212807869068 abs_error=0.00627016
n=320 central_norm_gap=0.217451773619 abs_error=0.00162626
n=1280 central_norm_gap=0.218619148604 abs_error=0.00045888
```
