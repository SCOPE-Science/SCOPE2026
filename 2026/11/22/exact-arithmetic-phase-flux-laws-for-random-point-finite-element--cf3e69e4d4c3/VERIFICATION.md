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

# Verification of the stated finite-jump flux theorem

The complete derivation is in \(\texttt{RESULT.md}\). Run \(\texttt{python3 verify.py}\) in the directory containing this file and the script. The script was run in the package preparation environment and returned \(\texttt{VERIFY\_OK 136}\).

Exact rational checks compare the closed inverse-resistance law with the direct stiffness-matrix solve for every admissible Bernoulli outcome at eight resolutions with two rational jump locations. Further exact checks test the strict-inverse-Jensen bias identity and exact-integrated deterministic Galerkin flux formula. Uniform-mixture moments are verified algebraically for selected orders. A separate 30,000-size numerical phase average for two rationally independent irrational interface locations checks the limiting mean-square and mean-bias constants to the documented tolerances.

These finite checks do not prove infinite equidistribution, completeness of the limit laws, universality of the theorem or historical priority. The corresponding analytic steps use the standard Kronecker–Weyl theorem, compactness, uniform Taylor estimates and exact Bernoulli mixtures. Independent mathematical audit has not been performed.
