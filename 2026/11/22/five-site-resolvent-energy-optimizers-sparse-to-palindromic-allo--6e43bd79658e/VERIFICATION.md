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

# Reproducibility and limitations

Run `python3 CHECK.py` using a standard Python 3 interpreter. This checks 6,000 exact-rational symmetrization identities, thousands of candidate-value and budget equalities, and 60,000 randomly sampled simplex points over 600 independently sampled positive energy scales. It also uses exact rational comparisons to test the displayed strict small- and large-energy sufficient inequalities. The expected first line is `PASS 68408 exact-rational identities or numerical stress assertions`.

The mathematical proof in `RESULT.md`, not numerical enumeration, establishes the statement for all positive real budgets and every complex weighted shift. A numerical optimizer or a finite random test cannot prove absence of other maxima; that part rests on strict convexity of the optimized difference variable and the global reduction to the two branches. The result does not establish a unique transition budget, nor a uniform statement for arbitrary chain lengths or other Schatten exponents. Scientific historical priority has not been independently audited.
