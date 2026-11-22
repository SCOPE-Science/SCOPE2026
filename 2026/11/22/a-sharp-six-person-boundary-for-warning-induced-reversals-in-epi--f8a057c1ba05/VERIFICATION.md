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

# Verification of the finite unanimous-warning epidemic theorem

The analytic proof is in `RESULT.md`. Run `python3 CHECKER.py` from any directory. The checker needs Python 3 and only its standard library; it does not import any other files. The checked embedded copy produced:

```
EXACT_RATIONAL_ASSERTIONS 58578
WITNESSES k=1,m=3 and k=2,m=2 satisfy strict high-transmission reversal
```

For each fixed small integer \(k,m\), the checker enumerates all binary first-generation outcomes and all binary terminal outcomes using exact rational masses, obtaining a finite-state expectation independently from the closed polynomial. It exercises heterogeneous residual protection vectors, both endpoints of the infection parameter, and a rational derivative-sign grid across additional integer sizes. It verifies the minimum integer-population bound within the defined family. **A finite rational grid is not a proof of universal derivative positivity, uniqueness or nonexistence.** These come from the derivative's proven unimodal shape and the exact endpoint sign as shown in `RESULT.md`.

The calculations do not model delayed information, multiple waves, undirected infection feedback, biological heterogeneity in source transmission, or empirical uncertainty. No independent audit was conducted.
