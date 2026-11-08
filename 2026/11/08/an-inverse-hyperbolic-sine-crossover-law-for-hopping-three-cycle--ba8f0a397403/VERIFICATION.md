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

# Reproduction

Run `python check_eos_crossover.py` in an environment with `mpmath` installed. The program uses 95-digit working precision to compute exact finite-parameter three-step residuals from the stated EOS map, recover its local period-three branch, verify positive single-step derivatives and attracting multipliers, and compare with the asymptotic phase, multiplier gap and parameter sensitivity. It prints `VERIFY_OK high_precision_period_three_and_response_cases=25 precision_digits=95` when all asserted finite checks pass.

The mathematical theorem is proved by the compact-uniform \(C^1\) approximation of the normalized return map and the implicit-function argument displayed in `RESULT.md`. The 25 high-precision computations are consistency tests, not an exhaustive search, proof of asymptotics, or independent scientific audit.
