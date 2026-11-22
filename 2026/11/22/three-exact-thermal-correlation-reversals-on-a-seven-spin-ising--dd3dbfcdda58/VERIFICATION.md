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

The accompanying `verify.py` constructs the cross-multiplied correlation polynomial with exact integers and verifies the three sign changes of its transformed coefficient sequence. It independently evaluates four rational witness points by direct enumeration of all 128 spin configurations using exact rational weights. The exact output is `SEVEN_CYCLE_THREE_REVERSALS_CERTIFIED 3 4 exact enumerations`. Finite enumeration confirms the witness signs; Descartes’ rule supplies the exhaustive three-root bound. The longer-cycle extension is analytic, based on finite strong-bond approximations. Independent audit has not been performed.
