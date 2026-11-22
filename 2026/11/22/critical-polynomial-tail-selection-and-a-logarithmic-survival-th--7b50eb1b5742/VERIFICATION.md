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

# Verification and limitations

The analytic claim is supported by the exact reflected Bessel kernel and by the sequence of local Gaussian estimates, a tilted Fourier tail bound, a telescoped recurrence, weighted Gaussian-sum asymptotics, and geometric final-state tightness described in `RESULT.md`. No finite test establishes the infinite-time limit by itself.

Run `python check_critical_tail.py` with Python, NumPy and SciPy. The script independently compares the reflected Bessel kernel with Poissonized binomial paths and a finite-generator matrix exponential, checks the telescoped recurrence and the harmonic identity of the minimal quasi-stationary law, and reports diagnostic finite-time leading-order ratios. The recorded execution passed 1,262 numerical/combinatorial assertions. Its strict floating-point tolerances depend on standard double-precision implementations.

The statement is restricted to fixed rates and exact geometric–power initial masses, with no general arbitrary slowly varying tail factors, no nonuniform parameter limit, and no broad necessary-and-sufficient domain theorem. Published-result comparisons are limited to the listed accessible evidence. Independent assessment has not been performed.
