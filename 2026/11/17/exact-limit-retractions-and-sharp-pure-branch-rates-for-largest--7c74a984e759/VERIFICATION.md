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

# Verification and limitations

The exact rational checker `verify.py` is standalone and uses the Python standard library. Execute `python3 verify.py`. The scientific proof uses explicit full-domain chamber entry, conserved physical angles, a solved one-dimensional affine recurrence, and chamber-specific composition. The computation checks 743 rational initial shapes; all 13 iterates from depth zero through twelve; projection idempotence and invariance; stable-chamber formulas; and sharp finite-entry witnesses. Execution returned:

`PASS: 743 exact-rational initial states; both projection identities, entry thresholds, iterates 0..12, and sharpness witnesses`

This finite test suite is not an exhaustive check of an uncountable domain or an independent formal proof. The theorem's infinite quantifiers are supported by the analytical chamber arguments in `RESULT.md`. Independent audit remains unperformed. Limits: strictly positive triangle angles, the two named largest-angle-bisection child maps and eventually constant itineraries; no random, adaptive or mixed-itinerary convergence rate is inferred.
