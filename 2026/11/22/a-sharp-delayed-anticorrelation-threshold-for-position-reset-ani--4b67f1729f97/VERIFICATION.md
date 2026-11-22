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

The analytical result follows from exact stationary generator identities and the conditional semigroup for the orthogonal squared displacement, followed by the sign of a strictly monotone exponential integral. In particular, all-parameter assertions and boundary classifications are proved symbolically, not by finite enumeration.

Run `python3 verification/VERIFY.py` using a standard Python 3 installation. The recorded run passed **1,477 standard-library exact-rational and numerical assertions**, including the mixed fourth-moment generator, sharp quadratic threshold, positive critical tail, strict single-zero regimes, resonant formula, and a finite-difference check of the forced covariance ODE.

An independent optional diagnostic `python3 verification/MONTE_CARLO.py` requires NumPy. Its recorded experiment used 180,000 sampled stationary histories, discretized the angular Brownian path and the complete reset process, and compared empirical squared-position cross-covariances at four lags to the closed-form formula. The approximation error was within 0.008 on this parameter example; its time discretization and finite sample do not establish an infinite-time identity.

Limitations: finite diagnostics do not establish novelty, do not replace the proof, and do not address unmodeled reset protocols. The stationary-moment identities already available in earlier literature are used as known inputs where relevant; the new subject of verification is the lag-dependent cross-energy sign threshold.
