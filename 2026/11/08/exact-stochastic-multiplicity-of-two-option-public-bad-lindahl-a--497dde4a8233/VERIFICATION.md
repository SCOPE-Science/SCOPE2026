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

Execute `python verification/check.py` with Python 3 and SymPy. The script independently constructs the two-inequality PF test and the endpoint-derivative criterion, exhausts 6561 positive integer cost arrays, checks nine additional rational lotteries per nonconstant array, evaluates both conditional-ratio integrals symbolically, and reports fixed-seed simulation sanity checks with 240000 replicates for each cost model.

Analytic verification: strict concavity of the sum of log costs gives at most one interior stationary point; the PF inequalities give exact endpoint/interior characterization; crossed preferences and the conditional ratio CDF prove the Stieltjes law. Uniform and exponential integrals yield the two closed forms. The finite enumeration covers only its stated small discrete inputs, and sampling is not an infinite proof. No independent external audit has been performed. The calculation does not certify absence of related unindexed publications.
