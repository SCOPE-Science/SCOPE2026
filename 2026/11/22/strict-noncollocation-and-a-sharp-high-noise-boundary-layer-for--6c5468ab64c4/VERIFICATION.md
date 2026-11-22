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

The executable `check_brownian_design.py` was run from this package's actual science path using SymPy, NumPy and SciPy. It passed exact symbolic comparisons for the integrated kernel products, the observation covariance inverse, the split and terminal directional derivative identities, and the high-noise and repeated-site Taylor coefficients. Numerical optimizations were also checked at noise variances \(10,30,100,300,1000\), with distinct interior nodes and scaled offsets trending toward \(1/2\) and \(1/6\). The scaled optimized replication gain tended toward \(1/18\). These numerical optimizations are illustrative only, not global-optimality certificates.

Mathematical global optimality, uniqueness for sufficiently high noise and the all-noise exclusion of boundary designs are supported by the analytic proof in `RESULT.md`. Exact symbolic identities were independently obtained through algebraic simplification; no infinite-domain conclusion was inferred from numerical enumeration. No outside mathematical review was performed.
