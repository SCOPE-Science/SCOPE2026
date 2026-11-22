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

For \(L,D,r>0\), the exact first-event transform derived from the reflected diffusion's step-killing boundary-value problem has a second-order Taylor expansion at the origin. The analytical moment formula yields \(\mathcal F(a)-1=a(2a^2/3-1)/(1+a)^2\) and the derivative numerator \(2a^3+6a^2+3a-3\). These establish the precise crossing and unique minimizer without numerical extrapolation.

`CHECK.py` is independently executable with Python 3 and no third-party packages. It checks exact rational Fano identities, numeric root values, and—separately—solves discretized reflected killed-generator equations for the Laplace transform and first two moments over multiple parameter regimes. All 130 assertions passed. The discretizations use finite intervals and are consistency checks; the proof of the unrestricted half-line result is in `RESULT.md`.

The model's instantaneous reset and ideal boundary assumptions are essential. The publication-priority assessment is based on the stated source inspections and searches; no independent scientific audit or external certification was performed.
