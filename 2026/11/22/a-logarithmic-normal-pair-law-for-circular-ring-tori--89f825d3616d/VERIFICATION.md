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

The included `checks/verify.py` was executed against the packaged source path using Python, NumPy, SciPy and SymPy. It passed exact rational arcsine-Legendre identities for orders zero through sixteen (nine even degrees), direct independent area-weighted samples for major/minor radius ratios 1.2, 3 and 8, and two finite angular spectral residual comparisons.

Direct numerical results (finite checks, not proof): for ratios 1.2, 3, 8, the measured \(\mathbb E[T^2]\) values were respectively 0.373317, 0.375903 and 0.375152 versus the exact 0.375. The measured fourth Legendre moments were 0.020670, 0.019190 and 0.020822 versus exact \((3/8)^4\). At angles 0.02 and 0.008 radians the density-series residual after subtraction of \((2/\pi^2)\log(1/\theta)\) was about 0.421475 and 0.421295, consistent with a bounded remainder.

The actual infinite argument is in `RESULT.md`: area-weight pushforward; addition theorem; arcsine-Legendre integral; globally \(L^1\)-summable Legendre series; split at harmonic order inverse to angle to prove the sharp logarithmic coefficient; integration for the event tail. There is no independent audit, no computer proof of an infinite assertion, and no claim of historical-priority certification.
