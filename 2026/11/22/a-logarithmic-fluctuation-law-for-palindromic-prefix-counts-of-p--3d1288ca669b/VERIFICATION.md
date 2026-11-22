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

# Reproducibility and verification scope

Run `python verify_fluctuations.py` with a standard Python 3 installation; the script uses no third-party dependencies. Its captured output is `verification_output.txt`.

The program computes the length sequence from integer recurrence, independently generates finite literal palindromic closures, constructs the two eigenvalues from integer period matrices, checks the two-eigenvalue formula across 630 phase-period combinations and evaluates 360,000 integer cutoffs over twelve different directives. All verified discrepancies between the exact count and the limiting staircase were within two integer positions of an actual threshold. Midpoint quadrature checks the predicted density mean, and for three directives the phase-conditioned ordinary-law mean agrees with the empirical 30,000-cutoff mean to within 0.0004.

Scientific limitations: all calculations are finite; spectral floating-point evaluations are approximate and are not substitutes for the symbolic proof of the all-parameter recurrence, positivity, rounding cutoff, or limiting harmonic law. The standalone proof in `RESULT.md` is the source of those infinite statements. No independent audit has been performed.
