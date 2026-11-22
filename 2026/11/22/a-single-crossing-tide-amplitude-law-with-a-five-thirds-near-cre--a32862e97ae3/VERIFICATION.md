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

The mathematical assertions are established by the conditional two-phase exponential-tail calculation, the strictly positive derivative of the normalized probability difference, its endpoint signs, and the arcsine-density asymptotic near the maximum tidal crest. These steps are recorded in RESULT.md.

To replay supplementary checks, run `python3 check_tidal_exceedance.py` from the extracted package. This test needs Python 3 standard library only and is deterministic. It independently integrates the original exceedance tail and the Bessel positive-part representation; checks signs and monotonicity at finite sampled parameters; compares a finite difference with the exact derivative formula; checks the \(5/3\) coefficient in the weak-amplitude regime; and reproduces the listed numerical benchmark.

Finite numerical experiments do not verify all real amplitudes, all thresholds or the asymptotic limit: those statements rest on the analytic proof. The empirical applicability of exponential surge tails, uniform independent phase and single-component sinusoidal tides was not tested. Independent scientific audit and field validation have not been performed.
