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

# Reproducibility and verification

Run `python check_b2_poisson_activation.py` with Python 3 and its standard library. The exact rational portions verify pair-sum uniqueness for finite geometric B2 spectra, convolution against the closed fourth-moment formula, the KKT waterline, normalization, and the sharp bound on reproducible rational inputs; the run emits `EXACT_B2_WATERLINE_CHECKS_PASS 1148`. A separate floating-point bisection computes the first four ordered transition radii for \(\{0,1,3,9,27\}\); its decimals are not proof of the distinctness theorem. The unrestricted finite and infinite statements instead follow from the compactness, stationary-condition and monotonic-threshold arguments in `RESULT.md`.

Scope limits: the exact rational computations cover selected finite B2 spectra and samples; no finite script can exhaust all infinite supports, prove source priority, or replace independent mathematical validation. The proof of the countable case requires the bound on \(L^4\) tails and weak compactness, and the limit at \(\rho=1\) uses flat coefficient approximants.
