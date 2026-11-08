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

# Reproducible checks

Run `python3 verify.py` in the directory containing the extracted files. It has no third-party dependencies and prints the exact pass count; in the tested environment it printed: `PASS: 1048 exact or controlled numerical assertions (925 conditional finite enumeration; 90 Dirichlet integrals; 33 asymptotic checks).`

The finite checks enumerate every possible subset of circular gap locations, conditional on the count of long gaps, for every order from three through eleven. A separate exact-rational Dirichlet calculation checks mixed moments and probability normalization for orders three through eight at three distinct radii. The numerical asymptotic checks examine three window parameters at three sample sizes and independently verify the finite covariance identity against its proposed limiting constant.

No finite or numerical check establishes the infinite-dimensional law. Its full argument is written under `## Proof` in RESULT.md, using standard binomial convergence and the method of factorial moments. No independent mathematical audit is claimed.
