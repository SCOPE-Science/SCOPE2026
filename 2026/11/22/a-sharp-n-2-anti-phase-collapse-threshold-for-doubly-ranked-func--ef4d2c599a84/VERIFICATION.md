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

# Reproducibility and limits

The accompanying `verify.py` uses only Python's standard library. Run `python verify.py`. The complete finite-rank enumeration, 300 randomized finite configurations, four sample-size experiments, and numerical Gaussian overlap integration each pass, giving 457 assertions. The test run produced limit estimate \(0.367834044\) and empirical all-tied frequencies approximately \(0.3851,0.3737,0.3616,0.3606\) at sizes \(60,140,300,500\); sampling error is present. Exact mathematical justification comes from the rank identity, rare-pair expansion and factorial-moment estimates in RESULT.md, not these simulations. No independent mathematical verification has been performed. The stated group-test implication assumes non-rejection on a constant summary vector.
