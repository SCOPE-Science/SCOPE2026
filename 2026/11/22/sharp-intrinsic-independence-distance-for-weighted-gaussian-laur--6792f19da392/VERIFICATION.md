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

# Verification and limits

The proof in `RESULT.md` establishes the covariance-zero set from the published theta quotient, converts zero covariance to independence for the proper Gaussian field, minimizes the complete hyperbolic distance over every zero-covariance pair, and obtains the sharp parameter transition and singular asymptotic. The calculation uses curvature \(-1\) throughout.

The standalone `verify_independence.py` script was run with Python and `mpmath` at 75-digit precision and returned `PASS 180 finite diagnostics (75-digit precision)`. Tested cases cover 24 nonexceptional combinations of annular modulus and logarithmic boundary weight, 144 direct-periodicity/geometry/strict-inequality checks, four truncated Laurent cancellations, 30 core or exceptional cases, and two near-exception asymptotic checks. The exact printed count of 180 is authoritative; the individual groups can be read in the checker source.

Numerical cancellation of a truncated Laurent series is not a proof that its infinite series vanishes, nor does a finite grid prove the global minimum. Those conclusions follow from the theta product and the strip distance identity plus a strict monotonicity argument. Source statements were checked in the accessible preprints; historical-priority checks remain best-knowledge, not independent certification.
