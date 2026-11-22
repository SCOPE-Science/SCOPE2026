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

# Verification

The claim is proved analytically in `RESULT.md` by the Gaussian likelihood-ratio rule, a global Hellinger affinity inequality, the chi-square central limit theorem, dominated convergence and evaluation of a Gaussian half-moment. Each assumption, boundary, quantifier and distinction between calibrated tests and hidden-age testing is explicit.

To replay finite checks, run `python3 verify.py` with SciPy and NumPy installed. The code independently integrates the two radial chi-square densities at their likelihood threshold for 12 cases, compares their exact misclassification total against the chi-square closed form, tests the Hellinger upper bound, compares critical-window error at population sizes 100–100000 and offsets spanning the window, and checks the stationary-reference-age integral and gamma-prefactor formula at three parameter choices. The current package's numerical verifier completed with `PASS`. Finite computations cannot establish infinite limits, independence of publications, or experimental viability.

The most material publication-priority limitation is the unavailable full primary manuscript (arXiv:2606.31634), whose abstract and public scientific synopsis were reviewed; two closest accessible complete result documents on the same Gaussian mixture were inspected. No independent audit was conducted.
