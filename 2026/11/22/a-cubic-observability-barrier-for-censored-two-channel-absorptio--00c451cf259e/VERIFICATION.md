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

# Reproducibility of the analytic claim

The proof in `RESULT.md` reconstructs every probability, score, asymptotic block and positive-definiteness claim. The high-precision standalone checker `CHECK.py` evaluates the exact three-parameter Fisher information by the full event integrals and censoring score, then takes the nuisance Schur complement. It checks three independent parameter choices, including coincident conditional rates. It separately integrates squared root-density differences for two distinct matched-intensity alternatives and includes the censored atom. All reported ratios converge to the claimed leading coefficients as the deadline decreases.

To run: `python CHECK.py` with `mpmath` installed. The calculation is finite, and the code does not prove infinite asymptotics. The exact derivation is the proof; numerical checks detect algebraic, normalization and numerical transcription errors. The information bound is for fixed positive interior rates and priors, while the Hellinger non-identifiability statement addresses two fixed models with matched initial marked intensities. No independent scientific audit has been conducted.
