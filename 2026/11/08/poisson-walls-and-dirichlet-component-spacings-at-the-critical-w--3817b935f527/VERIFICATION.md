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

Run `python3 verify.py` using Python 3 and no third-party packages. The verifier exactly enumerates the edge masks on the square of a cycle for seven and eight vertices (16,384 and 65,536 possibilities before filtering), checks the component-count identity on every configuration satisfying the five-window condition, confirms the exact wall edge-overlap combinatorics, and checks two exact rational moment formulas.

Observed output:

```
VERIFICATION_OK total_checks=8935 valid_configuration_checks_n7=2186 valid_configuration_checks_n8=6622
LIMIT: exhaustive only for n=7,8; asymptotic claims require analytic proofs.
```

This finite verification is not an independent proof of point-process convergence or the conditional Dirichlet limit. The general arguments, including fixed-order factorial-moment cluster estimates, are recorded in `RESULT.md`. The acceptance status is self-reviewed only, not externally certified.
