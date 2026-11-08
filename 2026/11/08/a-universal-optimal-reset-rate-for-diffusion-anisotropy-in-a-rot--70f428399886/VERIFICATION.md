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

# Reproducibility and scope

Run `python verify.py` in the directory containing the result, with Python 3 and SymPy installed. The program tests nine exact symbolic zero identities, including each renewal-reward covariance identity, both derivative formulas, the strict-anisotropy factorization, its maximum, and the two endpoint limits. It also tests twelve independently arranged evaluations of the cycle-moment formulas at positive reset and angular rates. The execution completed with:

```
PASS: nine symbolic identities and 12 independently evaluated renewal-moment cases
```

The symbolic identities check algebraic simplifications. The general regenerative central limit theorem is applied analytically in the proof using independent reset cycles and their finite moments. The positivity and uniqueness argument follows directly from the displayed derivative factorization. Neither a numerical sampling count nor the existence of a symbolic checker substitutes for a proof of the renewal or infinite-time assertions.

The covariance refers to the centered growth rate `Cov(X_t)/t`; the effective diffusion matrix is one half of this rate. Angle resets have no instantaneous positional jumps. Independent external audit and experimental verification are not performed.
