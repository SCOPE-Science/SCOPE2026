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

The accompanying `verify.py` evaluates the mathematical expressions in `RESULT.md` using only the Python 3 standard library. Running `python verify.py > verification_output.json` produced the included output containing 13,036 passed finite assertions and the explicit \(\lambda L=2\), \(p=0.7\) benchmark.

The program checks the exact closed-integral formula against direct midpoint quadrature for randomly selected locations, compares randomized feasible pairs with the analytically optimal pair, independently tests fixed-gap centering, checks the unique-root equation and phase boundary, probes the two different short-transect limits, and tests a large-transect expansion. Random sampling and finite numerical tests are not a proof of the continuum, uniqueness or asymptotic statements. Those are established by the sign and monotonicity arguments in `RESULT.md`.

The checker does not provide external certification or a field-calibrated detector model. The reproducible numerical evidence is supplementary to the analytical derivation.
