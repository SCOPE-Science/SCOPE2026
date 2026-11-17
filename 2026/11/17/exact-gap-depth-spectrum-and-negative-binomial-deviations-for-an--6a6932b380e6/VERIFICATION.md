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
The self-contained checker `checks/verify_gap_depth.py` uses Python standard-library integer arithmetic, `fractions`, `math` and a finite recurrence. It confirms 35 integer finite-word coefficients, 88 exact ratios of consecutive negative-binomial probabilities, four local asymptotic ratios, and seven finite-mean spectrum evaluations. Execute `python3 checks/verify_gap_depth.py` at the package root. The checker does not prove infinite Hausdorff dimension, infinite independence, or uniform Stirling remainders; these are established analytically in RESULT.md. No independent audit has been performed.
