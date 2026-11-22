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

The reported mean and capture-channel probability follow from explicit bounded solutions of the stopped jump-diffusion backward equations. The proof shows a uniform geometric tail for the stopping time, so generator uniqueness and optional-stopping identification apply even at the noncontractive endpoint.

For an independent numerical check, run `python verify.py` with Python 3 and the documented numerical dependencies. The code performs exact rational coefficient-recurrence checks, high-precision entire-series evaluations, second-order finite-difference solutions to the nonlocal boundary-value problem, the special elementary endpoint comparison and finite-parameter checks of limiting formulas. The recorded run passed 250 finite diagnostics.

Numerical tests do not establish the general formulas or the limiting asymptotics; those are proved by coefficient recurrences, boundary matching and dominated convergence of exponential series. No independent scientific audit or external formal certification has been performed.
