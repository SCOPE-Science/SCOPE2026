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

# Reproducibility

Run `python3 verify.py` in the same directory using Python 3.8+ and no external libraries. The verifier generates all ordinary set partitions by restricted-growth strings, discards precisely those with crossing block pairs, records every surviving singleton indicator, then evaluates an independent integer Walsh–Hadamard transform. It compares those values at every frequency to the separately computed Catalan-binomial multipliers through \(n=9\), including independently calculated endpoint projection kernels and exact rational norms. Direct integer formula comparisons through \(n=120\) check the zero shells and least nonzero multiplier gaps. The program's output concludes `PASS exact checks 8495`.

This computation verifies concrete finite instances only. The all-order assertions, unrestricted projection optimality, and asymptotic conclusion are established by the analytical proof in `RESULT.md`. No independent external audit is represented or implied.
