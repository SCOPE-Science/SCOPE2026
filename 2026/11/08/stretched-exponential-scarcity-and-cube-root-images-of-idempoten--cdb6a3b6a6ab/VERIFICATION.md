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

# Reproducibility and verification

The enclosed `checker.py` has no dependencies other than the Python standard library. Run `python3 checker.py` from this directory. A successful execution prints `ALL_CHAIN_RETRACTION_CHECKS_OK finite_brute_max_m=5 path_strips=7 count_m_11= 50021` and the two numeric reference constants.

The finite comparisons independently enumerate all discrete one-Lipschitz maps on chains with up to six truth values, test the equation \(f\circ f=f\), compare the resulting exact counts against the bounded-walk sum, and verify all twelve reported idempotent counts. Further tests compare total one-Lipschitz maps against an independently implemented increment-state recurrence and compare strip-walk matrix recurrences against direct path enumeration for \(d=0,\ldots,6\) and \(t=0,\ldots,12\).

Proof obligations not discharged by finite computations: the exact term-function representation at arbitrary \(m\), spectral inequalities for all strip widths and durations, the uniform saddle-point optimization, and the convergence-in-probability conclusion. Those are established by the analytic proof in `RESULT.md`. No independent proof validation or machine-formal proof has been performed.
