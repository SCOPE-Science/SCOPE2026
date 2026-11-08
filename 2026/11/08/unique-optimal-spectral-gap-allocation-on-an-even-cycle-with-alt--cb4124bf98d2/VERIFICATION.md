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

# Verification record

Execute `python3 verify.py` from the extracted package folder. The script uses Python's standard library (`fractions`, `itertools`) only. The actual execution output was:

```
EXACT_VERIFY_OK parameter_cases=48 principal_minors=1872 dual_energy_checks=48
```

For the 48 choices with \(m\in\{2,3\}\) and rational squared prices and budgets, the code recomputes the candidate rates, exact full budget, band polynomial, dual edge-energy ratio, and nonnegativity of every principal minor of \(L-\lambda(I-J/(2m))\). It does not use symbolic floating-point truncation or infer infinite validity from the samples. The proof in `RESULT.md` covers all \(m\ge2\), all positive real prices, all positive budgets and all independent edge weights. A separate numerical stress check of 12 parameter configurations on \(C_6,C_8,C_{12},C_{18}\) also agreed with the closed formula, but is not needed for the certificate. Independent external mathematical audit has not been performed.
