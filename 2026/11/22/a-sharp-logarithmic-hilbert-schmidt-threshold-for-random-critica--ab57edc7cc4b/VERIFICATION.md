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

# Mathematical verification

The assertion is reduced by the Poisson factorial-moment formula to one nonnegative double integral. The critical input is the angular average of the reciprocal boundary distance, whose coefficient is exactly \(1/\pi\); the remaining integral has explicit antiderivative \(2U^{3-2b}/[(b-1)(2b-3)]\). The proof controls its uniform error near \(b=3/2\) and establishes the divergent cases by positive shell lower bounds.

Run `python check.py` (requires `mpmath`) to reproduce 24 finite diagnostic assertions, covering kernel asymptotics, angular elliptic integrals and the limiting constant. This does not independently validate the infinite proof or historical originality.

The complete Pick interpolation implication is an application of the published Aleman–Hartz–McCarthy–Richter theorem; no other externally certified validation is claimed. The result does not imply a noninterpolation phase for \(b\le3/2\).
