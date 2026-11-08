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

# Reproducibility and scope of checks

Run `python verify_ratchet.py` with Python 3 and the standard library. It evaluates the piecewise-integral formula without simulation, checks the exact left-arm formula, strict rational lower/upper bounds, partition functions and negative rare-reset coefficient, then evaluates finite-rate analytic tail bounds. The rigorous frequent-reset conclusion follows from the tail-exponent asymptotics and \(A>B\), not from a finite set of sampled rates.

The proof independently establishes the renewal reduction, scale martingale, equilibrium integration, high-rate Gaussian-exponential comparison, continuity and smoothing. A separate finite-volume resolvent experiment, not part of the proof and not required for replay, confirmed the qualitative signs at moderate rates. The checker does not exhaustively test all rates, prove zero uniqueness, or supply independent scientific review.
