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

# Reproduction and evidence limits

The entire formal claim and its proofs are in `RESULT.md`. The independent executable `checker.py` requires Python 3 and only standard-library modules. Run `python checker.py` from the extracted package; a successful execution prints the number of passing finite deterministic assertions.

The diagnostics exercise: the Brownian renewal identity for a two-point reset measure; positive calibration integrals and the uniquely normalized physical rate; far-field logarithmic slopes; distinct one-point versus two-point measures indistinguishable over a right-hand target region; Fourier multipliers exhibiting quadratic attenuation; and mass normalization plus positivity for smooth oscillatory reset measures.

Finite checks do not establish all-target uniqueness, arbitrary-measure equivalence, or infinite-index asymptotics. Those assertions follow analytically from the proof's renewal calculation, positive-tail exponential, monotone integral, distributional Helmholtz inversion, and Fourier multiplier estimates. The public record contains no independent scientific audit and no field experimental verification.
