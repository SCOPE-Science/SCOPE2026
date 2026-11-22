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

# Verification of the mathematical statement

The exact mathematical evidence is the four-step analytic proof in `RESULT.md`: explicit decaying Bessel solution; strictly decreasing Bessel ratio elasticity from \(H>0\); resulting bijection of the two-rate uptake ratio onto a sharp open interval; explicit positive reconstruction and one-reading ambiguity family. Its assumptions, measured-data inequalities and proof scopes coincide with the claim.

The companion `verify.py` checks the same formulas using Python 3, SciPy and a deterministic random seed. Running `python verify.py` passed **18,012** numerical assertions, including 2,000 randomized inversions and a fixed example. No external files, observations or hidden data are required. Floating-point checks are supplementary only and do not establish the universal theorem or experimental noise robustness.

Scientific limitations: known first-order loss rates, known constant water-side mass transfer and porosity, shared infinite-bed exponential diffusivity, exact measurements; no claim regarding numerical stability near singular bounds, real-stream calibration or complete historical priority. Independent external audit was not performed.
