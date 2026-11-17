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

# Verification and reproduction

Run `python3 verify.py` with Python 3 and the standard library. The checker performs exact rational-arithmetic calculations for the matrix-square, quadratic two-step coefficient, quadratic asymptotic correction and diagonal scalar coefficient. It also tests eight specified ordered initial points for preservation of order, finite entry and invariance of the nonlinear smooth sector, and evaluates 24 finite two-step ratios. The diagonal rate is sampled separately.

Expected output:

```
VERIFY_OK exact_polynomial_identities=4 offdiagonal_trajectories=8 sampled_two_step_ratios=24 diagonal_check=1
```

The checked symbolic identities follow from the independently stated Taylor expansion \(\kappa(t)=t/2+t^2/8+O(t^4)\). The source of that expansion is the explicit elementary function \(\kappa(t)=\log((1+e^t)/2)\), which may be differentiated directly. The all-state finite cone-entry argument, nonzero limiting amplitude, and asymptotic error bounds are proved analytically in `RESULT.md`; a finite checker does not certify them on its own.

The separate high-precision check described in `RESULT.md` used the exact log-odds map at initial maxima \((0.81,0.66)\). Its output is supportive and is not required to execute the standalone checker or prove the theorem. Independent validation has not been carried out.
