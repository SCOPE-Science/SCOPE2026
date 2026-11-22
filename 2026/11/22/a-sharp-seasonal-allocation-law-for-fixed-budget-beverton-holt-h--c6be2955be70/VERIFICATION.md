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

- Run `python3 check.py` using Python 3 and the unmodified file in this package. The program requires only the standard library and uses fixed deterministic seeds.
- Exact rational checks reconstruct the period-two recurrence and both post-recruitment catches for sampled rational parameter values.
- Numerical tests compare the explicit optimizer with 41 feasible allocations per parameter sample across 1,200 parameter draws, and verify the complete interior regret formula whenever applicable.
- Iterative trials test convergence to the derived positive two-cycle and extinction when the two-season multiplier is below one.
- Observed replay result: `PASS: 59764 deterministic diagnostic assertions. Analytic proof required for universal claims.`
- The mathematical proof of the universal theorem is in `RESULT.md`: affine inverse dynamics, closed cycle, derivative sign, strict monotonicity, and algebraic regret identity. Sampling and floating-point iterations do not certify infinite domains or all parameter configurations.
- No external or independent mathematical audit was conducted. Historical priority is assessed only against the specifically listed evidence and remains provisional.
