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

# Verification and scope

Execute `python verification/check.py` with Python 3 and SymPy installed (see `verification/requirements.txt`). The checker uses exact symbolic simplification for six matrix/determinant/characteristic/derivative identities and 117,600 reproducible finite random-design comparisons for D-, A-, and E-information criteria across eight shears and seven horizon lengths. The recorded execution printed `6 symbolic identities passed` and `finite designs: 117600 criterion comparisons passed`.

The exact proof is in `RESULT.md`. Its global conclusions rely on positive definiteness, an analytic fixed-gap trace comparison, explicit one-variable derivatives, and strict monotonicity of a scalar function on a continuous interval. Finite tests do not certify all parameter values. At a finite horizon, each optimal unrestricted second time is clipped to the horizon. The E-optimal unconstrained value is not asserted to be attained if the horizon ends earlier.

The numerical example uses damping \(a=1\), shear \(s=4\), horizon \(T=3\), and the common noise variance normalized to one. No external independent proof validation has been performed.
