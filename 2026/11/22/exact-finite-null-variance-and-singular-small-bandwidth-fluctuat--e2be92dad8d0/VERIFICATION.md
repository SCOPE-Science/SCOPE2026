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

Run `python3 checker.py` with a standard Python 3 interpreter. The expected transcript is `PASS: 402 exact rational assertions`. All arithmetic uses Python `fractions.Fraction`, factorials, and explicit Laplace monomial integrals; no optional packages or network requests are required. The checker compares independently accumulated same-sign and opposite-sign frequency quadrants against the closed polynomial formula at 60 rational bandwidth values, checks moment identities, and samples exact finite-sample variance decompositions across integer sample sizes.

The proof in `RESULT.md` gives the all-bandwidth calculation, degeneracy argument, and almost-sure versus mean-square limit. Finite checker values and independent simulations cannot by themselves prove the infinite-domain statement. The statistical null is *known* standard Cauchy; estimated parameters and power are not verified. The almost-sure endpoint is not an original claim. Historical priority and mathematical correctness have not received an independent audit.
