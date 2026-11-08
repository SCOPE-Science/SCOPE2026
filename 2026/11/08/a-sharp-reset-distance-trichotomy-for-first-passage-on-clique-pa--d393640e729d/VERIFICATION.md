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

# Verification of the first-passage classification

Run `python3 check.py` with Python 3 (standard library only). This script builds the full finite-state continuous-time generator directly from the clique and attached path, adds reset transitions at non-source sites, and solves the transient mean hitting-time system using exact rational arithmetic.

The executed program reports 280 exact comparisons of reduced and full models, polynomial coefficient checks for lengths 1–44, and finite optimizer/monotonicity samples across clique sizes 2–24 and path lengths 1–13. No randomness, external downloads, or tolerance-based comparisons enter the exact generator checks.

The proof in `RESULT.md` gives the infinite-scope justification: (i) Laplace-transform backward recurrences, (ii) their binomial polynomial solution, (iii) Poisson restart renewal, and (iv) strictly positive derivative coefficients for every length at least three. Computation is not treated as proof for untested parameters. Independent scientific audit is not performed.
