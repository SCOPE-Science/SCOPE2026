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

# Verification of the fitted-Poisson critical-profile theorem

The proof in `RESULT.md` is the primary correctness evidence. The standalone script `check.py` exercises finite-sample and analytic identities using SciPy, and may be run via `python check.py` (Python 3, NumPy, SciPy).

Actual executed verification yielded **126 passing assertions**: 63 finite-binomial absolute-deviation identities, 13 Poisson absolute-deviation identities, 17 monotone profile checks, 20 boundary/profile-range checks, seven local cusp-coefficient tests, and six comparisons between centrally truncated finite-sample expectations (with negligible Poisson tails) and the critical integral. Numerically, at \(\kappa=0.2\), the limiting full \(\ell_1\) distance is \(1.099789562606\ldots\), and the first cusp coefficient is \(3.081939599442\ldots\).

Those finite checks are not exhaustive verification of all sample sizes or of analyticity and infinitely many modal cusps. No independent mathematical audit has been performed. No bootstrap calibration or power assertion is verified or claimed.
