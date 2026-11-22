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

# Verification of local microlensing peak-jet theorem

The analysis derives the magnification derivatives directly, eliminates every per-band affine source and blended-light nuisance, proves strict monotonicity of the sixth-jet invariant for all positive impact parameters, and gives an explicit inverse. The order-five sharpness argument is a continuous positive-parameter deformation, not a finite grid or numerical timeout.

Reproducibility: run `python3 check_peak_jet.py` with Python 3.10 or later; the script uses only `decimal`, `fractions` and `random` in the standard library. A recorded run passed 22,222 arithmetic checks, including 1,100 random four-parameter recovery exercises, 500 multi-passband deformation exercises, and the rational witness at impact parameter 1. These are supplementary consistency checks only; they do not validate the microlensing model on sky data or prove the theorem for a continuum of parameters.

For a genuine exact curve, the flux-independent invariant must lie strictly between \(20/9\) and \(25/9\). A generic proposed jet also needs the recovered positive blend flux and parameter-consistency conditions; the interval alone is not a sufficient astrophysical or mathematical admissibility test. Very large impact parameters induce divergent inverse sensitivity. No independent audit or empirical validation has been performed.
