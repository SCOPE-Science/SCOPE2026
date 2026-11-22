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

# Checks and limits

Run `python3 verify.py` with the standard Python 3 library. The verifier computes each pairwise effective resistance by independent series/parallel arc reduction using exact `fractions.Fraction` numbers; its output is `VERIFY_OK exact_rational_tests= 2883`. The 2,883 exact rational checks cover the critical segment at multiple sizes and budgets, designs just beyond it, random asymmetric allocations above the cost cutoff and constructive improvements below it. They validate finite test cases only. The theorem for all real parameters is certified in the displayed analytic proof, conditional on the standard series/parallel and Cauchy--Schwarz facts. No independent audit has been performed.
