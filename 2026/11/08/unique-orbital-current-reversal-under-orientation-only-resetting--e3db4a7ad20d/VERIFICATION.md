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

# Verification and reproducibility

Run `python3 verify_current.py` with Python 3's standard library. The actual replay returned:

```
PASS: 237 deterministic assertions; sample root 3.381098750015
```

The checker evaluates the exact polynomial/rational expression, an independently implemented stationary-generator mixed-moment system, and a numerical Poisson-reset-age mixture integral with Simpson quadrature. It checks both signs around 45 distinct parameter-specific roots and the critical stiffness boundary. The verification targets finite numerical consistency, not exhaustive enumeration. Global root uniqueness, current signs and thermal-noise invariance follow from the symbolic generator identities and Descartes sign argument in `RESULT.md`; those mathematical arguments require no numerical extrapolation. Only the specified zero-angular-diffusion, principal-axis orientation-only reset model is established. No independent scientific audit is claimed.
